#!/usr/bin/env python3
"""Unit test class for the access_nested_map function
   on the utils module"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Unit test class  for the access_nested_map function in the utils
    module"""
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_acces_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with various nested dictionary structures and
        paths
        Parameters
        nested_map: dict
            The nested dictionary structure to be accessed
        path: tuple
            The sequence of keys representing the path to the desired value
        expected: any
            THe expected result from accessing the path in the nested map
        Asserts
        assertEqual
            Ensures that access_nested_map(nested_map, path)
            matches the expected value
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
