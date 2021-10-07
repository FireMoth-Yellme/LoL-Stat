from API import *
import pandas as pd
import json
import ast

### get matchesId
matchId_BRONZE = pd.read_csv("data/{}".format(FILE_NAME_BRONZE_MATCHES)).values.tolist()
if len(matchId_BRONZE) > 0:
    print("read successfully : {length}".format(length=len(matchId_BRONZE)))
else:
    print('error')
matchId_SILVER = pd.read_csv("data/{}".format(FILE_NAME_SILVER_MATCHES)).values.tolist()
if len(matchId_SILVER) > 0:
    print("read successfully : {length}".format(length=len(matchId_BRONZE)))
else:
    print('error')
matchId_GOLD = pd.read_csv("data/{}".format(FILE_NAME_GOLD_MATCHES)).values.tolist()
if len(matchId_GOLD) > 0:
    print("read successfully : {length}".format(length=len(matchId_BRONZE)))
else:
    print('error')

# get timelinedata
# data_BRONZE = []
# for arr_matchId in matchId_BRONZE:
#     for i in range(3):
#         matchId = arr_matchId[i]
#         url = GET("asia", "/lol/match/v5/matches/{matchId}/timeline".format(matchId=matchId), False)
#         res = requests.get(url)
#         if ++LENGTH_OF_REQUESTS % 20 == 0:
#             sleep(1)
#             if LENGTH_OF_REQUESTS == 100:
#                 sleep(120)
#                 LENGTH_OF_REQUESTS = 0
#         if res.status_code == 200:
#             json_data = json.loads(res.text)
#             data_BRONZE.append(json_data)
#         else:
#             print("error : {code} where {matchId}".format(code=res.status_code, matchId=matchId))
#
# if len(data_BRONZE) > 0:
#     print("read successfully : {length}".format(length=len(data_BRONZE)))
#     with open("data/{}".format(FILE_NAME_BRONZE_TIMELINE), 'w') as outfile:
#         json.dump(data_BRONZE, outfile, indent=4)
# else:
#     print('error')

# SILVER
data_SILVER = []
for arr_matchId in matchId_SILVER:
    for i in range(3):
        matchId = arr_matchId[i]
        url = GET("asia", "/lol/match/v5/matches/{matchId}/timeline".format(matchId=matchId), False)
        res = requests.get(url)
        if ++LENGTH_OF_REQUESTS % 20 == 0:
            sleep(1)
            if LENGTH_OF_REQUESTS == 100:
                sleep(120)
                LENGTH_OF_REQUESTS = 0
        if res.status_code == 200:
            json_data = json.loads(res.text)
            data_SILVER.append(json_data)
        else:
            print("error : {code} where {matchId}".format(code=res.status_code, matchId=matchId))

if len(data_SILVER) > 0:
    print("read successfully : {length}".format(length=len(data_SILVER)))
    with open("data/{}".format(FILE_NAME_SILVER_DATA), 'w') as outfile:
        json.dump(data_SILVER, outfile, indent=4)
else:
    print('error')

# GOLD
data_GOLD = []
for arr_matchId in matchId_GOLD:
    for i in range(3):
        matchId = arr_matchId[i]
        url = GET("asia", "/lol/match/v5/matches/{matchId}/timeline".format(matchId=matchId), False)
        res = requests.get(url)
        if ++LENGTH_OF_REQUESTS % 20 == 0:
            sleep(1)
            if LENGTH_OF_REQUESTS == 100:
                sleep(120)
                LENGTH_OF_REQUESTS = 0
        if res.status_code == 200:
            json_data = json.loads(res.text)
            data_GOLD.append(json_data)
        else:
            print("error : {code} where {matchId}".format(code=res.status_code, matchId=matchId))

if len(data_GOLD) > 0:
    print("read successfully : {length}".format(length=len(data_GOLD)))
    with open("data/{}".format(FILE_NAME_GOLD_DATA), 'w') as outfile:
        json.dump(data_GOLD, outfile, indent=4)
else:
    print('error')