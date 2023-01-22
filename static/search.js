

function searching(){
    let searchQuery = document.getElementById("searchinput").value;
    console.log(searchQuery);
    document.getElementById("searchinput").value='';
    const request = new XMLHttpRequest()
    request.open('POST',`keke/${JSON.stringify(searchQuery)}`)
    request.send()
    fetch('http://127.0.0.1:5000/?#/keke/sample.json')
    
}