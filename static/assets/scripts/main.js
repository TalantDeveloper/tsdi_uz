// loader
// loader
// loader

var onx = document.getElementById('loader-box');
var bdy = document.getElementById('body');

setInterval(myTimer, 2000);

function myTimer() {
	onx.style.display = 'none';
	bdy.style.overflow = 'auto';
}

// loader// loader// loader// loader// loader// loader

$(document).ready (function (){
    // List box section


	$('.current-lang').click(function(){
    
		$('.langs').slideToggle();    
    });

	$('.right-tab').css('top', screen.height/2);

	$('#loader-box').css('top', $(window).scrollTop());
    $('.list').mouseenter( function () {
      $(this).find('.list-a').addClass('lists-a-befor');
    });
	
    $('.list').mouseleave( function () {
      $(this).find('.list-a').removeClass('lists-a-befor');
    });
	
	$('#list-menu').click( function () {
      $('.list').slideToggle();
    });

    $('.wk .inner-lists li').mouseenter( function () {
      $(this).find('a').css({'margin-left': '10px', 'color': '#2378c8'});
      $(this).find('.inner-inner-lists li a').css({'margin-left': '0', 'color': '#17202A'});
    });
    $('.wk .inner-lists li').mouseleave( function () {
      $(this).find('a').css({'margin-left': '0', 'color': '#17202A'});
    });

    $('.inner').mouseenter( function () {
      $(this).find('.inner-inner-lists').slideDown();
    });
    $('.inner').mouseleave( function () {
      $(this).find('.inner-inner-lists').slideUp();
    });
    
    $('.bottom .inner-lists li').mouseenter( function () {
      $(this).find('a').css({'margin-left': '10px'});
      $(this).find('.inner-inner-lists li a').css({'margin-left': '0'});
    });
    $('.bottom .inner-lists li').mouseleave( function () {
      $(this).find('a').css({'margin-left': '0',});
    });

	$('.taglist li').hover(function(){
    	$(this).find('a').css('color','#fff');
    },
      function(){
    	$(this).find('a').css('color','#1c74d6');
    });
    
    // Statistika

    // Kafedra section
    $('.kafedra a').mouseenter( function () {
      $(this).addClass('kafedra-a');
    });
    $('.kafedra a').mouseleave( function () {
      $(this).removeClass('kafedra-a');
    });

    $('.mudir-i').click( function () {
      $(this).toggleClass('fa-rotate-180');
      $('.xodimlar').slideToggle('slow');
    });
    // Markaz va bo'bolimlar

    $('.markaz a').mouseenter( function () {
      $('this h3').addClass('fa-rotate-180');
    });

    $('.left-fa, .right-fa').mouseenter( function () {
        $(this).css({'opacity': '1'});
      // alert($(window).width());
    });
    $('.left-fa, .right-fa').mouseleave( function () {
      $(this).css({'opacity': '0.5'});
    // alert($(window).width());
  });

});

// hamkorlar

const scrollContainer = document.getElementById("hamkor-scrol");

scrollContainer.addEventListener("wheel", (evt) => {
    evt.preventDefault();
    scrollContainer.scrollLeft += evt.deltaY;
});

