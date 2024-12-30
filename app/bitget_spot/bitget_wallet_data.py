import json

import app.bitget_spot.bitget_client_api as api


class WalletData:
    def __init__(self):
        self.client_api = api.BitgetApiClient()
        self.account_api = self.client_api.get_account_api()

    async def get_wallet_balance(self):
        params = {}
        response = self.account_api.assets(params)
        return response


