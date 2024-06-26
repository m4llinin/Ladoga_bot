__all__ = ['register_handlers']

from aiogram import Router
from aiogram.filters import Command

from filters.is_admin import IsAdmin

from .user_panel import register_users_handlers
from .admin_panel import register_admin_handlers
from .admin_panel.admin import admin


def register_handlers(router: Router):
    router.message.register(admin, IsAdmin(), Command("admin"))

    register_admin_handlers(router)
    register_users_handlers(router)
