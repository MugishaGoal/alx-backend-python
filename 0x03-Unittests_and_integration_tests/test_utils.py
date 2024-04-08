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


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator."""

    class TestClass:
        """Test class with a_method and a_property decorated with memoize."""

        def a_method(self):
            """A method to be memoized."""
            return 42

        @memoize
        def a_property(self):
            """A property using memoize."""
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """Test that memoization works as expected."""
        # Create an instance of TestClass
        test_instance = self.TestClass()

        # Call the memoized property twice
        result1 = test_instance.a_property()
        result2 = test_instance.a_property()

        # Assert that a_method was called only once
        mock_a_method.assert_called_once()

        # Assert that the results are equal
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
