import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "28268357")
    API_HASH = getenv("API_HASH", "e11e807755eadbc0bf3bb892b6ba11cd")
    TOKEN = getenv("TOKEN", "6691969058:AAEBOYd-7Hqguy2mkT8OV6dRqBQ9SrqANf0")
    OWNER_ID = getenv("OWNER_ID", "7102017280")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "7191474287")
    STRING_SESSION = getenv("STRING_SESSION", "") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "")
    DB_URI = getenv("DATABASE_URL", "")
    DB_URI = DB_URI.replace("postgres", "postgresql")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001928901017")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001928901017")
    SYS_ADMIN = getenv("SYS_ADMIN", "7102017280")
    DEV_USERS = getenv("DEV_USERS", "7102017280")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "TheUpdatesChannel")
    SUPPORT = getenv("SUPPORT", "TheSupportChat")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/a6aec3cd82b490cb5f047.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/a6aec3cd82b490cb5f047.jpg")
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7102017280").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "7102017280").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
