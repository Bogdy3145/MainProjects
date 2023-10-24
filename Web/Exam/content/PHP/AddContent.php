<?php

header('Access-Control-Allow-Origin: http://localhost:4200'); // Adjust the origin to match your Angular app URL
header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json'); // Set the response content type to JSON


$con = new mysqli("localhost", "root", "", "exam");

if (!$con) {
    die('Could not connect: ' . mysqli_error());
}

$errors = array();

try {
    if ($_SERVER["REQUEST_METHOD"] == "POST") {

        $data = json_decode(file_get_contents("php://input"),true);
        

        $descritpion = $data["Description"];
        $title = $data["Title"]; // Updated input name
        $url = $data["Url"];
        $userId = $data["UserId"];
        $date = $data["Date"];

        // Perform validation
        if (empty($descritpion)) {
            $errors[] = 'Author is required.';
        }

        if (empty($title)) {
            $errors[] = 'Title is required.';
        }

        if (empty($date)) {
            $errors[] = 'Comment is required.';
        }

        if (empty($url)) {
            $errors[] = 'Date is required.';
        }

        if (empty($userId)) {
            $errors[] = 'Date is required.';
        }

        if (empty($errors)) {
            $stmt = $con->prepare("INSERT INTO content (Date, Title, Description, Url, UserId) VALUES (?, ?, ?, ?, ?)");
            $stmt->bind_param("sssss", $date, $title, $descritpion, $url, $userId);

            if ($stmt->execute()) {
                
                $response = [
                    'message' => 'The content' . htmlspecialchars($data["Title"]) . 'has been added',
                    'date' => htmlspecialchars($data["Date"]),
                    'title' => htmlspecialchars($data["Title"]),
                    'description' => htmlspecialchars($data["Description"]),
                    'url' => htmlspecialchars($data["Url"])
                ];
                
                // $response = [
                //     'data' => $data
                // ];
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
