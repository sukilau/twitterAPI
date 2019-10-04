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
    