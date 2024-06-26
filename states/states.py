from aiogram.fsm.state import StatesGroup, State


class Back(StatesGroup):
    activities = State()
    price_list = State()


class Text(StatesGroup):
    text = State()
