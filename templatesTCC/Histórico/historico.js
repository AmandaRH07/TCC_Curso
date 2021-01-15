var $input    = document.getElementById('selecao-arquivo-receita');
    
    $fileName = document.getElementById('file-name');
    

$input.addEventListener('change', function(){
  $fileName.textContent = this.value;
})

  var $input2    = document.getElementById('selecao-arquivo-atestado');
    
  $fileName2 = document.getElementById('file-name2');
  

$input2.addEventListener('change', function(){
$fileName2.textContent = this.value;
}
);

