"""
tweet_scraper.py
author: github.com/sstraw
source: github.com/sstraw/tweet_scraper
desc  : Simple module for scraping tweets from a twitter user.
credit:
Twitter API access derived from work by:
https://github.com/kennethreitz/twitter-scraper
"""
import bs4
import requests
from datetime import datetime


def retrieve(
    user,
    min_id   = None, 
    max_id   = None,
    n_tweets = 20,
    max_reqs = None
):
    """
    Generator that retrieves a given user's tweets. Can use min_id
    and max_id to specify which tweets to fetch, which are non-
    inclusive. n_tweets specifies most tweets to fetch
    (Default 20). Set n_tweets to None for no limit.
    max_reqs is used to specify a maximum number of requests
    to the api
    
    Parameters:
        min_id   : Lowest tweet ID, non inclusive, to collect
        max_id   : Highest tweet ID, non inclusive, to collect
        n_tweets : Max number of tweets to retrieve
        max_reqs : Max number of requests to twitter to make
    """

    url = ''.join((
        'https://twitter.com/i/profiles/show/',
        user,
        '/timeline/tweets',
    ))

    params = {
        'include_available_features' : 1,
        'include_entities'           : 1,
        'include_new_items_bar'      : "true"
    }

    if max_id:
        params['max_position'] = max_id
    if min_id:
        params['min_position'] = min_id

    retrieved_tweets = 0
    n_requests       = 0

    with requests.Session() as r_session:
        while True:
            r           = r_session.get(url, params=params)
            n_requests += 1
            r_json      = r.json()

            for t in parse(r_json['items_html']):
                retrieved_tweets += 1
                yield t

                if (n_tweets != None and
                    retrieved_tweets >= n_tweets
                ):
                    return

            if r_json['has_more_items'] == False:
                return

            if (max_reqs != None and
                max_reqs <= n_requests
            ):
                return

            params['max_position'] = r_json['min_position']


def parse(html):
    """
    Generator function. Given the provided HTML, loop through
    and return dictionary objects of tweets containing the
    following:
        -tweet_id
        -link
        -text
        -timestamp
    """
    soup = bs4.BeautifulSoup(
        html,
        'html.parser'
    )

    for stream_item in soup.find_all(class_='stream-item'):
        tweet = dict()

        tweet_item = stream_item.find(class_ = 'tweet')
        tweet_text = stream_item.find(class_ = 'tweet-text')
        time_item  = stream_item.find(class_ = '_timestamp')

        tweet['tweet_id']  = stream_item['data-item-id']
        tweet['link']      = tweet_item ['data-permalink-path']
        tweet['text']      = tweet_text.text
        
        _timestamp = datetime.fromtimestamp(int(time_item['data-time'])) 
        tweet['timestamp'] = _timestamp.isoformat()

        yield tweet 


def main():
    """
    Main function if called from command line
    """
    import argparse
    import json

    parser = argparse.ArgumentParser(
        description=("Simple script for scraping twitter user pages. "
                     "Inspired by "
                     "https://github.com/kennethreitz/twitter-scraper")
    )
    parser.add_argument('username', help='Username of page to scrape')
    parser.add_argument('--max-id',       default=None,
                        help='Max tweet ID to pull (Non-inclusive)')
    parser.add_argument('--min-id',       default=None,
                        help='Min tweet ID to pull (Non-inclusive)')
    parser.add_argument('-n',             default=20, type=int,
                        help='Max number of tweets to retrieve')
    parser.add_argument('--max-requests', default=None,
                        help=('Max number of requests to make. '
                              'One request gets at most 20 tweets'))

    args = parser.parse_args()

    for tweet in retrieve(
        args.username,
        max_id = args.max_id,
        min_id = args.min_id,
        n_tweets = args.n,
        max_reqs = args.max_requests
    ):
        print (json.dumps(tweet))

                          

if __name__ == '__main__':
    main()
