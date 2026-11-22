# Eval results

## 22 Nov 2026 · claude-sonnet-5-5 · one run per case

Mean competency score per answer (1–4), with the expected band.

| Set | Weak | Middling | Strong | Rises weak → strong |
|---|---|---|---|---|
| Metrics | 1.50 (1–2) | 2.25 (1.75–2.75) | 2.80 (2.75–4) | yes |
| Estimation | 1.50 (1–2) | 2.00 (1.75–2.75) | 3.00 (2.75–4) | yes |
| Prioritization | 1.20 (1–2) | 2.40 (1.75–2.75) | 3.00 (2.75–4) | yes |
| Product design | 1.17 (1–2) | – | 2.83 (2.75–4) | yes |

- Same answer at two levels: APM 3.00, Group PM 2.00 (APM should be higher: yes).
- Benchmark, the worked split-the-bill answer: 3.20 (should be 3 or above: yes).

**Result: all 13 assertions pass.**

What changed to get there: on the first full run, the middling prioritization answer scored 1.60 and the strong design answer 2.71, just outside their bands. Reading the feedback, the coach was right about the answers: the middling one had no goal, and the strong one was light on business judgment and trade-offs. Both answers were rewritten to match their intended level; the bands were not changed.

**Caveats.** One run per case, so scores can move between runs; three results sit within 0.1 of a band edge (metrics strong 2.80, design strong 2.83, and the middling metrics answer). The bands are the author's and haven't been checked against human interviewers' scores. Rerun with `python3 scripts/run_evals.py`.
