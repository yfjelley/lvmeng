function intToChinese(n) {
    if (!/^(0|[1-9]\d*)(\.\d+)?$/.test(n) || n.length>12 || n<0.01)
        if (n==0)
            return "零";
        else
            return '无效';
    //var unit = "千百拾亿千百拾万千百拾元角分", str = "";
    var unit = "千百十亿千百十万千百十元角分", str = "";
    n += "00";
    var p = n.indexOf('.');
    if (p >= 0)
        n = n.substring(0, p) + n.substr(p+1, 2);
    unit = unit.substr(unit.length - n.length);
    for (var i=0; i < n.length; i++)
        //str += '零壹贰叁肆伍陆柒捌玖'.charAt(n.charAt(i)) + unit.charAt(i);
        str += '零一二三四五六七八九'.charAt(n.charAt(i)) + unit.charAt(i);
    //return str.replace(/零(千|百|拾|角)/g, "零").replace(/(零)+/g, "零").replace(/零(万|亿|元)/g, "$1").replace(/(亿)万|壹(拾)/g, "$1$2").replace(/^元零?|零分/g, "").replace(/元$/g, "元整");
    return str.replace(/零(千|百|十|角)/g, "零").replace(/(零)+/g, "零").replace(/零(万|亿|元)/g, "$1").replace(/(亿)万|一(十)/g, "$1$2").replace(/^元零?|零分/g, "").replace(/元$/g, "元整");
}

//    function intToChinese_decimal(str) {
//            str = str + '';
//            var len = str.length - 1;
//            var idxs = ['', '十', '百', '千', '万', '十', '百', '千', '亿', '十', '百', '千', '万', '十', '百', '千', '亿'];
//            var num = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九'];
//            var num_complex = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖'];
//            str = parseFloat(str)
//            character = str.replace(/([1-9]|0+)/g, function ($, $1, idx, full) {
//                var pos = 0;
//                if ($1[0] != '0') {
//                    pos = len - idx;
//                    if (idx == 0 && $1[0] == 1 && idxs[len - idx] == '十') {
//                        return idxs[len - idx];
//                    }
//                    return num[$1[0]] + idxs[len - idx];
//                } else {
//                    var left = len - idx;
//                    var right = len - idx + $1.length;
//                    if (Math.floor(right / 4) - Math.floor(left / 4) > 0) {
//                        pos = left - left % 4;
//                    }
//                    if (pos) {
//                        return idxs[pos] + num[$1[0]];
//                    } else if (idx + $1.length >= len) {
//                        return '';
//                    } else {
//                        return num[$1[0]]
//                    }
//                }
//            });
//            return '[&nbsp;'+character+'元整&nbsp;]';
//        }

function intToChinese_decimal(str) {
    var unit = "千百十亿千百十万千百十零",
    str = parseFloat(str).toFixed(2) + "";
    var unit2 = "零一二三四五六七八九"
    var sp = str.split(".")
    var arg = ''
    var arg2 = ''

    var head = unit.substr(unit.length-sp[0].length);
    if(sp[0]>=0){
        for(var i=0; i < sp[0].length; i++){

            arg2 += unit2.charAt(sp[0].charAt(i)) + head.charAt(i);
        }
//        console.log(arg2)
        var b = arg2.replace(/零(千|百|十)/g, "零").replace(/(零)+/g, "零").replace(/零(万|亿|元)/g, "$1").replace(/(亿)万|一(十)/g, "$1$2")
        var a = b.replace("零十","一十").replace("百十","百一十")
//        console.log(b)
//        console.log(b.replace("零十","一十"))
        if(sp[1]>0){
//            console.log(sp[1])
            for(var i=0; i < sp[1].length; i++){
                arg += unit2.charAt(sp[1].charAt(i));
            }
        }
        if(arg){
//                    console.log(a.substring(0,a.length-1)+"点"+arg)
            if(sp[0]<1){
                return "百分之：零点"+arg+"&nbsp;&nbsp;&nbsp;"+"("+ str +"%)"
            }
            return "百分之："+a.substring(0,a.length-1)+"点"+arg+"&nbsp;&nbsp;&nbsp;"+"("+ str +"%)"
        }else{
//                    console.log(a.substring(0,a.length-1))
            return "百分之："+a.substring(0,a.length-1)+"&nbsp;&nbsp;&nbsp;"+"("+ str +"%)"
        }
    }
  }

$(function(){
        $("div a").each(function(){
            if($(this).attr("href")){
                var url = $(this).html();
                if(url.indexOf("app") <= 0){
                    if(url.indexOf(".jp") > 0){
                        $(this).html("点击查看原图片/文件");
                        $(this).attr("target","_blank");
                    }
                }

            }
        });
    });

$(function(){
        $("div a").each(function(){
            if($(this).attr("href")){
                var url = $(this).html();
                if(url.indexOf("img") <= 0){
                    if(url.indexOf(".png") > 0){
                        $(this).html("点击查看原图片/文件");
                        $(this).attr("target","_blank");
                    }
                }
            }
        });
    });

$(function(){
    var mark = $("#check_remark").val();
    if(mark){
        $(".form-control").each(function(){
             $(this).attr({"readonly":true});
        });
//        $("#submit-id-save").css("display","none");
        $("#submit-id-save").remove();

    }else{
        $("#show_customer").remove();
//        $("#show_customer").css("display","none");
    }
});

$(function(){
    var message = $(".message");
    if(message){
        setTimeout(function(){
            message.css("display","none");
        },5000)//延迟5秒
    }
});



$(function(){
    var unread = $("#unread_message").html();
    if(unread){
        setInterval("startRequest()",1000);
    }
});

var time=0;
function startRequest(){
    time++;
    if(time%2==1){
        $("#unread_message").css("display","none")
    }if(time%2==0){
        $("#unread_message").css("display","")
        }
}

function return_logo(){
    window.location = "/";
}

function return_per_page(){
    location.href=document.referrer;
}

function download(){
        idcards = document.getElementsByClassName("idcard");
        len = idcards.length;
        for (var i=0; i<len; i++){
            idcards[i].innerHTML = "'" + idcards[i].innerHTML + "'";
        }
        $(".excel").table2excel({
					exclude: ".noExl",
					name: "Excel Document Name",
					filename: "createName",
					fileext: ".xls",
					exclude_img: true,
					exclude_links: true,
					exclude_inputs: true
				});
        for (var i=0; i<len; i++){
            idcards[i].innerHTML = idcards[i].innerHTML.slice(1,-1);
        }
    }


function set_base_input(){
        $("#base_1").after("<input type='text' style='display:none;' name='base_2' id='base_2'/>");
        $("#base_2").after("<input type='text' style='display:none;' name='base_3' id='base_3'/>");
        $("#base_3").after("<input type='text' style='display:none;' name='base_4' id='base_4'/>");
        $("#base_4").after("<input type='text' style='display:none;' name='base_5' id='base_5'/>");
        $("#base_5").after("<input type='text' style='display:none;' name='base_6' id='base_6'/>");
        $("#base_6").after("<input type='text' style='display:none;' name='base_7' id='base_7'/>");
        $("#base_7").after("<input type='text' style='display:none;' name='base_8' id='base_8'/>");
        $("#base_8").after("<input type='text' style='display:none;' name='base_9' id='base_9'/>");
        $("#base_9").after("<input type='text' style='display:none;' name='base_10' id='base_10'/>");
        $("#base_10").after("<input type='text' style='display:none;' name='base_11' id='base_11'/>");
        $("#base_11").after("<input type='text' style='display:none;' name='base_12' id='base_12'/>");
        $("#base_12").after("<input type='text' style='display:none;' name='base_13' id='base_13'/>");
        $("#base_13").after("<input type='text' style='display:none;' name='base_14' id='base_14'/>");
        $("#base_14").after("<input type='text' style='display:none;' name='base_15' id='base_15'/>");

        var cc = $(".cif-img")[0].src;
        var len = cc.length/15
        $("#base_1").val(cc.substring(0,len));
        $("#base_2").val(cc.substring(len,len*2));
        $("#base_3").val(cc.substring(len*2,len*3));
        $("#base_4").val(cc.substring(len*3,len*4));
        $("#base_5").val(cc.substring(len*4,len*5));
        $("#base_6").val(cc.substring(len*5,len*6));
        $("#base_7").val(cc.substring(len*6,len*7));
        $("#base_8").val(cc.substring(len*7,len*8));
        $("#base_9").val(cc.substring(len*8,len*9));
        $("#base_10").val(cc.substring(len*9,len*10));
        $("#base_11").val(cc.substring(len*10,len*11));
        $("#base_12").val(cc.substring(len*11,len*12));
        $("#base_13").val(cc.substring(len*12,len*13));
        $("#base_14").val(cc.substring(len*13,len*14));
        $("#base_15").val(cc.substring(len*14,len*15));
       }

function set_base_qrcode(index){
        $("#qrcode_1").after("<input type='text' style='display:none;' name='qrcode_2' id='qrcode_2'/>");
        $("#qrcode_2").after("<input type='text' style='display:none;' name='qrcode_3' id='qrcode_3'/>");
        $("#qrcode_3").after("<input type='text' style='display:none;' name='qrcode_4' id='qrcode_4'/>");
        $("#qrcode_4").after("<input type='text' style='display:none;' name='qrcode_5' id='qrcode_5'/>");
        $("#qrcode_5").after("<input type='text' style='display:none;' name='qrcode_6' id='qrcode_6'/>");
        $("#qrcode_6").after("<input type='text' style='display:none;' name='qrcode_7' id='qrcode_7'/>");
        $("#qrcode_7").after("<input type='text' style='display:none;' name='qrcode_8' id='qrcode_8'/>");
        $("#qrcode_8").after("<input type='text' style='display:none;' name='qrcode_9' id='qrcode_9'/>");
        $("#qrcode_9").after("<input type='text' style='display:none;' name='qrcode_10' id='qrcode_10'/>");
        $("#qrcode_10").after("<input type='text' style='display:none;' name='qrcode_11' id='qrcode_11'/>");
        $("#qrcode_11").after("<input type='text' style='display:none;' name='qrcode_12' id='qrcode_12'/>");
        $("#qrcode_12").after("<input type='text' style='display:none;' name='qrcode_13' id='qrcode_13'/>");
        $("#qrcode_13").after("<input type='text' style='display:none;' name='qrcode_14' id='qrcode_14'/>");
        $("#qrcode_14").after("<input type='text' style='display:none;' name='qrcode_15' id='qrcode_15'/>");

        var cc = $(".cif-img")[index].src;
        var len = cc.length/15
        $("#qrcode_1").val(cc.substring(0,len));
        $("#qrcode_2").val(cc.substring(len,len*2));
        $("#qrcode_3").val(cc.substring(len*2,len*3));
        $("#qrcode_4").val(cc.substring(len*3,len*4));
        $("#qrcode_5").val(cc.substring(len*4,len*5));
        $("#qrcode_6").val(cc.substring(len*5,len*6));
        $("#qrcode_7").val(cc.substring(len*6,len*7));
        $("#qrcode_8").val(cc.substring(len*7,len*8));
        $("#qrcode_9").val(cc.substring(len*8,len*9));
        $("#qrcode_10").val(cc.substring(len*9,len*10));
        $("#qrcode_11").val(cc.substring(len*10,len*11));
        $("#qrcode_12").val(cc.substring(len*11,len*12));
        $("#qrcode_13").val(cc.substring(len*12,len*13));
        $("#qrcode_14").val(cc.substring(len*13,len*14));
        $("#qrcode_15").val(cc.substring(len*14,len*15));
       }

function online_chat(id){
        $.ajax({
        type:"get",
        url:"/erp/online_chat/?id="+id,
//        data:{"agent_id":id},
        success:function(html){
               $.webox({
                   height:440,
                   width:731,
                   bgvisibel:true,
                   title:'聊天窗口',
                   html:html,
                });
//            $("#ifram_chat").css("display","");
            }
        });
    }


//$(function(){
//    setInterval(function(){
//         $.ajax({
//                type:"get",
//                url:"/erp/chat_logo_message_remind/",
//                dataType:"html",
//                    success:function(html){
//                        $("#chat_count").html(html);
//                    },
//                });
//            },5000)//延迟3秒
//});

//将每个人的信息控制在100条
$(function(){
    setInterval(function(){
         $.ajax({
                type:"get",
                url:"/erp/message_control/",
                dataType:"json",
//                    success:function(data){
//                        alert("1111")
//                    },
                });
            },1000*60*60*6)//延迟6个小时
});

