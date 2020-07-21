const IncomingForm = require('formidable').IncomingForm

module.exports = function upload(req, res) {
  var form = new IncomingForm()

  form.on('file', (field, file) => {
    // Do something with the file
    // e.g. save it to the database
    // you can access it using file.path
    //Use temp file path to pass onl python script to populate database
    var spawn = require("child_process").spawn;
    var process = spawn('python',["./python/process.py", file.path] ); 


  })
  form.on('end', () => {
    res.json()
  })
  form.parse(req)
}