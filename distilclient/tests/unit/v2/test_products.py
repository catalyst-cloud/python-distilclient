# Copyright (c) 2017 Catalyst IT Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mock
import uuid

import distilclient
from distilclient import base
from distilclient.tests.unit import utils
from distilclient.v2 import client


class ProductsTest(utils.TestCase):

    def setUp(self):
        super(ProductsTest, self).setUp()
        self.client = client.Client(session=client.session.Session(),
                                    api_version=distilclient.API_MAX_VERSION,
                                    distil_url=uuid.uuid4().hex, retries=3,
                                    input_auth_token='token')

    @mock.patch.object(base.Manager, '_list')
    def test_list(self, mock_list):
        self.client.products.list()
        mock_list.assert_called_with('/v2/products', 'products')

    @mock.patch.object(base.Manager, '_list')
    def test_list_with_regions(self, mock_list):
        self.client.products.list(regions=["nz-hlz-1", "nz-por-1"])
        mock_list.assert_called_with('/v2/products?regions=nz-hlz-1,nz-por-1',
                                     'products')