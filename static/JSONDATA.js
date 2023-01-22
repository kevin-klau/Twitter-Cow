const button = document.getElementById("theButton")
const data = document.getElementById("info")

const cars = [
 { "make":"Porsche", "model":"911S" },
 { "make":"Mercedes-Benz", "model":"220SE" },
 { "make":"Jaguar","model": "Mark VII" }
];

button.onclick= function(){

fetch("http://127.0.0.1:5000/receiver", 
    {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'Accept': 'application/json'
    },
    body:JSON.stringify(cars)}).then(res=>{
        if(res.ok){
            return res.json()
        }else{
            alert("something is wrong")
        }
    }).then(jsonResponse=>{
        jsonResponse.map(Main=> 
Main.make==="Porsche"? data.innerHTML +="<p>"+ Main.make+" "+" is a good product":
data.innerHTML +="<p>"+ Main.make+" "+"is an average product" ) 
}).catch((err) => console.error(err));} 