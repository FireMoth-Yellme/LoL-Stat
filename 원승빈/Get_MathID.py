import API
from API import *


def main():
    API.init()
    summoner_puuid = []
    with open(API.SUMMONER_FILE_NAME, 'r') as json_file:
        json_data = json.load(json_file)
        summoner_puuid.append(json_data['puuid'])
    if len(summoner_puuid)>0:
        print("read successfully : {length}".format(length=len(summoner_puuid)))
    else:
        print('failed to read puuid')
    matches = []
    for i in range(10):
        url = GET("ASIA", "/lol/match/v5/matches/by-puuid/{puuid}/ids?start={count}&count=100".format(puuid=summoner_puuid[0], count=i*100), True)
        res = requests.get(url)
        if ++API.LENGTH_OF_REQUESTS % 20 == 0:
            sleep(1)
        if API.LENGTH_OF_REQUESTS == 100:
            sleep(120)
            LENGTH_OF_REQUESTS = 0
        if res.status_code == 200:
            json_data = json.loads(res.text)
            matches += json_data
        else:
            print("error : {code}".format(code=res.status_code))    # errorCode 429: too many requests
    if len(matches)>0:
        with open(API.MATCH_FILE_NAME, 'a') as outfile:
            json.dump(matches, outfile, indent=4)
    else:
        print('error')
if __name__ == '__main__':
    main()