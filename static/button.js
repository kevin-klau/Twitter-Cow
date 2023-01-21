function incrementVal(){
    let value = parseInt(document.getElementById('sean-button').value, 10)
    value = isNaN(value) ? 0 : value;
    value += 1;
    console.log(value);
}
