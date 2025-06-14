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
from aliyunsdkdcdn.endpoint import endpoint_data

class DescribeDcdnUserDomainsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dcdn', '2018-01-15', 'DescribeDcdnUserDomains')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PageNumber(self): # Integer
		return self.get_query_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Integer
		self.add_query_param('PageNumber', PageNumber)
	def get_CheckDomainShow(self): # Boolean
		return self.get_query_params().get('CheckDomainShow')

	def set_CheckDomainShow(self, CheckDomainShow):  # Boolean
		self.add_query_param('CheckDomainShow', CheckDomainShow)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_ChangeEndTime(self): # String
		return self.get_query_params().get('ChangeEndTime')

	def set_ChangeEndTime(self, ChangeEndTime):  # String
		self.add_query_param('ChangeEndTime', ChangeEndTime)
	def get_PageSize(self): # Integer
		return self.get_query_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Integer
		self.add_query_param('PageSize', PageSize)
	def get_Tags(self): # RepeatList
		return self.get_query_params().get('Tag')

	def set_Tags(self, Tag):  # RepeatList
		for depth1 in range(len(Tag)):
			if Tag[depth1].get('Value') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Value', Tag[depth1].get('Value'))
			if Tag[depth1].get('Key') is not None:
				self.add_query_param('Tag.' + str(depth1 + 1) + '.Key', Tag[depth1].get('Key'))
	def get_WebSiteType(self): # String
		return self.get_query_params().get('WebSiteType')

	def set_WebSiteType(self, WebSiteType):  # String
		self.add_query_param('WebSiteType', WebSiteType)
	def get_Coverage(self): # String
		return self.get_query_params().get('Coverage')

	def set_Coverage(self, Coverage):  # String
		self.add_query_param('Coverage', Coverage)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_DomainStatus(self): # String
		return self.get_query_params().get('DomainStatus')

	def set_DomainStatus(self, DomainStatus):  # String
		self.add_query_param('DomainStatus', DomainStatus)
	def get_DomainSearchType(self): # String
		return self.get_query_params().get('DomainSearchType')

	def set_DomainSearchType(self, DomainSearchType):  # String
		self.add_query_param('DomainSearchType', DomainSearchType)
	def get_ChangeStartTime(self): # String
		return self.get_query_params().get('ChangeStartTime')

	def set_ChangeStartTime(self, ChangeStartTime):  # String
		self.add_query_param('ChangeStartTime', ChangeStartTime)
