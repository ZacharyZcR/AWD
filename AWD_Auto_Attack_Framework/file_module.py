import os

def read_txt_array(target_file):
	try:
		target_array = []
		line_count = 0
		config_file=open(target_file)
		for line in config_file:
			line=line.strip('\r\n')
			target_array.append(line)
			print (line)
			line_count += 1
		print "Total line:",line_count
		print "File Read Succeed."
		print "*******************************************************"
		return target_array
		config_file.close()
	except:
		print "File Read Failed."
		print "*******************************************************"

def read_txt_variable(target_file):
	try:
		config_file=open(target_file)
		target_variable = config_file.readline()
		target_variable = target_variable.strip('\r\n')
		print "*",target_variable,"*"
		print "File Read Succeed."
		print "*******************************************************"
		config_file.close()
		return target_variable
	except:
		print "File Read Failed."
		print "*******************************************************"
		
def write_txt(target_file,content):
	try:
		config_file = open(target_file,"a")
		config_file.write(content)
		config_file.write("\r\n")
		config_file.close()
		print "File Write Succeed."
		print "*******************************************************"
	except:
		print "File Write Failed."
		print "*******************************************************"