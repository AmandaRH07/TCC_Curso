$(document).ready(function(){
    $('.start-btn-family').click(function(){ //REMOVER LINHA NA IMPLEMENTAÇÃO EDITAR/EXCLUIR
        
        $('.modal-box-family').toggleClass("show-modal-family");
        $('.start-btn-family').toggleClass("show-modal-family"); //REMOVER LINHA NA IMPLEMENTAÇÃO EDITAR/EXCLUIR
        if($(".modal-box-family").hasClass("show-modal-family")){
            $("body").css({"overflow":"hidden"});
            $('.container').animate({"opacity": "0.5"}, "slow");
            $('.navbar').animate({"opacity": "0.5"}, "slow");
        }
    });
    $('.fa-times-family').click(function(){
        $('.modal-box-family').toggleClass("show-modal-family");
        $('.start-btn-family').toggleClass("show-modal-family"); //REMOVER LINHA NA IMPLEMENTAÇÃO EDITAR/EXCLUIR
        $("body").css({"overflow":"auto"});
        $('.container').animate({"opacity": "1"}, "slow");
        $('.navbar').animate({"opacity": "1"}, "slow");
    });
    }); //REMOVER LINHA NA IMPLEMENTAÇÃO EDITAR/EXCLUIR