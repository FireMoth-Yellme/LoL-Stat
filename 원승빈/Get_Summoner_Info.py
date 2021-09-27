from API import *

url = GET("kr", "/lol/summoner/v4/summoners/by-puuid/{encryptedPUUID}".format(encryptedPUUID=PUUID), False)
res = requests.get(url)

if ++LENGTH_OF_REQUESTS % 20 == 0:
    sleep(1)
    if LENGTH_OF_REQUESTS == 100:
        sleep(120)
        LENGTH_OF_REQUESTS = 0
if res.status_code == 200:
    json_data = json.loads(res.text)

else:
    print("error : {code}".format(code=res.status_code))

with open(SUMMONER_FILE_NAME, 'w') as outfile:
    json.dump(json_data, outfile, indent=4)


