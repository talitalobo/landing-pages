<?php
// Check for empty fields
if(empty($_POST['name'])  		||
   empty($_POST['email']) 		||
   empty($_POST['phone']) 		||
   empty($_POST['message'])	||
   !filter_var($_POST['email'],FILTER_VALIDATE_EMAIL))
   {
	echo "No arguments Provided!";
	return false;
   }
	
$name = $_POST['name'];
$email_address = $_POST['email'];
$phone = $_POST['phone'];
$message = $_POST['message'];
	
// Create the email and send the message
$to = 'talitabac@gmail.com'; // Add your email address inbetween the '' replacing yourname@yourdomain.com - This is where the form will send a message to.
$email_subject = "Contato RunMusic de:  $name";
$email_body = "Nova mensagem.\n\n"."Detalhes:\n\nNome: $name\n\nEmail: $email_address\n\nTelefone: $phone\n\nMenssagem:\n$message";
$headers = "From: noreply@runmusic.me\n"; 
$headers .= "Reply-To: $email_address";	
mail($to,$email_subject,$email_body,$headers);
return true;			
?>