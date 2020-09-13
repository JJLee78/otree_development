$(function() {
    // ********************************************************************************************************** //
    // size parameters for small and large pie charts
    // ********************************************************************************************************** //
    var pie_width = 40;
    var pie_height = 40;
    var relative_size = '95%';
    var margin = 0;
    var labels = false;

    if ( large_pies === 'True' && one_choice === 'True' ) {
        pie_width = 260;
        pie_height = 260;
        margin = 20;
        relative_size = '75%';
        labels = true;
    }

    sliced_a = [false, false]
    border_a = ['#ffffff', '#ffffff']
    width_a = [0.5, 0.5]
    if ( option_to_pay === 'A' && payoff === payoff_a_hi ) {
        sliced_a = [true, false]
        border_a = ['#28a745', '#ffffff']
        width_a = [2.5, 0.5]
    }
    if ( option_to_pay === 'A' && payoff === payoff_a_lo ) {
        sliced_a = [false, true]
        border_a = ['#ffffff', '#28a745']
        width_a = [0.5, 2.5]
    }

    sliced_b = [false, false]
    border_b = ['#ffffff', '#ffffff']
    width_b = [0.5, 0.5]
    if ( option_to_pay === 'B' && payoff === payoff_b_hi ) {
        sliced_b = [true, false]
        border_b = ['#28a745', '#ffffff']
        width_b = [2.5, 0.5]
    }
    if ( option_to_pay === 'B' && payoff === payoff_b_lo ) {
        sliced_b = [false, true]
        border_b = ['#ffffff', '#28a745']
        width_b = [0.5, 2.5]
    }

    // ********************************************************************************************************** //
    // base configuration of pie chart
    // ********************************************************************************************************** //
    var baseConfig = {
        credits: {
            enabled: false
        },
        chart: {
            backgroundColor:'rgba(255, 255, 255, 0.002)',
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            spacingBottom: margin,
            spacingTop: margin,
            spacingLeft: margin,
            spacingRight: margin,
            width: pie_width,
            height: pie_height
        },
        tooltip: {
            enabled: false
        },
        navigation: {
            buttonOptions: {
                enabled: false
            }
        },
        plotOptions: {
            pie: {
                size: relative_size,
                center: ['50%', '50%'],
                colors: ['#afcede', '#b3b3b3'],
                borderColor: '#ffffff',
                borderWidth: 0.5,
                showInLegend: labels,
                point: {
                    events: {
                        legendItemClick: function() {
                            return false;
                      }
                    }
                },
                allowPointSelect: false,
                slicedOffset: 5,
                dataLabels: {
                    enabled: labels,
                    useHTML: true,
                    style: {"fontSize": "12px"},
                    distance: 10,
                    softConnector: true,
                    connectorWidth: 1.5,
                    connectorPadding: 5,
                    formatter: function () {
                        if (this.percentage !== 0) {
                            return this.point.name;
                        }
                    }
                }
            },
            series: {
                animation: false,
                states: {
                    hover: {
                        enabled: false
                    }
                }
            }
        },
        legend: {
            enabled: labels,
            layout: 'vertical',
            verticalAlign: 'top',
            width: 200,
            itemStyle: {"fontWeight": "normal"},
            borderWidth: 1,
            borderRadius: 4,
            useHTML: true,
            labelFormatter: function() {
                if (percentage === 'False') {
                    return this.name + ' with probability ' +
                           this.y * num_choices + '/' + num_choices;
                } else {
                    return this.name + ' with probability ' +
                           this.percentage + '%';
                }
            }
        }
    };

    // ********************************************************************************************************** //
    // "A" lotteries
    // ********************************************************************************************************** //
    var lottery_a = [];
    for (var j = 1; j <= num_choices; ++j) {
        lottery_a[j] = {
            title: {
                text: ''
            },
            series: [{
                type: 'pie',
                data: [{
                    name: lottery_a_hi,
                    y: [j]/num_choices,
                    sliced: sliced_a[0],
                    borderColor: border_a[0],
                    borderWidth: width_a[0]
                },
                    {
                    name: lottery_a_lo,
                    y: (num_choices-[j])/num_choices,
                    sliced: sliced_a[1],
                    borderColor: border_a[1],
                    borderWidth: width_a[1]
                }]
            }]
        };

        $('#pie_a_'+[j]).highcharts(
                $.extend(baseConfig, lottery_a[j])
        );
    };

    // ********************************************************************************************************** //
    // "B" lotteries
    // ********************************************************************************************************** //
    var lottery_b = [];
    for (var j = 1; j <= num_choices; ++j) {
        lottery_b[j] = {
            title: {
                text: ''
            },
            series: [{
                type: 'pie',
                data: [{
                    name: lottery_b_hi,
                    y: [j]/num_choices,
                    sliced: sliced_b[0],
                    borderColor: border_b[0],
                    borderWidth: width_b[0]
                },{
                    name: lottery_b_lo,
                    y: (num_choices-[j])/num_choices,
                    sliced: sliced_b[1],
                    borderColor: border_b[1],
                    borderWidth: width_b[1]
                }]
            }]
        };

        $('#pie_b_'+[j]).highcharts(
                $.extend(baseConfig, lottery_b[j])
        );
    };
});