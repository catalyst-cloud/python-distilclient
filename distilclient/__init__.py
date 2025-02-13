
#    Copyright 2012 OpenStack Foundation
# Copyright 2015 Chuck Fouts
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

__all__ = ['__version__']

import pbr.version

version_info = pbr.version.VersionInfo('python-distilclient')

try:
    __version__ = version_info.version_string()
except AttributeError:
    __version__ = None


API_MAX_VERSION = '1'
API_MIN_VERSION = '2'
API_DEPRECATED_VERSION = []
