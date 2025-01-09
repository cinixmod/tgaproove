# Rym-Approval By @RymOfficial

from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    CHID = int(getenv("CHID", "")) # Make Bot Admin In This Channel
    SUDO = list(map(int, getenv("SUDO", "5038784553").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()

# Rym-Approval By @RymOfficial
