<?php

if (isset($_POST['email']) && isset($_POST['name']) && isset($_POST['subject'])) {
#Receive user input
$email = $_POST['email'];
$name = $_POST['name'];
$subject = $_POST['subject'];

#Send email
$mailTo = "katie_blalock@yahoo.com";
$headers = "From: ".$email;
$txt = "You have received an email from ".$name." .\n\n".$subject;

mail($mailTo, $subject, $txt, $headers);
header("Location: home.html?mailsend");
}

?>