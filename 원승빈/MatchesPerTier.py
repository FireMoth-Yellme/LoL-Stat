from API import *
import pandas as pd
import json

# BRONZE I~IV의 소환사 각 10명씩
# summoners_BRONZE = [[0]*10 for i in range(4)]
# for i in range(4):
#     summoners = pd.read_csv("data/{}".format(FILE_NAME_BRONZE_SUMMONERS[i]))
#     summonerId = summoners['summonerId']
#     for j in range(10):
#         summoners_BRONZE[i][j] = summonerId[j]
# print(summoners_BRONZE)

# SILVER I~IV의 소환사 각 10명씩
summoners_SILVER = pd.read_csv("data/{}".format(FILE_NAME_SILVER_SUMMONERS)).iloc[:, 1:] # 1열에 인덱스값이 들어서 제거해줌
puuid_SILVER = summoners_SILVER.values.tolist() #dataframe상태로는 쓰기가 힘들어서 list로 변환
outfile = open(FILE_NAME_SILVER_MATCHES, "w")
outfile.close()
for list in puuid_SILVER:
    for puuid in list:
        url = GET("asia", "lol/match/v5/matches/by-puuid/{puuid}/ids?type={type}&count={count}".
                  format(puuid=puuid, type="ranked", count=10), True)
        print(url)
        # res = requests.get(url)
        # if ++LENGTH_OF_REQUESTS % 20 == 0:
        #     sleep(1)
        #     if LENGTH_OF_REQUESTS == 100:
        #         sleep(120)
        #         LENGTH_OF_REQUESTS = 0
        #
        # if res.status_code == 200:
        #     matches = json.loads(res.text)
        # else:
        #     print("error : {code}".format(code=res.status_code))
        # if len(matches) > 0:
        #     with open(FILE_NAME_SILVER_MATCHES,'a') as outfile:
        #         json.dump(outfile, matches, indent=4)
# GOLD I~IV의 소환사 각 10명씩
# summoners_GOLD = [[0]*10 for i in range(4)]
# for i in range(4):
#     summoners = pd.read_csv("data/{}".format(FILE_NAME_GOLD_SUMMONERS[i]))
#     summonerId = summoners['summonerId']
#     for j in range(10):
#         summoners_GOLD[i][j] = summonerId[j]
# print(summoners_GOLD)