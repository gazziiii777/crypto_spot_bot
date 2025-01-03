import app.bitget_spot.bitget_client_api as api


class BitgetWalletData:
    """
    Класс, отвечает за все возможные операции связанные с кошельком на бирже bitget
    """

    def __init__(self):
        self.client_api = api.BitgetApiClient()
        self.account_api = self.client_api.get_account_api()

    def get_wallet_balance(self):
        """
        Метод, возвращает все монеты, которые есть на кошельке bitget
        """
        params = {}
        response = self.account_api.assets(params)
        return response
