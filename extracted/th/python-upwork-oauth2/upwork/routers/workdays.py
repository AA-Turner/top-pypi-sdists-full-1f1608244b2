# Licensed under the Upwork's API Terms of Use;
# you may not use this file except in compliance with the Terms.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author::    Maksym Novozhylov (mnovozhilov@upwork.com)
# Copyright:: Copyright 2020(c) Upwork.com
# License::   See LICENSE.txt and TOS - https://developers.upwork.com/api-tos.html


class Api:
    """ """

    client = None

    def __init__(self, client):
        self.client = client

    def get_by_company(self, company, from_date, till_date, params={}):
        """Get Workdays by Company
        
        Parameters:
        :param company: 
        :param from_date: 
        :param till_date: 
        :param params:  (Default value = {})

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_by_contract(self, contract, from_date, till_date, params={}):
        """Get Workdays by Contract
        
        Parameters:
        :param contract: 
        :param from_date: 
        :param till_date: 
        :param params:  (Default value = {})

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")
