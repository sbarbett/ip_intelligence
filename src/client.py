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
from .connection import Connection
from .ip_lookup import IPLookup

class Client:
	def __init__(self, api_key, secret, service=False):
		"""Initialize the API client.

		Arguments:
		api_key -- The IPI API api_key
		secret -- The shared secret
		service -- By default will be GeoPoint Standard. Must be set to True for 
				   GeoPoint Premium

		"""
		self.connection = Connection(api_key, secret, service)

	def ip_lookup(self, ip=None):
		return IPLookup(self.connection, ip)