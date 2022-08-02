
$(document).ready(function () {
    $(".btn-see").click(function (e) { 
        e.preventDefault();
        
        gal = $(this).data("btn");
        
        window.location.href = '../admin/viewgallery/?space='+gal+'';
    });


    $(".return").click(function (e) { 
        e.preventDefault();

        window.location.href = '../';
        // window.location.href = '../';
    });

    $(".reload").click(function (e) { 
        e.preventDefault();

        window.location.reload(1);
        // window.location.href = '../';
    });

    $(".down").click(function (e) { 
        e.preventDefault();
        let h = $('html, body').height();
        $('html, body').scrollTop($('html, body').scrollTop() + h);
        $(this).fadeOut(function(){
            $(".up").show();
        });
    });

    $(".up").click(function (e) { 
        e.preventDefault();
        let h = $('html, body').height();
        $('html, body').scrollTop($('html, body').scrollTop() - h);
        $(this).fadeOut(function(){
            $(".down").show();
        });
    });
});

