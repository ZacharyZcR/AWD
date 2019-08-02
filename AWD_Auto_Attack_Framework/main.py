import tools
import time

print "*******************************************************"
print "**************AWD_Auto_Attack_Framework****************"
print "*******************************************************"
print "**************Press_Enter_To_Initialization************"
print "*******************************************************"
enter = raw_input()
tools.flag_upload_address()
tools.team_token()
tools.team_base_url_list()
tools.webshell_url()
tools.trojan_url()
tools.living_check()
print "**************************Initialization_Complete**************************"
time.sleep(2)
while (1):
	print "*******************************************************"
	print "1.Implant Trojan."
	print "2.Implant File."
	print "3.Get flag."
	print "4.Store flag."
	print "5.Get Score."
	print "6.Singe Rce."
	print "7.Multi Rce."
	print "8.Confirm Config."
	print "9.Monitor Trojan."
	print "*******************************************************"
	choose = int(raw_input("Please Input:"))
	if choose == 1:
		tools.trojan_implant()
	if choose == 2:
		tools.file_implant()
	if choose == 3:
		tools.catch_flag()
	if choose == 4:
		tools.store_flag()
	if choose == 5:
		tools.upload_flag()
	if choose == 6:
		tools.remote_command()
	if choose == 7:
		tools.remote_command_multi()
	if choose == 8:
		tools.confirm()
	if choose == 9:
		tools.living_check()
	 