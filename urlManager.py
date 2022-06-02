from bs4 import BeautifulSoup
from requests_html import HTML
from requests_html import HTMLSession
import requests
import sys


class UrlGenerator():
    def __init__(self):
        self.url = 'https://www.google.com/search?q='
        self.results = []

    # Google search with queries and parameters
    def google_search(self, query, timeline='qdr:h', page='5', retry=10):
        search_url = self.url + query + \
            '&tbs={timeline}&start={page}'.format(timeline=timeline, page=page)
        response = self.get_source(search_url)
        retry_count = 0
        while response is None:
            retry_count += 1
            if retry_count > retry:
                print('Reached Retry Limit', file=sys.stderr)
                sys.exit(-1)
            response = self.get_source(search_url)

        self.parse_googleResults(response)

    def get_source(self, url):
        try:
            session = HTMLSession()
            response = session.get(url)
            return response
        except requests.exceptions.RequestException as e:
            print(e, file=sys.stderr)
            return None

    # Google Search Result Parsing
    def parse_googleResults(self, response):
        css_identifier_result = "tF2Cxc"
        css_identifier_title = "h3"
        css_identifier_link = "yuRUbf"
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.findAll("div", {"class": css_identifier_result})
        for result in results:
            title = result.find(css_identifier_title).get_text()
            link = result.find("div", {"class": css_identifier_link}).find(
                href=True)['href']
            self.results.append({'title': title, 'link': link})