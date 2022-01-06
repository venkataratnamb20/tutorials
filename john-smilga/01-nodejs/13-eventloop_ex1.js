// node- npm
// npm --version
// install package locally to use in a specific project
// npm i <package name>
// install package globally to use it in any project
// npm install -g <package name>
// npm init (Initialize the project and create the package.json with step by step, enter to skip)
// npm init -y (Intialize the project and create package.json with default settings)
// npm install (Execute this command to install dependencies listed in package.json)
// install npm dev dependencies
// npm i <package name> --save-dev
// npm i nodemon --save-dev

console.log("First!!")
setTimeout(() => {
    console.log('second')
}, 0)
console.log('Third');

// Following process alive until kill process or CTRL+C
setInterval(() => {
    console.log('Hello setInterval!!!');
}, 2000)
console.log('End log. But I will run first')