$(document).ready(function(){

        $('.start-btn').click(function(){
        
            $('.modal-box').toggleClass("show-modal");
            $('.start-btn').toggleClass("show-modal");
            if($(".modal-box").hasClass("show-modal")){
                $("body").css({"overflow":"hidden"});
                
            }
        });

    $('.fa-times').click(function(){
        $('.modal-box').toggleClass("show-modal");
        $('.start-btn').toggleClass("show-modal");
        $("body").css({"overflow":"auto"});
        
    });
});