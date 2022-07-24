# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.product import Product  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProductsController(BaseTestCase):
    """ProductsController integration test stubs"""

    def test_get_product_by_id(self):
        """Test case for get_product_by_id

        Find Product by ID
        """
        response = self.client.open(
            '/v2/products/{id}'.format(id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_product(self):
        """Test case for update_product

        Updates a Product in the store with form data
        """
        response = self.client.open(
            '/v2/products/{id}'.format(id=789),
            method='PUT',
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
