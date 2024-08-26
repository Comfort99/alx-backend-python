#!/usr/bin/env python3
""" Integration Test """
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """ A class that Inherits from Unittest
     to test GithubOrgClient objects """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ A method that test Org method and return a json """
        test_org = GithubOrgClient(org_name)
        test_org.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
