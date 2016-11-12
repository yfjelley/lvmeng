$(function () {

    daily_netvalue = calculate_daily_netvalue(netvalue)
    drawdown = calculate_drawdown(netvalue)
    netvalue_histogram_set = calculate_daily_netvalue_histogram(daily_netvalue_list)
    accumulated_top_5_pz = top_5_pz_data_acculumate(top_5_tz_data)
    if (all_pz_render['value']!=[]){
        all_pz_render['value'] = scalarMultiply_array(all_pz_render['value'],100)
    }


    calculate_all_number()
    plot_chart1('#chart1');

    //plot_chart2('#chart2');
    //plot_chart3('#chart3');
    //plot_chart4('#chart4');
    /*$('a[data-toggle="tab"]').live('shown.bs.tab', function (e) {
     console.dir(e);
     $('.tab-content .tab-pane.active .statistic_highchart').highcharts().setSize($('.tab-pane').width(),$('.tab-pane').height());
     })  */
});




// CLASSYLOADER
// -----------------------------------

(function(window, document, $, undefined){

    $(function(){

        var $scroller       = $(window),
            inViewFlagClass = 'js-is-in-view'; // a classname to detect when a chart has been triggered after scroll

        $('[data-classyloader]').each(initClassyLoader);

        function initClassyLoader() {

            var $element = $(this),
                options  = $element.data();

            // At lease we need a data-percentage attribute
            if(options) {
                if( options.triggerInView ) {

                    $scroller.scroll(function() {
                        checkLoaderInVIew($element, options);
                    });
                    // if the element starts already in view
                    checkLoaderInVIew($element, options);
                }
                else
                    startLoader($element, options);
            }
        }
        function checkLoaderInVIew(element, options) {
            var offset = -20;
            if( ! element.hasClass(inViewFlagClass) &&
                $.Utils.isInView(element, {topoffset: offset}) ) {
                startLoader(element, options);
            }
        }
        function startLoader(element, options) {
            element.ClassyLoader(options).addClass(inViewFlagClass);
        }

    });

})(window, document, window.jQuery);

//accumulate value for each pz
function top_5_pz_data_acculumate(){
    accumulated_top_5_pz =[[],[],[],[],[]]
    for (i = 0; i < top_5_tz_data.length; i++) {
        accumulated_value = 0
        for (j = 0; j < top_5_tz_data[i].length; j++) {
            accumulated_value += top_5_tz_data[i][j][1]
            accumulated_top_5_pz[i].push([top_5_tz_data[i][j][0], accumulated_value])
        }

    }
    return accumulated_top_5_pz

}

//calculate daily netvalue list from netvalue
function calculate_daily_netvalue(netvalue){
    daily_netvalue_list = [];

    for (i = 1; i < netvalue.length; i++) {
        daily_netvalue = netvalue[i][1] - netvalue[i-1][1];
        daily_netvalue_list.push([netvalue[i][0], daily_netvalue])
    }
    return daily_netvalue_list
}

//calculate drawdown given netvalue list
function calculate_drawdown(netvalue){
    drawdown_list = [];
    previous_netvalue_list = [];

    for (i = 1; i < netvalue.length; i++) {
        previous_netvalue_list.push(netvalue[i-1][1])

        previous_max = Math.max.apply(null, previous_netvalue_list)
        //max number from 0 to i - 1, not i !

        if (netvalue[i][1] >= previous_max){
            drawdown = 0;
        }
        else{
            drawdown = (netvalue[i][1] - previous_max) / previous_max
        }

        drawdown_list.push([netvalue[i][0], drawdown])
    }
    return drawdown_list
}

function calculate_daily_netvalue_histogram(daily_netvalue){

    //bins under distribution to plot histogram
    bins = [-0.03, -0.025, -0.02, -0.015, -0.01, -0.005, 0, 0.005, 0.01, 0.015, 0.02, 0.025, 0.03]
    //value to calculate histogram
    value = [];
    for (i = 1; i < daily_netvalue.length; i++) {
        value.push(daily_netvalue[i][1]);
        //push value into the list to calculate
    }
    var result =  histogram({
        data : value,
        bins : bins,
    })

    return result

}

function calculate_all_number(){
    var no_risk_profit = 0.03
    //无风险收益: 3% 年化

    drawdown_value_list = []
    for (i = 1; i < drawdown.length; i++) {
        drawdown_value_list.push(drawdown[i][1])
    }

    daily_netvalue_value_list = []
    for (i = 1; i < drawdown.length; i++) {
        daily_netvalue_value_list.push(daily_netvalue[i][1])
    }

    netvalue_value_list = []
    for (i = 1; i < drawdown.length; i++) {
        netvalue_value_list.push(netvalue[i][1])
    }

    //至今净值收益
    number_1 = netvalue.slice(-1)[0][1].toFixed(4)

    //render to html
    $("#number_1").html(number_1)

    //夏普比
    /*
    夏普比例=（收益率-无风险收益）/收益率标准差
    无风险收益: 3% 年化

        年化收益率=(YTDr-1)*250 / 交易日
        标准差=原始标准差*sqrt(250);
        原始标准差：每日收益率的标准差
    */
    standard_deviation = getStandardDeviation(daily_netvalue_value_list,8)
    standard_deviation_year = standard_deviation * Math.sqrt(250)
    profit_year = ((number_1 - 1) * 250) / daily_netvalue.length
    sharp_ratio = ((profit_year - no_risk_profit )/ standard_deviation_year).toFixed(5)
    $("#number_2").html(sharp_ratio)

    //索提诺比

    less_risk_netvalue_list = []
    for (i = 1; i < daily_netvalue_value_list.length; i++) {
        if (daily_netvalue_value_list[i] < no_risk_profit / daily_netvalue_value_list.length){
            less_risk_netvalue_list.push(daily_netvalue_value_list[i])
        }
    }

    sotino_ratio = (profit_year / (getStandardDeviation(less_risk_netvalue_list,8) * Math.sqrt(250))).toFixed(4)
    $("#number_3").html(sotino_ratio)


    //最大连续回撤
    number_4 = Math.min.apply(null, drawdown_value_list).toFixed(4)
    $("#number_4").html(number_4)


    //回撤均值

    number_5 = getAverageFromNumArr(drawdown_value_list,4)
    $("#number_5").html(number_5)

    //回撤标准差
    number_6 = getStandardDeviation(drawdown_value_list,4)
    $("#number_6").html(number_6)

    //最大单日亏损

    number_7 = Math.min.apply(null, daily_netvalue_value_list).toFixed(4)
    $("#number_7").html(number_7)

    //最大单日收益

    number_8 = Math.max.apply(null, daily_netvalue_value_list).toFixed(4)
    $("#number_8").html(number_8)

    //平均日收益

    number_9 = getAverageFromNumArr(daily_netvalue_value_list,5)
    $("#number_9").html(number_9)


    //每日收益标准差
    number_10 = getStandardDeviation(daily_netvalue_value_list,5)
    $("#number_10").html(number_10)

}

//scale, and convert to percentage wise
//this applies to dict like this ['time', 'value']
function scalarMultiply(arr, multiplier) {
   for (var i = 0; i < arr.length; i++)
   {
      arr[i][1] *= multiplier;
   }
   return arr;
}

//this applys to array
function scalarMultiply_array(arr, multiplier) {
   for (var i = 0; i < arr.length; i++)
   {
      arr[i] *= multiplier;
   }
   return arr;
}


function plot_chart1(chart_id){
    //plot_data = scalarMultiply(netvalue, 100)
    plot_data = netvalue
    // Create the chart
    $(chart_id).highcharts('StockChart', {

        chart: {
            animation: {
                duration: 1000
            }
        },
        rangeSelector : {
            selected : 5
        },

        title : {
            text : '净值收益曲线'
        },

        yAxis : {
            title : {
                text : '净值'
            },
            min: 0.8,
        },
        credits: {
            enabled: false
        },
        exporting: {
            enabled:false
        },

        series : [{
            name : '净值收益',
            data : plot_data,
            id : 'dataseries',
            type : 'area',

            tooltip : {
                pointFormat: "{series.name}: {point.y:.4f}"
            },
            fillColor : {
                linearGradient : {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 1
                },
                stops : [
                    [0, Highcharts.getOptions().colors[0]],
                    [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                ]
            },
        },{

            onSeries : 'dataseries',
            width : 16,
            style : {// text style
                color : 'white'
            },
            states : {
                hover : {
                    fillColor : '#395C84' // darker
                }
            }
        }]
    });
    //$(chart_id).highcharts().setSize($('.tab-pane').width(),$('.tab-pane').height());
}


function plot_chart2(chart_id){
    plot_data = scalarMultiply(daily_netvalue, 100)

    // Create the chart
    $(chart_id).highcharts('StockChart', {
        rangeSelector : {
            selected : 5
        },

        title : {
            text : '每日净值收益图'
        },
        yAxis : {
            title : {
                text : '净值收益 %'
            },
        },
        credits: {
            enabled: false
        },

        exporting: {
            enabled:false
        },

        series : [{
            name : '每日净值收益',
            data : plot_data,
            type : 'column',
            tooltip : {
                pointFormat: "{series.name}: {point.y:.2f} %"
            },

        }]
    });
    $(chart_id).highcharts().setSize($('.tab-pane').width(),$('.tab-pane').height());
}

function plot_chart3(chart_id){
    plot_data = scalarMultiply(drawdown, 100)
    // Create the chart
    $(chart_id).highcharts('StockChart', {
        rangeSelector : {
            selected : 5
        },

        title : {
            text : '每日回撤图'
        },

        yAxis : {
            title : {
                text : '回撤 %'
            },
        },

        credits: {
            enabled: false
        },

        exporting: {
            enabled:false
        },

        series : [{
            name : '每日回撤',
            data : plot_data,
            type : 'column',
            tooltip : {
                pointFormat: "{series.name}: {point.y:.2f} %"
            },
    }]
    });
    $(chart_id).highcharts().setSize($('.tab-pane').width(),$('.tab-pane').height());

}

function plot_chart4(chart_id){
    categories = []
    data = []
    total_length = daily_netvalue_list.length

    for (i = 1; i < netvalue_histogram_set.length; i++) {
        categories.push(netvalue_histogram_set[i]['x'])
        data.push(netvalue_histogram_set[i]['y'] * 100 /total_length)
    }

    var chart = new Highcharts.Chart({
        chart: {
            renderTo: chart_id.slice(1),//remove the first character, like '#chart4' => 'chart4'
            type: 'column',
            margin: 75,
            options3d: {
                enabled: true,
                alpha: 15,
                beta: 15,
                depth: 50,
                viewDistance: 25
            }
        },
        title: {
            text: '每日损益分布'
        },
        xAxis: {
            categories: categories
        },
        yAxis: {
            title: {
                text: '频率 %'
            }
        },
        credits: {
            enabled: false
        },
        plotOptions: {
            column: {
                depth: 25
            }
        },
        exporting: {
            enabled:false
        },

        series: [{
            name: '每日损益分布 %',
            data: data,
            tooltip : {
                valueDecimals: 2
            },
        }]
    });

    function showValues() {
        $('#R0-value').html(chart.options.chart.options3d.alpha);
        $('#R1-value').html(chart.options.chart.options3d.beta);
    }

    // Activate the sliders
    $('#R0').on('change', function () {
        chart.options.chart.options3d.alpha = this.value;
        showValues();
        chart.redraw(false);
    });
    $('#R1').on('change', function () {
        chart.options.chart.options3d.beta = this.value + '%';
        showValues();
        chart.redraw(false);
    });

    showValues();
    $(chart_id).highcharts().setSize($('.tab-pane').width(),$('.tab-pane').height());

}


function plot_chart5(chart_id){
    $(chart_id).highcharts({
        chart: {
            type: 'column',
        },
        title: {
            text: '损益分析'
        },

        xAxis: {
            categories: all_pz_render['pz_name']
        },
        yAxis: {
            title: {
                text: '损益 %'
            }
        },
        credits: {
            enabled: false
        },
        exporting: {
            enabled:false
        },

        plotOptions: {
            line: {
                dataLabels: {
                    enabled: true
                },
                enableMouseTracking: false
            }
        },
        tooltip: {
            pointFormat: "{series.name}: {point.y:.2f} %",
        },
        series: [{
            name: '损益值',
            data: all_pz_render['value'],
            //data: all_pz_render['value']


        }
        ]
    });
    $(chart_id).highcharts().setSize($('.tab-pane').width(),$('.tab-pane').height());
}


function plot_chart6(chart_id){
        var seriesOptions = [],
        seriesCounter = 0,
        names = top_5_tz_name,
        // create the chart when all data is loaded
        createChart = function () {

            $(chart_id).highcharts('StockChart', {

                rangeSelector: {
                    selected: 5
                },

                yAxis: {
                    labels: {
                        formatter: function () {
                            return (this.value > 0 ? ' + ' : '') + this.value + '%';
                        }
                    },

                },
                credits: {
                    enabled: false
                },
                exporting: {
                    enabled:false
                },

                tooltip: {
                    pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y:.2f}%</b><br/>',
                },
                series: seriesOptions

            });
        };

    $.each(names, function (i, name) {

        //$.getJSON('http://www.highcharts.com/samples/data/jsonp.php?filename=' + name.toLowerCase() + '-c.json&callback=?',    function (data) {

            seriesOptions[i] = {
                name: name,
                data: accumulated_top_5_pz[i]
            };
            // As we're loading the data asynchronously, we don't know what order it will arrive. So
            // we keep a counter and create the chart when all the data is loaded.
            seriesCounter += 1;

            if (seriesCounter === names.length) {
                createChart();
            }
        //});

    });

    $(chart_id).highcharts().setSize($('.tab-pane').width(),$('.tab-pane').height());
}


//Purpose: Calculate standard deviation, variance, and average among an array of numbers.
var isArray = function (obj) {
	return Object.prototype.toString.call(obj) === "[object Array]";
},
getNumWithSetDec = function( num, numOfDec ){
	var pow10s = Math.pow( 10, numOfDec || 0 );
	return ( numOfDec ) ? Math.round( pow10s * num ) / pow10s : num;
},
getAverageFromNumArr = function( numArr, numOfDec ){
	if( !isArray( numArr ) ){ return false;	}
	var i = numArr.length,
		sum = 0;
	while( i-- ){
		sum += numArr[ i ];
	}
	return getNumWithSetDec( (sum / numArr.length ), numOfDec );
},
getVariance = function( numArr, numOfDec ){
	if( !isArray(numArr) ){ return false; }
	var avg = getAverageFromNumArr( numArr, numOfDec ),
		i = numArr.length,
		v = 0;

	while( i-- ){
		v += Math.pow( (numArr[ i ] - avg), 2 );
	}
	v /= numArr.length;
	return getNumWithSetDec( v, numOfDec );
},
getStandardDeviation = function( numArr, numOfDec ){
	if( !isArray(numArr) ){ return false; }
	var stdDev = Math.sqrt( getVariance( numArr, numOfDec ) );
	return getNumWithSetDec( stdDev, numOfDec );
};