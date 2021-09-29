from API import *

TYPE    = "ranked"     # ranked / normal 
START   = 0
COUNT   = 100

num_of_iterator = 2     # 100 * num_of_iterator

### get puuid by JSON file
with open(FILE_NAME_BY_SUMMONER, "r") as json_file:
    json_data = json.load(json_file)
    puuid=json_data["puuid"]
if len(puuid) > 0:
    print("read successfully")
else:
    print('error')

data = []

for iterator in range(num_of_iterator):

    ### get matchId
    url = GET("asia", "lol/match/v5/matches/by-puuid/{puuid}/ids?type={type}&start={start}&count={count}".
        format(puuid=puuid, type=TYPE, start=(START+iterator*100), count=COUNT), True)
    res = requests.get(url)

    # requests는 1초에 20개, 2분에 100개로 제한되기에 딜레이를 넣어줍니다.
    if ++LENGTH_OF_REQUESTS % 20 == 0:  
        sleep(1)
        if LENGTH_OF_REQUESTS == 100:
            sleep(120)
            LENGTH_OF_REQUESTS = 0

    if res.status_code == 200:
        matches = json.loads(res.text)
    else:
        print("error : {code}".format(code=res.status_code))    # errorCode 429: too many requests

    if len(matches) > 0:
        print("read successfully : {length}".format(length=len(matches)))
        data += matches
    else:
        print('error')

if len(data) > 0:
    with open(MATCH_FILE_NAME_BY_SUMMONER, 'w') as outfile:
        json.dump(data, outfile, indent=4)
else:
    print('error')
