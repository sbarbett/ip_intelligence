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
import json
from .check_json import CheckJSON

def check_json(key, obj, error):
	if key not in obj:
		raise KeyError(error)
	else:
		return obj[key]

class IPLookup:
	def __init__(self, connection, ip):
		self.connection = connection
		self.ip_lookup = self.connection.get(ip)
		self.ip_info = check_json('ipinfo', self.ip_lookup, 'No IP info returned.')
		self.key_error = 'Field is not applicable to this license.'

	# IP Data
	def info(self):
		"""Return all IP info as an object"""
		return self.ip_info

	def anonymizer_status(self):
		"""Returns anonymizer status"""
		return self.ip_info['anonymizer_status']

	def ip_type(self):
		"""Returns IP type which should be mapped or private"""
		return self.ip_info['ip_type']

	def ip_address(self):
		"""Returns the IP address"""
		return self.ip_info['ip_address']

	# Proxy Data
	def proxy_data(self):
		"""Creates a proxy data object containing proxy info"""
		return ProxyData(self.ip_info, self.key_error)

	# Location
	def location(self):
		"""Creates a location object containing location info"""
		return Location(self.ip_info, self.key_error)

	# Country Data
	# def country_data(self):
	# 	"""Return all country data as an object"""

class ProxyData:
	def __init__(self, ip_info, key_error):
		self.key_error = key_error
		self.proxy_data = check_json('ProxyData', ip_info, key_error)

	def info(self):
		"""Return all proxy data as an object"""
		return self.proxy_data

	def proxy_level(self):
		"""Returns proxy level"""
		return check_json('proxy_level', self.proxy_data, self.key_error)

	def proxy_type(self):
		"""Returns proxy type"""
		return check_json('proxy_type', self.proxy_data, self.key_error)

	def proxy_last_detected(self):
		"""Returns when a proxy was last detected"""
		return check_json('proxy_last_detected', self.proxy_data, self.key_error)

class Location:
	def __init__(self, ip_info, key_error):
		self.key_error = key_error
		self.location = check_json('Location', ip_info, key_error)

	def info(self):
		"""Returns all location info as an object"""
		return self.location

	def dma(self):
		"""Returns DMA"""
		return check_json('dma', self.location, self.key_error)

	def region(self):
		"""Returns region"""
		return check_json('region', self.location, self.key_error)