

## HOW TO AVOID BOT DETECTION
## 1. use a RESIDENTIAL IP ADDRESS ( HOME ADDRESS )
## 2. use a well known USER AGENET string
## The plan for today
## We are only scraping TEXT from HTML today
## We are only scraping TEXT from HTML today
## We are only scraping TEXT from HTML today

## Things we won't do, but would make it way better for web scraping
##  - Not JavaScript
##  - Not CSS
##  - Not Images
##  - Maybe PDFs
##
## How to get ***AI TRAINING DATA***
## How to get ***AI TRAINING DATA***
## Web Scraping with Python
## TODO - bypas website blockers to get the data ANYWAY!!!!

## arg that is the starting point URL
## fetch then parse for <a> anchor tags


import re
import sys
import uuid
import time
import queue
import requests
#import threading
import asyncio

## URL Fetcher Worker
## How to bypass the bot detectors
## - user agent
## - , 'Cookie': 'paset here' - bypass user human verificatin
## - ignore robots.txt - not nice, but everyone does it anyway
## - use a domastic residential IP address
## - 
def relativeFix(url):
    return url
    ## check if url is root or withtout
    ## fix relative paths so they become absolute
    
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
headers = {'User-Agent': user_agent}
rootUrl = None
completedUrls = {}
## TODO spin up multiple web fetches ( it is the slowest )
def url_fetch_worker(urls: Queue, pages: Queue):
    ## TODO
    ## TODO
    ## TODO
    ## TODO PDF READER
    ## TODO ✅ prevent re-downloaded previous URLS
    ## TODO relative url support ( href=/asdfasf )
    ## TODO max depth ( to prevent too much download )
    ## TODO limit number of URLs
    ## TODO domain lock so we don't donwload the ENTIRE WEB
    ## TODO
    while True:
        if urls.empty():
            print("no urls, sleeping for 1 second")
            time.sleep(1)
            continue
        url = urls.get()
        url = relativeFix(url)
        if url in completedUrls:
            print("already saw this URL")
            continue
        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )
            pages.put(response.text)
            print(f'Captured Successfully {url}')
        except Exception as e:
            print(f'Failed to get URL: {url}')
            print(e)
    
    completedUrls[url] = True
    return "done"

## HTML Parser
def html_parser_worker(urls: Queue, pages: Queue):
    find_urls = r'href=["\']([^"\']+)["\']'
    while True:
        if pages.empty():
            print('no pages, sleeping for 1 second')
            time.sleep(1)
            continue
        page = pages.get()

        ## Parse for more links to crawl
        links = re.findall(find_urls, page)
        for link in links:
            urls.put(link)

        ## Save data it is gold
        with open(f'downloads/page_{str(uuid.uuid8())}', 'w') as file:
            file.write(page)

async def main():
    global rootUrl
    ## List of URLS we need to fetch
    urls = queue.Queue()

    ## HTML pages ready for parse
    pages = queue.Queue()

    ## Check Command line user input for root URL
    if len(sys.argv) < 2:
        cmd = sys.argv[0]
        print('Usage Instructions:\n')
        print('\t                     the root url to start')
        print(f'\tpython {cmd} https://www.pubnub.com/\n\n')
        return

    rootUrl = sys.argv[1]
    urls.put(rootUrl)
    print(f'Root url starting at: "{rootUrl=}"')

    results = await asyncio.gather(
        asyncio.to_thread(html_parser_worker, urls, pages),
        asyncio.to_thread(url_fetch_worker, urls, pages),
    )
    print(result)

asyncio.run(main())
