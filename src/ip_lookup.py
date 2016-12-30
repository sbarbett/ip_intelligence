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

class IPLookup:
	def __init__(self, connection, ip):
		self.connection = connection
		self.ip = self.connection.get(ip)

	# IP Data
	def ip_info(self):
		"""Return all IP info as an object"""
		return self.ip['ipinfo']

	def anonymizer_status(self):
		"""Returns anonymizer status"""
		return self.ip['ipinfo']['anonymizer_status']

	def ip_type(self):
		"""Returns IP type which should be mapped or private"""
		return self.ip['ipinfo']['ip_type']

	def ip_address(self):
		"""Returns the IP address"""
		return self.ip['ipinfo']['ip_address']

	# Proxy Data
	def proxy_data(self):
		"""Return all proxy data as an object"""
		return self.ip['ipinfo']['ProxyData']

	def proxy_level(self):
		"""Returns proxy level"""
		return self.ip['ipinfo']['ProxyData']['proxy_level']

	def proxy_type(self):
		"""Returns proxy type"""
		return self.ip['ipinfo']['ProxyData']['proxy_type']

	def proxy_last_detected(self):
		"""Return proxy type"""
		return self.ip['ipinfo']['ProxyData']['proxy_last_detected']

	# Location
	def location(self):
		"""Return all location data as an object"""
		return self.ip['ipinfo']['Location']

	# Country Data
	# def country_data(self):
	# 	"""Return all country data as an object"""