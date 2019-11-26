# -*- coding:utf-8 -*-
import os
import hashlib
import time 
import shutil

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
	global dir_list
	global root
	md5_list = []
	file_list = []
	dir_list = []
	for root,dirs,files in os.walk(startpath,topdown=True):
		for d in dirs:
			dir_list.append(root+'/'+d)
		for f in files:
			if f[-4:] == '.txt':
				continue
			file_list.append(root+'/'+f)
			md5_list.append(get_file_md5(root+'/'+f))
			
def file_md5_defense():
	file_backup()
	global root
	file_md5_build('./')
	old_list = []
	old_dir_list = []
	new_list = []
	new_dir_list = []
	check_list = []
	old_file_list = []
	new_file_list = []
	check_file_list = []
	old_file_list = file_list[:]
	old_list = md5_list[:]
	old_dir_list = dir_list[:]
	while (1):
		print "*******************************************************"
		print '[+]The old file total:',len(old_list)
		print '[+]The old dir total:',len(old_dir_list)
		print "*******************************************************"
		check_list = old_list[:]
		check_file_list = old_file_list[:]
		file_md5_build('./')
		new_list = md5_list[:]
		new_file_list = file_list[:]
		new_dir_list = dir_list[:]
		sign2 = 0
		
		for i in range(len(old_dir_list)):
			sign3 = 0
			for j in range(len(new_dir_list)):
				if (old_dir_list[i] == new_dir_list[j]):
					sign3 = 1
					break
			if sign3 == 0:
				sign3 = 1
				print old_dir_list[i].replace('./',''),'Disappear!'
				try:
					shutil.copytree(tgt+old_dir_list[i].replace('./','/'),old_dir_list[i])
					print "[+]Repaired."
				except:
					print "[-]No such dir."
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
				try:
					os.remove(new_file_list[i])
					shutil.copyfile(tgt+new_file_list[i].replace('./','/'),new_file_list[i])
					print "[+]Repaired."
				except:
					print "[-]No such file."
		for i in range(len(check_list)):
			if check_list[i] != '0' and sign2 != 1:
				print check_file_list[i].replace('./',''),'Disappear!'
				sign2 = 0
				try:
					shutil.copyfile(tgt+check_file_list[i].replace('./','/'),check_file_list[i])
					print "[+]Repaired."
				except:
					print "[-]No such file."
				
		print "*******************************************************"
		print '[+]Total file:',len(new_list)
		print '[+]Total dir:',len(new_dir_list)
		print "*******************************************************"
		time.sleep(5)

def file_md5_check():
	file_backup()
	global root
	file_md5_build('./')
	old_list = []
	old_dir_list = []
	new_list = []
	new_dir_list = []
	check_list = []
	old_file_list = []
	new_file_list = []
	check_file_list = []
	old_file_list = file_list[:]
	old_list = md5_list[:]
	old_dir_list = dir_list[:]
	while (1):
		print "*******************************************************"
		print '[+]The old file total:',len(old_list)
		print '[+]The old dir total:',len(old_dir_list)
		print "*******************************************************"
		check_list = old_list[:]
		check_file_list = old_file_list[:]
		file_md5_build('./')
		new_list = md5_list[:]
		new_file_list = file_list[:]
		new_dir_list = dir_list[:]
		sign2 = 0
		
		for i in range(len(old_dir_list)):
			sign3 = 0
			for j in range(len(new_dir_list)):
				if (old_dir_list[i] == new_dir_list[j]):
					sign3 = 1
					break
			if sign3 == 0:
				sign3 = 1
				print old_dir_list[i].replace('./',''),'Disappear!'
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
		for i in range(len(check_list)):
			if check_list[i] != '0' and sign2 != 1:
				print check_file_list[i].replace('./',''),'Disappear!'
				sign2 = 0
		print "*******************************************************"
		print '[+]Total file:',len(new_list)
		print '[+]Total dir:',len(new_dir_list)
		print "*******************************************************"
		time.sleep(5)

def file_log_add():
	php_list=[]
	for root,dirs,files in os.walk('./',topdown=True):
		for f in files:
			if f[-4:] == '.php':
				php_list.append(root+'/'+f)

	for i in range(len(php_list)):
		php_list[i] = php_list[i].replace('//','/')
		print php_list[i]
	print '[+]Total PHP file:',len(php_list)
	confirm = raw_input("Confirm Open Log Monitoring. 1 or 0:")
	if confirm == '1':
		print "*******************************************************"
		for i in range(len(php_list)):
			level_dir = 0
			for j in range(len(php_list[i])):
				if php_list[i][j] == '/':
					level_dir += 1
			lines = open(php_list[i],"r").readlines()
			length = len(lines)-1
			for j in range(length):
				if '<?php' in lines[j]:
					lines[j]=lines[j].replace('<?php','<?php\nrequire_once("./'+'../'*(level_dir-1)+'log.php");')
			open(php_list[i],'w').writelines(lines)
		print "[+]Log monitoring turned on."

def file_backup():
	src = './'
	try:
		shutil.copytree(src,tgt)
		print "[+]File backup succeed."
	except:
		print "[-]File backup fail.Maybe it exists."
		
def file_backup_remove():
	try:
		shutil.rmtree(tgt)
		print "[+]File backup remove succeed."
	except:
		print "[-]File backup remove fail.Maybe it doesn't exist."

global tgt
tgt = './backup'