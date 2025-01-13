import app.exchanges.mexc_spot.mexc_client_api as api


class MexcMarketdata:
    """
    -
    """

    def __init__(self):
        self.spot_client = api.MexcApi().get_spot_client()

    def get_first_binds(self, symbol: str):
        try:
            response = self.spot_client.order_book(symbol + 'USDT', 1)
            if not response['bids']:
                return False
        except:
            return False

        return response['bids'][0][0]
