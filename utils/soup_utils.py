from bs4 import BeautifulSoup


def make_soup(html_text):
    return BeautifulSoup(html_text, 'html.parser')

