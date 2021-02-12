
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
    today = new Date()
    console.log(data)

    d = parseInt(today.getDate())
    m = parseInt(today.getMonth() + 1)
    y = parseInt(today.getFullYear())

   data = data.split('-')

   ano_nasc = parseInt(data[0])
   mes_nasc = parseInt(data[1])
   dia_nasc = parseInt(data[2])

   if (ano_nasc <= y){
       if (mes_nasc <= m){
           if( dia_nasc <= d){
               verifica = true
           }
           else {
               verifica = false
           }
       }
       else {
           verifica = false
       }
   }
   else {
    verifica = false
   }

   return verifica
}

