
$(document).ready(function(){

    $(".form-1").animate({opacity: '1'}, 1200, function(){});
    $(".button-submit").click(function (e) { 
        e.preventDefault();
        // console.log("HOLA")
        let answers = {type: $("#type").val(), customer: $("#customer").val(), name : $("#name").val(), email: $("#email").val(), phone : $("#phone").val()};
        var error = false
        for (const [k, v] of Object.entries(answers)) {
            if (v == ""){
                // console.log(k, "ERROR")
                // console.log("#"+k+"")
                $("#"+k+"").css("border", "2px solid rgb(226, 61, 61)");
                error = true
            } 
        }

        if (error) {
            $(".form-main").append('<div style="font-weight: 300; font-style: italic; color: red;">Te ha faltado llenar algunos campos</div>');
        } else {
            $(".form-main").fadeOut(1000, function () {
                var name = answers.name
                var fn = name.replace(/ .*/,'');
                $(".form-1").animate({opacity: '0'}, 700, function(){});
                $(".form-title").html("Perfecto "+fn+", iniciemos con nuestro proceso de remodelación"); 
                $(".info-upload").show();
                $(".info-upload").animate({opacity: '1'}, 700, function(){});
            });
        }  
    });

    $(".form-item").click(function (e) { 
        e.preventDefault();

        // $(".input-box").animate({opacity: '0'}, 700, function(){});

        var data = $(this).data("type")
        // console.log(data)
        
        if (data !== "Estrato" && data !== "Comodidades") {
            var offset = $(this).offset();
            var top = offset.top;
            var left = offset.left;
            
            $(".estrato-box").animate({opacity: '0'}, 0, function(){});
            var viewportWidth = $("body").innerWidth();
    
            var total = ((left / viewportWidth) * 100) - 15.2
            $(".input-box").css({left: total+"vw", position:'absolute'});
            $(".input-title").html(data);
            
            $("#input").data("type", data);
            $("#input").val("");
    
            // $(".input-box").fadeIn();
            $(".input-box").animate({opacity: '1'}, 100, function(){});
        } else if (data == "Comodidades") {
            $(".input-box").animate({opacity: '0'}, 00, function(){});
            $(".estrato-box").animate({opacity: '0'}, 0, function(){});
            var offset = $(this).offset();
            var top = offset.top;
            var left = offset.left;
            
            var viewportWidth = $("body").innerWidth();
    
            var total = ((left / viewportWidth) * 100) - 15.2
            $(".comodities-box").css({left: total+"vw", top: (top+10)+"px", position:'absolute'});
            $(".input-title").html(data);

            $(".comodities-box").animate({opacity: '1'}, 100, function(){});
        } else {
            $(".input-box").animate({opacity: '0'}, 00, function(){});
            $(".comodities-box").animate({opacity: '0'}, 0, function(){});
            var offset = $(this).offset();
            var top = offset.top;
            var left = offset.left;
            
            var viewportWidth = $("body").innerWidth();
    
            var total = ((left / viewportWidth) * 100) - 15.2
            $(".estrato-box").css({left: total+"vw", top: (top+10)+"px", position:'absolute'});
            $(".input-title").html(data);

            $(".estrato-box").animate({opacity: '1'}, 100, function(){});


         
        }
    });

    $(".next-button1").click(function (e) { 
        e.preventDefault();
        $(".etapa1").html('<i class="fas fa-check"></i>');
        $(".etapa1").addClass("checked");
        $(".etapa1").removeClass("current");
        $(".line-1").addClass("checked");
        $(".etapa-1").animate({opacity: '0'}, 700, function(){
            $(".etapa-1").hide();
            $(".etapa-2").show();
            $(".etapa-2").animate({opacity: '1'}, 700, function(){
                $(".etapa2").addClass("current");
            });
        });
    });

    
    $(".input-save").click(function (e) { 
        e.preventDefault();
        $(".input-box").animate({opacity: '0'}, 700, function(){});
    });


    $(".input-save2").click(function (e) { 
        e.preventDefault();
        $(".estrato-box").animate({opacity: '0'}, 700, function(){});
    });

    $(".input-save3").click(function (e) { 
        e.preventDefault();
        $(".comodities-box").animate({opacity: '0'}, 700, function(){});
    });



    let dollarUSLocale = Intl.NumberFormat('en-US');

    $("#input").on("input", function() {
        var data = $(this).data("type")
        var id = data.toLowerCase();

        // console.log("a")
        // // console.log($(this).val()+"m²")
        if (id == "precio") {
            $("#"+id).html("$"+dollarUSLocale.format($(this).val()));
            $("#"+id+"-form").val($(this).val());
        } else if (id == "area") {
            $("#"+id).html($(this).val()+"m²");
            $("#"+id+"-form").val($(this).val());
        } else {
            $("#"+id).html($(this).val());
            $("#"+id+"-form").val($(this).val());
        }

    });
    
    $("select").on("input", function() {
        var data = $(this).data("type")


        // console.log($("select").val())

        $("#estrato").html($(this).val());
        $("#estrato-form").val($(this).val());
    }); 

    let comodities = []
    $('input[type="checkbox"]').change(function() {

        $($(this).data('com')).appendTo('#comodidades');

        if ($(this).is(':checked')) {
            comodities.push($(this).data('com'));
        } else {
            var index = comodities.indexOf($(this).data('com'))
            comodities.splice(index, 1)
            // comodities.push($(this).data('com'));
            
        }

        // // console.log(comodities.length)
        updateComodities(comodities)


     });
});

function updateComodities(comodities) {
    let comodidades = comodities
    $("#comodidades").html("");

    comodidades.forEach(function(v, k, array) {
        var text = $("#comodidades").html();
        $("#comodidades").html(v);
        if (text == "") {
            $("#comodidades").html(v);
            $("#comodidades-form").val(v);
        } else {
            $("#comodidades").html(text+", "+v+"");
            $("#comodidades-form").val(text+", "+v+"");
        }
        
    })
}