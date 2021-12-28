//read and display http files

const http = require('http');
const fs = require('fs');

fs.readFile('./html/index.html', (err, indexHtml) => {
    if (err) {
        console.log(err);
        return
    }
    fs.readFile('./html/about.html', (err,aboutHtml) => {
        if (err) {
            console.log(err);
            return
        }
        fs.readFile('./html/contact.html', (err, contactHtml) => {
            if (err) {
                console.log(err);
                return
            }

            http.createServer((req, res) => {
                if (req.url === '/') {
                    res.write(indexHtml);
                    res.end();
                }
                else if (req.url === '/about') {
                    res.write(aboutHtml);
                    res.end();
                }
                else if (req.url === '/contact') {
                    res.write(contactHtml);
                    res.end();
                }
                else {
                    res.end(`
                    <h1>Oops!</h1>
                    <p>We can't seem to find the page you are looking for</p>
                    <a href="/">back home</a>
                    `)
                }
            }).listen(8300)
        })
    })

})