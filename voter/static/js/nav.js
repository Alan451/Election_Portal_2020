$(document).ready(function(){
    $("#mobile_nav").click(function(){
        if($("#primary_nav").css('left') > "-1px"){
            $("#primary_nav").animate({left: "-9rem"}, 150);
			$("body").css("overflow-x","hidden");
			$("#primary_nav").css("overflow-y","hidden");
		}else{
            $("#primary_nav").animate({left: "0px"}, 150);
			$("body").css("overflow-x","hidden");	
		}
    });
    
    if($(window).width() <= 1280) {
        $("#primary_nav").animate({left: "-9rem"}, 150);
        $("body").css("overflow-x","hidden");
        $("#primary_nav").css("overflow-y","hidden");
    }

    $(window).resize(
        function () {
          if ($(window).width() <= 1024 ) {
            $("#primary_nav").animate({left: "-9rem"}, 150);
            $("body").css("overflow-x","hidden");
            $("#primary_nav").css("overflow-y","hidden");
          } else {
            $("#primary_nav").animate({left: "0px"}, 150);
			$("body").css("overflow-x","hidden");
          }
        }
    );
});//end