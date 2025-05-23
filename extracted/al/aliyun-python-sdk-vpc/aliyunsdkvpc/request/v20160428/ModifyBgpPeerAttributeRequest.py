# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkvpc.endpoint import endpoint_data

class ModifyBgpPeerAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ModifyBgpPeerAttribute','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_BgpGroupId(self): # String
		return self.get_query_params().get('BgpGroupId')

	def set_BgpGroupId(self, BgpGroupId):  # String
		self.add_query_param('BgpGroupId', BgpGroupId)
	def get_PeerIpAddress(self): # String
		return self.get_query_params().get('PeerIpAddress')

	def set_PeerIpAddress(self, PeerIpAddress):  # String
		self.add_query_param('PeerIpAddress', PeerIpAddress)
	def get_BfdMultiHop(self): # Integer
		return self.get_query_params().get('BfdMultiHop')

	def set_BfdMultiHop(self, BfdMultiHop):  # Integer
		self.add_query_param('BfdMultiHop', BfdMultiHop)
	def get_EnableBfd(self): # Boolean
		return self.get_query_params().get('EnableBfd')

	def set_EnableBfd(self, EnableBfd):  # Boolean
		self.add_query_param('EnableBfd', EnableBfd)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_BgpPeerId(self): # String
		return self.get_query_params().get('BgpPeerId')

	def set_BgpPeerId(self, BgpPeerId):  # String
		self.add_query_param('BgpPeerId', BgpPeerId)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
