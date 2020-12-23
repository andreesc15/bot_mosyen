from random import choice
import time
import tweepy

consumer_key ="[redacted]"
consumer_secret ="[redacted]"
access_token ="[redacted]"
access_token_secret ="[redacted]"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#--master database
_actors = [n[:-1] for n in open("actor.txt","r").readlines()]
_events = [n[:-1] for n in open("event.txt","r").readlines()]
_objects = [n[:-1] for n in open("object.txt","r").readlines()]
templates = [n[:-1] for n in open("template.txt","r").readlines()]
#--end of master database

#--secondary database
actors = [n for n in _actors]
events = [n for n in _events]
objects = [n for n in _objects]

while True:
	try:
		if len(actors) == 0:
			actors.extend(_actors)
		if len(events) == 0:
			events.extend(_events)
		if len(objects) == 0:
			objects.extend(_objects)

		curr_actor = choice(actors)
		curr_event = choice(events)
		curr_object = choice(objects)

		actors.remove(curr_actor)
		events.remove(curr_event)
		objects.remove(curr_object)

		motion = choice(templates).replace("<actors>",curr_actor).replace("<events>",curr_event).replace("<objects>",curr_object)
		api.update_status(motion)
		print(motion)
		time.sleep(1800)
	except TweepyError:
		continue
