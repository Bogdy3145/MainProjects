<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, OPTIONS, PUT');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json');

session_start();

$con = new mysqli("localhost", "root", "", "guestbook");

if (!$con) {
    die('Could not connect: ' . mysqli_error());
}

//if (isset($_SESSION["role"]) && $_SESSION["role"] == "admin") {
    if (true){
    try {
        if ($_SERVER["REQUEST_METHOD"] == "PUT") {
            $data = json_decode(file_get_contents("php://input"), true);
            $titleToUpdate = mysqli_real_escape_string($con, $data["Title"]);
            $title = mysqli_real_escape_string($con, $data["Title"]);
            $author = mysqli_real_escape_string($con, $data["Author"]);
            $comment = mysqli_real_escape_string($con, $data["Comment"]);
            $date = mysqli_real_escape_string($con, $data["Date"]);
            
            // Check if the title exists in the database
            $checkQuery = "SELECT * FROM guestbook WHERE title = '$titleToUpdate'";
            $result = $con->query($checkQuery);
            
            if ($result->num_rows > 0) {
                // Title exists, perform the update
                $sql = "UPDATE guestbook SET author='$author', comment='$comment', date='$date' WHERE title = '$titleToUpdate'";
                $con->query($sql);

                $response = [
                    'message' => 'The book ' . htmlspecialchars($data["Title"]) . ' has been updated',
                    'author' => htmlspecialchars($data["Author"]),
                    'title' => htmlspecialchars($data["Title"]),
                    'comment' => htmlspecialchars($data["Comment"]),
                    'date' => htmlspecialchars($data["Date"])
                ];

                echo json_encode($response);
            } else {
                // Title does not exist, display an error message
                //echo "Title does not exist";
            }

            mysqli_close($con);
        }
    } catch (Exception $e) {
        //echo 'Caught exception: ', $e->getMessage(), "\n";
    }
} else {
    // Restrict access for non-admin users
    //echo "Access denied. You do not have sufficient privileges.";
    echo json_encode("BAD");
    exit(); // Terminate the script
}
?>
