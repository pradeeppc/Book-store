import json
import sys
import argparse
from http import HTTPStatus

import requests


def setUpData(order_id):
    data = {
        "items": [
            {
                "name": "Harry Potter and the Chamber of Secrets J.K. Rowling",
                "price_per_unit": 199,
                "product_id": 1,
                "quantity": 1
            },
            {
                "name": "Kashi: Secret of the Black Temple",
                "price_per_unit": 300,
                "product_id": 2,
                "quantity": 2
            }
        ],
        "order_customer": {
            "customer_id": 14,
            "email": "test@test.com",
            "name": "Test User"
        },
        "order_id": order_id,
        "status": 1,
        "total": "499.00"
    }

    return data


def send_order(data):

    token ='1c4822358e3600d43851c80554d7b02093f5e5c8'

    headers = {
        'Authorization': f'Token {token}',
        'Content-type': 'application/json'
    }

    response = requests.put(
        'http://127.0.0.1:8000/api/order/add/',
        headers=headers,
        data=json.dumps(data))

    if response.status_code == HTTPStatus.NO_CONTENT:
        print('Ops! Something went wrong!')
        sys.exit(1)

    print('Request was successfull')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Create a order for test')

    parser.add_argument('--orderid',
                        dest='order_id',
                        required=True,
                        help='Specify the the order id')

    args = parser.parse_args()

    data = setUpData(args.order_id)
    send_order(data)
