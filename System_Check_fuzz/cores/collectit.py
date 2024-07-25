import sys 
import requests
import re
from plugins.colors import red, running, end, bad, yellow, green, good, info, darkyellow, blue, darkgreen, white
from plugins.hidden import hidden
from plugins.port import ports

from plugins.censy import censys
from plugins.honeypott import honeypot
from plugins.reverseip import reverseLookup
from plugins.whoiss import whois
from cores.SystemCheck import mysystem


modules = [ports, hidden, censys, honeypot, reverseLookup, whois]

def getto(typ):
	
	if typ == '0':
		sys.stdout.write('\t\t\t\t%s%sChecking your system\'s status from %swww.tenta.com/test%s' % ('\033[97m[~]\033[0m', darkyellow, white, end)+ '\n' + '\n')
		print (darkgreen + ('-' * 150) + end + '\n' + '\n')
		mysystem()
		return typ

	elif typ == '1':
		typ = 'Port scan by ip'
		inp = input('%s%s%s>>%s' % (yellow, typ, red, end))		
		modules[0](inp)
		return typ

	elif typ == '2':
		typ = 'Robots.txt enumeration'
		inp = input('%s%s%s>>%s' % (yellow, typ, red, end))
		modules[1](inp)
		return typ

	elif typ == '3':
		typ = 'Censys by ip'
		inp = input('%s%s%s>>%s' % (yellow, typ, red, end))
		for ip in inp:
			modules[2](ip)
			return typ	

	elif typ == '4':
		typ = 'Detect honeypot by ip'
		inp = input('%s%s%s>>%s' % (yellow, typ, red, end))
		modules[3](inp) 
		return typ

	elif typ == '5':
		typ = 'Reverse IP lookup'
		inp = input('%s%s%s>>%s' % (yellow, typ, red, end))
		modules[4](inp)
		return typ

	elif typ == '6':
		typ = 'Whois lookup by ip'
		inp = input('%s%s%s>>%s' % (yellow, typ, red, end))
		modules[5](inp)
		return typ

def ifNone(run):

	if run == True:
		
		run = input('%s%sRun all the modules at once? y/n %s>>%s'% (info, darkyellow, red, end))
		if run == 'y':
			try:
				inp = input('Enter url%s>%s%s%s'% (red, end, blue, end))
				for call in modules[::-1]: 
					print('%s%sRunning the query' % (running, darkyellow))
					while call:
						call(inp)
						return run
				if run == 'n':
					quit('')
				if run != 'y' or 'n':
					print('\t%s\n>>%s%sInvalid_input%s%s<<' % (red, end, '\033[5m', end, red))
					quit('')

			except KeyboardInterrupt:
					print('\n\t%s>>%s%sKeyboard_Interrupt%s%s<<'% (red, end, '\033[5m', end, red))

			finally:
					pass

def filing(inp):#fileName is basically the name of the file 

	if inp == True:
		try:
			with open("inp" + ".txt") as test:
				print(test.read())
		except ValueError:
			pass




				


				

			
		


			
			



				


			
			
			



					



		
		

		


		


		





