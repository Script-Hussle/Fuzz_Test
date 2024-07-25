import sys
import requests
from plugins.config import proxies, headers

def ports(inp):

		results = requests.get('https://api.hackertarget.com/nmap/?q=%s' % inp, headers=headers, proxies=proxies).text 
		sys.stdout.write(results + '\n')



	