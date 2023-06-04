import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "15717664"))
    API_HASH = os.environ.get("API_HASH", "3088912bd7fc0a996a9d8741c8e68255")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6002579398:AAEva9Gl2fhjIlv496uuX21-oDQbWycK0RE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLcBu2Io7vm3j5s8d9aMkxA22lM-bFGuMf4LJvF2ljuNfgv3rvGdchA5BEqpxPofRWRIqPRl60jiszAjpj43pC-GCy1BBlxVIpHjdmq0WPu1q_0-2pLXsbdKm9z5jDzVFBuPjfDTbSyDoAIKoTXj7aBfgZyd9x948t2IB2ENdzxUqOljLSpHwGkou1APiAnb-otPVbsqylFutozR2vlcfHLPU-4_7bd56Nx_EXAHIsXRq0RejPgeFzJwb3fhdPga1hCANTEcOFdrRqlrzi9tewjuplPpWX7OIKqeHlIYZQmq2S1mcbxKnD9up1NQj4Dqig9xCiXG-hYhSbvcEpiCk-13J2c=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "arsenamusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "fifinafia") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "fafifufi") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5667815815")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
