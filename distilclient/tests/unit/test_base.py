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

from distilclient.common.apiclient import base as common_base
from distilclient.tests.unit import utils
from distilclient.tests.unit.v2 import fakes


cs = fakes.FakeClient()


class BaseTest(utils.TestCase):

    def test_resource_repr(self):
        r = common_base.Resource(None, dict(foo="bar", baz="spam"))
        self.assertEqual(repr(r), "<Resource baz=spam, foo=bar>")

    def test_eq(self):
        # Two resources of the same type with the same id: equal
        # The truth of r1==r2 does not imply that r1!=r2 is false in PY2.
        # Test that inequality operator is defined and that comparing equal
        # items returns False.
        r1 = common_base.Resource(None, {'id': 1, 'name': 'hi'})
        r2 = common_base.Resource(None, {'id': 1, 'name': 'hello'})
        self.assertTrue(r1 == r2)
        self.assertFalse(r1 != r2)

        # Two resources with no ID: equal if their info is equal
        # The truth of r1==r2 does not imply that r1!=r2 is false in PY2.
        # Test that inequality operator is defined and that comparing equal
        # items returns False.
        r1 = common_base.Resource(None, {'name': 'joe', 'age': 12})
        r2 = common_base.Resource(None, {'name': 'joe', 'age': 12})
        self.assertTrue(r1 == r2)
        self.assertFalse(r1 != r2)
