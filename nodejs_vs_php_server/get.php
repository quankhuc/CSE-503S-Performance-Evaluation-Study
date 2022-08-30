<?php
  include 'data.php';
  session_start();
  ini_set("session.cookie_httponly", 1);
  header("Content-Type: application/json");

  echo json_encode(array(
    "first_name" => $_SESSION['first_name'],
    "last_name" => $_SESSION['last_name'],
    "status" => $_SESSION['status']
  ))

  session_destroy();
  exit;
?>