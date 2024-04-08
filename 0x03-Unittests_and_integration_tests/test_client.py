#!/usr/bin/env python3
"""Tests a client module"""


import unittest
from typing import Any
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class."""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name: str, mock_get_json: Any) -> None:
        """Test GithubOrgClient.org method."""
        expected_url = f"https://api.github.com/orgs/{org_name}"
        expected_result = {"login": org_name}

        # Mocking the get_json method to return expected result
        mock_get_json.return_value = expected_result

        # Creating GithubOrgClient instance
        client = GithubOrgClient(org_name)

        # Calling the org method
        result = client.org

        # Asserting that get_json is called once with the expected argument
        mock_get_json.assert_called_once_with(expected_url)

        # Asserting that the result is as expected
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
