import sys
from requests import get
from plugins.config import proxies, headers


def whois(inp):
    result = get('http://api.hackertarget.com/whois/?q=' + inp, headers=headers, proxies=proxies).text
    sys.stdout.write(result)
