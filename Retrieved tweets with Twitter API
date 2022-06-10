# source: https://towardsdatascience.com/an-extensive-guide-to-collecting-tweets-from-twitter-api-v2-for-academic-research-using-python-3-518fcb71df2a
# For sending GET requests from the API
import requests
# For saving access tokens and for file management when creating and adding to the dataset
import os
# For dealing with json responses we receive from the API
import json
# For displaying the data after
import pandas as pd
# For saving the response data in CSV format
import csv
# For parsing the dates received from twitter in readable formats
import datetime
import dateutil.parser
import unicodedata
# To add wait time between requests
import time

# put your token here
os.environ['TOKEN'] = 'AAAAA'


def auth():
    return os.getenv('TOKEN')


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def create_url(keyword, start_date, end_date, max_results=10):
    search_url = "https://api.twitter.com/2/tweets/search/all"  # Change to the endpoint you want to collect data from

    # change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)


def connect_to_endpoint(url, headers, params, next_token=None):
    params['next_token'] = next_token  # params object received from create_url function
    response = requests.request("GET", url, headers=headers, params=params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def append_to_csv(json_response, fileName):
    # A counter variable
    counter = 0

    # Open OR create the target CSV file
    csvFile = open(fileName, "a", newline="", encoding='utf-8')
    csvWriter = csv.writer(csvFile)

    # Loop through each tweet
    for tweet in json_response['data']:

        # We will create a variable for each since some of the keys might not exist for some tweets
        # So we will account for that

        # 1. Author ID
        author_id = tweet['author_id']

        # 2. Time created
        created_at = dateutil.parser.parse(tweet['created_at'])

        # 3. Geolocation
        if ('geo' in tweet):
            geo = " "
        else:
            geo = " "

        # 4. Tweet ID
        tweet_id = tweet['id']

        # 5. Language
        lang = tweet['lang']

        # 6. Tweet metrics
        retweet_count = tweet['public_metrics']['retweet_count']
        reply_count = tweet['public_metrics']['reply_count']
        like_count = tweet['public_metrics']['like_count']
        quote_count = tweet['public_metrics']['quote_count']

        # 7. source
        source = " "

        # 8. Tweet text
        text = tweet['text']

        # Assemble all data in a list
        res = [author_id, created_at, geo, tweet_id, lang, like_count, quote_count, reply_count, retweet_count, source,text]

        # Append the result to the CSV file
        csvWriter.writerow(res)
        counter += 1

    # When done, close the CSV file
    csvFile.close()

    # Print the number of tweets for this iteration
    print("# of Tweets added from this response: ", counter)


# Inputs for tweets
bearer_token = auth()
headers = create_headers(bearer_token)
keyword = "Singapore wp -is:retweet lang:en"

start_list = ['2006-04-01T00:00:00.000Z',
              '2006-05-01T00:00:00.000Z',
              '2006-06-01T00:00:00.000Z',
              '2006-07-01T00:00:00.000Z',
              '2006-08-01T00:00:00.000Z',
              '2006-09-01T00:00:00.000Z',
              '2006-10-01T00:00:00.000Z',
              '2006-11-01T00:00:00.000Z',
              '2006-12-01T00:00:00.000Z',
              '2007-01-01T00:00:00.000Z',
              '2007-02-01T00:00:00.000Z',
              '2007-03-01T00:00:00.000Z',
              '2007-04-01T00:00:00.000Z',
              '2007-05-01T00:00:00.000Z',
              '2007-06-01T00:00:00.000Z',
              '2007-07-01T00:00:00.000Z',
              '2007-08-01T00:00:00.000Z',
              '2007-09-01T00:00:00.000Z',
              '2007-10-01T00:00:00.000Z',
              '2007-11-01T00:00:00.000Z',
              '2007-12-01T00:00:00.000Z',
              '2008-01-01T00:00:00.000Z',
              '2008-02-01T00:00:00.000Z',
              '2008-03-01T00:00:00.000Z',
              '2008-04-01T00:00:00.000Z',
              '2008-05-01T00:00:00.000Z',
              '2008-06-01T00:00:00.000Z',
              '2008-07-01T00:00:00.000Z',
              '2008-08-01T00:00:00.000Z',
              '2008-09-01T00:00:00.000Z',
              '2008-10-01T00:00:00.000Z',
              '2008-11-01T00:00:00.000Z',
              '2008-12-01T00:00:00.000Z',
              '2009-01-01T00:00:00.000Z',
              '2009-02-01T00:00:00.000Z',
              '2009-03-01T00:00:00.000Z',
              '2009-04-01T00:00:00.000Z',
              '2009-05-01T00:00:00.000Z',
              '2009-06-01T00:00:00.000Z',
              '2009-07-01T00:00:00.000Z',
              '2009-08-01T00:00:00.000Z',
              '2009-09-01T00:00:00.000Z',
              '2009-10-01T00:00:00.000Z',
              '2009-11-01T00:00:00.000Z',
              '2009-12-01T00:00:00.000Z',
              '2010-01-01T00:00:00.000Z',
              '2010-02-01T00:00:00.000Z',
              '2010-03-01T00:00:00.000Z',
              '2010-04-01T00:00:00.000Z',
              '2010-05-01T00:00:00.000Z',
              '2010-06-01T00:00:00.000Z',
              '2010-07-01T00:00:00.000Z',
              '2010-08-01T00:00:00.000Z',
              '2010-09-01T00:00:00.000Z',
              '2010-10-01T00:00:00.000Z',
              '2010-11-01T00:00:00.000Z',
              '2010-12-01T00:00:00.000Z',
              '2011-01-01T00:00:00.000Z',
              '2011-02-01T00:00:00.000Z',
              '2011-03-01T00:00:00.000Z',
              '2011-04-01T00:00:00.000Z',
              '2011-05-01T00:00:00.000Z',
              '2011-06-01T00:00:00.000Z',
              '2011-07-01T00:00:00.000Z',
              '2011-08-01T00:00:00.000Z',
              '2011-09-01T00:00:00.000Z',
              '2011-10-01T00:00:00.000Z',
              '2011-11-01T00:00:00.000Z',
              '2011-12-01T00:00:00.000Z',
              '2012-01-01T00:00:00.000Z',
              '2012-02-01T00:00:00.000Z',
              '2012-03-01T00:00:00.000Z',
              '2012-04-01T00:00:00.000Z',
              '2012-05-01T00:00:00.000Z',
              '2012-06-01T00:00:00.000Z',
              '2012-07-01T00:00:00.000Z',
              '2012-08-01T00:00:00.000Z',
              '2012-09-01T00:00:00.000Z',
              '2012-10-01T00:00:00.000Z',
              '2012-11-01T00:00:00.000Z',
              '2012-12-01T00:00:00.000Z',
              '2013-01-01T00:00:00.000Z',
              '2013-02-01T00:00:00.000Z',
              '2013-03-01T00:00:00.000Z',
              '2013-04-01T00:00:00.000Z',
              '2013-05-01T00:00:00.000Z',
              '2013-06-01T00:00:00.000Z',
              '2013-07-01T00:00:00.000Z',
              '2013-08-01T00:00:00.000Z',
              '2013-09-01T00:00:00.000Z',
              '2013-10-01T00:00:00.000Z',
              '2013-11-01T00:00:00.000Z',
              '2013-12-01T00:00:00.000Z',
              '2014-01-01T00:00:00.000Z',
              '2014-02-01T00:00:00.000Z',
              '2014-03-01T00:00:00.000Z',
              '2014-04-01T00:00:00.000Z',
              '2014-05-01T00:00:00.000Z',
              '2014-06-01T00:00:00.000Z',
              '2014-07-01T00:00:00.000Z',
              '2014-08-01T00:00:00.000Z',
              '2014-09-01T00:00:00.000Z',
              '2014-10-01T00:00:00.000Z',
              '2014-11-01T00:00:00.000Z',
              '2014-12-01T00:00:00.000Z',
              '2015-01-01T00:00:00.000Z',
              '2015-02-01T00:00:00.000Z',
              '2015-03-01T00:00:00.000Z',
              '2015-04-01T00:00:00.000Z',
              '2015-05-01T00:00:00.000Z',
              '2015-06-01T00:00:00.000Z',
              '2015-07-01T00:00:00.000Z',
              '2015-08-01T00:00:00.000Z',
              '2015-09-01T00:00:00.000Z',
              '2015-10-01T00:00:00.000Z',
              '2015-11-01T00:00:00.000Z',
              '2015-12-01T00:00:00.000Z',
              '2016-01-01T00:00:00.000Z',
              '2016-02-01T00:00:00.000Z',
              '2016-03-01T00:00:00.000Z',
              '2016-04-01T00:00:00.000Z',
              '2016-05-01T00:00:00.000Z',
              '2016-06-01T00:00:00.000Z',
              '2016-07-01T00:00:00.000Z',
              '2016-08-01T00:00:00.000Z',
              '2016-09-01T00:00:00.000Z',
              '2016-10-01T00:00:00.000Z',
              '2016-11-01T00:00:00.000Z',
              '2016-12-01T00:00:00.000Z',
              '2017-01-01T00:00:00.000Z',
              '2017-02-01T00:00:00.000Z',
              '2017-03-01T00:00:00.000Z',
              '2017-04-01T00:00:00.000Z',
              '2017-05-01T00:00:00.000Z',
              '2017-06-01T00:00:00.000Z',
              '2017-07-01T00:00:00.000Z',
              '2017-08-01T00:00:00.000Z',
              '2017-09-01T00:00:00.000Z',
              '2017-10-01T00:00:00.000Z',
              '2017-11-01T00:00:00.000Z',
              '2017-12-01T00:00:00.000Z',
              '2018-01-01T00:00:00.000Z',
              '2018-02-01T00:00:00.000Z',
              '2018-03-01T00:00:00.000Z',
              '2018-04-01T00:00:00.000Z',
              '2018-05-01T00:00:00.000Z',
              '2018-06-01T00:00:00.000Z',
              '2018-07-01T00:00:00.000Z',
              '2018-08-01T00:00:00.000Z',
              '2018-09-01T00:00:00.000Z',
              '2018-10-01T00:00:00.000Z',
              '2018-11-01T00:00:00.000Z',
              '2018-12-01T00:00:00.000Z',
              '2019-01-01T00:00:00.000Z',
              '2019-02-01T00:00:00.000Z',
              '2019-03-01T00:00:00.000Z',
              '2019-04-01T00:00:00.000Z',
              '2019-05-01T00:00:00.000Z',
              '2019-06-01T00:00:00.000Z',
              '2019-07-01T00:00:00.000Z',
              '2019-08-01T00:00:00.000Z',
              '2019-09-01T00:00:00.000Z',
              '2019-10-01T00:00:00.000Z',
              '2019-11-01T00:00:00.000Z',
              '2019-12-01T00:00:00.000Z',
              '2020-01-01T00:00:00.000Z',
              '2020-02-01T00:00:00.000Z',
              '2020-03-01T00:00:00.000Z',
              '2020-04-01T00:00:00.000Z',
              '2020-05-01T00:00:00.000Z',
              '2020-06-01T00:00:00.000Z',
              '2020-07-01T00:00:00.000Z',
              '2020-08-01T00:00:00.000Z',
              '2020-09-01T00:00:00.000Z',
              '2020-10-01T00:00:00.000Z',
              '2020-11-01T00:00:00.000Z',
              '2020-12-01T00:00:00.000Z',
              '2021-01-01T00:00:00.000Z',
              '2021-02-01T00:00:00.000Z',
              '2021-03-01T00:00:00.000Z',
              '2021-04-01T00:00:00.000Z',
              '2021-05-01T00:00:00.000Z',
              '2021-06-01T00:00:00.000Z',
              '2021-07-01T00:00:00.000Z',
              '2021-08-01T00:00:00.000Z',
              '2021-09-01T00:00:00.000Z',
              '2021-10-01T00:00:00.000Z',
              '2021-11-01T00:00:00.000Z',
              '2021-12-01T00:00:00.000Z',
              '2022-01-01T00:00:00.000Z',
              '2022-02-01T00:00:00.000Z',
              '2022-03-01T00:00:00.000Z', ]

end_list = ['2006-04-30T00:00:00.000Z',
            '2006-05-30T00:00:00.000Z',
            '2006-06-30T00:00:00.000Z',
            '2006-07-30T00:00:00.000Z',
            '2006-08-30T00:00:00.000Z',
            '2006-09-30T00:00:00.000Z',
            '2006-10-30T00:00:00.000Z',
            '2006-11-30T00:00:00.000Z',
            '2006-12-30T00:00:00.000Z',
            '2007-01-30T00:00:00.000Z',
            '2007-02-28T00:00:00.000Z',
            '2007-03-30T00:00:00.000Z',
            '2007-04-30T00:00:00.000Z',
            '2007-05-30T00:00:00.000Z',
            '2007-06-30T00:00:00.000Z',
            '2007-07-30T00:00:00.000Z',
            '2007-08-30T00:00:00.000Z',
            '2007-09-30T00:00:00.000Z',
            '2007-10-30T00:00:00.000Z',
            '2007-11-30T00:00:00.000Z',
            '2007-12-30T00:00:00.000Z',
            '2008-01-30T00:00:00.000Z',
            '2008-02-28T00:00:00.000Z',
            '2008-03-30T00:00:00.000Z',
            '2008-04-30T00:00:00.000Z',
            '2008-05-30T00:00:00.000Z',
            '2008-06-30T00:00:00.000Z',
            '2008-07-30T00:00:00.000Z',
            '2008-08-30T00:00:00.000Z',
            '2008-09-30T00:00:00.000Z',
            '2008-10-30T00:00:00.000Z',
            '2008-11-30T00:00:00.000Z',
            '2008-12-30T00:00:00.000Z',
            '2009-01-30T00:00:00.000Z',
            '2009-02-28T00:00:00.000Z',
            '2009-03-30T00:00:00.000Z',
            '2009-04-30T00:00:00.000Z',
            '2009-05-30T00:00:00.000Z',
            '2009-06-30T00:00:00.000Z',
            '2009-07-30T00:00:00.000Z',
            '2009-08-30T00:00:00.000Z',
            '2009-09-30T00:00:00.000Z',
            '2009-10-30T00:00:00.000Z',
            '2009-11-30T00:00:00.000Z',
            '2009-12-30T00:00:00.000Z',
            '2010-01-30T00:00:00.000Z',
            '2010-02-28T00:00:00.000Z',
            '2010-03-30T00:00:00.000Z',
            '2010-04-30T00:00:00.000Z',
            '2010-05-30T00:00:00.000Z',
            '2010-06-30T00:00:00.000Z',
            '2010-07-30T00:00:00.000Z',
            '2010-08-30T00:00:00.000Z',
            '2010-09-30T00:00:00.000Z',
            '2010-10-30T00:00:00.000Z',
            '2010-11-30T00:00:00.000Z',
            '2010-12-30T00:00:00.000Z',
            '2011-01-30T00:00:00.000Z',
            '2011-02-28T00:00:00.000Z',
            '2011-03-30T00:00:00.000Z',
            '2011-04-30T00:00:00.000Z',
            '2011-05-30T00:00:00.000Z',
            '2011-06-30T00:00:00.000Z',
            '2011-07-30T00:00:00.000Z',
            '2011-08-30T00:00:00.000Z',
            '2011-09-30T00:00:00.000Z',
            '2011-10-30T00:00:00.000Z',
            '2011-11-30T00:00:00.000Z',
            '2011-12-30T00:00:00.000Z',
            '2012-01-30T00:00:00.000Z',
            '2012-02-28T00:00:00.000Z',
            '2012-03-30T00:00:00.000Z',
            '2012-04-30T00:00:00.000Z',
            '2012-05-30T00:00:00.000Z',
            '2012-06-30T00:00:00.000Z',
            '2012-07-30T00:00:00.000Z',
            '2012-08-30T00:00:00.000Z',
            '2012-09-30T00:00:00.000Z',
            '2012-10-30T00:00:00.000Z',
            '2012-11-30T00:00:00.000Z',
            '2012-12-30T00:00:00.000Z',
            '2013-01-30T00:00:00.000Z',
            '2013-02-28T00:00:00.000Z',
            '2013-03-30T00:00:00.000Z',
            '2013-04-30T00:00:00.000Z',
            '2013-05-30T00:00:00.000Z',
            '2013-06-30T00:00:00.000Z',
            '2013-07-30T00:00:00.000Z',
            '2013-08-30T00:00:00.000Z',
            '2013-09-30T00:00:00.000Z',
            '2013-10-30T00:00:00.000Z',
            '2013-11-30T00:00:00.000Z',
            '2013-12-30T00:00:00.000Z',
            '2014-01-30T00:00:00.000Z',
            '2014-02-28T00:00:00.000Z',
            '2014-03-30T00:00:00.000Z',
            '2014-04-30T00:00:00.000Z',
            '2014-05-30T00:00:00.000Z',
            '2014-06-30T00:00:00.000Z',
            '2014-07-30T00:00:00.000Z',
            '2014-08-30T00:00:00.000Z',
            '2014-09-30T00:00:00.000Z',
            '2014-10-30T00:00:00.000Z',
            '2014-11-30T00:00:00.000Z',
            '2014-12-30T00:00:00.000Z',
            '2015-01-30T00:00:00.000Z',
            '2015-02-28T00:00:00.000Z',
            '2015-03-30T00:00:00.000Z',
            '2015-04-30T00:00:00.000Z',
            '2015-05-30T00:00:00.000Z',
            '2015-06-30T00:00:00.000Z',
            '2015-07-30T00:00:00.000Z',
            '2015-08-30T00:00:00.000Z',
            '2015-09-30T00:00:00.000Z',
            '2015-10-30T00:00:00.000Z',
            '2015-11-30T00:00:00.000Z',
            '2015-12-30T00:00:00.000Z',
            '2016-01-30T00:00:00.000Z',
            '2016-02-28T00:00:00.000Z',
            '2016-03-30T00:00:00.000Z',
            '2016-04-30T00:00:00.000Z',
            '2016-05-30T00:00:00.000Z',
            '2016-06-30T00:00:00.000Z',
            '2016-07-30T00:00:00.000Z',
            '2016-08-30T00:00:00.000Z',
            '2016-09-30T00:00:00.000Z',
            '2016-10-30T00:00:00.000Z',
            '2016-11-30T00:00:00.000Z',
            '2016-12-30T00:00:00.000Z',
            '2017-01-30T00:00:00.000Z',
            '2017-02-28T00:00:00.000Z',
            '2017-03-30T00:00:00.000Z',
            '2017-04-30T00:00:00.000Z',
            '2017-05-30T00:00:00.000Z',
            '2017-06-30T00:00:00.000Z',
            '2017-07-30T00:00:00.000Z',
            '2017-08-30T00:00:00.000Z',
            '2017-09-30T00:00:00.000Z',
            '2017-10-30T00:00:00.000Z',
            '2017-11-30T00:00:00.000Z',
            '2017-12-30T00:00:00.000Z',
            '2018-01-30T00:00:00.000Z',
            '2018-02-28T00:00:00.000Z',
            '2018-03-30T00:00:00.000Z',
            '2018-04-30T00:00:00.000Z',
            '2018-05-30T00:00:00.000Z',
            '2018-06-30T00:00:00.000Z',
            '2018-07-30T00:00:00.000Z',
            '2018-08-30T00:00:00.000Z',
            '2018-09-30T00:00:00.000Z',
            '2018-10-30T00:00:00.000Z',
            '2018-11-30T00:00:00.000Z',
            '2018-12-30T00:00:00.000Z',
            '2019-01-30T00:00:00.000Z',
            '2019-02-28T00:00:00.000Z',
            '2019-03-30T00:00:00.000Z',
            '2019-04-30T00:00:00.000Z',
            '2019-05-30T00:00:00.000Z',
            '2019-06-30T00:00:00.000Z',
            '2019-07-30T00:00:00.000Z',
            '2019-08-30T00:00:00.000Z',
            '2019-09-30T00:00:00.000Z',
            '2019-10-30T00:00:00.000Z',
            '2019-11-30T00:00:00.000Z',
            '2019-12-30T00:00:00.000Z',
            '2020-01-30T00:00:00.000Z',
            '2020-02-28T00:00:00.000Z',
            '2020-03-30T00:00:00.000Z',
            '2020-04-30T00:00:00.000Z',
            '2020-05-30T00:00:00.000Z',
            '2020-06-30T00:00:00.000Z',
            '2020-07-30T00:00:00.000Z',
            '2020-08-30T00:00:00.000Z',
            '2020-09-30T00:00:00.000Z',
            '2020-10-30T00:00:00.000Z',
            '2020-11-30T00:00:00.000Z',
            '2020-12-30T00:00:00.000Z',
            '2021-01-30T00:00:00.000Z',
            '2021-02-28T00:00:00.000Z',
            '2021-03-30T00:00:00.000Z',
            '2021-04-30T00:00:00.000Z',
            '2021-05-30T00:00:00.000Z',
            '2021-06-30T00:00:00.000Z',
            '2021-07-30T00:00:00.000Z',
            '2021-08-30T00:00:00.000Z',
            '2021-09-30T00:00:00.000Z',
            '2021-10-30T00:00:00.000Z',
            '2021-11-30T00:00:00.000Z',
            '2021-12-30T00:00:00.000Z',
            '2022-01-30T00:00:00.000Z',
            '2022-02-28T00:00:00.000Z',
            '2022-03-22T00:00:00.000Z', ]


max_results = 300

# Total number of tweets we collected from the loop
total_tweets = 0

# Create file
csvFile = open("wp.csv", "a", newline="", encoding='utf-8')
csvWriter = csv.writer(csvFile)

# Create headers for the data you want to save, in this example, we only want save these columns in our dataset
csvWriter.writerow(
    ['author id', 'created_at', 'geo', 'id', 'lang', 'like_count', 'quote_count', 'reply_count', 'retweet_count',
     'source', 'tweet'])
csvFile.close()

for i in range(0, len(start_list)):

    # Inputs
    count = 0  # Counting tweets per time period
    max_count = 300  # Max tweets per time period
    flag = True
    next_token = None

    # Check if flag is true
    while flag:
        # Check if max_count reached
        if count >= max_count:
            break
        print("-------------------")
        print("Token: ", next_token)
        url = create_url(keyword, start_list[i], end_list[i], max_results)
        json_response = connect_to_endpoint(url[0], headers, url[1], next_token)
        result_count = json_response['meta']['result_count']

        if 'next_token' in json_response['meta']:
            # Save the token to use for next call
            next_token = json_response['meta']['next_token']
            print("Next Token: ", next_token)
            if result_count is not None and result_count > 0 and next_token is not None:
                print("Start Date: ", start_list[i])
                append_to_csv(json_response, "wp.csv")
                count += result_count
                total_tweets += result_count
                print("Total # of Tweets added: ", total_tweets)
                print("-------------------")
                time.sleep(5)
                # If no next token exists
        else:
            if result_count is not None and result_count > 0:
                print("-------------------")
                print("Start Date: ", start_list[i])
                append_to_csv(json_response, "wp.csv")
                count += result_count
                total_tweets += result_count
                print("Total # of Tweets added: ", total_tweets)
                print("-------------------")
                time.sleep(5)

            # Since this is the final request, turn flag to false to move to the next time period.
            flag = False
            next_token = None
        time.sleep(5)
print("Total number of results: ", total_tweets)
