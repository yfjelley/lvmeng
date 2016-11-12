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
        //$('.js-vertigo').css('height', $(document).height()*1.1);
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

    $("input[type='checkbox").on('click', function (e) {
        if($("input[type='checkbox']").prop('checked')){    //选中
            $('.btn-register').css('background', '#E60012').removeAttr("disabled");
        }else{
            //$(this).siblings().find('.btn-register').attr('disabled', 'false');
            //$("input[type='checkbox']").attr('checked', false);
           $('.btn-register').attr('disabled', 'true').css('background', '#999999');
        }
    });
    
    $('.niujidui-protocol').on('click', function (e) {
        // 注意: 不定时的话,节点还没有创建就执行了(删除不了)
        window.setTimeout(function () {
            //$('.modal-backdrop').removeClass('in').removeClass();
            $('body .modal-backdrop').remove();
        },0.1);
    })

});

/*
$(function ()
{ $("[data-toggle='popover']").popover();
});*/
