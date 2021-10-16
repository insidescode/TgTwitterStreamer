# Telegram - Twitter - Bot
# Github.com/New-dev0/TgTwitterStreamer
# GNU General Public License v3.0


from Configs import Var

REPO_LINK = "https://t.me/Aarzaai_Ishq"


CUSTOM_FORMAT = """🎊 **[Aarz-e-ishq](https://t.me/Aarzaai_Ishq)** :

🍿 {TWEET_TEXT}

• Follow **[Aarzaai_Ishq]({_REPO_LINK})**"""


if not Var.CUSTOM_TEXT:
    Var.CUSTOM_TEXT = CUSTOM_FORMAT
