let val = 0;
function incrementVal(){
    document.getElementById('sean-button').inc = ++val;
    console.log(val);
    fetch('http://127.0.0.1:5000/keke')
        
}
