<?php
$connect = mysql_connect('localhost', 'root','usbw');

		if(!$connect){
			die('Failed to connect: ' . mysql_error());
		}

		if(!mysql_select_db('gemeenteloket')){
			die('Failed to select DB:' . mysql_error());
		}

		$result = mysql_query('SELECT * FROM login');
		$names = array();
		$passes = array();
		while($row = mysql_fetch_array($result)){
		$user = $row['name'];
		array_push($names, $user);
		}
		
		$result = mysql_query('SELECT * FROM login');
		while($row = mysql_fetch_array($result)){
		$pass = $row['pass'];
		array_push($passes, $pass);
		}

$user = $_POST["user"];
$pass =  $_POST["pass"];


		$key_user = array_search($user, $names); //find key from names array
		$key_pass = array_search($pass, $passes); //find key from passes array
		$pass_correct = $passes[$key_user]; //finds correct password
		
		if  ($pass_correct == $pass) {
			session_start();
			$_SESSION["user"] = $user;
			$_SESSION["login"] = "ok";
			
		} else {
			header('Location: '. "index.php");
		}
?>