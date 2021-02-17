function gerarPDF(){
    botoes = document.querySelectorAll('.btn')
    botoes[0].style.display = 'none'
    botoes[1].style.display = 'none'

    print()
    
    botoes[0].style.display = 'block'
    botoes[1].style.display = 'block'
}
