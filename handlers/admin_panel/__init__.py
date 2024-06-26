__all__ = ['register_admin_handlers']

import asyncio

from aiogram import F, Router

from utils import load_texts
from states.states import Text

from .admin import admin_clb
from .edit_text import edit_text, wait_text, get_text, choose_subclass

texts: dict = asyncio.run(load_texts())


def register_admin_handlers(router: Router):
    router.callback_query.register(admin_clb, F.data == "admin")
    router.callback_query.register(edit_text, F.data == "edit_text")
    router.callback_query.register(choose_subclass, F.data == "actions" or F.data == "price_list")
    router.callback_query.register(wait_text)
    router.message.register(get_text, F.text, Text.text)
