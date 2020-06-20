#!/usr/bin/env python3
import sys
from twython import Twython

#-- Twitter instance setup
TWITTER = open("TwiTokens.txt", "r").read().splitlines()
apiKey = TWITTER[0]
apiSecret = TWITTER[1]
accessToken = TWITTER[2]
accessTokenSecret = TWITTER[3]

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
#--

def getUserInfobyID(userid):
        """ 
        Returns info on user passed to the function as a dictionary object. 
        """
        # Difference between lookup_user and show_user is list vs dictionary. Not sure on benefits of either yet.
        return api.show_user(user_id=userid)

def getUserInfobyName(username):
        """
        Returns info on user passed to the function as a dictionary object.
        """
        # Difference between lookup_user and show_user is list vs dictionary. Not sure on benefits of either yet.
        return api.show_user(screen_name=username)

def getFollowersbyName(username):
        """
        return a list of followers of the username passed as an argument as a dictionary object.
        """
        return api.get_followers_ids(screen_name=username)

def getFollowersbyID(userid):
        """
        return a list of followers of the username passed as an argument as a dictionary object.
        """
        return api.get_followers_ids(user_id=userid)

def getFriendsbyName(username):
        """
        return a list of "friends"; people the username follows as a dictionary object.
        """
        return api.get_friends_ids(screen_name=username)

def getFriendsbyID(userid):
        """
        return a list of "friends"; people the username follows as a dictionary object.
        """
        return api.get_friends_ids(user_id=userid)

def getUserTimeline(username: str, count: int):
	"""
	return a list of the latest tweets.
	"""
	return api.get_user_timeline(screen_name=username, count=count)

if __name__ == "__main__":
	print("This is a supporting file. Please run stalkerbot.py, or antistalkerbot.py.")
	sys.exit()

