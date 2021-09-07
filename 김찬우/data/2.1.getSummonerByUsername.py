from API import *

### in API.py
# USERNAME = "야식은치킨이지"

### get summoner data
url = GET("kr", "lol/summoner/v4/summoners/by-name/{summonerName}".format(summonerName=USERNAME), False)
res = requests.get(url)

if res.status_code == 200:
    json_data = json.loads(res.text)
    print("read successfully : {length}".format(length=len(json_data)))
    with open(FILE_NAME_BY_SUMMONER, 'w') as outfile:
        json.dump(json_data, outfile, indent=4)
else:
    print("error")