"""Offline tests for run_evals.py (no API calls). Run: python3 -m unittest discover -s scripts"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import run_evals as r  # noqa: E402


class Evals(unittest.TestCase):
    def test_the_eval_file_is_valid(self):
        self.assertEqual(r.check(r.load()), [])

    def test_parse_scores_takes_the_last_line_and_ignores_bad_values(self):
        text = 'feedback...\nSCORES: {"Structure": 2}\nmore\nSCORES: {"Structure": 3, "Metrics": 4, "Bogus": 9}\n'
        self.assertEqual(r.parse_scores(text), {"Structure": 3.0, "Metrics": 4.0})
        self.assertIsNone(r.parse_scores("no scores here"))
        self.assertIsNone(r.parse_scores("SCORES: {not json}"))

    def test_grade_checks_bands_order_and_levels(self):
        evals = [
            {"id": 1, "group": "metrics-calibration", "assert": {"mean_score_between": [1, 2]}},
            {"id": 2, "group": "metrics-calibration", "assert": {"mean_score_between": [1.75, 2.75]}},
            {"id": 3, "group": "metrics-calibration", "assert": {"mean_score_between": [2.75, 4]}},
            {"id": 4, "assert": {"apm_mean_above_gpm_mean": True}},
        ]
        ok, _ = r.grade(evals, {1: 1.5, 2: 2.2, 3: 3.4}, {4: (3.0, 2.0)})
        self.assertTrue(ok)
        ok, fails = r.grade(evals, {1: 2.5, 2: 2.2, 3: 3.4}, {4: (2.0, 3.0)})
        self.assertFalse(ok)
        joined = " ".join(fails)
        self.assertIn("id 1: mean 2.50 outside", joined)
        self.assertIn("don't rise", joined)
        self.assertIn("APM 2.00 not above", joined)

    def test_check_flags_unknown_asserts_and_missing_files(self):
        bad = [{"id": 1, "prompt": "p", "expected_output": "e", "assert": {"nope": 1}, "files": ["references/missing.md"]},
               {"id": 1, "prompt": "", "expected_output": "e"}]
        joined = " ".join(r.check(bad))
        for part in ("unknown assert nope", "file not found", "duplicate id 1", "missing prompt"):
            self.assertIn(part, joined)


if __name__ == "__main__":
    unittest.main()
