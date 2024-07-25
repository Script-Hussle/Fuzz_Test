import sys
import requests
import re
from plugins.config import proxies, headers
def hidden (inp):

	shows = requests.get('http://%s/robots.txt' % inp, headers=headers).text
	for show in shows:
		sys.stdout.write(show)

	

			
		
		
	
			



		
		
	
