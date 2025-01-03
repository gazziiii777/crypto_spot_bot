import app.mexc_spot.mexc_client_api as api


class MexcWalletData:
    """
    -
    """

    def __init__(self):
        self.spot_client = api.MexcApi().get_spot_client()

    async def get_wallet_balance(self):
        """
        -
        """
        response = self.spot_client.account_information()
        return response
