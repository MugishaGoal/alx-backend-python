#!/usr/bin/env python3
"""A TestAccessNestedMap method to test that the method returns
what it is supposed to"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that the access_nested_map function returns the
        expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that accessing non-existent keys raises a KeyError."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for the get_json function."""

    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected result."""
        # Creates a mock response object with json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Sets the return value of the mocked get method
        mock_get.return_value = mock_response

        # Calls the get_json function
        result = get_json(test_url)

        # Asserts that the mocked get method was called exactly once test_url
        mock_get.assert_called_once_with(test_url)

        # Asserts that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
