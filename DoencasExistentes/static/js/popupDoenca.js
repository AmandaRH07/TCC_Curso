$(document).ready(function(){
    $('.start-btn').click(function(){ //REMOVER LINHA NA IMPLEMENTAÇÃO EDITAR/EXCLUIR
        
        $('.modal-box').toggleClass("show-modal");
        $('.start-btn').toggleClass("show-modal"); //REMOVER LINHA NA IMPLEMENTAÇÃO EDITAR/EXCLUIR
        if($(".modal-box").hasClass("show-modal")){
            $("body").css({"overflow":"hidden"});
            $('.main').animate({"opacity": "0.5"}, "slow");
            $('.container').animate({"opacity": "0.5"}, "slow");
            $('.navbar').animate({"opacity": "0.5"}, "slow");
        }
    });
    $('.fa-times').click(function(){
        $('.modal-box').toggleClass("show-modal");
        $('.start-btn').toggleClass("show-modal"); //REMOVER LINHA NA IMPLEMENTAÇÃO EDITAR/EXCLUIR
        $("body").css({"overflow":"auto"});
        $('.main').animate({"opacity": "1"}, "slow");
        $('.container').animate({"opacity": "1"}, "slow");
        $('.navbar').animate({"opacity": "1"}, "slow");
    });
    }); //REMOVER LINHA NA IMPLEMENTAÇÃO EDITAR/EXCLUIR