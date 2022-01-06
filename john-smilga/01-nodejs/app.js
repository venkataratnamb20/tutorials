const {readFile} = require('fs');

getText = (path) => {
    return new Promise((resolve, reject) => {
        readFile(path, 'utf8', (err, data) => {
            if (err) {
                reject(err);
                return
            } else {
                resolve(data);
            }
        })
    })
}

getText('./content/subfolder/test.txt')
.then((data) => {console.log(data)})
.catch((err) => {console.log(err)})