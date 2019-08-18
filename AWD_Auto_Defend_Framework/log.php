<?php
	//By ZacharyZcR
	error_reporting(0);
	//Monitor part
	//--------------Parameters Edit--------------
	$FILE_Fisrt_Parameter="pic";
	//-------------------------------------------
	//-------------------------------------------
	date_default_timezone_set('Asia/Shanghai');
	$ip = $_SERVER["REMOTE_ADDR"];
	$agent    = $_SERVER["HTTP_USER_AGENT"];
	$filename = $_SERVER['PHP_SELF'];
	$parameter= $_SERVER["QUERY_STRING"];
	$cookie   = $_SERVER["HTTP_COOKIE"];
	$accept   = $_SERVER['HTTP_ACCEPT'];
	$method   = $_SERVER['REQUEST_METHOD']; 
	$time     = date('Y-m-d H:i:s',time());
	$Dport    = $_SERVER["SERVER_PORT"];
	$Aport    = $_SERVER ["REMOTE_PORT"];
	$payload  = file_get_contents('php://input');
	$name=$_FILES[$FILE_Fisrt_Parameter]['name'];
	$size=$_FILES[$FILE_Fisrt_Parameter]['size'];
	$type=$_FILES[$FILE_Fisrt_Parameter]['type'];
	$tmp_name=$_FILES[$FILE_Fisrt_Parameter]['tmp_name'];
	$file_content=file_get_contents($_FILES[$FILE_Fisrt_Parameter]['tmp_name']);
	a
	$logname = $ip.'.txt';
	$success = 'Attack Success!'."\r\n";
	$fail = 'Attack Fail!'."\r\n";
	$threaten_list = array("select","union","insert","alter","from","where","and","or","order","group","master","exec","|",".","+","*","[","]",",","?",":","'");
	$banner = '********************************************'."\r\n";
	$warning = 'Warning.Uploading File!'."\r\n";
	
	$log_time = 'Time：'.$time."\r\n";
	$log_ip = 'IP：'.$ip."\r\n";
	$log_address = 'Address and parameter：'.$filename.'?'.$parameter."\r\n";
	$log_UA = 'User agent：'.$agent."\r\n";
	$log_cookie ='Cookie：'.$cookie."\r\n";
	$log_accept ='Accept：'.$accept."\r\n";
	$log_method ='Method：'.$method."\r\n";
	$log_port ='Attack port：'.$Aport.' Denfense port：'.$Dport."\r\n";
	$log_payload = 'Payload：'.$payload."\r\n";
	$log_file_name = 'File name：'.$name."\r\n";
	$log_file_size = 'File size：'.$size."\r\n";
	$log_file_type = 'File type：'.$type."\r\n";
	$log_file_tmp_name = 'File tmp name：'.$tmp_name."\r\n";
	$log_file_content = 'File content:'.$file_content."\r\n";
	
	$dlog = fopen($logname, "a");
	fwrite($dlog, $log_time);
	fwrite($dlog, $log_ip);
	fwrite($dlog, $log_port);
	fwrite($dlog, $log_method);
	fwrite($dlog, $log_address);
	fwrite($dlog, $log_UA);
	fwrite($dlog, $log_cookie);
	fwrite($dlog, $log_accept);
	fwrite($dlog, $log_payload);
	if ($name != ''){
		fwrite($dlog, $warning);
		fwrite($dlog, $log_file_name);
		fwrite($dlog, $log_file_size);
		fwrite($dlog, $log_file_type);
		fwrite($dlog, $log_file_tmp_name);
		fwrite($dlog, $log_file_content);
	};
	fwrite($dlog, $banner);
	fclose($dlog);
	//Why must I explain to you ?
	
	//Rebound part 
	//Don't be attacked forever.
	//Show them their weapons' power!
	//----------------------------------------
	//$target = "";
	//----------------------------------------
	/*if ($method == "GET"){
		$ch = curl_init();
		curl_setopt($ch,CURLOPT_URL,$target);
		curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
		curl_setopt($ch,CURLOPT_HEADER,0);
		curl_setopt($ch,CURLOPT_USERAGENT,$agent);
		curl_setopt($ch,CURLOPT_COOKIE,$cookie);
		$output = curl_exec($ch);
		curl_close($ch);
	
		$dlog = fopen($logname, "a");
		if($output === FALSE ){
				fwrite($dlog, curl_error($rb));
				fwrite($dlog, $fail);
				fwrite($dlog, $banner);
			}
			else {
				fwrite($dlog, $success);
				fwrite($dlog, $banner);
			}
			fclose($dlog);
	}
	if ($method == "POST"){
		$ch = curl_init();
		curl_setopt($ch,CURLOPT_URL,$target);
		curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
		curl_setopt($ch,CURLOPT_HEADER,0);
		curl_setopt($ch,CURLOPT_USERAGENT,$agent);
		curl_setopt($ch,CURLOPT_COOKIE,$cookie);
		curl_setopt($ch,CURLOPT_POSTFIELDS,$payload);
		$output = curl_exec($ch);
		curl_close($ch);
	
		$dlog = fopen($logname, "a");
		if($output === FALSE ){
				fwrite($dlog, curl_error($rb));
				fwrite($dlog, $fail);
				fwrite($dlog, $banner);
			}
			else {
				fwrite($dlog, $success);
				fwrite($dlog, $banner);
			}
			fclose($dlog);
	}*/
	//Firewall part
	for ($i=0;$i<=count($threaten_list);$i++){
		if (strpos($parameter,$threaten_list[$i])!== false || strpos($payload,$threaten_list[$i])!== false){
			$alog = fopen("attack_log.txt", "a");
			fwrite($alog, $$log_time);
			fwrite($alog, $log_ip);
			fwrite($alog, $log_method);
			fwrite($alog, $log_address);
			fwrite($alog, $log_payload);
			fwrite($alog, $banner);
			fclose($alog);
			sleep(15);
			die("Go out hacker!");
		};
	};
	
	
?>
