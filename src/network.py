# Copyright 2017 NeuStar, Inc.All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from .check_json import CheckJSON
from .domain import Domain
from .organization_data import OrganizationData

class Network:
	def __init__(self, ip_info):
		self.network = CheckJSON('Network', ip_info).key_valid()

	# Full Response
	def info(self):
		"""Returns all network info as an object"""
		return self.network

	# Domain
	def domain(self):
		"""Creates a domain object containing domain info"""
		return Domain(self.network)

	# Organization Data
	def organization_data(self):
		"""Creates a organization data object containing domain info"""
		return OrganizationData(self.network)

	# Individual Fields
	def connection_type(self):
		"""Returns connection type"""
		return CheckJSON('connection_type', self.network).key_valid()

	def ip_routing_type(self):
		"""Returns IP routing type"""
		return CheckJSON('ip_routing_type', self.network).key_valid()

	def hosting_facility(self):
		"""Returns hosting facility info"""
		return CheckJSON('hosting_facility', self.network).key_valid()

	def asn(self):
		"""Returns ASN"""
		return CheckJSON('asn', self.network).key_valid()

	def carrier(self):
		"""Returns carrier info"""
		return CheckJSON('carrier', self.network).key_valid()

	def line_speed(self):
		"""Returns line speed"""
		return CheckJSON('line_speed', self.network).key_valid()

	def organization(self):
		"""Returns organization"""
		return CheckJSON('organization', self.network).key_valid()