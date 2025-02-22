function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i in uiBathrooms) {
      if (uiBathrooms[i].checked) {
        return parseInt(i) + 1;
      }
    }
    return -1; // Invalid Value
  }
  
  function getBHKValue() {
      var uiBHK = document.getElementsByName("uiBHK");
      for (var i in uiBHK) {
          if (uiBHK[i].checked) {
          return parseInt(i) + 1;
          }
      }
      return -1; // Invalid Value
      }
  
  function onClickedEstimatePrice() {
      console.log("Estimate price button clicked");
      var sqft = document.getElementById("uiSqft");
      var bhk = getBHKValue();
      var bathrooms = getBathValue();
      var location = document.getElementById("uiLocations");
      var estPrice = document.getElementById("uiEstimatedPrice");
      
      var url = "http://localhost:5000/predict_home_price";   
  
      $.post(url, {
          total_sqft: parseFloat(sqft.value),
          bhk: bhk,
          bath: bathrooms,
          location: location.value
      }, function (data, status) {
          console.log(data.estimated_price);
          estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
          console.log(status);
      });
  }
  
  // function onPageLoad() {
  //   console.log("document loaded");
  //   var url = "http://localhost:5000/get_location_names";                     
  //   $.get(url, function (data, status) {
  //     console.log("got response for get_location_names request");
  //     if (data) {
  //       var locations = data.locations;
  //       var uiLocations = document.getElementById("uiLocations");
  //       $("#uiLocations").empty();
  //       for (var i in locations) {
  //         var opt = new Option(locations[i]);
  //         $("#uiLocations").append(opt);
  //       }
  //     }
  //   });
  // }
  function onPageLoad() {
    console.log("document loaded");
    var url = "http://localhost:5000/get_location_names"; // Replace with your actual endpoint
    
    $.get(url, function (data, status) {
      console.log("Got response for get_location_names request");
      
      if (data && data.locations) {
        var locations = data.locations;
        var uiLocations = document.getElementById("uiLocations");
        $("#uiLocations").empty(); // Clear the existing options
        
        // Add the default "Choose a Location" option
        var defaultOption = document.createElement("option");
        defaultOption.value = "";
        defaultOption.disabled = true;
        defaultOption.selected = true;
        defaultOption.textContent = "Choose a Location";
        uiLocations.appendChild(defaultOption);
        
        // Add the dynamic locations from the JSON response
        for (var i = 0; i < locations.length; i++) {
          var opt = new Option(locations[i], locations[i]);
          uiLocations.appendChild(opt);
        }
      }
    });
  }
  
  window.onload = onPageLoad;
  
  
  