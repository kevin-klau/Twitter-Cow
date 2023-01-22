function readfileio(){
    const fs = require("fs");

    fs.readFile("../Scrape/ScrapedInfo.txt", (err, data) => {
    if (err) throw err;

    console.log(data.toString());
    });
}