//EVENT LOOP
// when the web page is reloaded, only request will print on console 
// and other messsages will not print
const http = require('http');

server = http.createServer((req, res) => {
    console.log('Request event')
    res.write(`
    <h1> Hello World! </h1>
    <p>Sample server for test EVENT LOOP </p>
    `)
    res.end();
})

server.listen(8010, () => {
    console.log('Server listening on port: 8010')
})