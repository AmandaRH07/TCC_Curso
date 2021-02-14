$(document).ready(function(){
    if ($('#option-yes').prop("checked")) {
        $('.active').each(function(){$(this).show()})
    } else {
        $('.active').each(function(){$(this).hide()})
    }

    $('#option-yes').click(function(){
        $('.active').each(function(){$(this).show()})
    })

    $('#option-no').click(function(){
        $('.active').each(function(){$(this).hide()})
    })
})