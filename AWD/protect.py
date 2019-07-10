#By ZacharyZcR
import os
import sys
import re

file_list=os.listdir(os.getcwd())
php_list=[]

for i in range(len(file_list)):
	if file_list[i][-3:] == 'php':
		php_list.append(file_list[i])
		
for i in range(len(php_list)):
	print php_list[i]
	
print "A total of",len(php_list),"documents"
print "*******************************************************"
confirm = raw_input("Confirm Open Log Monitoring. 1 or 0:")
if confirm == '1':
	print "*******************************************************"
	for i in range(len(php_list)):
		lines=open(php_list[i],"r").readlines()
		length = len(lines)-1
		for j in range(length):
			if '<?php' in lines[j]:
				lines[j]=lines[j].replace('<?php','<?php\nrequire_once(\'log.php\');')
		open(php_list[i],'w').writelines(lines)
	print "Log monitoring turned on."