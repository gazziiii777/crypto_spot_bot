import asyncio

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.tg.keyboards as kb
import app.tg.message_text as message_data
import app.bitget_spot.bitget_wallet_data as bitget_wallet
import app.bitget_spot.bitget_market_data as bitget_market
import app.mexc_spot.mexc_wallet_data as mexc_wallet
import app.mexc_spot.mexc_market_data as mexc_market

router = Router()

message_text = message_data.MessageText()

bitget_wallet_data = bitget_wallet.BitgetWalletData()
bitget_market_data = bitget_market.BitgetMarketData()

mexc_wallet_data = mexc_wallet.MexcWalletData()
mexc_market_data = mexc_market.MexcMarketdata()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Првиет!',
                         reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('/help')


@router.message(F.text == 'Баланс')
async def button_get_balance(message: Message):
    async def bitget_balance_task():
        params = {
            "wallet_balance_func": bitget_wallet_data.get_wallet_balance,
            "market_first_binds_func": bitget_market_data.get_first_binds,
            "exchange": "Bitget",
            "balance": "data",
            "coin": "coin",
            "available": "available"
        }
        bitget_message_text = await message_text.wallet_text(params)
        await message.answer(bitget_message_text)

    async def mexc_balance_task():
        params = {
            "wallet_balance_func": mexc_wallet_data.get_wallet_balance,
            "market_first_binds_func": mexc_market_data.get_first_binds,
            "exchange": "Mexc",
            "balance": "balances",
            "coin": "asset",
            "available": "free"
        }
        mexc_message_text = await message_text.wallet_text(params)

        await message.answer(mexc_message_text)

    await asyncio.gather(bitget_balance_task(), mexc_balance_task())
