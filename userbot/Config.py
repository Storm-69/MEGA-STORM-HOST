import os
from telethon.tl.types import ChatBannedRights
ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os
    class Config(object):
        LOGGER = True
 
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", False)
        HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", False)
 
        DB_URI = os.environ.get("DATABASE_URL", None)

        COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\.")

        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
        SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\.")
     
        UPSTREAM_REPO = os.environ.get(
            "UPSTREAM_REPO", "https://github.com/H1M4N5HU0P/MAFIABOT"
        )
        STRING_SESSION = os.environ.get("STRING_SESSION", None)
        ALIVE_NAME = os.environ.get("ALIVE_NAME", False)
else:
    class Config(object):
        DB_URI = None
