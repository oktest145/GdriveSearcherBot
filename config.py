import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "1877823049:AAHwk3MsNz7SZ-gH5tAYF3K82Dg_37HmwD0")
API_ID = int(os.environ.get("API_ID", 3900425))
API_HASH = os.environ.get("API_HASH", "1affe5d43671e10d86514330afe05028")
RESULTS_COUNT = int(os.environ.get("RESULTS_COUNT", 4))  # NOTE Number of results to show, 4 is better
SUDO_CHATS_ID = list(set(int(x) for x in os.environ.get("SUDO_CHATS_ID", "-1001136335119 -1001491774644").split()))
DRIVE_NAME = list(set(x for x in os.environ.get("TorrentLeech-Gdrive,"Leecher bot","Mirror-2").split(",")))
DRIVE_ID = list(set(x for x in os.environ.get("DRIVE_ID","").split()))
INDEX_URL = list(set(x for x in os.environ.get("INDEX_URL", "").split()))
