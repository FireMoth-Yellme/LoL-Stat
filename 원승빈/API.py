import requests
import json
from time import sleep

def init():
    global PRIVATE_KEY,QUEUE,TIER ,DIVISION,PAGE,SUMMONER_NAME,ACCOUNT_ID,COUNT,FILE_NAME,PUUID_FILE_NAME,MATCH_FILE_NAME,MATCH_DATA_FILE_NAME,SUMMONER_FILE_NAME,LENGTH_OF_REQUESTS,MATCH_COUNT,MATCH_TIMELINE_FILE_NAME
    PRIVATE_KEY = "RGAPI-6469837c-d690-4459-9d06-0ab2838c3e08"
    QUEUE       = "RANKED_SOLO_5x5"
    TIER        = "GOLD"
    DIVISION    = "III"
    PAGE        = "1"
    SUMMONER_NAME = "대마법사 김알트"
    ACCOUNT_ID = "daL9coVEk8d9KF710CZ4CCXr8_zETFdOZP9IBT5onHu3"
    #PUUID = "-5nPSbE4z1TqnJjrJmNsCN6TjtApWg5n75c6UfaQQs2WvwPWyr7XqksDBqNlPnAA93YH1-Gxh79wmA"

    FILE_NAME               = "data_summoner_{tier}_{division}_{queue}.json".format(tier=TIER, division=DIVISION, queue=QUEUE)
    PUUID_FILE_NAME         = "data_summoner_puuid_{tier}_{division}_{queue}.json".format(tier=TIER, division=DIVISION, queue=QUEUE)
    MATCH_FILE_NAME         = "data_summoner_match_{name}.json".format(name=SUMMONER_NAME)
    MATCH_DATA_FILE_NAME    = "data_summoner_match_data_{name}.json".format(name=SUMMONER_NAME)
    MATCH_TIMELINE_FILE_NAME = "data_summoner_timeline_data_{name}.json".format(name=SUMMONER_NAME)
    SUMMONER_FILE_NAME      = "data_summoner_info_{summonername}.json".format(summonername=SUMMONER_NAME)

    LENGTH_OF_REQUESTS = 0
    MATCH_COUNT = 0

# GET function
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

