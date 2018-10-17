"""DataParserLib dictionary parser test."""
# coding=utf-8
import unittest
import json

from dataparserlib.dictionary import flatten_dictionary


class DataParserLibConfigTest(unittest.TestCase):
    """Automated data_parser_lib python test framework."""

    def setUp(self):
        """Build base environment data."""
        with open("../projectinfo.json", "rb") as project_info_json:
            project_data = json.load(project_info_json)
        self.dictionary_data = project_data

    def test_flatten_dictionary_parser(self):
        """Test flatten_dictionary function call."""
        flat_project_data = flatten_dictionary(self.dictionary_data)
        self.assertEqual(flat_project_data["report"]["info.name"], "DataParserLib")


if __name__ == '__main__':
    unittest.main(verbosity=2)
