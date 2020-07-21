import React, {useEffect, useState} from 'react'

import DataTable from 'react-data-table-component';

import {TableContainer, RefreshButon} from './table.styles'




const Table = () => {
  
  const [rows, setRows] = useState([])
  const columns = [
    {
      name: 'Id',
      selector: 'id',
      sortable: true,
    },
    {
      name: 'Xref',
      selector: 'Xref',
      sortable: true,
    },
    {
      name: 'Yref',
      selector: 'Yref',
      sortable: true,
    },
    {
      name: 'Date',
      selector: 'Date',
      sortable: true,
    },
    {
      name: 'Value',
      selector: 'Value',
      sortable: true,
    },
  ];

  const refreshTable = () => {
    fetch("http://localhost:8000/pulldata")
    .then(response => response.json())
    .then(resultData => {
      //console.log(resultData)
      
      // const rowData = []
      // resultData.forEach(row => {
      //   rowData.push([row.id, row.Xref, row.Yref, row.Date, row.Value])
      // });
      setRows(resultData)
    })
    
  }
  
  useEffect(() => {
    refreshTable()
    
    }, [])
    console.log(rows)
    return(
      <TableContainer>
      <RefreshButon onClick={refreshTable}>Refresh</RefreshButon>
      <DataTable
      title="Rainfall"
      columns={columns}
      data={rows}
      fixedHeader
      fixedHeaderScrollHeight="300px"
    />
    </TableContainer>
    )
}

export default Table
    
