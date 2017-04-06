// Assign 'active' class to navbar item based on current page URL
// https://gist.github.com/daverogers/5375778
$(document).ready(function() {
  // get current URL path and assign 'active' class
  var pathname = window.location.pathname;
  $(`.nav > li > a[href='${pathname}']`).parent().addClass('active');
});

function setFooterStyle() {
  var docHeight = $(window).height();
  var footerHeight = $('#footer').outerHeight();
  var footerTop = $('#footer').position().top + footerHeight;
  if (footerTop < docHeight) {
      $('#footer').css('margin-top', (docHeight - footerTop) + 'px');
  } else {
      // have some separation between content
      $('#footer').css('margin-top', '50px');
  }
  $('#footer').removeClass('invisible');
}
$(document).ready(function() {
  setFooterStyle();
  window.onresize = setFooterStyle;
});
