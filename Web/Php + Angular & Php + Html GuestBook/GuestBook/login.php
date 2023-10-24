<?php
session_start();

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve username and password from the form
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Connect to the database and perform the query
    $con = new mysqli("localhost", "root", "", "guestbook");
    if (!$con) {
        die('Could not connect: ' . mysqli_error());
    }

    // Prepare the SQL statement to retrieve user details
    $sql = "SELECT * FROM user WHERE username = '$username' AND password = '$password'";
    $result = $con->query($sql);

    // Check if a matching user is found
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();

        // Retrieve the role of the user
        $role = $row["role"];

        // Store the role in the session
        $_SESSION["role"] = $role;

        // Redirect to addbook.html if the login is successful
        header("Location: addbook.html");
        exit();
    } else {
        echo "Invalid username or password.";
    }

    // Close the database connection
    mysqli_close($con);
}
?>
