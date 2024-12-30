# import bitget_spot.v1.mix.order_api as maxOrderApi
import logging
import os

import bitget.bitget_api as baseApi

from dotenv import load_dotenv
from bitget.exceptions import BitgetAPIException

if __name__ == '__main__':
    load_dotenv()

    baseApi = baseApi.BitgetApi(os.getenv('BITGET_API_KEY'), os.getenv('BITGET_SECRET_KEY'),
                                os.getenv('BITGET_PASSPHRASE'))
    # Demo 1:place order
    # maxOrderApi = maxOrderApi.OrderApi(apiKey, secretKey, passphrase)
    # try:
    #     params = {}
    #     params["symbol"] = "BTCUSDT_UMCBL"
    #     params["marginCoin"] = "USDT"
    #     params["side"] = "open_long"
    #     params["orderType"] = "limit"
    #     params["price"] = "27012"
    #     params["size"] = "0.01"
    #     params["timInForceValue"] = "normal"
    #     response = maxOrderApi.placeOrder(params)
    #     print(response)
    # except BitgetAPIException as e:
    #     print("error:" + e.message)
    #
    # # Demo 2:place order by post directly
    # baseApi = baseApi.BitgetApi(apiKey, secretKey, passphrase)
    # try:
    #     params = {}
    #     params["symbol"] = "BTCUSDT_UMCBL"
    #     params["marginCoin"] = "USDT"
    #     params["side"] = "open_long"
    #     params["orderType"] = "limit"
    #     params["price"] = "27012"
    #     params["size"] = "0.01"
    #     params["timInForceValue"] = "normal"
    #     response = baseApi.post("/api/mix/v1/order/placeOrder", params)
    #     print(response)
    # except BitgetAPIException as e:
    #     print("error:" + e.message)

    # Demo 3:send get request
    try:
        params = {}
        params["productType"] = "umcbl"
        response = baseApi.get("/api/mix/v1/market/contracts", params)
        print(response)
    except BitgetAPIException as e:
        print("error:" + e.message)

    # Demo 4:send get request with no params
    try:
        response = baseApi.get("/api/spot/v1/account/getInfo", {})
        print(response)
    except BitgetAPIException as e:
        print("error:" + e.message)

    # Demo 5:send get request
    try:
        params = {}
        params["symbol"] = "AIUSDT"
        params["businessType"] = "spot"
        response = baseApi.get("/api/v2/common/trade-rate", params)
        print(response)
    except BitgetAPIException as e:
        print("error:" + e.message)
