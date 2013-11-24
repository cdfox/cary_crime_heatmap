function initialize() {
	var mapOptions = {
		center: new google.maps.LatLng(35.7914, -78.7814),
		zoom: 13,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	var map = new google.maps.Map(document.getElementById("map_canvas"),
		mapOptions);

	heatmapData = [];
	for (var i in crimes) {
		var crime_location = new google.maps.LatLng(crimes[i].lat, crimes[i].lng);
		heatmapData.push(crime_location);
	}

	var heatmap = new google.maps.visualization.HeatmapLayer({
	  data: heatmapData,
	  radius: 50,
	  //maxIntensity: 500
	});
	heatmap.setMap(map);
}   