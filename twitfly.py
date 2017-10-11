import time
import json
from twitter import Twitter
from twitter.oauth import OAuth
from twitter.stream import TwitterStream, Timeout, HeartbeatTimeout, Hangup

def loadKeys():
	with open("keys.json","r") as f:
		keys = json.load(f)
		return keys

def getLastId():
	with open("last_id","r") as f:
		return int(f.read())

def saveLastId(last_id):
	with open("last_id","w") as f:
		f.write(str(last_id))


last_id = getLastId()
	
keys = loadKeys()
auth = OAuth(keys['token'],keys['tokensecret'],keys['key'],keys['apisecret'])

#stream = TwitterStream(auth=auth,domain='userstream.twitter.com')
t = Twitter(auth=auth)


while True:
	tweets = t.statuses.user_timeline(screen_name='secretflying', since_id=last_id)
	for tweet in tweets:
		id = tweet['id']
		text = tweet['text']
	#	print(text.encode('utf-8'))
	#	print(id)
		last_id = max(last_id,id)
		if text.lower().find("denver") != -1 :
			t.statuses.retweet(id=id)

	time.sleep(60)
	#print("==================")

saveLastId(last_id)

