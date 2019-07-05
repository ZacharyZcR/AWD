507f546195544d36a02a24f1e73eb773 = 19991108 
一位武汉妹子的生日。

攻击操作顺序为：
1，手工种base_shell.php
2，运行trojan.py批量上传不死马和不死getshell
3，运行get_score.py自动提交flag拿分
防御操作顺序为：
1，手工down源码
2，把protect.py放到保护目录运行
3，将改好的源码回传
4，上传log.php开启监测

其中，需要改IP的有：
log.php
get_flag.php
trojan.py
while_get_flag.php
改成自己的ip，别人访问会爆假flag，自己访问会爆真flag

增加了文件读取功能
get_score.py文件每一行一个已经种好get_flag.php的url
trojan.py文件每一行一个上传文件目录的url（以/结尾，文件会自动连接当前目录的webshell一句话，然后往里面写一个不死马和一个不死getflag文件）

不死马可以单独上传也可以批量上传