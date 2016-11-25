<?php	
	$servername = "52.165.29.136";
	$username = "root";
	$password = "Nopassword01";
	$dbname = "autohome";

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);

	// Check connection
	if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
	} 
	$sql = "SELECT * FROM switch";
	$result = $conn->query($sql);
	if ($result->num_rows > 0) {
    	// output data of each row
    		while($row = $result->fetch_assoc()) {
        		$arr = array("sw1" => $row["sw_1"],"sw2" => $row["sw_2"],"sw3" => $row["sw_3"],"temp" => $row["temp"]);
    		}
	} else {
    		echo "0 results";
	}

	echo json_encode($arr);
	$conn->close();
?>
