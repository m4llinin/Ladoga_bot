from aiogram.filters import BaseFilter
from aiogram.types import Message

from config.settings import ADMIN_ID


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message):
        if str(message.from_user.id) in ADMIN_ID:
            return True
        return False
