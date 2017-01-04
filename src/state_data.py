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

class StateData:
	def __init__(self, location):
		self.state_data = CheckJSON('StateData', location).key_valid()

	# Full Response
	def info(self):
		"""Return all state data as an object"""
		return self.state_data

	# Individual Fields
	def state_cf(self):
		"""Returns state confidence factor"""
		return CheckJSON('state_cf', self.state_data).key_valid()

	def state(self):
		"""Returns state"""
		return CheckJSON('state', self.state_data).key_valid()

	def state_code(self):
		"""Returns state code"""
		return CheckJSON('state_code', self.state_data).key_valid()