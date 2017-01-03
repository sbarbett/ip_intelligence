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

class CheckJSON:
	def __init__(self, key, obj, ip_info=False):
		self.key_error = 'Field is not applicable to this license.'
		if ip_info is True:
			self.key_error = 'No IP info returned.'
		self.key = key
		self.obj = obj

	def key_valid(self):
		if self.key not in self.obj:
			raise KeyError(self.key_error)
		else:
			return self.obj[self.key]