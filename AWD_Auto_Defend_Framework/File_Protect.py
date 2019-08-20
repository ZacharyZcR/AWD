# -*- coding:utf-8 -*-
import os
import hashlib
import time 
import shutil

def file_tree(startpath):
	for root,dirs,files in os.walk(startpath,topdown=True):
		level = root.replace(startpath,'').count(os.sep)
		dir_indent = "|---" * (level-1) + "|---"
		file_indent = "|---" * level + "|---"
		if not level:
			print root.replace(startpath,'')
		else:
			print dir_indent+os.path.basename(root)
		for f in files:
			print file_indent+f
			
def get_file_md5(filename):
	m = hashlib.md5()
	with open(filename,'rb') as fobj:
		while True:
			data = fobj.read(4096)
			if not data:
				break
			m.update(data)
	return m.hexdigest()
	
def file_md5_build(startpath):
	global md5_list
	global file_list
	global root
	md5_list = []
	file_list = []
	for root,dirs,files in os.walk(startpath,topdown=True):
		for f in files:
			file_list.append(root+'/'+f)
			md5_list.append(get_file_md5(root+'/'+f))
	
def file_md5_check():
	global root
	file_md5_build('./')
	old_list = []
	new_list = []
	check_list = []
	old_file_list = []
	new_file_list = []
	check_file_list = []
	old_file_list = file_list[:]
	old_list = md5_list[:]
	while (1):
		print "*******************************************************"
		print 'The old file total:',len(old_list)
		print "*******************************************************"
		check_list = old_list[:]
		check_file_list = old_file_list[:]
		file_md5_build('./')
		new_list = md5_list[:]
		new_file_list = file_list[:]
		sign2 = 0
		for i in range(len(new_list)):
			sign = 0
			for j in range(len(old_list)):
				if (new_list[i] == old_list[j] and new_file_list[i] == old_file_list[j]):
					check_list[j] = '0'
					sign = 1
					break
			if sign == 0:
				sign2 = 1
				print new_file_list[i].replace('./',''),'Add or Changed!'
				os.remove(new_file_list[i])
				try:
					shutil.copyfile('./backup'+new_file_list[i].replace('./','/'),new_file_list[i])
					print "Repaired."
				except:
					print "No such file."
		for i in range(len(check_list)):
			if check_list[i] != '0' and sign2 != 1:
				print check_file_list[i].replace('./',''),'Disappear!'
				sign2 = 0
				try:
					shutil.copyfile('./backup'+check_file_list[i].replace('./','/'),check_file_list[i])
					print "Repaired."
				except:
					print "No such file."
				
		print "*******************************************************"
		print 'Total file:',len(new_list)
		print "*******************************************************"
		time.sleep(5)
		
def file_log_add():
	php_list=[]
	for root,dirs,files in os.walk('./',topdown=True):
		for f in files:
			if f[-4:] == '.php':
				php_list.append(root+'/'+f)

	for i in range(len(php_list)):
		print php_list[i]
	print 'Total PHP file:',len(php_list)
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
		
def file_function_check():
	php_list=[]
	for root,dirs,files in os.walk('./',topdown=True):
		for f in files:
			if f[-4:] == '.php':
				php_list.append(root+'/'+f)

	for i in range(len(php_list)):
		print php_list[i]
	print 'Total PHP file:',len(php_list)
	danger_function_list = ['eval','system','base64','$_GET','$_POST']
	for i in range(len(danger_function_list)):
		for j in range(len(php_list)):
			lines=open(php_list[j],"r").readlines()
			for k in range(len(lines)):
				if danger_function_list[i] in lines[k]:
					print "*******************************************************"
					print 'Warning!',php_list[j],'has danger function',danger_function_list[i],'in line:',k+1
					print "*******************************************************"
					
def file_backup():
	src = './'
	tgt = './backup'
	try:
		shutil.copytree(src,tgt)
		print "File backup Succeed."
	except:
		print "File backup fail.Maybe exist."

print "*******************************************************"
print "**************AWD_Auto_Defend_Framework****************"
print "*******************************************************"		
while (1):
	print "*******************************************************"
	print "1.Build file tree."
	print "2.Start file protect module."
	print "3.PHP file add log."
	print "4.File backup."
	print "5.File function check."
	choose = int(raw_input('Please Input:'))
	print "*******************************************************"
	if choose == 1:
		file_tree('./')
	if choose == 2:
		file_md5_check()
	if choose == 3:
		file_log_add()
	if choose == 4:
		file_backup()
	if choose == 5:
		file_function_check()