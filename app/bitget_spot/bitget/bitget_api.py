#!/usr/bin/python
from app.tg import Client
from app.tg import GET, POST


class BitgetApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, first)

    def post(self, request_path, params):
        return self._request_with_params(POST, request_path, params)

    def get(self, request_path, params):
        return self._request_with_params(GET, request_path, params)
