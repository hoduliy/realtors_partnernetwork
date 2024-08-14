# Хэндлеры для пользователей с обычным статусом
"""
Основной файл
Состоит из функций-обработчиков с декораторами
"""

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

# Создаем роутер, дальше будем привязывать к нему обработчики
router = Router()


@router.message(Command("start"))
async def handler_start(msg: Message):
    # msg.answer аналогично bot.send_message(msg.chat.id, "ТЕКСТ")
    await msg.answer(f"Приветствую, {msg.from_user.first_name}! Этот бот есть реферальная система для риелторов по продаже и аренде недвижимости")


@router.message()
async def handler_any_message(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")
