var map, pointarray, heatmap;
var data = good_data;
var taxiData = [];
var mapOptions = {
          center: new google.maps.LatLng(40, 0),
          zoom: 3,
          mapTypeId: google.maps.MapTypeId.ROADMAP,
          panControl: false,
          streetViewControl: false,
          mapTypeControl: false,
          zoomControl: false
        };
        map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);
var slider;
var old_slider = 0;
var new_data = cumulativeBucket(data);
console.log("new_data is: ", new_data);


$("body").on("submit", "#form", function(e){
    e.preventDefault();

    var text = $(document.getElementById("search")).val();
    if(text !== "galicia")
        alert("Event currently unmapped");
    else
        slidechange(2);
});

for(var i = 0; i < data.length; i++) {
    taxiData.push(new google.maps.LatLng(data[i][0], data[i][1]));
}

console.log("cumulative buckets, ", cumulativeBucket(data));
console.log(taxiData);

function heatMap(arr) {
    var mapOptions = {
          center: new google.maps.LatLng(40, 0),
          zoom: 4,
          mapTypeId: google.maps.MapTypeId.ROADMAP,
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

        pointArray = new google.maps.MVCArray(arr);

        heatmap = new google.maps.visualization.HeatmapLayer({
            data: pointArray
        });

        heatmap.setMap(map);
}

function slidechange(slider_num) {
    if(slider_num == 0 || slider_num == 1)
        return;
    else {
        console.log("new data: ", new_data[slider_num/2]);
        console.log("slider_num: ", slider_num);
        console.log("length of bucket: ", new_data[Math.round(slider_num/2) - 1].length)
        heatMap(new_data[Math.round(slider_num/2) - 1]);
    }
}

function cumulativeBucket(data) {
  var mintime = data[0][2];
  var maxtime = data[0][2];
  for (var i = 0; i < data.length; i++) {
    if (data[i][2] > maxtime) {
      maxtime = data[i][2];
    }
    else if (data[i][2] < mintime) {
      mintime = data[i][2]
    }
  }
  // divide into 5 buckets
  var interval = (maxtime - mintime) / 5;
  var buckets = [];
  // initialize buckets
  for (var i = 0; i < 5 ; i++) {
    buckets[i] = new Array();
  } 

  for (var i = 0; i < data.length; i++) {
    bucket = Math.round((data[i][2] - mintime) / interval) - 1;
    bucket = bucket < 0 ? 0 : bucket;

    var obj = new google.maps.LatLng(data[i][0], data[i][1]);
    buckets[bucket].push(obj);
    // push data to all upper buckets
    for (var j = bucket + 1; j < 5; j++) {
      buckets[j].push(obj);
    }
  }
  return buckets;

}

function initialize() {

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
            // console.log(data.value);
            stupid = true;
            // The value as a ratio of the slider (between 0 and 1)
            console.log(parseInt(data.ratio* 10));
            slider = Math.round(data.ratio * 10);

            if(old_slider !== slider)
            {
                slidechange(slider);
            }
            old_slider = Math.round(data.ratio * 10);
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


        $('.my-button').avgrund({
            height: 200,
            holderClass: 'custom',
            showClose: true,
            showCloseText: 'x',
            onBlurContainer: '.container',
            template: '<h4>Select a current event</h4><form id="form"><input id="search" type="search" placeholder="Search..." value=""></form>'
        });


    google.maps.event.addDomListener(window, 'load', initialize);