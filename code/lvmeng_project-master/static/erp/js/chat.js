//$(document).ready(function() {
////    function e() {
////
////        var g = $("#textarea").val();
////
////        null != g && "" != g ? ($(".chat01_content").scrollTop($(".mes" + a).height()), $("#textarea").val("")) : alert("\u8bf7\u8f93\u5165\u804a\u5929\u5185\u5bb9!")
////
////        if(g){
////        var talk_user = $("#talk_user").val();
//////        alert(talk_user);
////            $.ajax({
////                type:"post",
////                url:"/erp/save_user_message/",
////                data:{
////                    content:g,
////                    talk_user:talk_user
////                },
////                dataType:"html",
////                success:function(html){
////                    $(".chatLeft").html(html);
////                }
////            });
////        }
////    }
////    var a = 3,
////    b = "img/head/2024.jpg",
//////    c = "img/head/2015.jpg",
////    d = "\u738b\u65ed";
//
//    $(".close_btn").click(function() {
//        $(".chatBox").hide()
//    }),
//
//    $(".chat03_content li").click(function() {
////        var b = $(this).index() + 1;
//        alert($(this).find(".chat03_name").attr("id"))
//////        a = b,
//////        c = "img/head/20" + (12 + a) + ".jpg",
////        d = $(this).find(".chat03_name").text(),
////
////        $(".chat01_content").scrollTop(0),
////        $(this).addClass("choosed").siblings().removeClass("choosed"),
////        $(".talkTo a").text($(this).children(".chat03_name").text()),
////        $(".mes" + b).show().siblings().hide()
//    }),
//
//    $(".chat02_bar img").click(function() {
//        e()
//    }),
//
////    $.fn.setSelection = function(a, b) {
////        if (0 == this.length) return this;
////        if (input = this[0], input.createTextRange) {
////            var c = input.createTextRange();
////            c.collapse(!0),
////            c.moveEnd("character", b),
////            c.moveStart("character", a),
////            c.select()
////        } else input.setSelectionRange && (input.focus(), input.setSelectionRange(a, b));
////        return this
////    },
////    $.fn.focusEnd = function() {
////        this.setCursorPosition(this.val().length)
////    }
//}),
// (jQuery);chatLeft


$(function(){

    $(".close_btn").click(function() {
//        $(".chatBox").hide()
        $(".chatBox").remove();
    });

    $(".chat03_content li").click(function() {
//        alert($(this).find(".chat03_name").attr("id"))
            var talk_user = $(this).find(".chat03_name").attr("id")
            $.ajax({
                type:"get",
                url:"/erp/chat_user_message/",
                data:{
                    talk_user:talk_user
                },
                dataType:"html",
                success:function(html){
                    $(".chat01").html(html);
                    $(".chat01_content").scrollTop($(".mes3").height()*10000)
                }
            });
    });

    $(".chat02_bar img").click(function() {
        var g = $("#textarea").val();

        if(g){
        var talk_user = $("#talk_user").val();
         $("#textarea").val("");
//        alert(talk_user);
            $.ajax({
                type:"post",
                url:"/erp/save_user_message/",
                data:{
                    content:g,
                    talk_user:talk_user
                },
                dataType:"html",
                success:function(html){
                    $(".chat01_content").html(html);
                    $(".chat01_content").scrollTop($(".mes3").height()*10000)
                }
            });
        }else{
            alert("\u8bf7\u8f93\u5165\u804a\u5929\u5185\u5bb9!");
            return false;
        }
    });
});

$(function(){
        update($("#talk_user").val());
        setInterval(function(){
            var talk_user = $("#talk_user").val();
            if(talk_user){
                $.ajax({//检查是否有新消息
                    type:"get",
                    url:"/erp/check_new_message/",
                    data:{
                        talk_user:talk_user,
                    },
                    dataType:"json",
                        success:function(json){
                            if(json.result == "true"){
                                update(talk_user);
                            }
                        },
                });
            }
        },3000)//延迟3秒
});

function update(talk_user){
    $.ajax({
        type:"get",
        url:"/erp/chat_user_message/",
        data:{
            talk_user:talk_user,
            extra:"extra"
        },
        dataType:"html",
            success:function(html){
                $(".chat01").html(html);
                $(".chat01_content").scrollTop($(".mes3").height()*10000);
            },
    });
}

$(document).keypress(function(event){
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){
        var values = $("#textarea").val().trim();
        if(values != ''){
            $("#send_btn").click();
//            alert("\u53d1\u9001\u5185\u5bb9\u4e0d\u80fd\u4e3a\u7a7a\uff01");
//        }else{
//            $("#send_btn").click();
        }

    }
});






