# Copyright 2010 Jacob Kaplan-Moss
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
Exception definitions.
"""

from distilclient.common.apiclient.exceptions import *  # noqa


class VersionNotFoundForAPIMethod(Exception):
    msg_fmt = "API version '%(vers)s' is not supported."

    def __init__(self, version):
        self.version = version

    def __str__(self):
        return self.msg_fmt % {"vers": self.version}
