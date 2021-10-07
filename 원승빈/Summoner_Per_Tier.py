import requests

from API import *
import pandas as pd
import json

# get summoner data of BRONZE I~IV
# for i in range(4):
#     url = GET("kr", "/lol/league/v4/entries/{queue}/{tier}/{division}".format(queue = QUEUE, tier = BRONZE, division = DIVISIONS[i]), False)
#     res = requests.get(url)
#     if res.status_code == 200:
#         json_data = json.loads(res.text)
#         print("read successfully : {length}".format(length=len(json_data)))
#         with open(FILE_NAME_BRONZE[i], 'w') as outfile:
#             json.dump(json_data, outfile, indent=4)
#     else:
#         print("error")
# # get summoners of BRONZE I~IV
puuid_BRONZE = [[0]*10 for x in range(4)]
for i in range(4):
    with open("data/{}".format(FILE_NAME_BRONZE[i]), "r") as json_file:
        summoners = pd.read_json(json_file)
        summonerId = summoners["summonerId"]
    if len(summonerId) > 0:
        for j in range(10):
            url = GET("kr", "/lol/summoner/v4/summoners/{encryptedSummonerId}".format(encryptedSummonerId=summonerId[j]),False)
            res = requests.get(url)
            if res.status_code == 200:
                if ++LENGTH_OF_REQUESTS % 20 == 0:
                    sleep(1)
                if LENGTH_OF_REQUESTS == 100:
                    sleep(120)
                    LENGTH_OF_REQUESTS = 0
                json_data = json.loads(res.text)
                print("read successfully : {length}".format(length=len(json_data)))
                puuid_BRONZE[i][j] = json_data['puuid']
    else:
        print('error')
pd.DataFrame(puuid_BRONZE).to_csv("data/{}".format(FILE_NAME_BRONZE_SUMMONERS), index=False)
#
#
# # SILVER
# for i in range(4):
#     url = GET("kr", "/lol/league/v4/entries/{queue}/{tier}/{division}".format(queue = QUEUE, tier = SILVER, division = DIVISIONS[i]), False)
#     res = requests.get(url)
#     if res.status_code == 200:
#         json_data = json.loads(res.text)
#         print("read successfully : {length}".format(length=len(json_data)))
#
#         with open(FILE_NAME_SILVER[i], 'w') as outfile:
#             json.dump(json_data, outfile, indent=4)
#     else:
#         print("error")

# puuid_SILVER = [[0]*10 for x in range(4)]
# for i in range(4):
#     with open("data/{}".format(FILE_NAME_SILVER[i]), "r") as json_file:
#         summoners = pd.read_json(json_file)
#         summonerId = summoners["summonerId"]
#     if len(summonerId) > 0:
#         for j in range(10):
#             url = GET("kr", "/lol/summoner/v4/summoners/{encryptedSummonerId}".format(encryptedSummonerId=summonerId[j]),False)
#             res = requests.get(url)
#             if res.status_code == 200:
#                 if ++LENGTH_OF_REQUESTS % 20 == 0:
#                     sleep(1)
#                     if LENGTH_OF_REQUESTS == 100:
#                         sleep(120)
#                         LENGTH_OF_REQUESTS = 0
#                 json_data = json.loads(res.text)
#                 print("read successfully : {length}".format(length=len(json_data)))
#                 puuid_SILVER[i][j] = json_data['puuid']
#             else:
#                 print("error")
#     else:
#         print('error')
# pd.DataFrame(puuid_SILVER).to_csv("data/{}".format(FILE_NAME_SILVER_SUMMONERS), index=False)

# GOLD
# for i in range(4):
#     url = GET("kr", "/lol/league/v4/entries/{queue}/{tier}/{division}".format(queue = QUEUE, tier = GOLD, division = DIVISIONS[i]), False)
#     res = requests.get(url)
#     if res.status_code == 200:
#         json_data = json.loads(res.text)
#         print("read successfully : {length}".format(length=len(json_data)))
#         with open(FILE_NAME_GOLD[i], 'w') as outfile:
#             json.dump(json_data, outfile, indent=4)
#     else:
#         print("error")
puuid_GOLD = [[0]*10 for x in range(4)]
for i in range(4):
    with open("data/{}".format(FILE_NAME_GOLD[i]), "r") as json_file:
        summoners = pd.read_json(json_file)
        summonerId = summoners["summonerId"]
    if len(summonerId) > 0:
        for j in range(10):
            url = GET("kr", "/lol/summoner/v4/summoners/{encryptedSummonerId}".format(encryptedSummonerId=summonerId[j]),False)
            res = requests.get(url)
            if res.status_code == 200:
                if ++LENGTH_OF_REQUESTS % 20 == 0:
                    sleep(1)
                    if LENGTH_OF_REQUESTS == 100:
                        sleep(120)
                        LENGTH_OF_REQUESTS = 0
                json_data = json.loads(res.text)
                print("read successfully : {length}".format(length=len(json_data)))
                puuid_GOLD[i][j] = json_data['puuid']
    else:
        print('error')
pd.DataFrame(puuid_GOLD).to_csv("data/{}".format(FILE_NAME_GOLD_SUMMONERS), index=False)
