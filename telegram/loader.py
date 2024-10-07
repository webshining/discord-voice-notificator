from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.utils.i18n import I18n
from aiogram.fsm.storage.memory import MemoryStorage

from config import I18N_DOMAIN, I18N_PATH
from tgconfig import TELEGRAM_BOT_TOKEN

bot = Bot(
    TELEGRAM_BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML, link_preview_is_disabled=True
    ),
)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


i18n = I18n(path=I18N_PATH, domain=I18N_DOMAIN)
_ = i18n.gettext


rabbit_connection = None
rabbit_channel = None
