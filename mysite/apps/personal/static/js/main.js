// Assign "active" class to navbar item based on current page URL
// https://gist.github.com/daverogers/5375778
$(document).ready(function() {
  // get current URL path and assign 'active' class
  var pathname = window.location.pathname;
  $('.nav > li > a[href="'+pathname+'"]').parent().addClass('active');
});
