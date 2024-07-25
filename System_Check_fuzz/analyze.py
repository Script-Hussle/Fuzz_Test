#!/usr/bin/env python3.10.5
import sys
import os
import requests
import argparse
from cores.collectit import getto, ifNone, filing
from cores.SystemCheck import mysystem
from plugins.colors import green, red, bad, end, yellow, white, good, running, spotred, blue, darkgreen, darkyellow, info


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--start', help='access modules', dest='start', action='store_true')
parser.add_argument('-r', '--run', help='run all modules', dest='run', action='store_true')
parser.add_argument('-c', '--check', help='check my online status', dest='check', action='store_true')
args = parser.parse_args()

typ = args.start
run = args.run
check = args.check


def banner():
	print('''
    	         %s________
    	         %s||______)            _________  _________ 
      	         %s||______            (______  / (______  /  
      	         %s||______%s)  ||   ||       /  /       /  /      __    __  ____
      	         %s||         ((___))      /  /___    /  /___    %s||\  /|| //_%s-%s_)
      	         %s||          \___/      /_______)  /_______)   || \/ || \\____                                                         
     '''%(red, red, red, white, red, white, red, white, red, white))

def menu():
	print('''  
     %s_____________%smenu%s_____________      
       
                                          
     %s1.%s %sPort scan                        
                                           
     %s2.%s %sRobots.txt enumeration 

     %s3.%s %sCensys  

     %s4.%s %sDetect honeypot  

     %s5.%s %sReverse IP lookup  

     %s6.%s %sWhois lookup 

     %s0.%s %sSystem Check     
     
     	   %s%sType 'exit' to quit                        
     %s_______________________________

    ''' %(red, white, red, white, end, yellow, white, end, yellow, white,
     end, yellow, white, end, yellow, white, end, yellow, white, end, yellow, white, end, yellow, info, darkyellow, red)) 



def analyze():

	if typ:  
		print (red + ('*' * 150) + end)
		banner()
		menu()
		inp = input('\033[1;91m>>\033[0m%s' % yellow)
		getto(inp)
		if inp == '':
			print('\n%s%sNo value supplied!%s' %(bad, '\033[5m', end))
			return typ


		elif inp == 'exit':
			inp = False
			print(r'''            						 %s%sGood luck!!%s
                               		              %s----------------
                   %s0101010
		  %s010101010
	         %s010            010101     010101    0101010   010        0101     0101    0101010101  0101  0101
                 %s010   01010   01010101   01010101   01010101  010        0101     0101   01010101001  0101  010
                 %s010   01010  0101%s||%s%s0101 0101%s||%s%s0101  010%s| \%s%s010 010        0101     0101  0101          0101010
                 %s010     101  0101%s||%s%s0101 0101%s||%s%s0101  010%s|_|%s%s010 010 	  0101     0101  0101          0101  010
                  %s0101010101   01010101   01010101   01010101  0101010101  01010101010    01010101010  0101    010
                   %s010101010    010101     010101    0101010   0101010101    01010101      0101010101  0101    0101

		'''% (spotred, white, end, darkyellow, red, red, red, red, red, darkyellow, end, red, darkyellow, end, red, darkyellow,
		 end, red, red, darkyellow, end, red, darkyellow, end, red, darkyellow, end, red, white, white))
    	 
def runall():

	if run:
		banner()
		print (red + ('-' * 150) + end)
		ifNone(run)

def take(param):
	if param:
		print (darkyellow + ('-' * 150) + end + '\n')
		xss(param)
			

if typ == True:
	analyze()
if run:
	runall()
if check:
	print (darkyellow + ('-' * 150) + end + '\n')
	mysystem()



		

	
	




		


     
	
		
			



		
		
		
	
		
		
	
	
		

	
		
		
			

		



	
			
			
			

			
		

			
		
			

		

				
					
					
						
						
					
				
					
					
					
						
						
		
			
		


					

				
					
				
				
		
		
			


		
	
		
			
			
			







	



		












   	 
                                     

 





