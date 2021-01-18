import os
from urllib import parse
from arenaclient.match.matches import HttpApiMatchSource
# docker run -it --entrypoint /bin/bash -v D:\proj\aiarena-client\arenaclient\configs\config_dev.py:/root/aiarena-client/config.py --name AC 6266ef93e52b
ARENA_CLIENT_ID = "ac_name"
API_TOKEN = "ac_key"

ROUNDS_PER_RUN = 1
BASE_WEBSITE_URL = "api_endpoint"
API_MATCHES_URL = parse.urljoin(BASE_WEBSITE_URL, "/api/arenaclient/matches/")
API_RESULTS_URL = parse.urljoin(BASE_WEBSITE_URL, "/api/arenaclient/results/")
API_SET_STATUS_URL = parse.urljoin(BASE_WEBSITE_URL, "/api/arenaclient/set-status/")
MATCH_SOURCE_CONFIG = HttpApiMatchSource.HttpApiMatchSourceConfig(api_url=BASE_WEBSITE_URL,api_token=API_TOKEN)

# PATHS AND FILES
TEMP_PATH = "/tmp/aiarena/"
LOCAL_PATH = os.path.dirname(__file__)
WORKING_DIRECTORY = LOCAL_PATH  # same for now
LOG_FILE = os.path.join(WORKING_DIRECTORY, "../aiarena-client.log")
# LOG_FILE = "/root/aiarena-client.log"
REPLAYS_DIRECTORY = os.path.join(WORKING_DIRECTORY, "../replays")
BOTS_DIRECTORY = os.path.join(WORKING_DIRECTORY, "../bots")
CLEAN_BOT_DIRECTORIES_BEFORE_MATCH_START = False
SC2_HOME = "/root/StarCraftII/"
MAX_GAME_TIME = 80640