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

class CreateDcdnDeliverTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dcdn', '2018-01-15', 'CreateDcdnDeliverTask')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Reports(self): # String
		return self.get_body_params().get('Reports')

	def set_Reports(self, Reports):  # String
		self.add_body_params('Reports', Reports)
	def get_Schedule(self): # String
		return self.get_body_params().get('Schedule')

	def set_Schedule(self, Schedule):  # String
		self.add_body_params('Schedule', Schedule)
	def get_Name(self): # String
		return self.get_body_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_body_params('Name', Name)
	def get_DomainName(self): # String
		return self.get_body_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_body_params('DomainName', DomainName)
	def get_Deliver(self): # String
		return self.get_body_params().get('Deliver')

	def set_Deliver(self, Deliver):  # String
		self.add_body_params('Deliver', Deliver)
