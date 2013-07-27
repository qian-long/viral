go.onclick = function () {
    var text = $(document.getElementById("search")).val();
    if(text !== "royal baby")
        alert("Please type in 'royal baby'");
    else
        heatMap();
}
var map, pointarray, heatmap;
var data = good_data;
var taxiData = [];

for(var i = 0; i < data.length; i++) {
    taxiData.push(new google.maps.LatLng(data[i][0], data[i][1]));
}

console.log(taxiData);

function heatMap() {
    var mapOptions = {
          center: new google.maps.LatLng(40, 0),
          zoom: 3,
          mapTypeId: google.maps.MapTypeId.TERRAIN,
          panControl: false,
          streetViewControl: false,
          mapTypeControl: false,
          zoomControl: false
        };
        map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);

        // var marker = new google.maps.Marker({
        //   position: new google.maps.LatLng(0,0),
        //   map: map,
        //   title: 'Hello World!',
        //   icon: '../static/img/dots/reddot.png'
        // });

        pointArray = new google.maps.MVCArray(taxiData);

        heatmap = new google.maps.visualization.HeatmapLayer({
            data: pointArray
        });

        heatmap.setMap(map);
}

function initialize() {
        var mapOptions = {
          center: new google.maps.LatLng(40, 0),
          zoom: 3,
          mapTypeId: google.maps.MapTypeId.TERRAIN,
          panControl: false,
          streetViewControl: false,
          mapTypeControl: false,
          zoomControl: false
        };
        map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);

        // var marker = new google.maps.Marker({
        //   position: new google.maps.LatLng(0,0),
        //   map: map,
        //   title: 'Hello World!',
        //   icon: '../static/img/dots/reddot.png'
        // });

        // pointArray = new google.maps.MVCArray(taxiData);

        // heatmap = new google.maps.visualization.HeatmapLayer({
        //     data: pointArray
        // });

        // heatmap.setMap(map);

        var boxText = document.createElement("div");
        boxText.style.cssText = "border: 1px solid black; margin-top: 8px; background: yellow; padding: 5px;";
        boxText.innerHTML = "City Hall, Sechelt<br>British Columbia<br>Canada";

        var myOptions = {
            content: boxText
            ,disableAutoPan: false
            ,maxWidth: 0
            ,pixelOffset: new google.maps.Size(-140, 0)
            ,zIndex: null
            ,boxStyle: { 
            background: "url('tipbox.gif') no-repeat"
            ,opacity: 0.75
            ,width: "280px"
            }
            ,closeBoxMargin: "10px 2px 2px 2px"
            ,closeBoxURL: "http://www.google.com/intl/en_us/mapfiles/close.gif"
            ,infoBoxClearance: new google.maps.Size(1, 1)
            ,isHidden: false
            ,pane: "floatPane"
            ,enableEventPropagation: false
        };

        // google.maps.event.addListener(marker, "click", function (e) {
        //     ib.open(theMap, this);
        // });

        var ib = new InfoBox(myOptions);



        // Animation of topbar
        $('#droptop').animate({
            top: -30
        }, 1000, 'easeInOutBack');

        var overDrop = false;
        var temp = false;
        $('#droptop').hover(function(){
            overDrop = true;
            slideUp();
        }, function(){
            overDrop = false;
            if(!stupid)
                slideDown();
            else
                temp = true;
        });

        var stupid = false;
        $(document.body).mousedown(function(){
            stupid = true;
            console.log("SDFSDF");
        }).mouseup(function(){
            if(temp){
                temp=false;
                slideDown();
            }
            stupid = false;
        });

        function slideUp(){
            $('#droptop h2').stop().animate({
                marginTop: '-13px'
            }, 250);
        };

        function slideDown(){
            $('#droptop h2').stop().animate({
                marginTop: '42px'
            }, 250);
        };



        // Activate slider
        $("#my-input").bind("slider:changed", function (event, data) {
            // The currently selected value of the slider
            console.log(data.value);
            stupid = true;

            // The value as a ratio of the slider (between 0 and 1)
            console.log(data.ratio);
        });
      }

      function toggleHeatmap() {
  heatmap.setMap(heatmap.getMap() ? null : map);
}


function changeGradient() {
  var gradient = [
    'rgba(0, 255, 255, 0)',
    'rgba(0, 255, 255, 1)',
    'rgba(0, 191, 255, 1)',
    'rgba(0, 127, 255, 1)',
    'rgba(0, 63, 255, 1)',
    'rgba(0, 0, 255, 1)',
    'rgba(0, 0, 223, 1)',
    'rgba(0, 0, 191, 1)',
    'rgba(0, 0, 159, 1)',
    'rgba(0, 0, 127, 1)',
    'rgba(63, 0, 91, 1)',
    'rgba(127, 0, 63, 1)',
    'rgba(191, 0, 31, 1)',
    'rgba(255, 0, 0, 1)'
  ]
  heatmap.setOptions({
    gradient: heatmap.get('gradient') ? null : gradient
  });
}

function changeRadius() {
  heatmap.setOptions({radius: heatmap.get('radius') ? null : 20});
}

function changeOpacity() {
  heatmap.setOptions({opacity: heatmap.get('opacity') ? null : 0.2});
}


    google.maps.event.addDomListener(window, 'load', initialize);