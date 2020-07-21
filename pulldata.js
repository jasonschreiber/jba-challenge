
let sqlite3 = require('sqlite3').verbose();

 


module.exports = function pulldata(req, res) {
  // open the database
  let db = new sqlite3.Database('./python/db/pythonsqlite.db');
  let sql = `SELECT * FROM precipitation LIMIT 1000;`;

  let data = [];

  db.all(sql, [], (err, rows) => {
    if (err) {
      throw err;
    }
    rows.forEach((row) => {   
      data.push(row);      
    });
    
    res.json(data);
  });
  db.close()
  
}
