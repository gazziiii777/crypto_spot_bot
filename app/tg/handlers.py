from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.tg.keyboards as kb
import app.bitget_spot.bitget_wallet_data as bitget_wallet

router = Router()

bitget_wallet_data = bitget_wallet.WalletData()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Првиет!',
                         reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('/help')


@router.message(F.text == 'Баланс')
async def button_get_balance(message: Message):
    text = ''
    bitget_balance = await bitget_wallet_data.get_wallet_balance()
    for item in bitget_balance['data']:
        coin = item['coin']
        available = round(float(item['available']), 2)
        text += f'<b>{coin}</b>:{available}\n'
    await message.answer(text)
