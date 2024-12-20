<?php
$email = $_POST['email'];
$to = $email;
$subject = "Portfolio : Message de s$_POST['name'] $_POST['lastName'];";
$txt = $_POST['message'];
$headers = ['From' => $email, 'Reply-To' => $email, 'Content-type' => 'text/html; charset=iso-8859-1'];

mail($to,$subject,$txt,$headers);
?>