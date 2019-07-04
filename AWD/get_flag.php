<?php
	$ip = $_SERVER["REMOTE_ADDR"];
	if($ip=='117.173.217.106'){
		echo("Administrator Confirmation.\r\n");
		system("cat /flag");
	}
	else echo('flag{'.md5(mt_rand()).'}');
//By ZacharyZcR