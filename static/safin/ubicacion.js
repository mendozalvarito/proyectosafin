$(function(){
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(getCoords,getError);
    }else {
        initialize(-11.022923,-68.759169);
    }
    function getCoords(position) {
     var lat = position.coords.latitude;
     var lng = position.coords.longitude;
     initialize(lat,lng);
    }
    function getError(err) {
        initialize(-11.022923,-68.759169);
    }
    function initialize(lat,lng)
    {
        var latlng = new goole.maps.LatLng(lat,lng);
        var mapSettings = {
            center: latlng,
            zoom: 15,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }
     map = new google.maps.Map($('#mapa').get(0),mapSettings);
    }
});