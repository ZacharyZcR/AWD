"""HTTP helpers. Responses are returned; request errors propagate to the caller."""

import requests

DEFAULT_TIMEOUT = 10


def get(address, data=None, *, timeout=DEFAULT_TIMEOUT):
    response = requests.get(address, params=data, timeout=timeout)
    response.raise_for_status()
    return response


def post(address, data=None, *, timeout=DEFAULT_TIMEOUT):
    response = requests.post(address, data=data, timeout=timeout)
    response.raise_for_status()
    return response


post_xwf = post


def post_json(address, data, *, timeout=DEFAULT_TIMEOUT):
    response = requests.post(address, json=data, timeout=timeout)
    response.raise_for_status()
    return response


def test(address, *, timeout=DEFAULT_TIMEOUT):
    return get(address, timeout=timeout).status_code == 200
