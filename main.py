# Точка входа, код запуска бота
# Для асинхронного запуска бота
import asyncio
# Логирование
import logging

# Основной модуль для работы с ботом
from aiogram import Bot, Dispatcher
# Настройки разметки сообщений (HTML, Markdown)
from aiogram.enums.parse_mode import ParseMode
# Хранилища данных для состояний бота
from aiogram.fsm.storage.memory import MemoryStorage
# Дефолтные настройки для разметки сообщений бота
from aiogram.client.default import DefaultBotProperties

# Наш модуль с настройками бота
import config
# Наш модуль с функционалом бота
from handlers import router


async def main():
    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # MemoryStorage - стирать все данные бота при перезапуске
    dp = Dispatcher(storage=MemoryStorage())
    # Подключение всех обработчиков, использующих router
    dp.include_router(router)
    # Удаление всех обновлений, которые были после завершения работы бота
    await bot.delete_webhook(drop_pending_updates=True)
    # Запуск бота в работу
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
