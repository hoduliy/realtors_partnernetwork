# Хэндлеры для пользователей с обычным статусом
"""
Основной файл
Состоит из функций-обработчиков с декораторами
"""

from aiogram import types, F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command

from database.methods import execute_db_func

# Импортируем наши клавиатуры
import keyboards.keyboard_utils as kb

# Создаем роутер, дальше будем привязывать к нему обработчики
router = Router()


@router.message(Command("start"))
async def handler_start(msg: Message, pool):
    # Пользователь уже зарегистрирован в системе
    if await execute_db_func(pool, "CHECK_REGISTER_USER", {"ID": msg.from_user.id}):
        # msg.answer аналогично bot.send_message(msg.chat.id, "ТЕКСТ")
        await msg.answer(
            text="C возвращением, " + msg.from_user.first_name + "! Вы уже зарегистрированы в системе",
            reply_markup=kb.kb_open_webapp
        )
    else:
        # msg.answer аналогично bot.send_message(msg.chat.id, "ТЕКСТ")
        await msg.answer(f"Приветствую, {msg.from_user.first_name}! Этот бот есть реферальная система для риелторов по продаже и аренде недвижимости")
        await msg.answer(
            text="Для продолжения работы необходимо зарегистрироваться в системе",
            reply_markup=kb.kb_register
        )


@router.callback_query(F.data.startswith("register_"))
async def handler_pre_register(callback: CallbackQuery, pool):
    if "realtor" in callback.data:
        await callback.message.edit_text(
            text="Вы решили стать риелтором. Далее должен быть агентский договор, но пока просто нажмите на кнопку :)",
            reply_markup=kb.kb_approval_realtor
        )
    elif "seller" in callback.data:
        await callback.message.edit_text(
            text="Вы решили стать продавцом. Далее должно быть пользовательское соглашение, но пока просто нажмите на кнопку :)",
            reply_markup=kb.kb_approval_seller
        )
    await callback.answer()


@router.callback_query(F.data.startswith("approval_"))
async def handler_pre_register(callback: CallbackQuery, pool):
    if "realtor" in callback.data:
        await execute_db_func(
            pool=pool,
            name="REGISTER_NEW_USER",
            params={
                "ID": callback.from_user.id,
                "LAST_NAME": callback.from_user.last_name,
                "FIRST_NAME": callback.from_user.first_name,
                "ROLE_NAME": "realtor"
            }
        )
        await callback.message.answer(
            text="Поздравляем, " + callback.from_user.first_name +"! Вы зарегистрированы в системе в качестве риелтора",
            reply_markup=kb.kb_open_webapp
        )
    elif "seller" in callback.data:
        await execute_db_func(
            pool=pool,
            name="REGISTER_NEW_USER",
            params={
                "ID": callback.from_user.id,
                "LAST_NAME": callback.from_user.last_name,
                "FIRST_NAME": callback.from_user.first_name,
                "ROLE_NAME": "seller"
            }
        )
        await callback.message.answer(
            text="Поздравляем, " + callback.from_user.first_name + "! Вы зарегистрированы в системе в качестве продавца",
            reply_markup=kb.kb_open_webapp
        )

    await callback.answer()





@router.message()
async def handler_any_message(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")
