from aiogram.dispatcher.filters.state import State, StatesGroup


class DistributionState(StatesGroup):
    WaitForMedia = State()
    ConfirmMedia = State()
