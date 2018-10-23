 // Note: This example requires that you consent to location sharing when
    // prompted by your browser. If you see the error "The Geolocation service
    // failed.", it means you probably did not give permission for the browser to
    // locate you.
var globalPos = "TEST MY_AJAX GLOBAL";
var vetsDict = []
var iconBase = "static/assets/img/avatar_mil.png";
// Map________________________________------------------------ //
    var map, infoWindow;
    
					  /**-------------------- VOr Map Buttons -------------------- ***
					       * The CenterControl adds a control to the map that recenters the map on
					       * Chicago.
					       * This constructor takes the control DIV as an argument.
					       * @constructor
					       */
					      function CenterControl(controlDiv, map) {
					
					        // Set CSS for the control border.
					        var controlUI = document.createElement('div');
					        var elem = document.createElement("i");
					        elem.setAttribute("class", "icon-file-cabinet");
					       
					        elem.style.fontSize = "10vh";
					        
					        controlUI.style.border = '2px solid #fff';
					        controlUI.style.borderRadius = '3px';
					        controlUI.style.boxShadow = '0 2px 6px rgba(0,0,0,.3)';
					        controlUI.style.cursor = 'pointer';
					        controlUI.style.marginBottom = '22px';
					        controlUI.style.textAlign = 'center';
					        controlUI.title = 'Click to recenter the map';
					        
					        var el = document.createElement('div');
					        


					        var myvar = '<span class="custom-dropdown big">'+
					        '    <select>    '+
					        '        <option>Filter : ALL </option>'+
					        '        <option>Air Force</option>  '+
					        '        <option>Army</option>'+
					        '        <option>Coast Guard</option>'+
					        '        <option>Marines</option>'+
					        '        <option>Navy</option>'+
					        '    </select>'+
					        '</span>';
					        
					     
					        var domString = myvar ;	
					        
					        el.innerHTML =  domString;
					        
					        
					        
					        // Set CSS for the control interior.
					        var controlText = document.createElement('div');
					        controlText.style.color = 'rgb(25,25,25)';
					        controlText.style.fontFamily = 'Roboto,Arial,sans-serif';
					        controlText.style.fontSize = '16px';
					        controlText.style.lineHeight = '38px';
					        controlText.style.paddingLeft = '5px';
					        controlText.style.paddingRight = '5px';
					        controlText.innerHTML = 'Center Map';
					        controlDiv.appendChild(el.firstChild);
					
					         
					
					      } 

    function initMap() {
	
      map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -34.397, lng: 150.644},
        zoom: 15,
        disableDefaultUI: true,
        zoomControl: true,
        gestureHandling: 'greedy',
      });
      infoWindow = new google.maps.InfoWindow;

      // Try HTML5 geolocation.
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
          var pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };
          
          infoWindow.open(map);
          map.setCenter(pos);
        }, function() {
          handleLocationError(true, infoWindow, map.getCenter());
        });
      } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
      }
				      var centerControlDiv = document.createElement('div');
				        var centerControl = new CenterControl(centerControlDiv, map);
				
				        centerControlDiv.index = 1;
				        map.controls[google.maps.ControlPosition.TOP_LEFT].push(centerControlDiv);
				        
    }
    
    
    function addmarker(vet) {

    	pos = {lat:vet['vet_Lat'],lng: vet['vet_Lon']};
    	
        var marker = new google.maps.Marker({
            position: pos,
            draggable: false,
            title: vet['username'],
            map: map,
            
        });
        //CUSSOMIZE INFO WINDOW RIC GUIDANCE 
        var content = '<div id="iw-container">' +
        '<div class="iw-title">'+ vet['username']  +  '</div>' +
        '<div class="iw-content">' +
          '<div class="iw-subTitle"></div>' +
          '<div class="iw-img"><img src="media/'+ vet['ava_user']  +'" height="115" width="83"></div>' +
          '<p>ADD CUSTOM CAPTION OR CONTENTS !!!!!!!</p>' +
          '<div class="iw-subTitle">Contacts</div>' +
          '<p>VISTA ALEGRE ATLANTIS, SA<br>3830-292 Ílhavo - Portugal<br>'+
          '<br>Phone. +351 234 320 600<br>e-mail: geral@vaa.pt<br>www: www.myvistaalegre.com</p>'+
        '</div>' +
        '<div class="iw-bottom-gradient"></div>' +
      '</div>';  
var infowindow = new google.maps.InfoWindow({
content: content,

// Assign a maximum value for the width of the infowindow allows
// greater control over the various content elements
maxWidth: 350
});
        google.maps.event.addListener(marker,'click',function() {
        	 infowindow.open(map,marker);
        	  });
    }
    
    function addmarker2(partner) {

    	pos = {lat:partner['partner_Lat'],lng: partner['partner_Lon']};
    	
        var marker = new google.maps.Marker({
            position: pos,
            draggable: false,
            title: partner['username'],
            map: map
            
        });
        
        //CUSSOMIZE INFO WINDOW RIC GUIDANCE 
        var content = '<div id="iw-container">' +
        '<div class="iw-title">'+ partner['username']  +  '</div>' +
        '<div class="iw-content">' +
          '<div class="iw-subTitle"></div>' +
          '<div class="iw-img"><img src="media/'+ partner['ava_user']  +'" height="115" width="83"></div>' +
          '<p>ADD CUSTOM CAPTION OR CONTENTS !!!!!!!</p>' +
          '<div class="iw-subTitle">Contacts</div>' +
          '<p>VISTA ALEGRE ATLANTIS, SA<br>3830-292 Ílhavo - Portugal<br>'+
          '<br>Phone. +351 234 320 600<br>e-mail: geral@vaa.pt<br>www: www.myvistaalegre.com</p>'+
        '</div>' +
        '<div class="iw-bottom-gradient"></div>' +
      '</div>';  
var infowindow = new google.maps.InfoWindow({
content: content,

// Assign a maximum value for the width of the infowindow allows
// greater control over the various content elements
maxWidth: 350
});
        google.maps.event.addListener(marker,'click',function() {
        	 infowindow.open(map,marker);
        	  });
    }   
    
    function handleLocationError(browserHasGeolocation, infoWindow, pos) {
      infoWindow.setPosition(pos);
      infoWindow.setContent(browserHasGeolocation ?
                            'Error: The Geolocation service failed.' :
                            'Error: Your browser doesn\'t support geolocation.');
      infoWindow.open(map);
    }
    
function ajaxCall(x){
		
		$.ajax({
	        url: "ajax/getLocation",
	        type:"Post",
	        dataType: 'json',
	       
    		data: {
				// here getdata should be a string so that
				// in your views.py you can fetch the value using get('getdata')
				'getdata': JSON.stringify(x)
    		},
	        success: function (res, status) {
	    		console.log("ajax Post Success")
	    		
	        },
	        error: function (res) {
	        	console.log(res)                                                                                                                          
	        }
		});	
	}
function showLocation(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    var results = {"lat" : latitude,"lon" : longitude};
    ajaxCall(results);
}

 function errorHandler(err) {
    if(err.code == 1) {
       alert("Error: Access is denied!");
    } else if( err.code == 2) {
       alert("Error: Position is unavailable!");
    }
 }
	
 function getLocation() {

    if(navigator.geolocation) {
       
       // timeout at 60000 milliseconds (60 seconds)
       var options = {timeout:60000};
       navigator.geolocation.getCurrentPosition(showLocation, errorHandler, options);
    } else {
       alert("Sorry, browser does not support geolocation!");
    }
 }
 function ajaxCallGet(){
	 $.ajax({
	        url: "ajax/getLocation",
	        type:"GET",
	        dataType: 'json',
	       
			
	        success: function (context) {
	    		var veti = 1;
	    		var partneri = 1;
	    		for(x in context.queryVet){
	    			
	    			
	    			
	    			//addmarker(vetsPos,tempPic,context.query[i]['username']); 
	    			addmarker(context.queryVet[veti]);
	    			veti++;
    			}
	    		for(y in context.queryPartners){
	    			
	    			//addmarker(vetsPos,tempPic,context.query[i]['username']); 
	    			addmarker2(context.queryPartners[partneri],1);
	    			partneri++;
    			}
    		},
	        error: function (res) {
	        	console.log("ARR");                                                                                                                          
	        }
		});	
 }

    $(document).ready(function() {
    	
    	getLocation();
    	ajaxCallGet();
    	
    });
    