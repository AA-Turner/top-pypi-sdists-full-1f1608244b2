# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

from . import base_service
from .. import resources
from ..paginator import Paginator
from .. import errors

class BankAccountDetailsService(base_service.BaseService):
    """Service class that provides access to the bank_account_details
    endpoints of the GoCardless Pro API.
    """

    RESOURCE_CLASS = resources.BankAccountDetail
    RESOURCE_NAME = 'bank_account_details'


    def get(self,identity,params=None, headers=None):
        """Get encrypted bank details.

        Returns bank account details in the flattened JSON Web Encryption
        format described in RFC 7516

        Args:
              identity (string): Unique identifier, beginning with "BA".
              params (dict, optional): Query string parameters.

        Returns:
              BankAccountDetail
        """
        path = self._sub_url_params('/bank_account_details/:identity', {
          
            'identity': identity,
          })
        

        response = self._perform_request('GET', path, params, headers,
                                         retry_failures=True)
        return self._resource_for(response)
  
