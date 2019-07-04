#By ZacharyZcR
import os
import sys
import re

file_list=os.listdir(os.getcwd())
php_list=[]

for i in range(len(file_list)):
	if re.search('php',file_list[i]):
		php_list.append(file_list[i])
		
for i in range(len(php_list)):
	print php_list[i]
	
print "A total of",len(php_list),"documents"
print "*******************************************************"
confirm = raw_input("Confirm Open Log Monitoring. 1 or 0:")
if confirm == '1':
	print "*******************************************************"
	for i in range(len(php_list)):
		php_write_in = open(php_list[i],"a")
		php_write_in.write("<?php require_once('log.php') ?>")
	print "Log monitoring turned on."