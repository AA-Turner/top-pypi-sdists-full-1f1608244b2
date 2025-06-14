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
from aliyunsdkcdn.endpoint import endpoint_data

class PushObjectCacheRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Cdn', '2018-05-10', 'PushObjectCache')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ObjectPath(self): # String
		return self.get_query_params().get('ObjectPath')

	def set_ObjectPath(self, ObjectPath):  # String
		self.add_query_param('ObjectPath', ObjectPath)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_L2Preload(self): # Boolean
		return self.get_query_params().get('L2Preload')

	def set_L2Preload(self, L2Preload):  # Boolean
		self.add_query_param('L2Preload', L2Preload)
	def get_Area(self): # String
		return self.get_query_params().get('Area')

	def set_Area(self, Area):  # String
		self.add_query_param('Area', Area)
	def get_WithHeader(self): # String
		return self.get_query_params().get('WithHeader')

	def set_WithHeader(self, WithHeader):  # String
		self.add_query_param('WithHeader', WithHeader)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
