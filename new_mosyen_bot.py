from random import choice
import time
import tweepy

consumer_key ="ButjZZ6Hc7wQNX7Z7yUOGF1hi"
consumer_secret ="nbHgn2wRoCyJWkdsRjLKxrkHk2dLp2MolvX9beHqtIoIomOliu"
access_token ="1102923122896822274-MGhRHaCA5CWOTavEYjLdql9JMUYwWC"
access_token_secret ="xaibDbqfuDIrMQmGtwNZ2IB5scS7fqIaibFNL916XqliJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

actors = [n[:-1] for n in open("actor.txt","r").readlines()]
events = [n[:-1] for n in open("event.txt","r").readlines()]
objects = [n[:-1] for n in open("object.txt","r").readlines()]
templates = [n[:-1] for n in open("template.txt","r").readlines()]

while True:
	try:
		motion = choice(templates).replace("<actors>",choice(actors)).replace("<events>",choice(events)).replace("<objects>",choice(objects))
		api.update_status(motion)
		print(motion)
		time.sleep(3600)
	except KeyboardInterrupt:
		break