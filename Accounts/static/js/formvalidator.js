
function FormValidator(form) {

    const spanPassword = document.querySelector('#senha_validator')
    let validator 

    // validando se a senha eh forte
    // validator = senhaValida(form.senha.value)
    // console.log(validator)
    // if (!validator){
    //     return false
    // }

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

    return false
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

// function senhaValida(p) {
//     const spanPasswordUpper   = document.querySelector('#senha_validator_maiusculo')
//     const spanPasswordLower   = document.querySelector('#senha_validator_minusculo')
//     const spanPasswordNumber  = document.querySelector('#senha_validator_numero')
//     const spanPasswordSpecial = document.querySelector('#senha_validator_caractere_especial')
//     const spanPasswordLenght  = document.querySelector('#senha_validator_length')

//     var retorno = false;
//     var letrasMaiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
//     var letrasMinusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
//     var numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
//     var caracteresEspeciais = ["!","@","#","$","%","^","&","*","(",")","-","_","|"];

//     if (p.length < 8) {
//         spanPasswordLenght.style.display = 'block'
//         return retorno
//     }

//     var auxMaiuscula = 0;
//     var auxMinuscula = 0;
//     var auxNumero = 0;
//     var auxEspecial = 0;

//     for (var i = 0; i < p.length; i++) {
//         if (p[i] in letrasMaiusculas)
//             auxMaiuscula++;
//         else if (p[i] in letrasMinusculas)
//             auxMinuscula++;
//         else if (p[i] in numeros)
//             auxNumero++;
//         else if (p[i] in caracteresEspeciais)
//             auxEspecial++;
//     }

//     if (auxMaiuscula > 0) {
//         console.log("Cheguei maiusculo")
//         if (auxMinuscula > 0) {
//             console.log("Cheguei minusculo")
//             if (auxNumero > 0) {
//                 console.log("Cheguei numero")
//                 if (auxEspecial > 0) {
//                     console.log("Cheguei caractere especial")
//                     retorno = true;
//                 }
//                 else {
//                     console.log("Entrei else caractere especial")
//                     spanPasswordSpecial.style.display = 'block'
//                     retorno = false
//                     return retorno
//                 }
//             }
//             else {
//                 console.log("Entrei else numero")
//                 spanPasswordNumber.style.display = 'block'
//                 retorno = false
//                 return retorno
//             }
//         }
//         else {
//             console.log("Entrei else minusculo")
//             spanPasswordLower.style.display = 'block'
//             retorno = false
//             return retorno
//         }
//     }
//     else {
//         console.log("Entrei else maiusculo")
//         spanPasswordUpper.style.display = 'block'
//         retorno = false
//         return retorno
//     }

//     return retorno
// }