import styled from 'styled-components'

export const TableContainer = styled.div`
  background-color: white;
  padding: 32px;
  width: 55%;
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
  box-shadow: 0 15px 30px 0 rgba(0, 0, 0, 0.11), 0 5px 15px 0 rgba(0, 0, 0, 0.08);
  box-sizing: border-box;
`

export const RefreshButon = styled.button`
    position: relative;
    font-family: 'Roboto medium', sans-serif;
    font-size: 14px;
    height: 36px;
    min-width: 88px;
    padding: 6px 16px;
    line-height: 1.42857143;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    -ms-touch-action: manipulation;
    touch-action: manipulation;
    cursor: pointer;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    border: 0;
    border-radius: 2px;
    background: rgba(103, 58, 183, 1);
    color: #fff;
    outline: 0;
`