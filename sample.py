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
import ip_intelligence, sys

# The fifth argument is True if you are using a GeoPoint Premium
# license. Otherwise leave blank for Standard.
if len(sys.argv) != 4 and len(sys.argv) !=5:
    raise Exception("Expected use: python sample.py api_key secret ip [True]")

api_key = sys.argv[1]
secret = sys.argv[2]
ip = sys.argv[3]
gpp = False

if len(sys.argv) == 5:
	gpp = True

# If the client raises a KeyError and states that the field is not
# available, your access is not licensed for that information.
# Contact Neustar for further info.

# General IP Info
connection = ip_intelligence.Client(api_key, secret, gpp)
ip_info = connection.ip_lookup(ip)
print 'ip address %s' % ip_info.ip_address()
print 'ip type %s' % ip_info.ip_type()

# Proxy Information
proxy_data = ip_info.proxy_data()
print 'proxy level %s' % proxy_data.proxy_level()
print 'proxy last detected %s' % proxy_data.proxy_last_detected()
print 'proxy type %s' % proxy_data.proxy_type()

# Network Information
network = ip_info.network()
print 'connection type %s' % network.connection_type()
print 'ip routing type %s' % network.ip_routing_type()

# Domain Information
domain = network.domain()
print 'top level domain %s' % domain.tld()
print 'second level domain %s' % domain.sld()

# Organization Data
organization_data = network.organization_data()
print 'organization type %s' % organization_data.organization_type()

# Location
location = ip_info.location()
print 'region %s' % location.region()
print 'logitude %s' % location.longitude()
print 'latitude %s' % location.latitude()

# Country Data
country_data = location.country_data()
print 'country %s' % country_data.country()

# State Data
state_data = location.state_data()
print 'state %s' % state_data.state()

# City Data
city_data = location.city_data()
print 'city %s' % city_data.city()
print 'postal code %s' % city_data.postal_code()