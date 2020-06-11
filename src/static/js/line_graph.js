var hours = document.getElementById('hours').value;
var date = document.getElementById('dates').value;
var data_dates = jQuery.parseJSON(date);
var data_hours = jQuery.parseJSON(hours);
Highcharts.chart('container', {
  chart: {
    type: 'line'
  },
  title: {
    text: 'Last 10 days progress'
  },
  subtitle: {
    text: 'Source: ScreenshotsVisions.com'
  },
  xAxis: {
    categories:data_dates
  },
  yAxis: {
    title: {
      text: 'hours(hrs)'
    }
  },
  plotOptions: {
    line: {
      dataLabels: {
        enabled: true
      },
      enableMouseTracking: true
    }
  },
  series: [{
    name: 'hours',
    data: data_hours
  },]
});