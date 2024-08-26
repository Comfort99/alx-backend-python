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
        """Test that _public_repos_url returns
        the correct URL based on the org property."""

        expected_url = "https://api.github.com/orgs/google/repos"
        test_payload = {"repos_url": expected_url}

        # Patch the org property of GithubOrgClient
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload

            # Create an instance of GithubOrgClient
            client = GithubOrgClient('google')

            # Access the _public_repos_url property
            result = client._public_repos_url

            # Assert that the result is the expected URL
            self.assertEqual(result, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ A test function that test public repos
         and returns a json from a list of dictionaries """
        mock_playload = [{"name": "Play_value"}, {"name": "User_name"}]
        mock_json.return_value = mock_playload

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "hello/world"
            test_public = GithubOrgClient("google")
            self.assertEqual(test_public.public_repos(),
                             ["Play_value", "User_name"])

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ A test that test has_license methos
        By returning a boolean"""
        client = GithubOrgClient('Google')
        self.assertEqual(client.has_license(repo, license_key), expected)
