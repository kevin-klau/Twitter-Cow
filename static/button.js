let val = 0;
let arr = [];
function incrementVal(){
    document.getElementById('sean-button').inc = ++val;
    console.log(val);
    fetch('http://127.0.0.1:5000/keke')
    function readFile(ScrapedInfo) {
        const reader = new FileReader();
        reader.addEventListener('load', (event) => {
          const result = event.target.result;
          // Do something with result
        });
      
        reader.addEventListener('progress', (event) => {
          if (event.loaded && event.total) {
            const percent = (event.loaded / event.total) * 100;
            console.log(`Progress: ${Math.round(percent)}`);
          }
        });
        reader.readAsDataURL(file);
      }


}
