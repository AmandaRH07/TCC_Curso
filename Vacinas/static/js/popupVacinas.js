$(document).ready(function(){
    
        
    $('.modal-box').toggleClass("show-modal");

        if($(".modal-box").hasClass("show-modal")){
            $("html,body").css({"overflow":"hidden"});
            $('.center-vaccines').animate({"opacity": "0.5"}, "slow")
            $('.roof').animate({"opacity": "0.5"}, "slow")
            $('.navbar').animate({"opacity": "0.5"}, "slow")
        }
    });
    $('.fa-times').click(function(){
        $('.modal-box').toggleClass("show-modal");
       
        $("html,body").css({"overflow":"auto"});
        $('.center-vaccines').animate({"opacity": "1"}, "slow")
        $('.roof').animate({"opacity": "1"}, "slow")
        $('.navbar').animate({"opacity": "1"}, "slow")
    });