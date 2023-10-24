<?php
$con = new mysqli("localhost", "root", "", "guestbook");

if (!$con) {
    die('Could not connect: ' . mysqli_error());
}

$errors = array();

try {
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $author = $_POST["Author"];
        $title = $_POST["Title"]; // Updated input name
        $comment = $_POST["Comment"];
        $date = $_POST["Date"];

        // Perform validation
        if (empty($author)) {
            $errors[] = 'Author is required.';
        }

        if (empty($title)) {
            $errors[] = 'Title is required.';
        }

        if (empty($comment)) {
            $errors[] = 'Comment is required.';
        }

        if (empty($date)) {
            $errors[] = 'Date is required.';
        }

        if (empty($errors)) {
            $stmt = $con->prepare("INSERT INTO guestbook (author, title, comment, date) VALUES (?, ?, ?, ?)");
            $stmt->bind_param("ssss", $author, $title, $comment, $date);
            echo 'Row Updated successfully.';
            header("Location: AddBook.html");

            if ($stmt->execute()) {
                echo 'Guest book entry added successfully.';
                echo "<br />";
                echo 'Author: ', htmlspecialchars($_POST["Author"]);
                echo "<br />";
                echo 'Title: ', htmlspecialchars($_POST["Title"]); 
                echo "<br />";
                echo 'Comment: ', htmlspecialchars($_POST["Comment"]);
                echo "<br />";
                echo 'Date: ', htmlspecialchars($_POST["Date"]);
                echo "<br />";
            } else {

                printf("%d Row inserted.\n", mysqli_affected_rows($con));
            }

            $stmt->close();
        }
        else{
            header("Location: AddBook.html");

        }
    }
} catch (Exception $e) {
    echo 'Caught exception: ', $e->getMessage(), "\n";
}

mysqli_close($con);
?>
