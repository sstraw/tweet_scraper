# tweet_scraper
Python script/library for scraping tweets from a twitter user.

## Usage
```
>>> import tweet_scraper
>>> for t in tweet_scraper.retrieve('scumbots', n_tweets=2):
...     print (json.dumps(t, indent=2))
...
{
  "tweet_id": "1079434449635500032",
  "link": "/ScumBots/status/1079434449635500032",
  "text": "PowerShell_Empire_Agent found at https://pastebin.com/FtfFsAet\u00a0SHA256: dec16433087bf7927059980265bae41fc0bee12266dc4d6d25c21d1b805de458 C2: http://147[.]135[.]237[.]28:80",
  "timestamp": "2018-12-30T09:50:02"
}
{
  "tweet_id": "1079433699232530433",
  "link": "/ScumBots/status/1079433699232530433",
  "text": "njRat found at https://pastebin.com/0u2Bb5kE\u00a0 SHA256: d9db436b3e5910c0f878d0517ef0a09e40cd2d2bfa69701367a3f73d17fbd007 C2: tcp://dollar[.]ddns[.]net:2604",
  "timestamp": "2018-12-30T09:47:03"
}
```

### Command line
```
$ python3 ./tweet_scraper.py -h
usage: tweet_scraper.py [-h] [--max-id MAX_ID] [--min-id MIN_ID] [-n N]
                        [--max-requests MAX_REQUESTS]
                        username

Simple script for scraping twitter user pages. Inspired by
https://github.com/kennethreitz/twitter-scraper

positional arguments:
  username              Username of page to scrape

optional arguments:
  -h, --help            show this help message and exit
  --max-id MAX_ID       Max tweet ID to pull (Non-inclusive)
  --min-id MIN_ID       Min tweet ID to pull (Non-inclusive)
  -n N                  Max number of tweets to retrieve
  --max-requests MAX_REQUESTS
                        Max number of requests to make. One request gets at
                        most 20 tweets
lime:tweet_scraper sean$ python3 ./tweet_scraper.py -n 2 scumbots
{"tweet_id": "1079434449635500032", "link": "/ScumBots/status/1079434449635500032", "text": "PowerShell_Empire_Agent found at https://pastebin.com/FtfFsAet\u00a0 SHA256: dec16433087bf7927059980265bae41fc0bee12266dc4d6d25c21d1b805de458 C2: http://147[.]135[.]237[.]28:80", "timestamp": "2018-12-30T09:50:02"}
{"tweet_id": "1079433699232530433", "link": "/ScumBots/status/1079433699232530433", "text": "njRat found at https://pastebin.com/0u2Bb5kE\u00a0 SHA256: d9db436b3e5910c0f878d0517ef0a09e40cd2d2bfa69701367a3f73d17fbd007 C2: tcp://dollar[.]ddns[.]net:2604", "timestamp": "2018-12-30T09:47:03"}
```

## Credit
Derived largely from work by https://github.com/kennethreitz/twitter-scraper. I reimplemented the script to better suit some further functionality I needed and to reduce the library footprint.
