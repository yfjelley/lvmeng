$(function(){
        $('#pro_img').hover(function(){
            $('#pro_table').css('display','block');
        },
        function(){
            $('#pro_table').css('display','none');
        }
        );
    });

$(function(){
    $("#sell").click(function(){
        var va = $("#num").val();
        if(va==""){
            $("#false_title").css("display","block");
            $("#num").css("border-color","red");
        }else{
            $("#false_title").css("display","none");
            $("#num").css("border-color","#D3D5CE");
            alert("sell!!!!!!!!");
        }
    });
});

$(function(){
    $("#sell").hover(function(){
        $("#sell span").css("background","#D92D28");
        $("#sell img").css("display","none");
        $("#sell span").css("text-align","center");
        $("#sell").css("border-color","#D92D28");
    },function(){
        $("#sell span").css("background","#D3D5CE");
        $("#sell img").css("display","");
        $("#sell span").css("text-align","");
        $("#sell").css("border-color","#D3D5CE");
    });
});

$(function(){
    $("#buy").click(function(){
        var va = $("#num").val();
        if(va==""){
            $("#false_title").css("display","block");
            $("#num").css("border-color","red");
        }else{
            $("#false_title").css("display","none");
            $("#num").css("border-color","#D3D5CE");
            alert("buy!!!!!!!!!");
        }
    });
});

$(function(){
    $("#buy").hover(function(){
        $("#buy span").css("background","#0096D6");
        $("#buy span img").css("display","none");
        $("#buy span").css("text-align","center");
        $("#buy").css("border-color","#0096D6");
    },function(){
        $("#buy span").css("background","#D3D5CE");
        $("#buy img").css("display","");
        $("#buy span").css("text-align","");
        $("#buy").css("border-color","#D3D5CE");
    });
});

function showPic(id){
    $("#market_name").html(id);
    $("#select_area").css('display','block');
}

function closePic(){
    $("#select_area").css('display','none');
}

function close_trading(){
    $("#trading").css('display','none');
}

function trading_show(){
    closePic();
    var html = $("#market_name").html();
    $("#marketName").html(html);
    $("#trading").css('display','block');
}

function text_dis(){
    document.getElementById("fill").disabled=false;
}

function now_price(){
    document.getElementById("fill").disabled=true;
}

function market_price(){
    document.getElementById("fill").disabled=true;
}

function show_detail(id){
    if (id=='command'){
        $("#trade_pic").attr('class','active');
        $("#command").attr('class','empty');
        $("#trade_div").css("display","none");
        $("#storage_order").css("display","");
        getTime();
    }else{
        $("#command").attr('class','active');
        $("#trade_pic").attr('class','empty');
        $("#storage_order").css("display","none");
        $("#trade_div").css("display","");
    };
}

function change_style(num){
    if(num<=0||isNaN(num)){
        $("#num").val("");
        $("#sell span").css("background","#D3D5CE");
        $("#sell img").css("display","");
        $("#buy span").css("background","#D3D5CE");
        $("#buy img").css("display","");
        $("#sell span").css("text-align","");
        $("#buy span").css("text-align","");
        $("#sell").css("border-color","#D3D5CE");
        $("#buy").css("border-color","#D3D5CE");
        $("#cash_deposit").html("---");
    }else{
        $("#sell span").css("background","#D92D28");
        $("#sell img").css("display","none");
        $("#sell span").css("text-align","center");
        $("#buy span").css("background","#0096D6");
        $("#buy span img").css("display","none");
        $("#buy span").css("text-align","center");
        $("#sell").css("border-color","#D92D28");
        $("#buy").css("border-color","#0096D6");
        $("#cash_deposit").html("USD&nbsp;"+num*315);
    }
}

function show_span(id){
    if(id == 'tr_right'){
        $("#"+id).css("display","none");
        $("#tr_down").css("display","block");
        $("#advanced_options").css("display","block");
        $("#dott").css("top","378px");
        $("#usd").css("top","378px");
    }
    if(id == 'tr_down'){
        $("#"+id).css("display","none");
        $("#tr_right").css("display","block")
        $("#advanced_options").css("display","none");
        $("#dott").css("top","260px");
        $("#usd").css("top","260px");

    }

    if(id == 'span_down'){
        $("#pos_down").css("display","none");
        $("#span_right").css("display","block");
        $("#position2").css("display","none");
        $("#position1").css("display","none");
    }

    if(id == 'span_right'){
        if($("#advanced_options").css("display")=="block"){
            $("#dott").css("top","380px");
            $("#usd").css("top","380px");
        }else{
            $("#dott").css("top","260px");
            $("#usd").css("top","260px");
        }
        $("#span_right").css("display","none");
        $("#pos_down").css("display","block");
        $("#position2").css("display","");
        $("#position1").css("display","none");
    }
}

function showSpread(id){
    var num = $("#stopPrice").val();
    if(id==true){
        $("#price_spread").css("display","");
        if(!num){
            document.getElementById("compel").checked=true;
        }
        $("#warehouse2").html("0.25%");
    }else{
        $("#price_spread").css("display","none");
        if(num){
            document.getElementById("compel").checked=true;
        }else{
            document.getElementById("compel").checked=false;
        }
        $("#warehouse2").html("2");
    }
}

function stop_price(num){
    if(num<2||isNaN(num)){
        $("#stopPrice").val("");
        $("#warehouse3").css("display","none");
        $("#warehouse1").css("display","");
    }else{
        $("#warehouse1").css("display","none");
        $("#warehouse3").css("display","");
        document.getElementById("compel").checked=true;
        $("#warehouse6").html("$"+num*10);
        $("#warehouse4").html(0.70442);
        $("#warehouse5").html(0.70225);
    }
}

function limit_price(num){
    if(num<=0||isNaN(num)){
        $("#stopPrice").val("");
    }else{
        $("#warehouse_1").css("display","");
        $("#warehouse_6").html("$"+num*10);
        $("#warehouse_4").html(0.70442);
        $("#warehouse_5").html(0.70225);
    }
}

function dotted_check(){
   $("#position2").css("display","none");
   $("#position1").css("display","");
}

function usd_check(){
   $("#position1").css("display","none");
   $("#position2").css("display","");
}

function stop_price2(num){
    if(num<20||isNaN(num)){
        $("#stopPrice2").val("");
        $("#warehouse32").css("display","none");
        $("#warehouse12").css("display","");
        document.getElementById("compel").checked=false;
    }else{
        $("#warehouse12").css("display","none");
        $("#warehouse32").css("display","");
        document.getElementById("compel").checked=true;
        $("#warehouse62").html(num/10);
        $("#warehouse42").html(0.70442);
        $("#warehouse52").html(0.70225);
    }
}

function showSpread2(id){
    var num = $("#stopPrice2").val();
    if(id==true){
        $("#price_spread2").css("display","");
        if(!num){
            document.getElementById("compel").checked=true;

        }else{
            $("#promise").css("display","none");
            $("#dot_check").css("display","");
            var numb = $("#warehouse62").html();
            $("#dot_num").html(numb);
            $("#warehouse22").html("$176");
        }
    }
    else{
        $("#price_spread2").css("display","none");
        $("#promise").css("display","");
        $("#dot_check").css("display","none");
        if(num){
            document.getElementById("compel").checked=true;
        }else{
            document.getElementById("compel").checked=false;
        }
        $("#warehouse22").html("$20");
    }

}

function limit_price2(num){
    if(num%10==0){
        $("#shortest").css("display","none");
        $("#warehouse_12").css("display","");
        $("#warehouse_62").html(num/10);
        $("#warehouse_42").html(0.70442);
        $("#warehouse_52").html(0.70225);
    }else{
        $("#limit_price").val("");
        $("#shortest").css("display","");
        $("#warehouse_12").css("display","none");
    }
}

function color_contr(va){
    if(va==1){
        $("#select_opt").css("color","#0096D7");
    }else{
        $("#select_opt").css("color","#D92D27");
    }
}

function due_time(id){
    if(id=="due_down"){
        $("#"+id).css("display","none");
        $("#due_right").css("display","block");
        $("#due_div").css("display","none");
    }else{
        $("#"+id).css("display","none");
        $("#due_down").css("display","block");
        $("#due_div").css("display","block");
    }
}

function getTime(){
    var today = new Date();
    var date = today.getDate();
    var month = today.getMonth()+1;
    var year = today.getFullYear();
    var current = date+"/"+month+"/"+year;

    var h = today.getHours();
    var s = today.getSeconds();
    var m = today.getMinutes();
    if(m<10){
        m = "0"+m
    }
    if(h<10){
        h = "0"+h
    }
    if(s<10){
        s = "0"+s
    }
    $("#current_date").html(current);
    $("#current_time").html(h+":"+m+":"+s);
}

function setDis(id){
    if(id=="close_dis"){
        document.getElementById("fullDate").disabled=true;
        document.getElementById("hour").disabled=true;
        document.getElementById("minute").disabled=true;
        $("#fullDate").val("");
        $("#hour").val("");
        $("#minute").val("");
    }else{
        document.getElementById("fullDate").disabled=false;
        document.getElementById("hour").disabled=false;
        document.getElementById("minute").disabled=false;
    }
}

function storage_span(id){
    if(id=="arrow_text"){
        $("#arrow_down").css("display","none");
        $("#arrow_right").css("display","");
        $("#stor_div").css("display","none");
    }else{
        $("#"+id).css("display","none");
        $("#arrow_down").css("display","");
        $("#stor_div").css("display","");
    }
}

function sto_click(cli){
    var text = $("#sto_text").val();
    if(cli){
        $("#extra").css("display","");
        if(!text){
            $("#sto_price").html(176);
        }else{
            $("#extra1").css("display","none");
            $("#extra2").css("display","");
            var count = $("#sto_num").html();
            $("#extra_count").html(count);
        }
    }else{
        $("#extra").css("display","none");
        if(!text){
            $("#sto_price").html(20);
            $("#extra1").css("display","");
            $("#extra2").css("display","none");
            $("#extra_count").html("");
        }else{
            $("#extra1").css("display","");
            $("#extra2").css("display","none");
            $("#extra_count").html("");
        }
    }
}

function conf_func(num){
    if(num%10==0&&num>0){
        $("#conf_div").css("display","");
        $("#conf_text").css("display","none");
        $("#count_dotted").html(num/10);
    }else{
        $("#conf_input").val("");
        $("#conf_div").css("display","none");
        $("#conf_text").css("display","");
        $("#count_dotted").html("");
    }
}

function sto_func(num){
    if(num>=20&&!isNaN(num)){
        $("#sto_div").css("display","none");
        $("#sto_div2").css("display","");
        $("#sto_num").html(num/10);
        $("#num_first").html(0.12345);
        $("#num_seconds").html(0.45678);
    }else{
        $("#sto_text").val("");
        $("#sto_div2").css("display","none");
        $("#sto_div").css("display","");
    }
}

function per_price(num){
    $("#per_price").html(num);
}

function stod_click(id){
    if(id=="sto_usd"){
        $("#stor_div1").css("display","none");
        $("#stor_div").css("display","");
    }else{
        $("#stor_div").css("display","none");
        $("#stor_div1").css("display","");
    }

}

function storage_radio(id){
    if(id=="sto_radio"){
        $("#stor_div").css("display","");
        $("#stor_div2").css("display","none");
    }else{
        $("#stor_div").css("display","none");
        $("#stor_div2").css("display","block");
    }

}

function last_input(va){
    if(va==""){
        $("#last_market").css("display","none;");
        $("#la_span").css("display","");
        $("#last_price").css("display","");
        $("#last_market").css("display","none");
        $("#lastest").html(2);
        $("#hund").css("display","none");
    }else{
        $("#last_market").css("display","");
        $("#last_price").css("display","none");
        $("#la_span").css("display","none");
        $("#lastest").html(va*10);
        $("#hund").css("display","none");
    }

}

function last_checkbox(check){
    var v = $("#last_text").val();
    if(check){
        $("#last_extra").css("display","");
        if(v==""){
            $("#lastest").html(0.25);
            $("#hund").css("display","");
            $("#last_text").attr("min",17.3);
        }else{
            $("#last_text").attr("min",17.3);
        }
    }else{
        $("#last_text").attr("min",2);
        $("#last_extra").css("display","none");
        if(v==""){
            $("#last_extra").css("display","none");
            $("#lastest").html(2);
            $("#hund").css("display","none");
        }
    }
}

function la_change(va){
    if(va==""){
        $("#la_div").css("display","none");
        $("#la_price").html("");
    }else{
        $("#la_div").css("display","");
        $("#la_price").html(va*10);
    }
}