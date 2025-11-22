import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("8301448875:AAFk8jYF94cIKlRVX4FkMqcxp6hgzjPWoEk", "")

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 31064914))
    API_HASH = os.environ.get("API_HASH", "f6443d977b6ad8979696174c3f6cfd88")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Update channel for force subscription
    UPDATE_CHANNEL = "vkprojects"
    
    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    # Yeh line aapko khud jodna hoga (Kisi bhi jagah)
    ZEE5_COOKIES = "cjConsent=MHxOfDB8Tnww;cjUser=4e8d367e-8d56-46fc-b5ae-e4edc0e67d39;_cnv_id.60de=ac6992ef-f1db-485b-b156-75d431edc0ee.1763792530.2.1763800239.1763794752.6abf4a95-a52a-4bb4-8856-b79b3aadb0c0.48afeedb-51b3-4a2d-9cdc-2ca9843b8ed3..;__eoi=ID=756a51bd3355c55d:T=1763792537:RT=1763792537:S=AA-AfjZD7Z8601_-CBc4FSvaWUt-;__gads=ID=2733b53182138c35:T=1763792537:RT=1763800186:S=ALNI_MZsGKt1fhNtGtjY_tiWPosPA8RjTQ;_cnv_ses.60de=*"

    # Sql Database url
    DB_URI = os.environ.get("DATABASE_URL", "postgresql://serial:serial@localhost:5432/serial_db")
    
