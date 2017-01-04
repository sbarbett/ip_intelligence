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

class CityData:
	def __init__(self, location):
		self.city_data = CheckJSON('CityData', location).key_valid()

	# Full Response
	def info(self):
		"""Return all city data as an object"""
		return self.city_data

	# Individual Fields
	def area_code(self):
		"""Returns area code"""
		return CheckJSON('area_code', self.city_data).key_valid()

	def city(self):
		"""Returns city"""
		return CheckJSON('city', self.city_data).key_valid()

	def city_cf(self):
		"""Returns city confidence factor"""
		return CheckJSON('city_cf', self.city_data).key_valid()

	def city_ref_id(self):
		"""Returns city reference ID"""
		return CheckJSON('city_ref_id', self.city_data).key_valid()

	def postal_code(self):
		"""Returns postal code"""
		return CheckJSON('postal_code', self.city_data).key_valid()

	def time_zone(self):
		"""Returns time_zone"""
		return CheckJSON('time_zone', self.city_data).key_valid()