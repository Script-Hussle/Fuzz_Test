import requests
import time
import re
import sys
from plugins.config import proxies, headers
from plugins.colors import darkyellow, end, darkblue, yellow, darkgreen

def mysystem():
	
	print('\t''\t''\t''\t''\t''\t'"DateTime: %s%s%s" % (darkyellow, time.strftime("%c"), end)  + '\n' + '\n')

	ip = requests.get('http://tenta.com/test', headers=headers)
	stat = ip.status_code
	sys.stdout.write('Status Code:%s %s %s' % (darkyellow, stat, end) + '\n' + '\n')

	req = ip.request.headers
	sys.stdout.write('Request Headers: %s %s %s' % (darkyellow, req, end) + '\n' + '\n') 

	res = ip.headers
	sys.stdout.write('Response Headers:%s %s %s' % (darkyellow, res, end) + '\n' + '\n')
	
	#Now moving on to better things!
	print (darkgreen + ('-' * 150) + end + '\n')
	if ip:	
		try:
			time.sleep(1)				
			ServiceP = re.search(r'<p class="title">Internet Service Provider</p>\n<p class="dt-lg">(.*)</p>', ip.text).group(1)
			localIp = re.search(r'<p class="title">Local IP Address</p>\n<p class="dt-lg" id="parseLocalIp">(.*)</p>', ip.text).group(1)		
			PublicIp = re.search(r'<p class="dt-lg">(.*)</p>', ip.text).group(1)
			timeZone = re.search(r'<p class="title">Time Zone</p>\n<p class="dt">(.*)</p>', ip.text).group(1)
			latitude = re.search(r'<p class="title">Latitude/Longitude</p>\n<p class="dt">(.*)</p>', ip.text).group(1)
			online = re.search(r'<p class="title">Online:</p>\n<p class="dt" id="browserOnline">(.*)</p>', ip.text).group(1)
			#If you are online this variable will give out the value of true in lowercase letters because of javascript boolean values of that system's client side framework!!
			#So let's turn this value of true to online instead
			if online:
				online == 'true'
				online = 'Online'
			else:
				online == False

			platform = re.search(r'<p class="title">Platform:</p>\n<p class="dt" id="osPlatform">(.*)</p>', ip.text).group(1)
			if platform == True:
				platform = raw_input
				sys.stdout.write('Your OS Platform is:%s%s%s' % (darkgreen, platform, end) + '\n' + '\n')
			else:
				platform == False
				sys.stdout.write('Your OS Platform is: %sNot detected!%s' % (darkgreen, end) + '\n' + '\n')			

		except ConnectionError:
			pass
		finally:
			sys.stdout.write('online/offline: %s%s%s' % (darkgreen, online, end) + '\n' + '\n')
			sys.stdout.write('Your ISP is: %s%s%s' % (darkgreen, ServiceP, end) + '\n' + '\n')
			sys.stdout.write('Your local ip address is: %s%s%s' % (darkgreen, localIp, end) + '\n' + '\n')
			sys.stdout.write('Your Public ip address is: %s%s%s' % (darkgreen, PublicIp, end) + '\n' + '\n')
			sys.stdout.write('Your Time Zone is:%s%s%s' % (darkgreen, timeZone, end) + '\n' + '\n')
			sys.stdout.write('Your Latitude/Longitude is:%s%s%s' % (darkgreen, latitude, end) + '\n' + '\n')
			
			while True:
				try:
					location = re.search(r'<p class="title">Location</p>\n<p class="dt">(.*)<br />(.*)</p>', ip.text).group(1, 2)
					locate = location[1]
					sys.stdout.write('Your Location is: %s%s,%s%s' % (darkgreen, location[0], locate, end) + '\n'+ '\n')
				except ConnectionError:
					pass
				return 
	
	
	
		
		
		
