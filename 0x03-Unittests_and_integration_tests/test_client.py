#!/usr/bin/env python3
""" Integration Test """
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from fixtures import TEST_PAYLOAD
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ A class that Inherits from Unittest
     to test GithubOrgClient objects """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ A method that test Org method and
        return a value of passed name_url"""
        test_org = GithubOrgClient(org_name)
        test_org.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """ an org property that returns a value of a key """

        # patch the org property of GithubOrgClient
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])
