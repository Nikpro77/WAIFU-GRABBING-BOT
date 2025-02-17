class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1993048420"
    sudo_users = "1993048420", "5743248220", "1214348787", "5296961281"
    GROUP_ID = -1002023287369
    TOKEN = "8007953001:AAGWnhke82WRdBg6DQwa7oomBoEst1JjLnI"
    mongo_url = "mongodb+srv://niksharma92297:wWaifu@cluster0.ywgti.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://files.catbox.moe/m4g43m.jpg", "https://files.catbox.moe/1giocq.jpg", "https://files.catbox.moe/yj0rvl.jpg"]
    SUPPORT_CHAT = "waifu_support_group"
    UPDATE_CHAT = "waifu_support_group"
    BOT_USERNAME = "Waifu_Grabbing_robot"
    CHARA_CHANNEL_ID = "-1002003134505"
    api_id = 22867431
    api_hash = "24ef0e76ceb137563dc33722e4cd79bd"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
