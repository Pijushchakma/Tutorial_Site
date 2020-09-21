$(document).ready(function () {

    $(".main").hide();
    
    $("#name1").click(function () {
        $(".main").hide();
        $(".main1").show("fold", { horizFirst: true }, 1000);
    })
    $("#name2").click(function () {
        $(".main").hide();
        $(".main2").show("fold", { horizFirst: true }, 1000);
    })
    $("#name3").click(function () {
        $(".main").hide();
        $(".main3").show("fold", { horizFirst: true }, 1000);
    })
    $("#name4").click(function () {
        $(".main").hide();
        $(".main4").show("fold", { horizFirst: true }, 1000);
    })
    $("#name5").click(function () {
        $(".main").hide();
        $(".main5").show("fold", { horizFirst: true }, 1000);
    })
    $("#name6").click(function () {
        $(".main").hide();
        $(".main6").show("fold", { horizFirst: true }, 1000);
    })
    $("#name7").click(function () {
        $(".main").hide();
        $(".main7").show("fold", { horizFirst: true }, 1000);
    })
    $("#name8").click(function () {
        $(".main").hide();
        $(".main8").show("fold", { horizFirst: true }, 1000);
    })
    $("#name9").click(function () {
        $(".main").hide();
        $(".main9").show("fold", { horizFirst: true }, 1000);
    })
    $("#name10").click(function () {
        $(".main").hide();
        $(".main10").show("fold", { horizFirst: true }, 1000);
    })
    $("#name11").click(function () {
        $(".main").hide();
        $(".main11").show("fold", { horizFirst: true }, 1000);
    })
    $(".mark").click(function () {
        var name = $(this).attr('id');
        var url = '/increase?name=' + name;
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                location.reload();
            }
        };
        xhttp.open("GET", url, true);
        xhttp.send();
        
        


    })

    var cNmaes = $(".percentage").attr('class');
    var l = cNmaes.split(' ');
    var sequal = parseInt(l[1]);
    var total = parseInt(l[2]);
    var cl = "#data"+sequal;
    var m = ".main"+sequal;
    
    $(m).show("fold", { horizFirst: true }, 1000);
    
    $(cl).css({"background-color":"#1e5f74","border-radius":"4px"});
    sequal = sequal - 1;
    var per = Math.round((sequal / total) * 100);
    

    $(".percentage").html(` ${per}%   Complete `);
    $(".in").css({ "width": per + "%" })

    var name = $("#status").attr('class');
    var url = '/StatusChange?name=' + name + '&val=' + per;
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();

    $("#status").click(function () {
        $(".timeline").toggle("fold", { horizFirst: true }, 2000);
    })

})