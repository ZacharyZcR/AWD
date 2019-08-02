import requests

def get(address,data):
	try:
		r = requests.get(address,params=data)
		print "Target:",r.url
		print "Succeed."
		print "*******************************************************"
	except:
		print "Failed."
		print "*******************************************************"
		
def post(address,data):
	try:
		r = requests.post(address,data=data)
		print "Target:",r.url
		print "Post data:",data
		print "Succeed."
		print "*******************************************************"
	except:
		print "Failed."
		print "*******************************************************"
		
def xwf(address,data):
	try:
		headers = {'Content-Type':'application/x-www-form-urlencoded'}
		r = requests.post(address,data=data)
		print "Target:",r.url
		print "Post data:",data
		print "Succeed."
		print "*******************************************************"
	except:
		print "Failed."
		print "*******************************************************"

def json(address,data):
	try:
		headers = {'Content-Type':'application/json'}
		r = requests.post(address,data=data)
		print "Target:",r.url
		print "Post data:",data
		print "Succeed."
		print "*******************************************************"
	except:
		print "Failed."
		print "*******************************************************"
		
def test(address):
	try:
		r = requests.get(address)
		print "Target:",r.url
		print r.status_code
		if r.status_code == 200:
			print "Test Succeed"
		print "*******************************************************"
	except:
		print "Test Failed."
		print "*******************************************************"