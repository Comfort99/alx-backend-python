#!/usr/bin/env python3
""" Parameterize a unit test Model """
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize


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

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ A method that raises a KeyError
         If the key is not found """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(error.exception))


class TestGetJson(unittest.TestCase):
    """ Class that Inherits from unittest
     to test Get Json Method """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ A method to test Get Json Method
         if is returning a dictionary """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # call the function with the test URL
        result = get_json(test_url)

        # Assert that the mocked requests.get
        # was called exactly once with the test URL
        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ Class that Inherits from Unit test
     tO test  a cache decorator """

    class TestClass:
        """ Test Class for wrapping memorize """

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    with patch.object(TestClass, 'a_method') as mock:
        test_class = TestClass()
        test_class.a_property()
        test_class.a_property()
        mock.assert_called_once()
