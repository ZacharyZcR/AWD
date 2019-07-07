import sys
import os
import time
import _thread
import datetime

def get_os():
    os = platform.system()
    if os == "Windows":
        return "n"
    else:
        return "c"

def ping_ip(ip_str):
    cmd = ["ping", "-{op}".format(op=get_os()),
           "1", ip_str]
    output = os.popen(" ".join(cmd)).readlines()

    flag = False
    for line in list(output):
        if not line:
            continue
        if str(line).upper().find("TTL") >=0:
            flag = True
            break
    if flag:
        print("*** *** *** ip: %s is OK  *** *** ***"%(ip_str))

def find_ip(ip_prefix):
    for i in range(1,256):
        ip = ('%s.%s'%(ip_prefix,i))
        _thread.start_new_thread(ping_ip, (ip,))
        time.sleep(0.3)

if __name__ == "__main__":
    startTime = datetime.datetime.now()
    print("start time %s"%(time.ctime()))
    net=sys.argv[1]
    args = "".join(("192.168."+net+".1"))
    ip_prefix = '.'.join(args.split('.')[:-1])
    find_ip(ip_prefix)
    endTime = datetime.datetime.now()
    print("end time %s"%(time.ctime()))
    print("total takes :",(endTime - startTime).seconds)
