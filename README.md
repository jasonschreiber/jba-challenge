# jba-challenge
jba-challenge rainfall data to table

Python was used with a sqlite database to process the precipitation datafile into a structutred database. A GUI has been completed with a more modern take. I made a very basic GUI in React and node.js. A simple interface to uplaod a file to the browser, which is then sent to a nodejs rest api to send the file to the python script that processes the file and populates the sqlite database. The view can then be refreshed on the browser to view the data in a simple table.

The database can also be viewed stright DB Browser for SQLite.exe by opening the pythonsqlite.db in the python/db directory.
The react applciation has only been developed in dev. It can be pulled down to Visual studio. Run yarn add to install all dependencies and then npm run dev to start up the applciation and nodejs server. 

You need to also set the paths for self.database and self.logger in the process.py script.

![GitHub Logo](/images/GUI.PNG)
Format: ![Alt Text](url)
