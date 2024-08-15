# Вспомогательные функции/методы, помогающие формировать клавиатуры

# Импорт методов для кнопок и клавиатур
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


# ============= Клавиатура для пре-регистрации в боте ========================

kb_register = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Я риелтор", callback_data="register_realtor")],
        [InlineKeyboardButton(text="Я продавец", callback_data="register_seller")]
    ]
)

# ====== Клавиатура подтверждения соглашения для риелтора ===============

kb_approval_realtor = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Я согласен", callback_data="approval_realtor")]
    ]
)

# ====== Клавиатура подтверждения соглашения для продавца ===============

kb_approval_seller = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Я согласен", callback_data="approval_seller")]
    ]
)

# ================ Клавиатура для входа в WebApp ========================

kb_open_webapp = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Запустить", web_app=WebAppInfo(url='https://hoduliy.github.io/realtors_partnernetwork/index.html'))],
        [InlineKeyboardButton(text="Официальный чат", url='https://buhlovo-park.ru/')]
    ]
)
