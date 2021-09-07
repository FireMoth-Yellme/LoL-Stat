import requests
import json
from time import sleep

PRIVATE_KEY = "비-밀"

# API의 각종 parameter 값들을 지정해줍니다.
QUEUE       = "RANKED_SOLO_5x5"
TIER        = "PLATINUM"
DIVISION    = "III"
PAGE        = "1"

USERNAME    = "야식은치킨이지"

# 위에서 설정한 매개변수에 따라 파일 이름을 미리 만들어줍니다.
FILE_NAME                           = "data_summoner_{tier}_{division}_{queue}.json".format(tier=TIER, division=DIVISION, queue=QUEUE)
FILE_NAME_BY_SUMMONER               = "data_summoner_{username}.json".format(username=USERNAME)
PUUID_FILE_NAME                     = "data_summoner_puuid_{tier}_{division}_{queue}.json".format(tier=TIER, division=DIVISION, queue=QUEUE)
MATCH_FILE_NAME                     = "data_summoner_match_{tier}_{division}_{queue}.json".format(tier=TIER, division=DIVISION, queue=QUEUE)
MATCH_FILE_NAME_BY_SUMMONER         = "data_summoner_match_{username}.json".format(username=USERNAME)
MATCH_DATA_FILE_NAME                = "data_summoner_match_data_{tier}_{division}_{queue}.json".format(tier=TIER, division=DIVISION, queue=QUEUE)
MATCH_DATA_FILE_NAME_BY_SUMMONER    = "data_summoner_match_data_{username}.json".format(username=USERNAME)

# Too Many Requests를 방지하기 위해 보낸 request 횟수를 셉니다.
LENGTH_OF_REQUESTS = 0

# GET function - query가 있다면 optional에 True를 넣어줍니다.
def GET(country, api, optional):
    if optional:
        url = "https://{country}.api.riotgames.com/{api}&api_key={key}".format(
            country = country,
            api = api,
            key = PRIVATE_KEY
        )
    else:
        url = "https://{country}.api.riotgames.com/{api}?api_key={key}".format(
            country = country,
            api = api,
            key = PRIVATE_KEY
        )
    return url