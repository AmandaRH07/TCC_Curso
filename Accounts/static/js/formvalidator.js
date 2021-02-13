
function FormValidator(form) {

    const spanPassword = document.querySelector('#senha_validator')
    let validator 

    // validando senha
    if (form.senha.value != form.senha2.value) {
        spanPassword.style.display = 'block'
        return false
    }
    else {
        spanPassword.style.display = 'none'
        validator = true
    }

    // validando data de nascimento
    validator = ValidaData(form.nascimento.value)
    if (!validator){
        const spanData = document.querySelector('#nascimento_validator')
        spanData.style.display = 'block'
        return false
    }
    else {
        spanData.style.display = 'none'
    }

    return validator
}

function ValidaData(data) {
    let verifica = true

    let today = new Date()
    let form = new Date(data)

    if (form <= today){
        verifica = true
    }
    else{
        verifica = false
    }

    return verifica
}

