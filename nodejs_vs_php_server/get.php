<?php
  ini_set("session.cookie_httponly", 1);
  header("Content-Type: application/json");

  echo json_encode(array(
    "first_name" => "Quan",
    "last_name" => "Khuc",
    "status" => 200
  ));
  exit;
?>