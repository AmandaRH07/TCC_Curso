let main = document.querySelector(".content");
let center = document.querySelector('.center');
let modal_box = document.querySelector('.modal-box');
let title = document.querySelector('.title')
let navbar = document.querySelector('.navbar')

let botao = document.querySelector('.button_open')

$(document).ready(function(){
    $('.start-btn').click(function(){



        $('.modal-box').toggleClass("show-modal");
        // $('.start-btn').toggleClass("show-modal");

        if ($(".modal-box").hasClass("show-modal")) {

            $("html,body").css({"overflow":"hidden"});
            $('.content').animate({"opacity": "0.5"}, "slow")
            if (main.style.opacity = '0.5') {

                main.style.filter = 'blur(2px)';

            }

            $('.title').animate({"opacity": "0.5"}, "slow")
            if (title.style.opacity = '0.5') {

                title.style.filter = 'blur(2px)';

            }

            $('.navbar').animate({"opacity": "0.5"}, "slow");
            if (navbar.style.opacity = '0.5') {

                navbar.style.filter = 'blur(2px)';

            }

        } 


    });
    $('.fa-times').click(function(){
        $('.modal-box').toggleClass("show-modal");
        $('.start-btn').toggleClass("show-modal");

        

            $("html,body").css({"overflow":"auto"});
            $('.content').animate({"opacity": "1"}, "slow")
            if (main.style.opacity = '1') {

                main.style.filter = 'none';

            }

            $('.title').animate({"opacity": "1"}, "slow")
            if (title.style.opacity = '1') {

                title.style.filter = 'none';

            }

            $('.navbar').animate({"opacity": "1"}, "slow");
            if (navbar.style.opacity = '1') {

                navbar.style.filter = 'none';

            }

       
    });
});