import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


response = post_new_order(data.create_order_body)


def get_track_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER_PATH + track)
