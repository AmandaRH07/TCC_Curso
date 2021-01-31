let btn = document.getElementsByClassName('button-type');
for (let i = 0; i <= btn.length; i++) {
    btn[i].addEventListener("click", function() {
        let atual = document.getElementsByClassName("active");
        if(atual[0] != undefined){
        atual[0].className = atual[0].className.replace(" active", "");
        }
        this.className += " active";
    });
}

 