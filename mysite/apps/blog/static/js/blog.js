$(document).ready(function() {
  'use strict';

  $('.slide-down-fade-in')
    // .css('opacity', 0)
    .slideDown(1000)
    .animate(
      { opacity: 1 },
      { queue: false, duration: 1000 }
    );
});