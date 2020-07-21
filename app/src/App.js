import React, { Component } from 'react'
import './App.css'
import Upload from './components/upload/upload.component'
import Table from './components/table/table.component.jsx'

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="Card">
          <Upload />      
        </div>
          <Table/>

      </div>
    )
  }
}

export default App