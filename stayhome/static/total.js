var b =document.getElementById('active').innerHTML;
var a =document.getElementById('confirmed').innerHTML;
var c =document.getElementById('recovered').innerHTML;
var d =document.getElementById('deaths').innerHTML;



let labels2 = ['Confirmed', 'Active', 'Recovered' , 'Deaths'];
let data2 = [a, b, c , d];
let colors2 = ['#1e90ff', '#FFC312', '#16a085', '#e74c3c']

let mychart2 = document.getElementById("myChart2").getContext('2d');

let chart2 = new Chart(mychart2, {
  type:'bar',
  data: {
    labels: labels2,
    datasets: [{
      data: data2,
      backgroundColor: colors2
    }]
  },
  options: {
    title: {
      text: "Stats of COVID-19",
      display: true
    },
    legend:{
      display: false
    }
  }

});
