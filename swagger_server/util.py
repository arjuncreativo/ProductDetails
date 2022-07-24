
import os
import requests
from pymongo import MongoClient
import logging
logging.basicConfig(level=logging.INFO)


class MongoWrapper():

    def __init__(self) -> None:
        """
        Initialize Mongo DB Connection
        Get the connections tring from the environment variable
        mongodb://<user>:<password>@<host>:port/
        """
        try:
            str_connection = os.environ.get('ME_CONFIG_MONGODB_URL', None)
            self.client = MongoClient(str_connection)
            self.client.server_info()
            self.client.db = self.client.get_database(
                os.environ.get('DB', 'myretail'))

        except Exception as msg:
            logging.info('Mongo DB failure {}'.format(msg))
            logging.error('Mongo Db Connection failed')

    def get_item(self, id_):
        """
        Query an Item from mongo DB
        Args:
            id_ (integer): Id used to index the item in mongo collecction

        Returns:
            dict: Dictionary with id, price and currency code
            {'_id': 13860428.0, 'value': 10.0, 'currency_code': 'USD'}
        """
        price_info = {}
        result = self.client.db.price.find_one({'_id': id_})
        logging.info(result)
        if result:
            price_info['current_price'] = {'value': result['value'],
                                           'currency_code': result['currency_code']}
        return price_info

    def update_item(self, id_, payload):
        """ Update the price in to Mongo db

        Args:
            payload (dict): Include Id Price and currency code

        Returns:
            _type_: _description_
        """
        try:
            inserted_id = self.client.db.price.update_one(
                {"_id": int(id_)}, payload)
        except Exception as msg:
            logging.error('Insertion Failed : {}'.format(msg))
            inserted_id = None
        return inserted_id


def request_url(url, req_method='GET', payload={}):
    """
    Request a url and responds back with the result set
    Parrams
    url: The Url to get the response
    type: string
    req_method: GET, POST, PUT, DELETE
    payload: The payload that should be sent in the request body
    """
    response = {}
    try:
        results = requests.request(req_method, url=url, data=payload)
        if results.status_code == 200:
            results = results.json()
            logging.info('Product Details Response : {}'.format(results))
            response = {'name': results['data']['product']
                        ['item']['product_description']['title']}
    except KeyError as msg:
        response = {'error': 'No Products found'}
        logging.error('Incorrect Response : {}'.format(msg))
    except Exception as msg:
        response = {'error': 'No Products found'}
        logging.error('Failed to fetch the product : {}'.format(msg))

    return response
