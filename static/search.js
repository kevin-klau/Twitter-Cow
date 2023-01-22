let searchQuery = document.getElementById("searchinput").value;

function searching(){
    let searchQuery = document.getElementById("searchinput").value;
    console.log(searchQuery);
    document.getElementById("searchinput").value='';
    const vvv = [{searchQuery:searchQuery}];
    xhr.open("POST", "http://127.0.0.1:5000/keke", true)
    send(vvv)

    fetch()
 }