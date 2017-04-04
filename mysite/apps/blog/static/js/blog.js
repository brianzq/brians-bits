$(document).ready(function() {
  'use strict';

  console.log('action started.');
  $('.slide-down-fade-in')
    .css('opacity', 0)
    .slideDown(1000)
    .animate(
      { opacity: 1 },
      { queue: false, duration: 1000 }
    );
    console.log('action completed.');
});