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
        """Test that _public_repos_url returns the correct URL based on the org property."""

        expected_url = "https://api.github.com/orgs/google/repos"
        test_payload = {"repos_url": expected_url}

        # Patch the org property of GithubOrgClient
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload

            # Create an instance of GithubOrgClient
            client = GithubOrgClient('google')

            # Access the _public_repos_url property
            result = client._public_repos_url

            # Assert that the result is the expected URL
            self.assertEqual(result, expected_url)
