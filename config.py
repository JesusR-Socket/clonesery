#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5632637250:AAGFioU6gw87mIUiGT8XjU1gIIHN9E6Ky8c")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "12225868"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "ba4a6dfd31791f14316312a46584437b")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AgC6jUwAdQ7NZs46p8jaMrDPr928im7vhHvSTbvv_aNfhm4ZgKuj8hyXQQpK3SaQCX7WLcGavIp1Xp_8gAP5xbmjEoDgXNNSzTlmag0JATpwaKS8_6fvsdx7ezJ8SZEMuTXcq4B0WhTBg4bJPnD8f3V93hxNWHc0U6cCW1IHduhAH3vIntAubMGcM_Tf2vDHEU8o0OpDKBsZ7Gd_nbIoC7WeFZ_wWs7scEFMRZhxbV_r4dgPBzxUVY7B9IeFh3IaUSmd9g_OrIwNPOxxEOSWPZDvcjvoS6K9lLuyuUxEq9LGPtutsgOZDUpPR97wha6pKOXxhLKoDxrNnHcHprum3V6")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgresql://sery:xtcz1324@localhost:5432/serydb")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
