$(document).ready(function() {
  'use strict';

  $('.slide-down-fade-in')
    // .css('opacity', 0)
    .slideDown(500)
    .animate(
      { opacity: 1 },
      { queue: false, duration: 500 }
    );
});