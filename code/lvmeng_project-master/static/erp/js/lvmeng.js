$(document).ready(function () {
    /*$('.li-item').on('click', function (e) {
        console.log(this)
        //$(this).toggleClass('li-active', !$(this).hasClass('li-active'));
        $(this).parent().siblings().children('a').removeClass('li-active')

        $(this).toggleClass('li-active', !$(this).hasClass('li-active'));
    })

    $('.sidebar-subnav li a').on('click', function (e) {
        console.log(this)
        $(this).addClass('hover').siblings().removeClass('hover');
    })*/
    //var searches = location.pathname.split('/');
    //console.log(searches[searches.length - 2]);
    //console.log(location.href);
    if(location.hash !== ''){
        //console.log(location.hash.substring(location.hash.indexOf("#") + 1))
        $("." + location.hash.substr(location.hash.indexOf("#") + 1)).addClass('active')
    }


    //var imgSrc = $('#menu li.active img').attr('src');

    //var isrc = imgSrc.substring(0,".") + "_select.png";
    /*$('#menu li').on('click', function (event) {
        console.log(this);
        if($this.hasClass('active')){
            $(this).children('a').find('img').attr()
        }

    })*/
    //console.log($('#menu li.active img'));//.replace('.png', '_select.png'));
    //$('#menu li a[aria-expanded="true"] img').attr('src', imgSrc.replace('.png', '_select.png'));
});


var time=0;
$(function(){
    var unread = $("#redister_business").html();
    if(unread){
        setInterval(function(){
            time++;
            if(time%2==1){
                $("#lv_unread").css("display","none")
            }if(time%2==0){
                $("#lv_unread").css("display","")
                        }
                    }
            ,1000);
    }
});


