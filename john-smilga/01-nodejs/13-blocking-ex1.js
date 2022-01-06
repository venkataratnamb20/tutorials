// Blocking code blocks all users until the process of present user completes.
const http = require('http');

const port = 5500
const server = http.createServer((req, res) => {
    //
    if (req.url === '/') {
        res.write(`
    <h1>Home</h1>
    <h2>${req.url}</h2>
    `)
    res.end()
    }
    else if (req.url === '/about') {
        res.write(`
    <h1>About</h1>
    <h2>${req.url}</h2>
    `)
    // Blocking code
    for(let i = 0; i < 1000; i++) {
        for(let j = 0; j <1000; j++) {
            console.log(`${i} ${j}`)
        }
    }
    res.end()
    } else {
        res.write(`
    <h1>Other</h1>
    <h2>${req.url}</h2>
    <a href="/">back Home </a>
    `)
    res.end()
    }
    
})

server.listen(port, () => {
    console.log('listening on port ' + port);
    console.log(`http://localhost:${port}`);
})