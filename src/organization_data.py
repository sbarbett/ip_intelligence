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

class OrganizationData:
	def __init__(self, location):
		self.organization_data = CheckJSON('OrganizationData', location).key_valid()

	# Full Response
	def info(self):
		"""Return all organization data as an object"""
		return self.organization_data

	# Individual Fields
	def home(self):
		"""Returns home field"""
		return CheckJSON('home', self.organization_data).key_valid()

	def naics_code(self):
		"""Returns NAICS code"""
		return CheckJSON('naics_code', self.organization_data).key_valid()

	def isic_code(self):
		"""Returns ISIC code"""
		return CheckJSON('isic_code', self.organization_data).key_valid()

	def organization_type(self):
		"""Returns organization type"""
		return CheckJSON('organization_type', self.organization_data).key_valid()