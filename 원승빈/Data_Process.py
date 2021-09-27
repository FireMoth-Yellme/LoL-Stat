from IPython.display import display
import numpy as np
import pandas as pd
import json

SUMMONER_NAME = "대마법사 김알트"
PUUID = "-5nPSbE4z1TqnJjrJmNsCN6TjtApWg5n75c6UfaQQs2WvwPWyr7XqksDBqNlPnAA93YH1-Gxh79wmA"
MATCH_DATA_FILE_NAME    = "data_summoner_match_data_{name}.json".format(name=SUMMONER_NAME)

with open(MATCH_DATA_FILE_NAME, 'r') as file:
    match_json_data = json.load(file)

# 원 데이터를 평면화하여 데이터프레임으로 저장합니다. (원 데이터는 match_json_data에 남아 있습니다.)
df = pd.json_normalize(match_json_data)

# 경기의 meta 데이터 중 matchId와 participants(puuid)의 정보를 담은 df_meta라는 변수를 만들어줍니다.
df_meta = df.iloc[:, 1:3]
df_meta.columns = ['matchId', 'participants']

# 남은 경기 데이터 정보를 담은 df_info라는 변수를 만들어줍니다.
df_info = df.iloc[:, 3:]
df_info.columns = match_json_data[0]['info'].keys()

# 가져온 경기의 총 횟수를 따로 저장해줍니다. 337개의 경기데이터가 있기 때문에 10개로 지정해줍니다.
#match_length = len(match_json_data)
match_length = 10

# df_info에 담긴 데이터 중 상당한 부분을 차지하는 teams 변수 부분을 따로 빼내어 저장해줍니다.
arr_teams = df_info.pop('teams')
df_teams = pd.concat([pd.json_normalize(arr_teams[x]) for x in range(match_length)])
df_teams.index = range(match_length*2)

# df_info에 담긴 데이터 중 상당한 부분을 차지하는 participants 변수 부분을 따로 빼내어 저장해줍니다.
arr_participants = df_info.pop('participants')
df_participants = pd.concat([pd.json_normalize(arr_participants[x]) for x in range(match_length)])
df_participants.index = range(match_length*10)

df_meta['summonerIndex'] = df_meta.participants.map(lambda participants : participants.index(PUUID))
df_meta.head()

# data 변수는 그 때 그 때 사용하는 데이터를 담는 변수입니다.
data = df_participants[df_participants.puuid == PUUID].reset_index()   # 경기 참가자 중 소환사의 데이터를 찾아 따로 저장합니다.
display(data[["kills", "deaths", "assists"]].describe().iloc[1:])               # count index는 제외합니다.

# kda 구하기
kda = (data["kills"]+data["assists"])/data["deaths"]
kda.name = "kda"
kda[data["deaths"]==0] = -1                                                     # perfect score = -1

# 구한 데이터는 따로 저장하여 이후 활용하도록 하겠습니다.
data_kda = pd.concat([data[["win", "kills", "deaths", "assists"]], kda], axis=1)
display(data_kda.groupby(['win']).apply(lambda df: df.mean()))