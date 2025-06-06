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

class ListIpsecServerLogsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'ListIpsecServerLogs','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_MinutePeriod(self): # Integer
		return self.get_query_params().get('MinutePeriod')

	def set_MinutePeriod(self, MinutePeriod):  # Integer
		self.add_query_param('MinutePeriod', MinutePeriod)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_From(self): # Integer
		return self.get_query_params().get('From')

	def set_From(self, _From):  # Integer
		self.add_query_param('From', _From)
	def get_To(self): # Integer
		return self.get_query_params().get('To')

	def set_To(self, To):  # Integer
		self.add_query_param('To', To)
	def get_IpsecServerId(self): # String
		return self.get_query_params().get('IpsecServerId')

	def set_IpsecServerId(self, IpsecServerId):  # String
		self.add_query_param('IpsecServerId', IpsecServerId)
