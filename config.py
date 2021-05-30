import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "1877823049:AAHwk3MsNz7SZ-gH5tAYF3K82Dg_37HmwD0")
API_ID = int(os.environ.get("API_ID", 3900425))
API_HASH = os.environ.get("API_HASH", "1affe5d43671e10d86514330afe05028")
RESULTS_COUNT = int(os.environ.get("RESULTS_COUNT", 4))  # NOTE Number of results to show, 4 is better
SUDO_CHATS_ID = list(set(int(x) for x in os.environ.get("SUDO_CHATS_ID", "-1001136335119 -1001491774644").split()))
DRIVE_NAME = list(set(x for x in os.environ.get("1","Leech","TorrentLeech-Gdrive","May 2021","Leecher bot","TorrentLeech-Gdrive","TV Series","Shared Drive-2","Shared Drive","Mirror-2").split(",")))
DRIVE_ID = list(set(x for x in os.environ.get("DRIVE_ID","1tjT2mhPyOcf0mJjqbp1Qr0oR3PVOPnxM 1SrbdybfP0gB8HNup2uPMYzvidT10o2qW 18KkorUfSsPeN1TqpztHJGSkEpyPTSMtw 1-g6tlpSVbBqxzShOxX8wmEESzHXpffNU 18VMVflo4Q3895R7g7D3eac_5fAxGHLa4 14Uh1iodnWTqajJS9kwJP__gR8CEOZTVu 10CQK99lACCb-e_LSDOEWpjzMt7jUKmpN 1V7gapOG9FvvVqv7qj2IfpBhY119JaWaO 1SzDm2O7WG8jPycG0j3PCEJBeUmvTfUVX 1csgdnrvzr3tcbtqnh49igl3t0gbzrggd").split()))

