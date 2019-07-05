#By ZacharyZcR
import requests
import sys
import json
import string
import time

def get_flag(i):
	global flag_content
	r = requests.get(get_flag_url_array[i])
	flag_content = r.text.replace('Administrator Confirmation.\r\n','')
	if r.status_code == 200:
		print "Get flag succeed!"
		print "Team",i+1,"flag:",flag_content
		return flag_content
	else:
		print "Get flag failed!"

def post_flag():
	global flag_count
	if (get_or_post == '1'):
		get_data = {'token':token_content,'flag':flag}
		r = requests.get(flag_url_post,params=get_data)
		if (r.status_code == 200 and flag_content != ''):
			print "Post flag succeed!"
			print "The post data is:",r.url	
			flag_count += 1
		else:
			print "Post flag failed!"	
	if (post_model_choose == '1'):
		xw_post_data = {'token':token_content,'flag':flag}
		r = requests.post(flag_url_post,data=xw_post_data)
		if (r.status_code == 200 and flag_content != ''):
			print "Post flag succeed!"
			print "The post data is:",xw_post_data
			flag_count += 1
		else:
			print "Post flag failed!"
	if (post_model_choose == '2'):
		json_post_data = json.dumps({'token':token_content,'flag':flag})
		r = requests.post(url, data=json_post_data)
		if (r.status_code == 200 and flag_content != ''):
			print "Post flag succeed!"
			print "The post data is:",json_post_data
			flag_count += 1
		else:
			print "Post flag failed!"

print "Welcome to the fully automated score getting machine."
print "If you have any questions, please contact ZacharyZcR."
print "*******************************************************"
flag_url_post = raw_input("The flag upload address:")
r = requests.get(flag_url_post)
if r.status_code == 200:
	print "Flag submission page is working properly."
else:
	print "Flag submission page failed."
print "*******************************************************"
token_content = raw_input("Please input your team's token:")
print "*******************************************************"
get_or_post = raw_input("Choose a HTTP method.1.get 2.post:")
print "*******************************************************"
if get_or_post == '1':
	post_model_choose = '0'
if get_or_post == '2':
	post_model_choose = raw_input("Choose the data encode method.1.x-www-form-urlencoded 2.json:")
	print "*******************************************************"
team_number = input("Number of teams:")
print "*******************************************************"

get_flag_url_array = []
get_flag_url_txt = []

config_file=open('get_score_config.txt')
for line in config_file:
	line=line.strip('\r\n')
	get_flag_url_txt.append(line)
config_file.close()

for i in range(team_number):
	get_flag_url_array.append(get_flag_url_txt[i])
	print get_flag_url_array[i]
	r = requests.get(get_flag_url_array[i])
	if r.status_code == 200:
		print "Flag fetch page",i+1,"works well."
	else:
		print "Flag fetch page",i+1,"failed."
	print "*******************************************************"
time_selcet = input("Please select the attack frequency.Unit: Minutes:")
print "*******************************************************"
turns = 0
while (1):
	flag_count = 0
	localtime = time.asctime(time.localtime(time.time()))
	print "*******************************************************"
	print localtime
	print "*******************************************************"
	for i in range(team_number):
		flag=get_flag(i)
		post_flag()
		print "team",i+1,"OK"
		print "*******************************************************"
	turns += 1
	print "In turn",turns,",",flag_count,"teams has been got flag"
	print team_number-flag_count,"teams failed"
	time.sleep(time_selcet*60)