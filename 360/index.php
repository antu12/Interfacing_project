<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>AutoHome</title>
	<link href="bootstrap.min.css" rel="stylesheet">
	<link href="bootstrap-switch.min.css" rel="stylesheet">
	<script type="text/javascript" src="jquery-3.1.1.min.js"></script>
	<script src="bootstrap-switch.min.js"></script>
</head>
<body>
	<!-- Static navbar -->
    <nav class="navbar navbar-default navbar-static-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">AutoHome</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>


    <div class="container">

      <!-- Main component for a primary marketing message or call to action -->
      <div class="jumbotron">
      

        	
        	<h2>Prototype Room</h2>
  			<p>Check Your room temparature and access your switches here:</p>            
			  <table class="table">
			    <thead>
			      <tr>
			        <th>Selectors</th>
			        <th>Value / Name</th>
			      </tr>
			    </thead>
			    <tbody>
			      <tr>
			        <td>Temparature</td>
			        <td><div id="temp">0</div></td>
			      </tr>
			      <tr>
			        <td>Switch 1</td>
			        <td>Light 1</td>
			        <td><input type="checkbox" name="my-checkbox" id="sw1"></td>
			      </tr>
			      <tr>
			        <td>Switch 2</td>
			        <td>Light 2</td>
			        <td><input type="checkbox" name="my-checkbox" id="sw2"></td>
			      </tr>
			      <tr>
			        <td>Switch 3</td>
			        <td>Fan</td>
			        <td><input type="checkbox" name="my-checkbox" id="sw3"></td>
			      </tr>
			    </tbody>
			  </table>
      </div>
	
	</div> <!-- /container -->
	
	
	<script type="text/javascript">
		$(document).ready(function() {
			// body...
			var json="";
			var temp="";
			var sw3="";
			var sw2="";
			var sw1="";
			var callDb = function() {
				// body...
				$.ajax({
					method:'get',
					url:'data.php',
					success:function(data) {
						// body...
						$json=data;
						var obj = JSON.parse($json);
						$temp=obj.temp;
						$('#temp').html($temp);
						$sw1=obj.sw1;
						if ($sw1 == '0') {
							$("#sw1").bootstrapSwitch('state', false);
						}else{
							$('#sw1').bootstrapSwitch('state', true);
						}
						$sw2=obj.sw2;
						if ($sw2 == '0') {
							$('#sw2').bootstrapSwitch('state', false);
						}else{
							$('#sw2').bootstrapSwitch('state', true);
						}
						$sw3=obj.sw3;
						if ($sw3 == '0') {
							$('#sw3').bootstrapSwitch('state', false);
						}else{
							$('#sw3').bootstrapSwitch('state', true);
						}
					}
				});
			}

			setInterval(callDb,5000);
		});
	</script>
	<script type="text/javascript">
		$("[name='my-checkbox']").bootstrapSwitch();

			//switch 1
    		$("#sw1").on('switchChange.bootstrapSwitch',function(){
    			var st = $('#sw1').bootstrapSwitch('state');
        		$.ajax({
            		url: "update.php",
            		type: "POST",
            		data: {state: "sw_1,"+st}, //this sends the user-id to php as a post variable, in php it can be accessed as $_POST['uid']
            		success: function(data){
            			console.log(data);
                		//update some fields with the updated data
                		//you can access the data like 'data["driver"]'
            		}
        		});
    		});

    		//switch 2
    		$("#sw2").on('switchChange.bootstrapSwitch',function(){
    			var st = $('#sw2').bootstrapSwitch('state');
        		$.ajax({
            		url: "update.php",
            		type: "POST",
            		data: {state: "sw_2,"+st}, //this sends the user-id to php as a post variable, in php it can be accessed as $_POST['uid']
            		success: function(data){
            			console.log(data);
                		//update some fields with the updated data
                		//you can access the data like 'data["driver"]'
            		}
        		});
    		});

    		//switch 3
    		$("#sw3").on('switchChange.bootstrapSwitch',function(){
    			var st = $('#sw3').bootstrapSwitch('state');
        		$.ajax({
            		url: "update.php",
            		type: "POST",
            		data: {state: "sw_3,"+st}, //this sends the user-id to php as a post variable, in php it can be accessed as $_POST['uid']
            		success: function(data){
            			console.log(data);
                		//update some fields with the updated data
                		//you can access the data like 'data["driver"]'
            		}
        		});
    		});
		
	</script>
</body>
</html>