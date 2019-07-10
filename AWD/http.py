import requests
import time

def http():
	if (get_or_post == '1'):
		get_data = raw_input("Please input your data:")
		r = requests.get(target_url,params=get_data)
		if (r.status_code == 200):
			print "HTTP succeed!"
			print "Data is:",r.url	
		else:
			print "HTTP failed!"	
	if (post_model_choose == '1'):
		xw_post_data = raw_input("Please input your data:")
		r = requests.post(target_url,data=xw_post_data)
		if (r.status_code == 200 and flag_content != ''):
			print "HTTP succeed!"
			print "Data is:",xw_post_data
		else:
			print "HTTP failed!"
	if (post_model_choose == '2'):
		json_data = raw_input("Please input your data:")
		json_post_data = json.dumps(json_data)
		r = requests.post(target_url,data=json_post_data)
		if (r.status_code == 200 and flag_content != ''):
			print "HTTP succeed!"
			print "Data is:",json_post_data
		else:
			print "HTTP failed!"
			
target_url = raw_input("Please input your target url:")
get_or_post = raw_input("Choose a HTTP method.1.get 2.post:")
if get_or_post == '1':
	post_model_choose = '0'
if get_or_post == '2':
	post_model_choose = raw_input("Choose the data encode method.1.x-www-form-urlencoded 2.json:")

while (1):
	http();
