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
import requests, json
from hashlib import md5
from time import time

class Connection:
	def __init__(self, api_key, secret, service=None):
		self.endpoint = 'https://api.sec.neustar.biz/ipi/'
		if service is False:
			self.service = 'std/'
		elif service is True:
			self.service = 'gpp/'
		else:
			raise Exception('No service type specified.')
		self.version = 'v1/'
		self.method = 'ipinfo/'
		self.api_key = api_key
		self.secret = secret

	# Authenticate a signature
	def _auth(self):
		timestamp = str(int(time()))
		sig_unencoded = self.api_key + self.secret + timestamp
		sig = md5(sig_unencoded.encode()).hexdigest()
		return {'apikey': self.api_key, 'sig': sig, 'format': 'json'}

	def _is_json(self, rstring):
		try:
			json_object = json.loads(rstring)
		except ValueError as e:
			return False
		return True

	def get(self, ip):
		return self._do_call(ip, 'GET')

	def _do_call(self, ip, http_method):
		params = self._auth()
		url = self.endpoint + self.service + self.version + self.method + ip
		req = requests.request(http_method, url, params=params)
		# For debugging
		# print req.url
		if req.status_code is not requests.codes.OK:
			raise Exception('Auth error', req.status_code)
		elif self._is_json(req.text):
			return req.json()
		else:
			return req.text