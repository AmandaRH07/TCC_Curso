$(document).ready(function(){

        // $('.start-btn').click(function(){
        
            $('.modal-box').toggleClass("show-modal");
            // $('.start-btn').toggleClass("show-modal");
            console.log("teste")
            if($(".modal-box").hasClass("show-modal")){
                $("body").css({"overflow":"hidden"});
                $('main').animate({"opacity": "0.5"}, "slow");
                
            }
        });

    $('.fa-times').click(function(){
        $('.modal-box').toggleClass("show-modal");
        // $('.start-btn').toggleClass("show-modal");
        $("body").css({"overflow":"auto"})
        $('main').animate({"opacity": "1"}, "slow");
        
    });
// });