<?php

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, OPTIONS, POST');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json'); // Set the response content type to JSON

session_start();

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve username and password from the form
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Connect to the database and perform the query
    $con = new mysqli("localhost", "root", "", "exam");
    if (!$con) {
        die('Could not connect: ' . mysqli_error());
    }

    // Prepare the SQL statement to retrieve user details
    $sql = "SELECT * FROM User WHERE User = '$username' AND Password = '$password'";
    $result = $con->query($sql);

    // Check if a matching user is found
    if ($result->num_rows > 0) {
        
        $row = $result->fetch_assoc();

        // Retrieve the role of the user
        $role = $row["Role"];

        $response = ['role' => $role,
                    'userid' => $row['Id']];

        echo json_encode($response);

        // Store the role in the session
        $_SESSION["role"] = $role;

        // Redirect to addbook.html if the login is successful
        exit();
    } else {
        
    }

    // Close the database connection
    mysqli_close($con);
}
?>
