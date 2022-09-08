<?php
  header("Content-Type: application/json");
  $data_str = file_get_contents('php://input');
  $data_obj = json_decode($data_str, true);
  $first_name = $data_obj['first_name'];
  $last_name = $data_obj['last_name'];
  echo json_encode(array(
    'status' => 200,
    'first_name' => $first_name,
    'last_name' => $last_name
  ));
  $stmt->close();
?>