
function onClickedEstimateQuality() {
    console.log("Estimate price button clicked");
    var va = document.getElementById("va");
    var ca = document.getElementById("ca");
    var rs = document.getElementById("rs");
    var ch = document.getElementById("ch");
    var fsd = document.getElementById("fsd");
    var tsd = document.getElementById("tsd");
    var ph = document.getElementById("ph");
    var su = document.getElementById("su");
    var al = document.getElementById("al");

    var estQuality = document.getElementById("uiEstimatedQuality");
  
    //var url = "http://127.0.0.1:5000/predict_quality"; //Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/api/predict_quality"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        volatile_acidity: parseFloat(va.value),
        citric_acid: parseFloat(ca.value),
        residual_sugar: parseFloat(rs.value),
        chlorides: parseFloat(ch.value),
        free_sulfur_dioxide: parseFloat(fsd.value),
        total_sulfur_dioxide: parseFloat(tsd.value),
        ph: parseFloat(ph.value),
        sulphates: parseFloat(su.value),
        alcohol: parseFloat(al.value),
        

    },function(data, status) {
        console.log(data.estimated_quality);
        estQuality.innerHTML = "<h2>" + data.estimated_quality.toString() + "/10 Rating</h2>";
        console.log(status);
    });
}
