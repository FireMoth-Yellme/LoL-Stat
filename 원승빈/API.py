import requests
import json
from time import sleep

PRIVATE_KEY = "RGAPI-341a91fe-6529-467c-a445-91a275411c18"

# API의 각종 parameter 값들을 지정해줍니다.
QUEUE       = "RANKED_SOLO_5x5"
TIER        = "PLATINUM"
DIVISION    = "III"
PAGE        = "1"
# 각 티어, DIVISION을 나타내는 값들을 선언해줍니다.
DIVISIONS    = ["I","II","III","IV"]
FILE_NAME_BRONZE = ['BRONZE I', 'BRONZE II', 'BRONZE III', 'BRONZE IV']
FILE_NAME_SILVER = ['SILVER I', 'SILVER II', 'SILVER III', 'SILVER IV']
FILE_NAME_GOLD   = ['GOLD I', 'GOLD II', 'GOLD III', 'GOLD IV']
FILE_NAME_BRONZE_SUMMONERS = "BRONZE PUUID"
FILE_NAME_SILVER_SUMMONERS = "SILVER PUUID"
FILE_NAME_GOLD_SUMMONERS   = "GOLD PUUID"
FILE_NAME_BRONZE_MATCHES = "BRONZE MATCHIDS"
FILE_NAME_SILVER_MATCHES = "SILVER MATCHIDS"
FILE_NAME_GOLD_MATCHES   = "SILVER MATCHIDS"

BRONZE = "BRONZE"
SILVER = "SILVER"
GOLD = "GOLD"

USERNAME    = "쪼렙이다말로하자"

# 위에서 설정한 매개변수에 따라 파일 이름을 미리 만들어줍니다.
FILE_NAME                           = "data_summoner_{tier}_{division}_{queue}.json".format(tier=TIER, division=DIVISION, queue=QUEUE)
FILE_NAME_BY_SUMMONER               = "data_summoner_{username}.json".format(username=USERNAME)
PUUID_FILE_NAME                     = "data_summoner_puuid_{tier}_{division}_{queue}.json".format(tier=TIER, division=DIVISION, queue=QUEUE)
MATCH_FILE_NAME                     = "data_summoner_match_{tier}_{division}_{queue}.json".format(tier=TIER, division=DIVISION, queue=QUEUE)
MATCH_FILE_NAME_BY_SUMMONER         = "data_summoner_match_{username}.json".format(username=USERNAME)
MATCH_DATA_FILE_NAME                = "data_summoner_match_data_{tier}_{division}_{queue}.json".format(tier=TIER, division=DIVISION, queue=QUEUE)
MATCH_DATA_FILE_NAME_BY_SUMMONER    = "data_summoner_match_data_{username}.json".format(username=USERNAME)
MATCH_TIMELINE_DATA_FILE_NAME_BY_SUMMONER = "data_summoner_match_timeline_data_{username}.json".format(username=USERNAME)

# Too Many Requests를 방지하기 위해 보낸 request 횟수를 셉니다.
LENGTH_OF_REQUESTS = 0

# GET function - query가 있다면 optional에 True를 넣어줍니다.
def GET(country, api, optional):
    if optional:
        url = "https://{country}.api.riotgames.com{api}&api_key={key}".format(
            country = country,
            api = api,
            key = PRIVATE_KEY
        )
    else:
        url = "https://{country}.api.riotgames.com{api}?api_key={key}".format(
            country = country,
            api = api,
            key = PRIVATE_KEY
        )
    return url