$(document).ready(function(){
    $('.start-btn-family').click(function(){
        
        $('.modal-box').toggleClass("show-modal");
        $('.start-btn').toggleClass("show-modal");
        if($(".modal-box").hasClass("show-modal")){
            $("body").css({"overflow":"hidden"});
            $('.container').animate({"opacity": "0.5"}, "slow");
            $('.navbar').animate({"opacity": "0.5"}, "slow");
        }
    });
    $('.fa-times').click(function(){
        $('.modal-box').toggleClass("show-modal");
        $('.start-btn').toggleClass("show-modal");
        $("body").css({"overflow":"auto"});
        $('.container').animate({"opacity": "1"}, "slow");
        $('.navbar').animate({"opacity": "1"}, "slow");
    });
}); 