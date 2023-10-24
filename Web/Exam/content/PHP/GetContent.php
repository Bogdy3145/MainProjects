<?php

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json'); // Set the response content type to JSON

$con = new mysqli("localhost", "root", "", "exam");
if (!$con) {
    die('Could not connect: ' . mysqli_error());
}

$sql = "SELECT * FROM Content";
$result = $con->query($sql);
$data = array();

if($result = mysqli_query($con, $sql))
{
  $cr = 0;
  while($row = mysqli_fetch_assoc($result))
  { 
    $data[$cr]['Id'] = $row['Id'];
    $data[$cr]['Date'] = $row['Date'];
    $data[$cr]['Title'] = $row['Title'];
    $data[$cr]['Description'] = $row['Description'];
    $data[$cr]['Url'] = $row['Url'];
    $data[$cr]['UserId'] = $row['UserId'];

    $cr++;
  }
}

if (!empty($data)) {
    header('Contet-Type: application/json');
    echo json_encode($data);
} else {
    echo json_encode(array('message' => 'No records found.'));
}

$con->close();
?>
