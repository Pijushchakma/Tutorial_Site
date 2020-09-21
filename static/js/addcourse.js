$(document).ready(function () {
    $(".myButton").click(function () {
        var name = $(this).attr('id');
        var url = '/extraadd?name=' + name;
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if(this.readyState == 4 && this.status == 200) {
                
                location.reload();
            }
        };
        xhttp.open("GET", url, true);
        xhttp.send();
    })
    $(".container1").hide()
    $(".container1").show("fold", { horizFirst: true }, 500);
})
