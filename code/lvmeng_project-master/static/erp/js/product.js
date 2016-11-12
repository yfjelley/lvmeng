
    $(function(){
        $("#id_mini_sub").after("<span id='span_mini_sub' style='font-size:18px;color:blue;margin-left:10px;'></span>");
        var str1 = $("#id_mini_sub").val();
        if (str1){
            $("#span_mini_sub").html(intToChinese(str1));
        }

        $("#id_product_sum").after("<span id='span_product_sum' style='font-size:18px;color:blue;margin-left:10px;'></span>");
        var str = $("#id_product_sum").val();
        if (str){
            $("#span_product_sum").html(intToChinese(str));
        }

        $("#id_return_expected").after("<span id='span_return_expected' style='font-size:18px;color:blue;margin-left:10px;'></span>");
        var str2 = $("#id_return_expected").val();
        if (str2){
            var number = str2*100
            $("#span_return_expected").html(intToChinese_decimal(number));
        }

        $("#id_addition").after("<span id='span_addition' style='font-size:18px;color:blue;margin-left:10px;'></span>");
        var str3 = $("#id_addition").val();
        if (str3){
            $("#span_addition").html(intToChinese(str3));
        }

        $("#id_alert_line").after("<span id='span_alert_line' style='font-size:18px;color:blue;margin-left:10px;'></span>");
        var str4 = $("#id_alert_line").val();
        if (str4){
            var number = str4*100
            $("#span_alert_line").html(intToChinese_decimal(number));
        }

        $("#id_clearance_line").after("<span id='span_clearance_line' style='font-size:18px;color:blue;margin-left:10px;'></span>");
        var str5 = $("#id_clearance_line").val();
        if (str5){
            var number = str5*100
            $("#span_clearance_line").html(intToChinese_decimal(number));
        }

        $("#id_subscription_fee").after("<span id='span_subscription_fee' style='font-size:18px;color:blue;margin-left:10px;'></span>");
        var str6 = $("#id_subscription_fee").val();
        if (str6){
            var number = str6*100
            $("#span_subscription_fee").html(intToChinese_decimal(number));
        }

        $("#id_custody_fee").after("<span id='span_custody_fee' style='font-size:18px;color:blue;margin-left:10px;'></span>");
        var str7 = $("#id_custody_fee").val();
        if (str7){
            var number = str7*100
            $("#span_custody_fee").html(intToChinese_decimal(number));
        }

        $("#id_service_fee").after("<span id='span_service_fee' style='font-size:18px;color:blue;margin-left:10px;'></span>");
        var str8 = $("#id_service_fee").val();
        if (str8){
            var number = str8*100
            $("#span_service_fee").html(intToChinese_decimal(number));
        }

        $("#id_redemption_fee").after("<span id='span_redemption_fee' style='font-size:18px;color:blue;margin-left:10px;'></span>");
        var str9 = $("#id_redemption_fee").val();
        if (str9){
            var number = str9*100
            $("#span_redemption_fee").html(intToChinese_decimal(number));
        }

        $("#id_management_fee").after("<span id='span_management_fee' style='font-size:18px;color:blue;margin-left:10px;'></span>");
        var str10 = $("#id_management_fee").val();
        if (str10){
            var number = str10*100
            $("#span_management_fee").html(intToChinese_decimal(number));
        }

        $("#id_compensation").after("<span id='span_compensation' style='font-size:18px;color:blue;margin-left:10px;'></span>");
        var str11 = $("#id_compensation").val();
        if (str11){
            var number = str11*100
            $("#span_compensation").html(intToChinese_decimal(number));
        }


    });

    function ToChinese_mini_sub(str){
        $("#span_mini_sub").html(intToChinese(str));
    }

    function ToChinese_product_sum(str){
        $("#span_product_sum").html(intToChinese(str));
    }

    function ToChinese_decimal(str){
        $("#span_return_expected").html(intToChinese_decimal(str));
    }

    function ToChinese_addition(str){
        $("#span_addition").html(intToChinese(str));
    }

    function ToChinese_decimal_alert_line(str){
        $("#span_alert_line").html(intToChinese_decimal(str));
    }

    function ToChinese_decimal_clearance_line(str){
        $("#span_clearance_line").html(intToChinese_decimal(str));
    }

    function ToChinese_decimal_subscription_fee(str){
        $("#span_subscription_fee").html(intToChinese_decimal(str));
    }

    function ToChinese_decimal_custody_fee(str){
        $("#span_custody_fee").html(intToChinese_decimal(str));
    }

    function ToChinese_decimal_service_fee(str){
        $("#span_service_fee").html(intToChinese_decimal(str));
    }

    function ToChinese_decimal_redemption_fee(str){
        $("#span_redemption_fee").html(intToChinese_decimal(str));
    }

    function ToChinese_decimal_management_fee(str){
        $("#span_management_fee").html(intToChinese_decimal(str));
    }

    function ToChinese_decimal_compensation(str){
        $("#span_compensation").html(intToChinese_decimal(str));
    }

