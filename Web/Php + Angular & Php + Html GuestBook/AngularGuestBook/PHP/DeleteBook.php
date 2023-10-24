<?php

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE');
header('Access-Control-Allow-Headers: Content-Type');

$con = new mysqli("localhost", "root", "", "guestbook");

if (!$con) {
    die('Could not connect: ' . mysqli_error());
}

if ($_SERVER["REQUEST_METHOD"] == "DELETE") {
    $titleToDelete = $_GET["BookName"];

    if ($titleToDelete) {
        $sql = "DELETE FROM guestbook WHERE title = '$titleToDelete'";
        $result = $con->query($sql); 

        if ($result) {
            $response = array(
                "message" => "Row deleted successfully."
            );
            echo json_encode($response);
        } else {
            $response = array(
                "error" => "Failed to delete row."
            );
            echo json_encode($response);
        }
    }
}

mysqli_close($con);
?>
