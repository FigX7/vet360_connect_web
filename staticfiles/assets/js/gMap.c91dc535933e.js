 // Note: This example requires that you consent to location sharing when
    // prompted by your browser. If you see the error "The Geolocation service
    // failed.", it means you probably did not give permission for the browser to
    // locate you.
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
        zoom: 12,
        disableDefaultUI: true,
        zoomControl: true,
      });
      infoWindow = new google.maps.InfoWindow;

      // Try HTML5 geolocation.
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
          var pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };

          var iconBase = "static/assets/img/avatar_mil.png";
          var marker = new google.maps.Marker({
              position: pos,
              icon: iconBase,
              map: map
            });
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

    function handleLocationError(browserHasGeolocation, infoWindow, pos) {
      infoWindow.setPosition(pos);
      infoWindow.setContent(browserHasGeolocation ?
                            'Error: The Geolocation service failed.' :
                            'Error: Your browser doesn\'t support geolocation.');
      infoWindow.open(map);
    }
    