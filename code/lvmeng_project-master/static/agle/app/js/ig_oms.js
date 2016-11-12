/**
* Created by jiechaoli on 12/3/15.
*/

var app = angular.module('price_table',['smart-table']);
var chart_plot;
app.controller('price_tableCtrl', ['$scope', '$http', function ($scope, $http) {
    $scope.epics = []
    $http.get("epics")
        .then(function(res){
            $scope.epics = res.data
            for(var i = 0; i < $scope.epics.length; i++){
                socket_subscribe($scope.epics[i],$scope)
            };


    });
    //!!!Important!!!, add this to enable search, otherwise it will return blank
    $scope.displayedEpics= [].concat($scope.epics);
    $scope.active_epic = null;

    $scope.change_active_epic = function(epic) {
      $scope.active_epic = epic;
    }

    $scope.plot_chart = function(epic, chart_type, seconds){
        if (typeof(seconds)==='undefined') seconds = 1000;//default seconds is 1000
        rest_url =''
        if (chart_type == 'tick'){
            //tick level data
            rest_url = '/oms/pricedata/' + epic.name + '/?seconds='+ seconds +'&type=tick'
            $.getJSON(rest_url, function (data) {
                chart_plot = Highcharts.StockChart({
                    chart: {
                        renderTo: 'chart_'+chart_type,
                        ignoreHiddenSeries: true,
                        type: 'spline',
                        animation: Highcharts.svg, // don't animate in old IE
                        marginRight: 10,
                    },
                    plotOptions: {
                        series: {
                            shadow: false,
                            borderWidth: 0,
                            dataLabels: {
                                align: 'right',
                                x: 50,
                                y: 0,
                            }
                        }
                    },
                    title: {
                        text: epic.chinese_name
                    },
                    xAxis: {
                        type: 'datetime',
                        tickPixelInterval: 150,
                    },
                    yAxis: {
                        title: {
                            text: 'Value'
                        },

                    },
                    tooltip: {
                        formatter: function () {
                            return '<b>' + epic.chinese_name + '</b><br/>' +
                                    Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                                    Highcharts.numberFormat(this.y, 2);
                        }
                    },
                    credits: {
                        enabled: false
                    },
                    legend: {
                        enabled: false
                    },
                    exporting: {
                        enabled: false
                    },
                    series: [{
                        turboThreshold: 10000,//max data point
                        name: epic.chinese_name,
                        data: data,
                    }
                    ]
                });
            });

        }
        else{
            //candlestick, and type is interval
            rest_url = '/oms/pricedata/' + epic.name + '/?type=candlestick&interval='+ chart_type + '&seconds='+ seconds

            $.getJSON(rest_url, function (data) {
                chart_plot = Highcharts.StockChart({
                    chart: {
                        renderTo: 'chart_' + chart_type,
                        ignoreHiddenSeries: true,
                        type: 'spline',
                        animation: Highcharts.svg, // don't animate in old IE
                        marginRight: 10,

                    },
                    title: {
                        text: epic.chinese_name,
                    },
                    xAxis: {
                        type: 'datetime',
                        //tickPixelInterval: 150,
                    },
                    yAxis: {
                        title: {
                            text: 'Value'
                        },
                        plotLines: [{
                            value: 0,
                            width: 1,
                            color: '#808080'
                        }]
                    },

                    credits: {
                        enabled: false
                    },
                    legend: {
                        enabled: false
                    },
                    exporting: {
                        enabled: false
                    },
                    plotOptions: {
                        candlestick: {
                            color: 'green',
                            upColor: 'red'
                        },
                        series: {
                            shadow: false,
                            borderWidth: 0,
                            dataLabels: {
                                align: 'right',
                                x: 50,
                                y: 0,
                            }
                        }
                    },
                    series: [{
                        turboThreshold: 10000,//max data point
                        name: epic.chinese_name,
                        type: 'candlestick',
                        data: data,
                        tooltip: {
                            valueDecimals: 1
                        }
                    },

                    ]
                });
            })
        }


        Highcharts.setOptions({//set offset here tobe china time
            global: {
                timezoneOffset: -8 * 60
            }
        });

    }


    function socket_subscribe(epic, $scope) {
        var socket = io.connect(NODE_URL + "/" + epic['name'], {port: NODE_PORT});
        var epic_multiple_factor = epic['multiply_factor']

        socket.on('connect', function () {
            console.log("connect");
        });

        socket.on('message', function (message) {
            //Escape HTML characters
            var data = message.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
            var deal = JSON.parse(data);
            //console.log(deal);
            timestamp = parseFloat(deal[5]) * 1000
            bid_price = (parseFloat(deal[1]) * epic_multiple_factor).toFixed(1)
            offer_price = (parseFloat(deal[2]) * epic_multiple_factor).toFixed(1)
            change_price = parseFloat(deal[3]).toFixed(1)
            price = (parseFloat(bid_price) + parseFloat(offer_price)) / 2
            price = parseFloat(price.toPrecision(11))//keep only one decimal

            //update row data
            //must use apply here, otherwise, data binding won't work
            $scope.$apply(function() {
                for (var i = 0; i < $scope.epics.length; i++) {
                    if ($scope.epics[i]['name'] == epic['name']) {
                        $scope.epics[i]['offer'] = offer_price;
                        $scope.epics[i]['bid'] = bid_price;
                        $scope.epics[i]['change'] = change_price;
                    }
                }
            });
            //change row data every time, although its' not most efficient, it's most simple way
//{#            $scope.gridOptions.api.setRowData($scope.epics);#}


            if (chart_plot != undefined && chart_plot.series[0].name==epic['chinese_name']) {
//{#                    console.log(deal);#}
                if (chart_plot.series[0].type == 'spline') {
                    //only add data directly in spline plot, not candlestick
                    chart_plot.series[0].addPoint({x: timestamp, y: price}, true, true);
                }
                else if (chart_plot.series[0].type == 'candlestick') {
                    candlestick_interval = (chart_plot.series[0].data[1].x - chart_plot.series[0].data[0].x)

                    //update last data of candlestick, calculate open close high low
                    length = chart_plot.series[0].data.length

                    last_candlestick = chart_plot.series[0].data[length - 1]

                    if (timestamp - last_candlestick.x < candlestick_interval) {
                        //less than interval, just update last candlestick
                        //close is always the latest
                        last_candlestick.close = price
                        if (price > last_candlestick.high) {
                            last_candlestick.high = price
                        }

                        if (price < last_candlestick.low) {
                            last_candlestick.low = price
                        }

                        //just update the last item of data
                        //cannot not update like this: chart_plot.series[0].data[length - 1].update(last_candlestick)
                        //it will cause crash, too many recursion

                        chart_plot.series[0].data[length - 1].update([last_candlestick.x, last_candlestick.open, last_candlestick.high, last_candlestick.low, last_candlestick.close])

                    } else {
                        //otherwise, add a new candlestick
                        //create a new time, 5 minutes bigger
                        x = last_candlestick.x + candlestick_interval;
                        //everythin is the same because it only has one data point
                        open = price;
                        high = price;
                        low = price;
                        close = price;
                        chart_plot.series[0].addPoint([
                            x,
                            open,
                            high,
                            low,
                            close,
                        ]);
                    }
                }
            }
        });
    }
}]);

