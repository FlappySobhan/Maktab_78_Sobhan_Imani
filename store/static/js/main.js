$(document).ready(function() {
    $(window).scroll(function() {
      if ($(this).scrollTop() > 60) {
        $('#toTopBtn').fadeIn();
      } else {
        $('#toTopBtn').fadeOut();
      }
    });
  
    $('#toTopBtn').click(function() {
      $("html, body").animate({
        scrollTop: 0
      }, 500);
      return false;
    });
});