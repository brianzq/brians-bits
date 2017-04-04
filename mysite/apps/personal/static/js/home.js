$(document).ready(function() {
  var mq = window.matchMedia( '(min-width: 992px)' );
  if (mq.matches) {
    $('#avatar').css({'marginLeft': '0px'}).animate({'marginLeft': '+=20px'});
    $('#home-text').css({'marginLeft': '40px'}).animate({'marginLeft': '-=20px', 'marginRight': '+=20px'});
  } else {
    //
  }
});