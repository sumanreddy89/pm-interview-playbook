#!/usr/bin/env python3
"""Run the coach's scoring evals and check the scores, or just check the eval file.

    python3 scripts/run_evals.py --check            # validate evals.json; no API calls (CI runs this)
    ANTHROPIC_API_KEY=... python3 scripts/run_evals.py [--model claude-sonnet-5-5] [--only 4,5,6]

Run mode sends each case that has an "assert" to the Claude API with the skill and its
references as the system prompt, asks for the scores as JSON at the end, and checks:
- mean_score_between: the mean competency score falls in the band;
- within a group (for example metrics-calibration), means rise in id order: weak < middling < strong;
- apm_mean_above_gpm_mean: the same answer scores higher at APM than at Group PM.
Each case is one model call, so a full run costs a little; the model is pinned unless you pass --model.
Standard library only.
"""
import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "pm-interview-coach"
EVALS = SKILL / "evals" / "evals.json"
DEFAULT_MODEL = "claude-sonnet-5-5"
KNOWN_ASSERTS = {"mean_score_between", "apm_mean_above_gpm_mean"}
GROUP_FRAMEWORK = {
    "metrics-calibration": ["metrics.md", "india-pm.md"],
    "estimation-calibration": ["estimation.md", "india-pm.md"],
    "prioritization-calibration": ["prioritization.md", "india-pm.md"],
    "design-calibration": ["design-new-product.md", "india-pm.md"],
    "benchmark": ["metrics.md", "india-pm.md"],
}
SCORE_ASK = ("\n\nAfter your feedback, end with exactly one line in this form, using the competencies you scored:\n"
             'SCORES: {"Structure": 3, "Metrics and analytics": 2}')
LEVEL_ASK = ("\n\nAfter your feedback, end with exactly two lines in this form:\n"
             'SCORES_APM: {"Structure": 3}\nSCORES_GROUP_PM: {"Structure": 2}')


def load():
    return json.loads(EVALS.read_text(encoding="utf-8"))["evals"]


def check(evals):
    """Problems with the eval file, as a list of strings (empty = fine)."""
    problems, seen = [], set()
    for e in evals:
        i = e.get("id")
        if i in seen:
            problems.append(f"duplicate id {i}")
        seen.add(i)
        for key in ("prompt", "expected_output"):
            if not e.get(key):
                problems.append(f"id {i}: missing {key}")
        for key in (e.get("assert") or {}):
            if key not in KNOWN_ASSERTS:
                problems.append(f"id {i}: unknown assert {key}")
        band = (e.get("assert") or {}).get("mean_score_between")
        if band and not (len(band) == 2 and 1 <= band[0] <= band[1] <= 4):
            problems.append(f"id {i}: band must be [low, high] within 1-4")
        for f in e.get("files") or []:
            if not (SKILL / f).exists():
                problems.append(f"id {i}: file not found: {f}")
        if e.get("group") and e["group"] not in GROUP_FRAMEWORK:
            problems.append(f"id {i}: no framework mapping for group {e['group']}")
    return problems


def parse_scores(text, label="SCORES"):
    """The last '<label>: {...}' line, as {competency: score}; None if missing or malformed."""
    found = re.findall(rf"^{label}:\s*(\{{.*\}})\s*$", text, re.MULTILINE)
    if not found:
        return None
    try:
        data = json.loads(found[-1])
    except ValueError:
        return None
    scores = {k: float(v) for k, v in data.items() if isinstance(v, (int, float)) and 1 <= v <= 4}
    return scores or None


def mean(scores):
    return sum(scores.values()) / len(scores)


def grade(evals, means, level_means):
    """Check results against the asserts. Returns (passed, failures)."""
    failures = []
    for e in evals:
        a = e.get("assert") or {}
        if "mean_score_between" in a and e["id"] in means:
            lo, hi = a["mean_score_between"]
            m = means[e["id"]]
            if not lo <= m <= hi:
                failures.append(f"id {e['id']}: mean {m:.2f} outside {lo}-{hi}")
        if a.get("apm_mean_above_gpm_mean") and e["id"] in level_means:
            apm, gpm = level_means[e["id"]]
            if not apm > gpm:
                failures.append(f"id {e['id']}: APM {apm:.2f} not above Group PM {gpm:.2f}")
    groups = {}
    for e in evals:
        if e.get("group") in GROUP_FRAMEWORK and e["group"] != "benchmark" and e["id"] in means:
            groups.setdefault(e["group"], []).append(e["id"])
    for g, ids in groups.items():
        ms = [means[i] for i in sorted(ids)]
        if any(b <= a for a, b in zip(ms, ms[1:])):
            failures.append(f"{g}: means don't rise weak < middling < strong: " + ", ".join(f"{m:.2f}" for m in ms))
    return not failures, failures


def system_prompt(e):
    refs = SKILL / "references"
    parts = [(SKILL / "SKILL.md").read_text(encoding="utf-8"), (refs / "rubric.md").read_text(encoding="utf-8")]
    for name in GROUP_FRAMEWORK.get(e.get("group"), ["metrics.md"]):
        parts.append(f"# references/{name}\n" + (refs / name).read_text(encoding="utf-8"))
    for f in e.get("files") or []:
        parts.append(f"# {f}\n" + (SKILL / f).read_text(encoding="utf-8"))
    return "\n\n---\n\n".join(parts)


def ask(model, system, prompt, key):
    body = json.dumps({"model": model, "max_tokens": 2500, "temperature": 0, "system": system,
                       "messages": [{"role": "user", "content": prompt}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, headers={
        "content-type": "application/json", "x-api-key": key, "anthropic-version": "2023-06-01"})
    with urllib.request.urlopen(req, timeout=180) as r:
        data = json.load(r)
    return "".join(b.get("text", "") for b in data.get("content", []))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="validate the eval file only")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--only", help="comma-separated ids")
    args = ap.parse_args(argv)
    evals = load()
    problems = check(evals)
    if problems:
        print("\n".join(problems))
        return 1
    if args.check:
        print(f"evals.json OK: {len(evals)} cases, {sum(1 for e in evals if e.get('assert'))} with assertions")
        return 0
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        print("Set ANTHROPIC_API_KEY to run the evals (or use --check).")
        return 2
    only = {int(x) for x in args.only.split(",")} if args.only else None
    means, level_means = {}, {}
    for e in evals:
        if not e.get("assert") or (only and e["id"] not in only):
            continue
        levels = e["assert"].get("apm_mean_above_gpm_mean")
        text = ask(args.model, system_prompt(e), e["prompt"] + (LEVEL_ASK if levels else SCORE_ASK), key)
        if levels:
            a, g = parse_scores(text, "SCORES_APM"), parse_scores(text, "SCORES_GROUP_PM")
            if a and g:
                level_means[e["id"]] = (mean(a), mean(g))
                print(f"id {e['id']}: APM {mean(a):.2f}, Group PM {mean(g):.2f}")
            else:
                print(f"id {e['id']}: no parseable level scores")
        else:
            s = parse_scores(text)
            if s:
                means[e["id"]] = mean(s)
                print(f"id {e['id']} ({e.get('group', '')}): mean {mean(s):.2f} {s}")
            else:
                print(f"id {e['id']}: no parseable SCORES line")
    ok, failures = grade(evals, means, level_means)
    print("\n".join(["", "PASS" if ok else "FAIL"] + failures))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
