import app.bitget_spot.bitget_client_api as api


class MarketData:
    def __init__(self):
        self.client_api = api.BitgetApiClient()
        self.market_api = self.client_api.get_market_api()

    async def get_first_binds(self, symbol: str):
        """
        Метод, который возвращает первую цену по которой можно продать монету
        :param symbol: BTCUSDT
        :return:
        """
        params = {
            "symbol": symbol,
            "limit": 1
        }
        try:
            response = self.market_api.orderbook(params)
        except:
            response = 'Нельзя продать на споте'

        return response

    async def get_order_book(self, symbol: str):
        """
        Метод, который возвращает цену покупки asks (красный столбец)
        и цену по которой можно продать bids (зеленый столбец)
        :param symbol: торговая пара например BTCUSDT
        """
        pass
