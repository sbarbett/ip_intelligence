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

class Domain:
	def __init__(self, location):
		self.domain = CheckJSON('Domain', location).key_valid()

	# Full Response
	def info(self):
		"""Return all domain data as an object"""
		return self.domain

	# Individual Fields
	def sld(self):
		"""Returns second level domain"""
		return CheckJSON('sld', self.domain).key_valid()

	def tld(self):
		"""Returns top level domain"""
		return CheckJSON('tld', self.domain).key_valid()