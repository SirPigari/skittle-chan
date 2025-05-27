import discord
import platform

_os_name = platform.system()
_os_version = platform.version()

VERSION = "1.7"
__VERSION__ = "1.7"
CHATGPT_VERSION = "ChatGPT-4o"
DISCORD_BOT_TOKEN=''
CLIENT_ID='1210290698675560499'
CLIENT_SECRET=""
SKITTLE_CHAN_ID=''
COLOR_MAP = {
    "blue": discord.Color.blue(),
    "red": discord.Color.red(),
    "green": discord.Color.green(),
    "yellow": discord.Color.yellow(),
    "purple": discord.Color.purple(),
    "orange": discord.Color.orange(),
    "black": discord.Color.from_rgb(0, 0, 0),
    "white": discord.Color.from_rgb(255, 255, 255),
    "grey": discord.Color.from_srgb(128, 128, 128),
    "pink": discord.Color.from_rgb(255, 192, 203),
    "magenta": discord.Color.from_rgb(255, 0, 255),
    "blurple": discord.Color.blurple()
}
RPC_JOIN=''
PARTY_ID=''
SENDER_EMAIL = ""
SENDER_PASSWORD = ""  # format: xxxx xxxx xxxx xxxx
RECEIVER_EMAIL = ""
DOC_LINK = "Coming Soon"
CURRENT_OS = f"{_os_name}: {_os_version}"
MAIN_SERVER_ID = 1298283195250376834
SERVER_INVITE = "HMd6kNBamr"
ADMIN_ROLE_ID = 1298683444427100171
MOD_ROLE_ID = 1310322279049072680
MEMBER_ROLE_ID = 1298286918450020362
TICKET_CHANNEL_ID = 1310312589972209714
TICKET_MESSAGE_ID = 1310317168281255958
FLASK_SECRET_KEY = ""