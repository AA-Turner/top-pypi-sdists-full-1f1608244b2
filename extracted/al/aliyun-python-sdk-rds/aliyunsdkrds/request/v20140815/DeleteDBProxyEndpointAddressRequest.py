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
from aliyunsdkrds.endpoint import endpoint_data

class DeleteDBProxyEndpointAddressRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'DeleteDBProxyEndpointAddress','rds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_DBProxyConnectStringNetType(self): # String
		return self.get_query_params().get('DBProxyConnectStringNetType')

	def set_DBProxyConnectStringNetType(self, DBProxyConnectStringNetType):  # String
		self.add_query_param('DBProxyConnectStringNetType', DBProxyConnectStringNetType)
	def get_DBInstanceId(self): # String
		return self.get_query_params().get('DBInstanceId')

	def set_DBInstanceId(self, DBInstanceId):  # String
		self.add_query_param('DBInstanceId', DBInstanceId)
	def get_DBProxyEngineType(self): # String
		return self.get_query_params().get('DBProxyEngineType')

	def set_DBProxyEngineType(self, DBProxyEngineType):  # String
		self.add_query_param('DBProxyEngineType', DBProxyEngineType)
	def get_DBProxyEndpointId(self): # String
		return self.get_query_params().get('DBProxyEndpointId')

	def set_DBProxyEndpointId(self, DBProxyEndpointId):  # String
		self.add_query_param('DBProxyEndpointId', DBProxyEndpointId)
