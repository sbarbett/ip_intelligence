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
from .country_data import CountryData
from .state_data import StateData
from .city_data import CityData

class Location:
	def __init__(self, ip_info):
		self.location = CheckJSON('Location', ip_info).key_valid()

	# Full Response
	def info(self):
		"""Returns all location info as an object"""
		return self.location

	# Country
	def country_data(self):
		"""Creates a country data object containing country info"""
		return CountryData(self.location)

	# State
	def state_data(self):
		"""Creates a state data object containing state info"""
		return StateData(self.location)

	# City
	def city_data(self):
		"""Creates a city data object containing city info"""
		return CityData(self.location)

	# Individual Fields
	def dma(self):
		"""Returns DMA"""
		return CheckJSON('dma', self.location).key_valid()

	def region(self):
		"""Returns region"""
		return CheckJSON('region', self.location).key_valid()

	def geonames_id(self):
		"""Returns GeoNames ID"""
		return CheckJSON('geonames_id', self.location).key_valid()

	def longitude(self):
		"""Returns longitude"""
		return CheckJSON('longitude', self.location).key_valid()

	def msa(self):
		"""Returns MSA"""
		return CheckJSON('msa', self.location).key_valid()

	def latitude(self):
		"""Returns latitude"""
		return CheckJSON('latitude', self.location).key_valid()

	def continent(self):
		"""Returns continent"""
		return CheckJSON('continent', self.location).key_valid()
