# AWD
### AWD线下攻防常用自动化脚本

已经在平台测试过了，全部可用，适用鲁棒性有待检查。

有任何问题请联系QQ：2903735704

#### Vision 1.0.0

各个文件详解：

#### Python：

protect.py

功能：

搜索当前目录下文件名包含php的文件（实际上应该搜索包含.php的文件）

统计文件个数，输出

读入一个参数 1 或 0

1 执行对全部统计文件的内容更改，在文件尾加 php require_once('log.php')

0 退出程序


trojan.py

功能：

读入一句话木马名字，例如：123.php

读入要植入的不死马名字，例如 456.php （要和程序内的edit部分一致）

读入要植入的自动读取flag名字，例如 789.php （要和程序内的edit部分一致）

读入要批量上传的队伍数量（请和trojan_config.txt中的行数一致）

直接循环从trojan.txt读取url（url为上传文件的地址，以/结尾）

通过一句话木马批量植入不死马和自动读取flag

确认成功后每30秒连接一次，确认存活，如果没有存活重复植入


get_score.py

功能：

读入上传flag拿分的url，程序自动连接一次确认可用

读入队伍token

选择上传flag的方式，现在有get和post两种方式

选择post的话会提供 x-www 和 json 两种数据编码方式

选择get会以参数形式上传

读入要批量得分的队伍数量（请和get_score_config.txt中的行数一致）

循环从get_score_config.txt读取url（url为get_flag.php的url）

设定每轮的时间（建议每轮提交flag至少3次，有的时候连接失败）

开始循环提交flag，每轮提交成功的会在下面显示出来

http.py

功能：

循环提交get或post请求，具体用法自己研究一下代码吧，基本就是从get_score.py粘过来的

#### PHP：

while_get_flag：

上传后访问自动运行cat /flag命令，具体可以自己改

有一个IP匹配设置，只有访问IP为植入者IP会报正确flag，其他IP访问会报flag{md5(random())}

采用常见不死马设置

while_shell

常见不死马，md5=19991108

base_shell.php 

基础php一句话

get_flag.php 

上传后访问自动运行cat /flag命令，具体可以自己改

有一个IP匹配设置，只有访问IP为植入者IP会报正确flag，其他IP访问会报flag{md5(random())}

log.php

日志检测，提供IP确认功能，正确IP访问会报确认管理员字段（暂时没有卵用）

日志生成在当前目录下，每一个IP生成一个.txt文件

记录get，post访问记录，对文件上传也有记录，不确定能否记录内容

最后一部分提供反代代码（已经注释），可以根据规则自行使用，不赘述。


#### TXT：

trojan_config.txt

trojan.py的配置文件，里面包含几行（行数与输入的队伍数量一致），每一行是基础一句话的上传目录，以/结尾

get_score_config.txt

get_score.py的配置文件，里面包含几行（行数与输入的队伍数量一致），每一行是你的get_flag.php的路径，以.php结尾


#### Vision 1.0.1

更新内容：

在所有脚本内需要更改的地方用中文标注了，直接运行会导致报错

#### Vision 1.1.0

更新内容：

protect.py修改了增加require_once的代码，现在会自动寻找<?php并在他的下一行添加

log.php增加了关键字检测功能，具体列表可以自由添加

更新base_shell.php为config.php
