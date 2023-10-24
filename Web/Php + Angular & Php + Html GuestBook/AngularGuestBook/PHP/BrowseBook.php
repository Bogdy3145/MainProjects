<?php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json'); // Set the response content type to JSON


$con = new mysqli("localhost", "root", "", "guestbook");

if (!$con) {
    die('Could not connect: ' . mysqli_error());
}

// Number of records per page
$recordsPerPage = 2;

// Get the current page number from the request
$page = isset($_GET['page']) ? $_GET['page'] : 1;

// Calculate the offset for the database query
$offset = ($page - 1) * $recordsPerPage;

// Filter parameters
$filterAuthor = isset($_GET['filter_by_author']) ? $_GET['filter_by_author'] : '';
$filterTitle = isset($_GET['filter_by_title']) ? $_GET['filter_by_title'] : '';

// Build the SQL query with pagination and filtering
$sql = "SELECT * FROM guestbook WHERE author LIKE '%$filterAuthor%' AND title LIKE '%$filterTitle%' LIMIT $offset, $recordsPerPage";
$result = $con->query($sql);

$books = [];
// while ($row = $result->fetch_assoc()) {
//     $books[] = [
//         'author' => $row['author'],
//         'title' => $row['title'],
//         'comment' => $row['comment'],
//         'date' => $row['date']
//     ];
// }

if($result = mysqli_query($con, $sql))
{
  $cr = 0;
  while($row = mysqli_fetch_assoc($result))
  {
    $books[$cr]['Title'] = $row['title'];
    $books[$cr]['Author'] = $row['author'];
    $books[$cr]['Comment'] = $row['comment'];
    $books[$cr]['Date'] = $row['date'];
    
    $cr++;
  }
}

// Count the total number of records for pagination
$sqlCount = "SELECT COUNT(*) AS count FROM guestbook WHERE author LIKE '%$filterAuthor%' AND title LIKE '%$filterTitle%'";
$countResult = $con->query($sqlCount);
$totalRecords = $countResult->fetch_assoc()['count'];

// Calculate the total number of pages
$totalPages = ceil($totalRecords / $recordsPerPage);

// Prepare the response data
$response = [
    'books' => $books,
    'totalPages' => $totalPages
];

// Send the response as JSON
header('Content-Type: application/json');
echo json_encode($response);

mysqli_close($con);
?>
