let val = 0;
let arr = [];
function incrementVal(){
    document.getElementById('sean-button').inc = ++val;
    console.log(val);
    fetch('http://127.0.0.1:5000/keke')
        .then((response) => {
            if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
            }
            return response.txt();
        })
        .then((txt) => initialize(txt))
        .catch((err) => console.error(`Fetch problem: ${err.message}`));

}
