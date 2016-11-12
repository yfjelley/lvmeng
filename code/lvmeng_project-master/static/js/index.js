/**
 * Created by renjing on 16/8/3.
 */

var windowWidth, windowHeight;
function bgMouse() {
    $("body").mousemove(function(e) {
        var mouseX = e.pageX;
        var mouseY = e.pageY;
        var centralMouseX = (mouseX - (windowWidth / 2)) * -0.1;
        var centralMouseY = (mouseY - (windowHeight / 2)) * -0.09;
        TweenMax.to(".vertigo-bg", 0.75, {
            x: centralMouseX,
            y: centralMouseY
        });
    });
}

/*
function showIosC() {
    $('.ios_cover').css('display', 'block');
    $('.ios').css('display', 'none');
}

function hideIosC() {
    $('.ios_cover').css('display', 'none');
    $('.ios').css('display', 'block');
}
*/


$(document).ready(function () {
    windowWidth = $(window).innerWidth();
    windowHeight = $(window).height();

    if ($('.js-vertigo').length) {
        bgMouse();
    }

    $('.grid-item').popover({
        html : true,
        content: function() {
            return $("#popover-content").html();
        }
    });

    $('.grid-item3').popover({
        html : true,
        content: function() {
            return $("#popover-content3").html();
        }
    });

    $('.btn-phone').popover({
        html : true,
        content: function() {
            return $(".popover-content").html();
        }
    });
    
    $('.btn-toggole').click(function (event) {
        //$(this).addClass('.btn-checked').siblings().removeClass('.btn-checked');
        $(this).css('color', '#E60012').siblings().css('color', '#333333');

    })
});

/*
$(function ()
{ $("[data-toggle='popover']").popover();
});*/
