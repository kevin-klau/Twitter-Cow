
function searching(){
    let searchQuery = document.getElementById("searchinput").value;
    console.log(searchQuery);
    document.getElementById("searchinput").value='';
    const request = new XMLHttpRequest()
    request.open('POST',`keke/${JSON.stringify(searchQuery)}`)
    request.send(searchQuery)
 }