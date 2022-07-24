
import logging
import os
import connexion
from swagger_server import util
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from swagger_server.models.product import Price


@lru_cache
def get_product_by_id(id_):
    """Find Product by ID

    Returns a Product Details # noqa: E501

    :param id: ID of Product to return
    :type id: int

    :rtype: Product
    """
    product_details = {'id': id_}
    ins_mongo = util.MongoWrapper()
    results = []
    with ThreadPoolExecutor(2) as executor:
        results.append(executor.submit(util.request_url,
                       os.environ.get('PRODUCT_URL', '{}').format(id_)))
        results.append(executor.submit(ins_mongo.get_item, id_))

    for obj_future in as_completed(results):
        product_details.update(obj_future.result())
    return product_details


def update_product(id_, body):  # noqa: E501
    """Updates a Product in the store with form data

    :param id: ID of Product that needs to be updated
    :type id: int
    :param body: Updated user object
    :type body: dict | bytes

    :rtype: None
    """
    try:
        if not connexion.request.is_json:
            return {"error": "Incorrect Body or body not formated"}
        dct_body = connexion.request.get_json()
        payload = {"$set": {'value': dct_body['value'],
                   'currency_code': dct_body['currency_code']}}
    except Exception as msg:
        logging.error('Failed to insert the data : {}'.format(msg))
        return {"error": "Incorrect Body or body not formated"}
    obj_mongo = util.MongoWrapper()
    inserted_id = obj_mongo.update_item(id_, payload)
    if not inserted_id:
        return {"error": 'Update failed'}

    get_product_by_id.cache_clear()
    return {"SUCESS": "Product with id {} updated ".format(id_)}
