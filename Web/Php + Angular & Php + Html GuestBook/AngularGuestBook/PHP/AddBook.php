<?php

header('Access-Control-Allow-Origin: http://localhost:4200'); // Adjust the origin to match your Angular app URL
header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json'); // Set the response content type to JSON


$con = new mysqli("localhost", "root", "", "guestbook");

if (!$con) {
    die('Could not connect: ' . mysqli_error());
}

$errors = array();

try {
    if ($_SERVER["REQUEST_METHOD"] == "POST") {


        $data = json_decode(file_get_contents("php://input"),true);

        $author = $data["Author"];
        $title = $data["Title"]; // Updated input name
        $comment = $data["Comment"];
        $date = $data["Date"];

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

            if ($stmt->execute()) {
                

                $response = [
                    'message' => 'The book' . htmlspecialchars($data["Title"]) . 'has been added',
                    'author' => htmlspecialchars($data["Author"]),
                    'title' => htmlspecialchars($data["Title"]),
                    'comment' => htmlspecialchars($data["Comment"]),
                    'date' => htmlspecialchars($data["Date"])
                ];

                echo json_encode($response);
            } else {

                printf("%d Row inserted.\n", mysqli_affected_rows($con));
            }

            $stmt->close();
        }
        else{

        }
    }
} catch (Exception $e) {
    echo 'Caught exception: ', $e->getMessage(), "\n";
}

mysqli_close($con);
?>
