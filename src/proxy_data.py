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

class ProxyData:
	def __init__(self, ip_info):
		self.proxy_data = CheckJSON('ProxyData', ip_info).key_valid()

	def info(self):
		"""Return all proxy data as an object"""
		return self.proxy_data

	def proxy_level(self):
		"""Returns proxy level"""
		return CheckJSON('proxy_level', self.proxy_data).key_valid()

	def proxy_type(self):
		"""Returns proxy type"""
		return CheckJSON('proxy_type', self.proxy_data).key_valid()

	def proxy_last_detected(self):
		"""Returns when a proxy was last detected"""
		return CheckJSON('proxy_last_detected', self.proxy_data).key_valid()