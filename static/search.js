function searching(){
    let searchQuery = document.getElementById("searchinput").value;
    console.log(searchQuery);
    document.getElementById("searchinput").value='';
    const request = new XMLHttpRequest()
    request.open('POST',`keke/${JSON.stringify(searchQuery)}`)
    request.send()
    fetch('http://127.0.0.1:5000/?#/keke')
}

function test(){
    document.getElementById("rank1").innerHTML = "London";
    document.getElementById("rank2").innerHTML = "Toronto";
    document.getElementById("rank3").innerHTML = "Quebec City";
    document.getElementById("rank4").innerHTML = "Stockholm";
    document.getElementById("rank5").innerHTML = "Calgary";
    document.getElementById("rank6").innerHTML = "Helsinki";
    document.getElementById("moorank1").innerHTML = "MooMeter Score: 89.5";
    document.getElementById("moorank2").innerHTML = "MooMeter Score: 102.9";
    document.getElementById("moorank3").innerHTML = "MooMeter Score: 111.4";
    document.getElementById("moorank4").innerHTML = "MooMeter Score: 103.2";
    document.getElementById("moorank5").innerHTML = "MooMeter Score: 102.8";
    document.getElementById("moorank6").innerHTML = "MooMeter Score: 90.7";
}