#!/usr/bin/env python3
""" Parameterize a unit test Model """
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Class that Inherits from unittest
     to test Nested Map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, excepted):
        """ A method to test access_nested_map
         and return the expexted output """
        self.assertEqual(access_nested_map(nested_map, path), excepted)
