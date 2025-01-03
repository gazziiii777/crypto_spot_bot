import asyncio


class MessageText:

    @staticmethod
    async def wallet_text(params: dict):
        total_balance = 0
        message_text = f'{params['exchange']} Кошелек: \n'
        balance = await asyncio.to_thread(params['wallet_balance_func'])
        for item in balance[params['balance']]:  # бежим по нашему ответу (по каждой монетке)
            coin = item[params['coin']]
            available = round(float(item[params['available']]), 2)
            coin_bids = await asyncio.to_thread(params['market_first_binds_func'],
                                                coin)  # получаем перовое значение цены или строчку
            if coin_bids:  # Проверяем, продается ли эта монета на spot, если нет, то мы просто пропускаем
                coin_price_in_usdt = round(float(available) * float(coin_bids), 2)  # Узнаем цену монеты в USDT
                if coin_price_in_usdt > 0.5:  # Проверяем, если у нас на кошельке монет больше чем на 0.5$, то выводим ее
                    message_text += f'<b>{available} ${coin}</b> ~ {coin_price_in_usdt}$\n'
                    total_balance += coin_price_in_usdt
            else:
                if coin == 'USDT':
                    total_balance += available
                    message_text += f'<b>{available} ${coin}</b> ~ {available}$\n'
                else:
                    message_text += f'<s><b>{available} {coin}</b> ❗️</s>\n'
        message_text += f'Всего ~ {round(total_balance, 2)}$'
        return message_text
