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
from .proxy_data import ProxyData
from .location import Location
from .network import Network


class IPLookup:
	def __init__(self, connection, ip):
		self.connection = connection
		self.ip_lookup = self.connection.get(ip)
		self.ip_info = CheckJSON('ipinfo', self.ip_lookup, True).key_valid()

	# Full Response
	def info(self):
		"""Return all IP info as an object"""
		return self.ip_info

	# Proxy Data
	def proxy_data(self):
		"""Creates a proxy data object containing proxy info"""
		return ProxyData(self.ip_info)

	# Network
	def network(self):
		"""Creates a network object containing network info"""
		return Network(self.ip_info)

	# Location
	def location(self):
		"""Creates a location object containing location info"""
		return Location(self.ip_info)

	# Individual Fields
	def anonymizer_status(self):
		"""Returns anonymizer status"""
		return CheckJSON('anonymizer_status', self.ip_info).key_valid()

	def ip_type(self):
		"""Returns IP type which should be mapped or private"""
		return self.ip_info['ip_type']

	def ip_address(self):
		"""Returns the IP address"""
		return self.ip_info['ip_address']