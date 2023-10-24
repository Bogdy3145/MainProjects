<?php
session_start();

$con = new mysqli("localhost", "root", "", "guestbook");

if (!$con) {
    die('Could not connect: ' . mysqli_error());
}

if ($_SESSION["role"] == "admin") {
    // Allow access to all functionality

    try {
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $titleToUpdate = mysqli_real_escape_string($con, $_POST["Title"]);
            $title = mysqli_real_escape_string($con, $_POST["Title"]);
            $author = mysqli_real_escape_string($con, $_POST["Author"]);
            $comment = mysqli_real_escape_string($con, $_POST["Comment"]);
            $date = mysqli_real_escape_string($con, $_POST["Date"]);

            // Check if the title exists in the database
            $checkQuery = "SELECT * FROM guestbook WHERE title = '$titleToUpdate'";
            $result = $con->query($checkQuery);
            
            if ($result->num_rows > 0) {
                // Title exists, perform the update
                $sql = "UPDATE guestbook SET author='$author', comment='$comment', date='$date' WHERE (title = '$titleToUpdate')";
                $con->query($sql);

                echo 'Row Updated successfully.';
            } else {
                // Title does not exist, display an error message
                echo 'Title does not exist in the database.';
            }

            mysqli_close($con);
        }
    } catch (Exception $e) {
        echo 'Caught exception: ', $e->getMessage(), "\n";
    }
} else {
    // Restrict access for non-admin users
    echo "Access denied. You do not have sufficient privileges.";
    // Or redirect to a different page
    //header("Location: restricted.html");
    exit(); // Terminate the script
}
?>
