import styled, {css} from 'styled-components'

const HighLight = css`
    background-color: rgb(188, 185, 236);
`;


const DropzoneHighLight =props => {
    console.log(props.highlight)
    return props.highlight ? HighLight: ""
}

export const DropzoneContainer = styled.div`
    height: 200px;
    width: 200px;
    background-color: #fff;
    border: 2px dashed rgb(187, 186, 186);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    font-size: 16px;
    ${DropzoneHighLight}
`;





export const Icon = styled.img`
    opacity: 0.3;
    height: 64px;
    width: 64px;
`

export const FileInput = styled.input`
    display: none;
`

