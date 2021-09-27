from IPython.display import display
import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd
import json

SUMMONER_NAME = "대마법사 김알트"
PUUID = "-5nPSbE4z1TqnJjrJmNsCN6TjtApWg5n75c6UfaQQs2WvwPWyr7XqksDBqNlPnAA93YH1-Gxh79wmA"
MATCH_TIMELINE_FILE_NAME = "data_summoner_timeline_data_{name}.json".format(name=SUMMONER_NAME)

with open(MATCH_TIMELINE_FILE_NAME, 'r') as file:
    match_json_data = json.load(file)

df = pd.json_normalize(match_json_data)

df_meta = df.iloc[:, 1:3]
df_meta.columns = ['matchId', 'participants']

df_info = df.iloc[:, 3:]
df_info.columns = match_json_data[0]['info'].keys()

match_length = len(match_json_data)
#match_length = 10
arr_frames = df_info.pop('frames')
df_frames = pd.concat([pd.json_normalize(arr_frames[x]) for x in range(match_length)])
arr_participants = df_meta.pop('participants')
arr_index = []
for arr in arr_participants:
    arr_index.append(arr.index(PUUID))
count_index = 0
gold_data = []
#match index를 for문으로 돌리면 여러개의 매치를 받아올수 있겠지만. 일단 첫번째 경기를 분석해보자
match_index = 0
match_time_length = 17
display(arr_index[match_index])
currentGold = df_frames["participantFrames.{n}.{content}".format(n=arr_index[match_index], content="currentGold")]
display(currentGold)
currentGold[:18].plot.bar(rot=0)
plt.title("match{count}의 시간별 골드 데이터".format(count=count_index+1))
plt.xlabel("시간(분)0")
plt.ylabel("Gold")
plt.show()

