/**

 * 
 */
// Map________________________________------------------------ //
    var map, geocoder,geocodeResult,part_Lat,part_Lon,part_Pos;
	var  sdPos = {lat: 39.687399, lng: -101.908974};
	
	function initMap() {
        
		
        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 3,
          center: sdPos
        }); 
        



	 var geocoder = new google.maps.Geocoder();
	 document.getElementById('btn-geocode').addEventListener('click', function() {
         
		 geocodeAddress(geocoder, map);
		 
       });
	
	}
	function geocodeAddress(geocoder, resultsMap) {
		
	    var address = document.getElementById('partner_address').value;
	    geocoder.geocode({'address': address}, function(results, status) {
	      if (status === 'OK') {
	        resultsMap.setCenter(results[0].geometry.location);
	        resultsMap.setZoom(12);
	        var marker = new google.maps.Marker({
	          map: resultsMap,
	          position: results[0].geometry.location
	        });
	        geocodeResults = results;
	        part_Pos = results[0].geometry.location;
	       
	      } else {
	        alert('Geocode was not successful for the following reason: ' + status);
	      }
	    });
	    
	    
}
	function ajaxGeocode(x){
			
			$.ajax({
		        url: "ajax/setPartnerPos",
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

	function partSetPos(){
		ajaxGeocode(part_Pos);
    	
	}
	
$(document).ready(function() {
    	
    	
    	
    });
	 
   