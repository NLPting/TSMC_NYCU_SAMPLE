import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


import crawler_sample

def test_google_search():
    crawler = crawler_sample.GoogleCrawler()
    query = "TSMC Ingas"
    results = crawler.google_search(query)
    assert len(results) > 0

def test_get_source():
    crawler = crawler_sample.GoogleCrawler()
    target_url = 'https://www.reuters.com/technology/exclusive-ukraine-halts-half-worlds-neon-output-chips-clouding-outlook-2022-03-11/'
    response = crawler.get_source(target_url)
    assert response.status_code == 200

def test_scrape_google():
    query = 'https://www.google.com/search?q='+"TSMC Ingas"
    crawler = crawler_sample.GoogleCrawler()
    results = crawler.scrape_google(query)
    assert len(results) > 0


def test_html_getText():
    crawler = crawler_sample.GoogleCrawler()
    target_url = 'https://www.reuters.com/technology/exclusive-ukraine-halts-half-worlds-neon-output-chips-clouding-outlook-2022-03-11/'
    response = crawler.get_source(target_url)
    orignal_text = crawler.html_getText(response.text)
    assert len(orignal_text) > 0




