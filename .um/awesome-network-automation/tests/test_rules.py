import unittest
from unittest.mock import patch
from urllib.error import HTTPError
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import collect

class RulesTests(unittest.TestCase):
    def test_uses_pinned_template(self):
        with patch.object(collect, "readme_at", side_effect=["Guide", "Six months OR adoption; exceptions allowed"]) as read:
            rules = collect.contribution_rules("a" * 40)
        self.assertIn("exceptions allowed", rules)
        self.assertEqual(read.call_args_list[1].args, ("a" * 40, ".github/pull_request_template.md"))

    def test_historical_missing_template_keeps_guide(self):
        with patch.object(collect, "readme_at", side_effect=["Guide", HTTPError("url",404,"missing",None,None)]):
            self.assertEqual(collect.contribution_rules("a" * 40), "Guide")

    def test_api_failure_does_not_hide_rules(self):
        with patch.object(collect, "readme_at", side_effect=["Guide", HTTPError("url",403,"limited",None,None)]):
            with self.assertRaises(HTTPError): collect.contribution_rules("a" * 40)
