import json
import requests
from requests.exceptions import RequestException
import re
import time

def get_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        response = requests.get(url,headers = headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def main():
    url = 'https://www.aminer.cn/profile/j-wang/53f7c3efdabfae90ec11b6b8'
    html = get_page(url)
    print(type(html))
    print(html)

main()