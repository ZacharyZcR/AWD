<?php
	$ip = $_SERVER["REMOTE_ADDR"];
	if($ip=='需要改成自己IP'){
		echo("Administrator Confirmation.\r\n");
		system("cat /flag");
	}
	else echo('flag{'.md5(mt_rand()).'}');
//By ZacharyZcR