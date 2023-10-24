<?php
$con = new mysqli("localhost", "root", "", "guestbook");

if (!$con) {
    die('Could not connect: ' . mysqli_error());
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $titleToDelete = mysqli_real_escape_string($con, $_POST["title"]);

    if ($titleToDelete) {
        $sql = "DELETE FROM guestbook WHERE title = '$titleToDelete'";
        if ($con->query($sql)) {
            echo 'Entry deleted successfully.';
        } else {
            echo 'Error deleting entry: ' . mysqli_error($con);
        }
    }
}

mysqli_close($con);
?>
