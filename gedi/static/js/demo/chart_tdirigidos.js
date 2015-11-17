$(document).ready(function(){

   var datos_tdirigidos = {
   labels: ["January", "February", "March", "April", "May", "June", "July"],
   datasets: [
            {
                label: "Datos de mejores trabajos dirigidos",
                fillColor: "rgba(26,179,148,0.5)",
                strokeColor: "rgba(26,179,148,0.8)",
                highlightFill: "rgba(26,179,148,0.75)",
                highlightStroke: "rgba(26,179,148,1)",
                data: [20, 48, 40, 19, 86, 27, 90]
            }
        ]
    };

    var barOptions = {
        scaleBeginAtZero: true,
        scaleShowGridLines: true,
        scaleGridLineColor: "rgba(0,0,0,.05)",
        scaleGridLineWidth: 1,
        barShowStroke: true,
        barStrokeWidth: 2,
        barValueSpacing: 5,
        barDatasetSpacing: 1,
        responsive: true,
    }


    var ctx = document.getElementById("chart_tdirigidos").getContext("2d");
    var myNewChart = new Chart(ctx).Bar(datos_tdirigidos, barOptions);

});
