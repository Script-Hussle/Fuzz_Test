import sys
from requests import get
from plugins.config import proxies, headers


def censys(ip):
    dirty_response = get('https://censys.io/ipv4/%s/raw' % ip, headers=headers, proxies=proxies).text
    clean_response = dirty_response.replace('&#34;', '"')
    response = clean_response.split('<code class="json">')[1].split('</code>')[0]
    sys.stdout.write(response + '\n')
