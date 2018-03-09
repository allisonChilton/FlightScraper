import time
import json
from twitter import Twitter
from twitter.oauth import OAuth
from twitter.stream import TwitterStream, Timeout, HeartbeatTimeout, Hangup

def loadKeys():
	with open("keys.json","r") as f:
		keys = json.load(f)
		return keys

def getAccounts():
	with open("accounts.json","r") as f:
		return json.load(f)['accounts']

def saveAccounts(accounts):
	with open("accounts.json","w") as f:
            acstr = json.dumps(accounts)
            f.write(acstr)

def searchAndRetweet(screenname,last_id):
    tweets = t.statuses.user_timeline(screen_name=screenname, since_id=last_id)
    for tweet in tweets:
            id = tweet['id']
            text = tweet['text']
            last_id = max(last_id,id)
            if text.lower().find("denver") != -1 or text.lower().find("dallas") != -1:
                t.statuses.retweet(id=id)

    return last_id

accounts = getAccounts()
	
keys = loadKeys()
auth = OAuth(keys['token'],keys['tokensecret'],keys['key'],keys['apisecret'])

#stream = TwitterStream(auth=auth,domain='userstream.twitter.com')
t = Twitter(auth=auth)

#samp = {'accounts': [{'sn':'secretflying','id':971910235379195904},{'sn':'theflightdeal','id':971910235379195904}]}

while True:
    for ac in accounts:
        lid = searchAndRetweet(ac['sn'],ac['id'])
        ac['id'] = lid

    #print("==================")

    saveAccounts(accounts)
    time.sleep(60*10)
