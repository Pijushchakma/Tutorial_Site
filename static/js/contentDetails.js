$(document).ready(function(){
    $(".mark").click(function () {
        var name = $(this).attr('id');
        var url = '/increase?name=' + name;
        alert(url);
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if(this.readyState == 4 && this.status == 200) {

            }
        };
        xhttp.open("GET", url, true);
        xhttp.send();

        alert($(this).attr('id'));
        $(this).html('Marked Read');

    })
    // var a = $(".mark").attr('class');
    // var b =a.split(' ');
    // alert(b[1]);
})