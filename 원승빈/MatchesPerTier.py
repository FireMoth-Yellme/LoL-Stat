from API import *
import pandas as pd
import json

# BRONZE I~IV의 소환사 각 10명씩
# summoners_BRONZE = pd.read_csv("data/{}".format(FILE_NAME_BRONZE_SUMMONERS))
# puuid_BRONZE = summoners_BRONZE.values.tolist() #dataframe상태로는 쓰기가 힘들어서 list로 변환
# matchid_BRONZE = [[0]*10 for x in range(40)]
# index = 0
# for arr_puuid in puuid_BRONZE:
#     for puuid in arr_puuid:
#         url = GET("asia", "/lol/match/v5/matches/by-puuid/{puuid}/ids?type={type}&count={count}".
#                   format(puuid=puuid, type="ranked", count=10), True)
#         res = requests.get(url)
#         if ++LENGTH_OF_REQUESTS % 20 == 0:
#             sleep(1)
#             if LENGTH_OF_REQUESTS == 100:
#                 sleep(120)
#                 LENGTH_OF_REQUESTS = 0
#
#         if res.status_code == 200:
#             matches = json.loads(res.text)
#         else:
#             print("error : {code}".format(code=res.status_code))
#         if len(matches) > 0:
#             matchid_BRONZE[index] = matches
#         index += 1
# pd.DataFrame(matchid_BRONZE).to_csv("data/{}".format(FILE_NAME_BRONZE_MATCHES), index=False)

# SILVER I~IV의 소환사 각 10명씩
summoners_SILVER = pd.read_csv("data/{}".format(FILE_NAME_SILVER_SUMMONERS))
puuid_SILVER = summoners_SILVER.values.tolist() #dataframe상태로는 쓰기가 힘들어서 list로 변환
matchid_SILVER = [[0]*10 for x in range(40)]
index = 0
for arr_puuid in puuid_SILVER:
    for puuid in arr_puuid:
        url = GET("asia", "/lol/match/v5/matches/by-puuid/{puuid}/ids?type={type}&count={count}".
                  format(puuid=puuid, type="ranked", count=10), True)
        res = requests.get(url)
        if ++LENGTH_OF_REQUESTS % 20 == 0:
            sleep(1)
            if LENGTH_OF_REQUESTS == 100:
                sleep(120)
                LENGTH_OF_REQUESTS = 0

        if res.status_code == 200:
            matches = json.loads(res.text)
        else:
            print("error : {code}".format(code=res.status_code))
        if len(matches) > 0:
            matchid_SILVER[index] = matches
        index += 1
pd.DataFrame(matchid_SILVER).to_csv("data/{}".format(FILE_NAME_SILVER_MATCHES), index=False)

# GOLD I~IV의 소환사 각 10명씩
summoners_GOLD = pd.read_csv("data/{}".format(FILE_NAME_GOLD_SUMMONERS))
puuid_GOLD = summoners_GOLD.values.tolist() #dataframe상태로는 쓰기가 힘들어서 list로 변환
matchid_GOLD = [[0]*10 for x in range(40)]
index = 0
for arr_puuid in puuid_GOLD:
    for puuid in arr_puuid:
        url = GET("asia", "/lol/match/v5/matches/by-puuid/{puuid}/ids?type={type}&count={count}".
                  format(puuid=puuid, type="ranked", count=10), True)
        res = requests.get(url)
        if ++LENGTH_OF_REQUESTS % 20 == 0:
            sleep(1)
            if LENGTH_OF_REQUESTS == 100:
                sleep(120)
                LENGTH_OF_REQUESTS = 0

        if res.status_code == 200:
            matches = json.loads(res.text)
        else:
            print("error : {code}".format(code=res.status_code))
        if len(matches) > 0:
            matchid_GOLD[index] = matches
        index += 1
pd.DataFrame(matchid_GOLD).to_csv("data/{}".format(FILE_NAME_GOLD_MATCHES), index=False)