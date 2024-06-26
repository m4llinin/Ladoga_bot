import asyncio
import logging

from aiogram.types import BotCommand

from config.settings import bot, dp
from handlers import register_handlers

logger = logging.getLogger(__name__)


async def main():
    register_handlers(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    return await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
