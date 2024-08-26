#!/usr/bin/env python3
""" Integration Test """
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock


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
        with patch.object(GithubOrgClient,
                          'org', new_callable=PropertyMock) as mock_org:
            expected_url = "https://api.github.com/orgs/test_org/repos"
            payload = {"repos_url": expected_url}
            mock_org.return_value = payload
            test_repos = GithubOrgClient('test_org')
            result = test_repos._public_repos_url
            self.assertEqual(result, payload["repos_url"])
