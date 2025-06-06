# coding: utf-8

"""
    Coinbase Developer Platform APIs

    The Coinbase Developer Platform APIs - leading the world's transition onchain.

    The version of the OpenAPI document: 2.0.0
    Contact: cdp@coinbase.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cdp.openapi_client.models.create_solana_account_request import CreateSolanaAccountRequest

class TestCreateSolanaAccountRequest(unittest.TestCase):
    """CreateSolanaAccountRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSolanaAccountRequest:
        """Test CreateSolanaAccountRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateSolanaAccountRequest`
        """
        model = CreateSolanaAccountRequest()
        if include_optional:
            return CreateSolanaAccountRequest(
                name = 'my-wallet',
                account_policy = '123e4567-e89b-12d3-a456-426614174000'
            )
        else:
            return CreateSolanaAccountRequest(
        )
        """

    def testCreateSolanaAccountRequest(self):
        """Test CreateSolanaAccountRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
