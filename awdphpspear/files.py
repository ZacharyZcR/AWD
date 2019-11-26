import os

def read_array(target_file):
	print "*******************************************************"
	try:
		target_array = []
		line_count = 0
		config_file=open(target_file)
		for line in config_file:
			line=line.strip('\r\n')
			target_array.append(line)
			print (line)
			line_count += 1
		print "[+]Total line:",line_count
		print "[+]File Read Succeed."
		print "*******************************************************"
		return target_array
		config_file.close()
	except:
		print "[-]File Read Failed."
		print "*******************************************************"

def read_var(target_file):
	print "*******************************************************"
	try:
		config_file=open(target_file)
		target_variable = config_file.readline()
		target_variable = target_variable.strip('\r\n')
		print "*",target_variable,"*"
		print "[+]File Read Succeed."
		print "*******************************************************"
		config_file.close()
		return target_variable
	except:
		print "[-]File Read Failed."
		print "*******************************************************"
		
def write_txt(target_file,content):
	print "*******************************************************"
	if content != None:
		try:
			config_file = open(target_file,"a")
			config_file.write(content)
			config_file.write("\r\n")
			config_file.close()
			print "[+]File Write Succeed."
			print "*******************************************************"
		except:
			print "[-]File Write Failed."
			print "*******************************************************"
	else:
		print "[-]Content is None."
		print "*******************************************************"
		
def dir_tree(startpath):
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
			
def get_php_list(startpath):
	php_list=[]
	for root,dirs,files in os.walk(startpath,topdown=True):
		for f in files:
			if f[-4:] == '.php':
				root = root.replace('./','')
				php_list.append(root+'/'+f)
	for i in range(len(php_list)):
		print php_list[i]
	return php_list