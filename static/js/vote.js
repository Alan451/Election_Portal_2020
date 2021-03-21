let selected = false;
let selected_id = null;
let ids = [];
let designations = {
  'Vice President': 1,
  'General Secretary of Hostel Affairs Board': 2,
  'General Secretary of Technical Board': 3,
  'General Secretary of Cultural Board': 4,
  'General Secretary of Students&#x27; Welfare Board': 5,
  'General Secretary of Sports Board': 6,
  'General Seceratry of SAIL': 7,
  'General Seceratry of SWC': 8,
  'Under Graduate Senator': 9,
  'Post Graduate Senator': 9,
  'Girl Senator': 10
}

function getIds(contList) {
  for (let index = 0; index < contList.length; index++) {
    let element = contList[index];
    ids.push(element);
  }
  console.log(ids);
}

function setProgress(designation, total) {
  let x = designations[designation] / total * 100;
  let init = x - 1 / total * 100;
  let elem = $(".progress");
  let id = setInterval(frame, 0.5);
  function frame () {
    if(init > x) {
      clearInterval(id);
    } else {
      init += 0.15;
      elem.width(init + '%');
    }
  }
}

$(document).ready(function () {
  console.log();
  $.each(ids, function(index, value) {
    $("#" + ids[index]).hover(
      function () {
        $("#index_" + ids[index]).addClass("hidden");
        $("#text_" + ids[index]).removeClass("hidden");
      },
      function () {
        $("#index_" + ids[index]).removeClass("hidden");
        $("#text_" + ids[index]).addClass("hidden");
      }
    );


    $("#" + ids[index]).click(function () {
      $(".nota-effect").css("opacity", 1);
      $(".bg-custom").css("background", "rgba(231, 105, 15, 0.1)");
      $(".text-custom").css("color", "#E7690F");
      let nextBtn = $("#next-btn");
      
      if (
        (selected == false) &
        ((selected_id != input_id) | (input_id == null))
        ) {
        $("#" + ids[index]).delay(10).fadeOut(70).fadeIn(70).fadeOut(50).fadeIn(50);
        $("#" + ids[index]).addClass(" bg-gray-200");
        $("#action_box_container_" + ids[index]).addClass(" bg-black text-white");
        $("#action_box_container_" + ids[index]).html("<span class='flex'><svg class = 'm-0.5 ml-0 mt-1'width='17' height='17' viewBox='0 0 17 17' fill='none' xmlns='http://www.w3.org/2000/svg'><path fill-rule='evenodd' clip-rule='evenodd' d='M14.6409 4.48403C14.7901 4.63344 14.874 4.83598 14.874 5.04715C14.874 5.25832 14.7901 5.46086 14.6409 5.61028L6.93778 13.3134C6.78836 13.4626 6.58583 13.5464 6.37465 13.5464C6.16348 13.5464 5.96094 13.4626 5.81153 13.3134L2.3584 9.86028C2.21764 9.70921 2.14101 9.50942 2.14466 9.30297C2.1483 9.09653 2.23193 8.89955 2.37793 8.75355C2.52393 8.60755 2.7209 8.52392 2.92735 8.52028C3.13379 8.51663 3.33359 8.59327 3.48465 8.73403L6.37465 11.624L13.5147 4.48403C13.6641 4.3348 13.8666 4.25098 14.0778 4.25098C14.289 4.25098 14.4915 4.3348 14.6409 4.48403Z' fill='white'/></svg>Voted</span>");
        selected = true;
        selected_id = ids[index];
        $(".opted-for").html("You have Voted for " + $(".name_" + selected_id).html());
        $(".info-block").removeClass("hidden");
        nextBtn.removeAttr("disabled");
        nextBtn.removeClass("opacity-10 cursor-not-allowed");
        M.toast({html: 'Click Save to Continue! You can review your votes later'});
        voteClick(selected_id);
      } else if (ids[index] == selected_id) {
        var cha = String.fromCharCode(65+ids.indexOf(selected_id));
        $("#" + selected_id).removeClass(" bg-gray-200");
        $("#action_box_container_" + selected_id).removeClass(
          " bg-black text-white"
        );
        $("#action_box_container_" + selected_id).html(
          `<span id="text_${selected_id}" class="hidden" >Vote for</span><span id="index_${selected_id}">${cha}</span>`
        );
        selected = false;
        selected_id = null;
        $(".opted-for").html("Select the candidiate you want to vote for.");
        $(".info-block").addClass("hidden");
        nextBtn.attr("disabled", true);
        nextBtn.addClass("opacity-10 cursor-not-allowed");
        voteClick(selected_id);
      } else {
        var cha = String.fromCharCode(65+ids.indexOf(selected_id));
        $("#" + selected_id).removeClass(" bg-gray-200");
        $("#action_box_container_" + selected_id).removeClass(
          " bg-black text-white"
        );
        $("#action_box_container_" + selected_id).html(
          `<span id="text_${selected_id}" class="hidden" >Vote for</span><span id="index_${selected_id}">${cha}</span>`
        );
        $(this).delay(10).fadeOut(70).fadeIn(70).fadeOut(50).fadeIn(50);
        $(this).addClass(" bg-gray-200");
        $("#action_box_container_" + ids[index]).addClass(" bg-black text-white");
        $("#action_box_container_" + ids[index]).html("<span class='flex'><svg class = 'm-0.5 ml-0 mt-1'width='17' height='17' viewBox='0 0 17 17' fill='none' xmlns='http://www.w3.org/2000/svg'><path fill-rule='evenodd' clip-rule='evenodd' d='M14.6409 4.48403C14.7901 4.63344 14.874 4.83598 14.874 5.04715C14.874 5.25832 14.7901 5.46086 14.6409 5.61028L6.93778 13.3134C6.78836 13.4626 6.58583 13.5464 6.37465 13.5464C6.16348 13.5464 5.96094 13.4626 5.81153 13.3134L2.3584 9.86028C2.21764 9.70921 2.14101 9.50942 2.14466 9.30297C2.1483 9.09653 2.23193 8.89955 2.37793 8.75355C2.52393 8.60755 2.7209 8.52392 2.92735 8.52028C3.13379 8.51663 3.33359 8.59327 3.48465 8.73403L6.37465 11.624L13.5147 4.48403C13.6641 4.3348 13.8666 4.25098 14.0778 4.25098C14.289 4.25098 14.4915 4.3348 14.6409 4.48403Z' fill='white'/></svg>Voted</span>");
        selected = true;
        selected_id = ids[index];
        $(".opted-for").html("You have Voted for " + $(".name_" + selected_id).html());
        nextBtn.removeAttr("disabled");
        nextBtn.removeClass("opacity-10 cursor-not-allowed");
        M.toast({html: 'Click Save to Continue! You can review your votes later'});
        voteClick(selected_id);
      }
    });
  });

  $("#nota").click(function () {
    let nextBtn = $("#next-btn");
    if (selected_id) {
      var cha = String.fromCharCode(65+ids.indexOf(selected_id));
      $("#" + selected_id).removeClass(" bg-gray-200");
      $("#action_box_container_" + selected_id).removeClass(
        " bg-black text-white"
      );
      $("#action_box_container_" + selected_id).html(
        `<span id="text_${selected_id}" class="hidden" >Vote for</span><span id="index_${selected_id}">${cha}</span>`
      );
      selected = false;
      selected_id = null;
    }
    $(".nota-effect").css("opacity", 0.5);
    $(".bg-custom").css("background", "#E7690F");
    $(".text-custom").css("color", "rgb(236, 232, 229)");
    $(".opted-for").html("You have Voted for None Of The Above");
    $(".info-block").removeClass("hidden");
    nextBtn.removeAttr("disabled");
    nextBtn.removeClass("opacity-10 cursor-not-allowed");
    M.toast({html: 'You have selected None Of The Above, Click Save to Continue.'});
  });

  $("#info-btn").hover(
    function () {
      $("#info-txt").toggleClass("hidden");
    },
    function () {
      $("#info-txt").toggleClass("hidden");
    }
  );

  if ($(window).width() <= 768 ) {
    $("#next-btn").insertAfter("#nota");
  }

  $(window).resize(
    function () {
      if ($(window).width() <= 768 ) {
        $("#next-btn").insertAfter("#nota");
      } else {
        $("#nota").insertAfter("#next-btn");
      }
    }
  );
});

let input_id = null;
$(document).ready(function () {
document.onkeyup = function (e) {
  if(e.which-65>=ids.length){
    input_id = null;
  }
  else{
    input_id = ids[e.which-65];
    $("#" + input_id).trigger("click");
    console.log(input_id);
  }
}
});

