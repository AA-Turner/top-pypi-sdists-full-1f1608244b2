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

    def get_rooms(self, company, params={}):
        """Retrieve rooms information
        
        Parameters:
        :param company: 
        :param params:  (Default value = {})

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_room_details(self, company, room_id, params={}):
        """Get a specific room information
        
        Parameters:
        :param company: 
        :param room_id: 
        :param params:  (Default value = {})

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_room_messages(self, company, room_id, params={}):
        """Get messages from a specific room
        
        Parameters:
        :param company: 
        :param room_id: 
        :param params:  (Default value = {})

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_room_by_offer(self, company, offer_id, params={}):
        """Get a specific room by offer ID
        
        Parameters:
        :param company: 
        :param offer_id: 
        :param params:  (Default value = {})

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_room_by_application(self, company, application_id, params={}):
        """Get a specific room by application ID
        
        Parameters:
        :param company: 
        :param application_id: 
        :param params:  (Default value = {})

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def get_room_by_contract(self, company, contract_id, params={}):
        """Get a specific room by contract ID
        
        Parameters:
        :param company: 
        :param contract_id: 
        :param params:  (Default value = {})

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def create_room(self, company, params={}):
        """Create a new room
        
        Parameters:
        :param company: 
        :param params:  (Default value = {})

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def send_message_to_room(self, company, room_id, params={}):
        """Send a message to a room

        Parameters:
        :param company:
        :param room_id: 
        :param params:  (Default value = {})

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def send_message_to_rooms(self, company, params={}):
        """Send a message to a batch of rooms

        Parameters:
        :param company:
        :param params:  (Default value = {})

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def update_room_settings(self, company, room_id, username, params={}):
        """Update a room settings
        
        Parameters:
        :param company: 
        :param room_id: 
        :param username: 
        :param params:  (Default value = {})

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")

    def update_room_metadata(self, company, room_id, params={}):
        """Update the metadata of a room
        
        Parameters:
        :param company: 
        :param room_id: 
        :param params:  (Default value = {})

        """
        raise Exception("The legacy API was deprecated. Please, use GraphQL call - see example in this library.")
