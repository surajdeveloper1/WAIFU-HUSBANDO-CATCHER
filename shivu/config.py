class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6087651372"
    sudo_users = "6858718276", "6765826972"
    GROUP_ID = -1002316438413
    TOKEN = "7785998273:AAHER3KsHxhsZG2JFlA9uUOfeY0qwFW8i1c"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "https://t.me/harddubber4"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "@Waifugrab17bot"
    CHARA_CHANNEL_ID = "-1002316438413"
    api_id = 29382589
    api_hash = "0dc22be6e6ab6cc2dcdfbc85001bcab9"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
