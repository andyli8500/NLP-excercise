
#
# This is an example to use Twitter API and integrate with AWS.
# This code does 3 things:
#   1. grab random data from Twitter API
#   2. locate a few information I was interested. e.g. username, time, hashtags, location, etc.
#   3. then push the data into a AWS Kinesis Firehose Stream, which will then ingest to AWS ElasticSearch. Which is a tool made for search and visualization
#

# Import modules
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from pprint import pprint
import boto3
import json
import sys
import signal
# import base64

# Twitter security credentials 
ACCESS_TOKEN    = ""
ACCESS_SECRET   = ""
CONSUMER_KEY    = ""
CONSUMER_SECRET = ""

# Firehose stream name
FIREHOSE_STREAM = "<twitter-es>"

# Authenticate and initialize stream
oauth  = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
stream = TwitterStream(auth=oauth)#, domain='userstream.twitter.com')
tweets = stream.statuses.sample()

# Setup Firehose
client = boto3.client('firehose', region_name='us-east-1')

# Signal handler
def signal_handler(signal, frame):
    print "\n"
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
a = 1

# Start the loop to get the tweets.
for tweet in tweets :
    try :

        hashtags = tweet["entities"]["hashtags"]
        hts = []
        if len(hashtags) == 0 :
            hts.append("None")
        else :
            for ht in hashtags :
                hts.append(str(ht["text"]))

        output = {
            "user": tweet["user"],
            "location": tweet["place"]["name"],
            "timestamp_ms": tweet["timestamp_ms"],
            "created_at": tweet["created_at"],
            "hashtags": hts
        }


        data = json.dumps(output, 'utf-8')
        print data
        # encoded = base64.b64encode(data)
        # print encoded

        response = client.put_record(
            DeliveryStreamName=FIREHOSE_STREAM,
            Record = {
                 'Data': data
            }
        )
        a = 1
        print response

    except Exception as e:

        if a == 1:
            a = 0
            print '.'

        continue

