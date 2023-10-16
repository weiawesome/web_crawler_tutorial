import requests


def make_request(url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    headers = {'User-Agent': user_agent}
    return requests.get(url, headers=headers)

