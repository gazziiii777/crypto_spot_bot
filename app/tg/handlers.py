import asyncio

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.tg.keyboards as kb
import app.bitget_spot.bitget_wallet_data as bitget_wallet
import app.bitget_spot.bitget_market_data as bitget_market
import app.mexc_spot.mexc_wallet_data as mexc_wallet

router = Router()

bitget_wallet_data = bitget_wallet.BitgetWalletData()
bitget_market_data = bitget_market.BitgetMarketData()

mexc_wallet_data = mexc_wallet.MexcWalletData()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Првиет!',
                         reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('/help')


@router.message(F.text == 'Баланс')
async def button_get_balance(message: Message):
    async def task1():
        bitget_total_balance = 0
        text = 'Bitget Кошелек: \n'
        bitget_balance = await asyncio.to_thread(bitget_wallet_data.get_wallet_balance)
        for item in bitget_balance['data']:  # бежим по нашему ответу (по каждой монетке)
            coin = item['coin']
            available = round(float(item['available']), 2)
            coin_bids = await asyncio.to_thread(bitget_market_data.get_first_binds, coin + "USDT")  # получаем перовое значение цены или строчку
            if type(coin_bids) is not str:  # Проверяем, продается ли эта монета на spot, если нет, то мы просто пропускаем
                coin_price_in_usdt = round(float(available) * float(coin_bids['data']['bids'][0][0]),
                                           2)  # Узнаем цену монеты в USDT
                if coin_price_in_usdt > 0.5:  # Проверяем, если у нас на кошельке монет больше чем на 0.5$, то выводим ее
                    text += f'<b>{available} ${coin}</b> ~ {coin_price_in_usdt}$\n'
                    bitget_total_balance += coin_price_in_usdt
            else:
                if coin == 'USDT':
                    bitget_total_balance += available
                    text += f'<b>{available} ${coin}</b> ~ {available}$\n'
                else:
                    text += f'<b>{available} ${coin}</b> ❗️{coin_bids}❗️\n'
        text += f'Всего ~ {round(bitget_total_balance, 2)}$'
        await message.answer(text)

    async def task2():
        print(1)
        a = await mexc_wallet_data.get_wallet_balance()
        await message.answer(str(a))

    await asyncio.gather(task1(), task2())
