import API
from API import *

def main():
    API.init()
    match_id = []
    with open(API.MATCH_FILE_NAME, 'r') as json_file:
        json_data = json.load(json_file)
        for match in json_data:
            match_id.append(match)
    if len(match_id) > 0:
        print("read successfully : {length}".format(length=len(match_id)))
    else:
        print('error')

    COUNT = 0
    match_info = []
    for ID in match_id:
        #url = GET("asia", "/lol/match/v5/matches/{matchId}".format(matchId=ID), False) #match_Data
        url = GET("asia", "/lol/match/v5/matches/{matchId}/timeline".format(matchId=ID), False)
        res = requests.get(url)
        COUNT += 1
        if ++API.LENGTH_OF_REQUESTS % 20 == 0:
            sleep(1)
            if API.LENGTH_OF_REQUESTS == 100:
                sleep(120)
                API.LENGTH_OF_REQUESTS = 0
        if res.status_code == 200:
            json_data = json.loads(res.text)
            match_info.append(json_data)
            with open(API.MATCH_TIMELINE_FILE_NAME, 'w') as outfile:
                json.dump(match_info, outfile, indent=4)
        else:
            print("error : {code} where {matchId}".format(code=res.status_code, matchId=ID))
        if COUNT >= 10:
            break
if __name__ == '__main__':
    main()