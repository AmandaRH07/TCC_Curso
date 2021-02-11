let btnOutro = document.getElementById('outro');
let txtOutroSintoma = document.getElementById('txt-outro-sintoma');

btnOutro.addEventListener('click', function(e) {
    
    e.preventDefault();
    if (txtOutroSintoma.style.display == 'none') {
        txtOutroSintoma.style.display = 'block';
        btnOutro.style.backgroundColor = '#ED553B';
    } else {
        txtOutroSintoma.style.display = 'none';
        btnOutro.style.backgroundColor = '#FCFFF5';
    }

});