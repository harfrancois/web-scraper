import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_bitcoin"


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations = soup.find_all(title='Wikipedia:Citation needed')
    header = soup.find('h1')
    h1 = header.text
    result = len(citations)

    print(f'{h1} has {result} citations needed.')


get_citations_needed_count(url)


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all(title='Wikipedia:Citation needed')
    for result in results:
        text = result.parent.parent.parent.text
        print(text)


get_citations_needed_report(url)
