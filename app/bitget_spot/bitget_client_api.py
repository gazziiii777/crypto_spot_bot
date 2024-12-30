import os

from dotenv import load_dotenv
import app.bitget_spot.bitget.bitget_api as baseApi
import app.bitget_spot.bitget.v2.spot.account_api as accountApi

load_dotenv()


class BitgetApiClient:
    def __init__(self):
        self.api_key = os.getenv('BITGET_API_KEY')
        self.secret_key = os.getenv('BITGET_SECRET_KEY')
        self.passphrase = os.getenv('BITGET_PASSPHRASE')
        self.base_api = baseApi.BitgetApi(self.api_key, self.secret_key, self.passphrase)
        self.account_api = accountApi.AccountApi(self.api_key, self.secret_key, self.passphrase)

    def get_base_api(self):
        return self.base_api

    def get_account_api(self):
        return self.account_api
