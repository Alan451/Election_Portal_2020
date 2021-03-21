$(document).ready(function () {
    ids = $(".hover-effect");
    $.each(ids, function(index, value) {
      $(this).hover(
        function () {
          $(".index_" + $(this).attr('id')).addClass("hidden");
          $(".text_" + $(this).attr('id')).removeClass("hidden");
          $(".bg_" + $(this).attr('id')).addClass("bg-blue-500");
          $(".bg_" + $(this).attr('id')).removeClass("bg-black");
        },
        function () {
          $(".index_" + $(this).attr('id')).removeClass("hidden");
          $(".text_" + $(this).attr('id')).addClass("hidden");
          $(".bg_" + $(this).attr('id')).addClass("bg-black");
          $(".bg_" + $(this).attr('id')).removeClass("bg-blue-500");
        }
      );
    });
});