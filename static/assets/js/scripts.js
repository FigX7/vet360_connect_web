
	function openSignUp(){
		
		$("#myModal").modal();
	}


	function loginErrors(){
		$("#loginModal").modal();
		$('#signupbox').hide(); 
		$('#loginbox').show();
	}
	function signupErrors(){
		$('#loginModal').modal();
		$('#loginbox').hide(); 
		$('#signupbox').show();
	}
	
	function partloginErrors(){
		$("#partloginModal").modal();
		$('#partsignupbox').hide(); 
		$('#partloginbox').show();
	}
	function partsignupErrors(){
		$('#partloginModal').modal();
		$('#partloginbox').hide(); 
		$('#partsignupbox').show();
	}
	$("#menu").click(function(){
		
		$("#navcol-1").slideToggle("slow");
	});
	$("#xBtn").click(function(){
		
		$("#backdrop").css("display","none");
	});

	/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
	function openNav() {
	    document.getElementById("mySidenav").style.width = "150px";
	    document.getElementById("content_Main").style.marginLeft = "10px";
	    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
	}

	/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
	function closeNav() {
	    document.getElementById("mySidenav").style.width = "0";
	    document.getElementById("content_Main").style.marginLeft = "0";
	    document.body.style.backgroundColor = "white";
	}
	function openMenuDropDown(){
		if($('#dropMenu').css('display') == 'none'){
			$('#dropMenu').css('display',"block");
		}else if ($('#dropMenu').css('display') == 'block'){
			$('#dropMenu').css('display',"none");
		}
		
	}
	function closeProUpdate(){
		$("#myModal").css('display','none');
	}