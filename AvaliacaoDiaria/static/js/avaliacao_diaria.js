function mostrar(elemento){
    let display = document.getElementById(elemento).style.display;
      if(display == "none"){
          document.getElementById(elemento).style.display = 'block';
          document.getElementById('outro').style.backgroundColor = '#ED553B'
      }else{
          document.getElementById(elemento).style.display = 'none';
          document.getElementById('outro').style.backgroundColor = '#FCFFF5'
      }    
  }

