<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'vendor/phpmailer/phpmailer/src/Exception.php';
require 'vendor/phpmailer/phpmailer/src/PHPMailer.php';
require 'vendor/phpmailer/phpmailer/src/SMTP.php';

$mail = new PHPMailer(true);

try {
    // Vérification des données entrantes
    if (!isset($_POST['mail']) || !filter_var($_POST['mail'], FILTER_VALIDATE_EMAIL)) {
        die('Adresse email invalide.');
    }
    if (!isset($_POST['name']) || !isset($_POST['lastName']) || !isset($_POST['message'])) {
        die('Données manquantes.');
    }

    $senderEmail = $_POST['mail'];
    $name = htmlspecialchars($_POST['name']);
    $lastName = htmlspecialchars($_POST['lastName']);
    $message = htmlspecialchars($_POST['message']);

    // Paramètres SMTP
    $mail->isSMTP();
    $mail->Host = 'smtp.gmail.com';
    $mail->SMTPAuth = true;
    $mail->Username = 'beouche.zineddine@gmail.com'; // Votre adresse email
    $mail->Password = 'zrfi jqto jnsv iqgq';         // Votre mot de passe
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port = 587;

    // Expéditeur et destinataire
    $mail->setFrom('beouche.zineddine@gmail.com', 'Portfolio Contact');
    $mail->addReplyTo($senderEmail, $name . ' ' . $lastName);
    $mail->addAddress('beouche.zineddine@gmail.com', 'Nom du destinataire');

    // Contenu
    $mail->isHTML(true);
    $mail->Subject = 'Portfolio - Message de ' . $name . ' ' . $lastName;
    $mail->Body = nl2br($message);

    $mail->send();
    echo 'Email envoyé avec succès';
} catch (Exception $e) {
    echo "L'email n'a pas pu être envoyé. Erreur: {$mail->ErrorInfo}";
}

?>
