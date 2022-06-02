from bs4 import BeautifulSoup
from requests_html import HTML, HTMLSession
import requests
import sys, os, time, schedule, socket


class UrlGenerator():
    def __init__(self):
        self.url = 'https://www.google.com/search?q='
        self.results = []

    # Google search with queries and parameters
    def google_search(self, query, timeline='qdr:h', page='10', retry=10):
        search_url = self.url + query + \
            '&tbs={timeline}&start={page}&lr=lang_en'.format(timeline=timeline, page=page)
        response = self.get_source(search_url)
        retry_count = 0
        while response is None:
            print('Retrying Connection ...', file=sys.stderr)
            retry_count += 1
            if retry_count > retry:
                print('Reached Retry Limit', file=sys.stderr)
                os._exit(-1)
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


urlGenerator = UrlGenerator()
service_host = "localhost"
service_port = 7878


def time_str():
    t = time.localtime()
    current_time = time.strftime("%Y-%m-%d, %H:%M:%S", t)
    return current_time

def generate_url():
    query = "TSMC "
    supplier = ["Applied Materials", "ASML", "SUMCO"]
    results = []
    for sup in supplier:
        urlGenerator.google_search(query+sup, timeline='qdr:m')
        print(sup + ":")
        for res in urlGenerator.results:
            print('-', res['title'])
            if res['link'] not in results:
                results.append(res['link'])
        urlGenerator.results.clear()
    return results

def send_links(links):
    try:
        print('Sending Links ...')
        for link in links:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((service_host, service_port))
            print('-', link)
            outstr = link + '\n'
            sock.sendall(outstr.encode('ascii'))
            sock.close()
    except socket.error as e:
        print(e, file=sys.stderr)
        os._exit(1)


# Repeat the Job every hour
#@schedule.repeat(schedule.every().hour)
@schedule.repeat(schedule.every(5).minutes)
def job():
    print(time_str())
    results = generate_url()
    send_links(results)
    


if __name__ == '__main__':
    # Initial Job
    job()

    # Check pending job every 5 minutes
    while True:
        schedule.run_pending()
        time.sleep(60)