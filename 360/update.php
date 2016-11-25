<?php
	if(isset($_POST['state'])){
    //connect to the db
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
	$arr = explode(",", $_POST['state']);
	if ($arr[1] == "false") {
		$s=0;
	}else{
		$s=1;
	}
	$sql = "UPDATE `switch` SET `".$arr[0]."` = '".$s."' WHERE `switch`.`id_switch` = 'room1'";

	if (mysqli_query($conn, $sql)) {
    	echo "Record updated successfully";
	} else {
    	echo "Error updating record: " . mysqli_error($conn);
	}

	mysqli_close($conn);
}
?>