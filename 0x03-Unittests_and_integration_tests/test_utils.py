#!/usr/bin/env python3
"""A TestAccessNestedMap method to test that the method returns
what it is supposed to"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Tuple, Dict, Union


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
    """Tests the `get_json` function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Tests `get_json`'s output."""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator."""

    def test_memoize(self) -> None:
        """Test that memoization works as expected."""
        class TestClass:
            """Test class with a_method and a_property decorated with memoize."""

            def a_method(self) -> int:
                """A method to be memoized."""
                return 42

            @memoize
            def a_property(self) -> int:
                """A property using memoize."""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_instance = TestClass()
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()
            mock_a_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
