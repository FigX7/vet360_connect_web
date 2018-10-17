/**
 * 
 */
function initMap() {
        
		var  sdPos = {lat: 32.730588, lng: -117.143608};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 15,
          center: sdPos
        });

        
        var geocoder = new google.maps.Geocoder();

        document.getElementById('submit').addEventListener('click', function() {
          geocodeAddress(geocoder, map);
        });
       
}
function geocodeAddress(geocoder, resultsMap) {
    var address = document.getElementById('address').value;
    geocoder.geocode({'address': address}, function(results, status) {
      if (status === 'OK') {
        resultsMap.setCenter(results[0].geometry.location);
        var marker = new google.maps.Marker({
          map: resultsMap,
          position: results[0].geometry.location
        });
        alert(results[0].address_components[0].long_name);
      } else {
        alert('Geocode was not successful for the following reason: ' + status);
      }
    });
  }
   