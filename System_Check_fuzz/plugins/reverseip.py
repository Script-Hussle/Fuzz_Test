import sys
from requests import get
from plugins.config import proxies, headers
from plugins.colors import bad


def reverseLookup(inp):
	
    lookup = 'https://api.hackertarget.com/reverseiplookup/?q=%s' % inp
    try:
        result = get(lookup, headers=headers, proxies=proxies).text
        sys.stdout.write(result + '\n')
    except:
        sys.stdout.write('%s Invalid IP address' % bad)
