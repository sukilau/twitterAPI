import tweepy
from os import getenv
from dotenv import load_dotenv, find_dotenv


def reply_hashtag_bot(hashtag_list, text=None, filenames=None):
    for hashtag in hashtag_list:
        for tweet in tweepy.Cursor(api.search, q=hashtag).items(100):
            tweet_username = tweet.user.screen_name
            tweetid = tweet._json['id']
            print('Replying @{0} tweetid ={1}'.formattweet_username, tweetid)
        
            # upload images and get media_ids
            media_ids = []
            for filename in filenames:
                res = api.media_upload(filename)
                media_ids.append(res.media_id)

            # tweet with multiple images
            reply = '@'+tweet_username+' ' +text
            debug = api.update_status(status=reply, media_ids=media_ids, in_reply_to_status_id=tweetid)
#             debug = api.update_status(status=reply, in_reply_to_status_id=tweetid)
#             print(debug)


def reply_most_recent_tweet(text, image_list, user_id):
    """
    Reply to the most recent tweet made by the given user
    
    @param text: str, text of the reply tweet
    @param image_list: list of str, images to be uploaded the the reply tweet
    @param user_id: str, user ID of the original tweet 
    """
    
    # find the most recent tweet_id from user_id
    most_recent_tweet_id = find_most_recent_tweet_id(user_id)
    
    # upload media
    media_ids = [api.media_upload(filename).media_id for filename in image_list]
    
    # reply to tweet
    status = api.update_status(status=text, media_ids=media_ids, in_reply_to_status_id = most_recent_tweet_id)

    return


def find_most_recent_tweet_id(user_id):
    """
    Retrieve the most recent Tweet ID from the given user ID
    """
    # assume count=1 will return the most recent tweet
    query_result = api.user_timeline(user_id=user_id, count=1)
    return query_result[0]._json['id']


if __name__ == "__main__":
    # load env keys
    load_dotenv(find_dotenv())
    consumer_key = getenv('consumer_key')
    consumer_secret = getenv('consumer_secret')
    access_token = getenv('access_token')
    access_secret = getenv('access_secret')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    hashtag_list = ['#lskhere123']
    text = 'Halo~ Me again!'
    filenames = ['img/cat.png', 'img/cat.png']
    reply_hashtag_bot(hashtag_list, text=None, filenames=None)
    
