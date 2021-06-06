jQuery( document ).ready(function($) {

	var	$window = $(window),
		$header = $('#header'),
		$body = $('body');

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	let img = document.querySelector('#hover-img');

	img.addEventListener('mouseenter', function(e) {
		img.setAttribute('src', e.target.getAttribute('data-hover-src'));
	});
	img.addEventListener('mouseleave', function(e) {
		img.setAttribute('src', e.target.getAttribute('data-default-src'));
	});

	let img2 = document.querySelector('#hover-img2');
//Image 2
	img2.addEventListener('mouseenter', function(e) {
		img2.setAttribute('src', e.target.getAttribute('data-hover-src'));
	});
	img2.addEventListener('mouseleave', function(e) {
		img2.setAttribute('src', e.target.getAttribute('data-default-src'));
	});
//image 3
	let img3 = document.querySelector('#hover-img3');

	img3.addEventListener('mouseenter', function(e) {
		img3.setAttribute('src', e.target.getAttribute('data-hover-src'));
	});
	img3.addEventListener('mouseleave', function(e) {
		img3.setAttribute('src', e.target.getAttribute('data-default-src'));
	});
//image 4
	let img4 = document.querySelector('#hover-img4');

	img4.addEventListener('mouseenter', function(e) {
		img4.setAttribute('src', e.target.getAttribute('data-hover-src'));
	});
	img4.addEventListener('mouseleave', function(e) {
		img4.setAttribute('src', e.target.getAttribute('data-default-src'));
	});
//image 5
let img5 = document.querySelector('#hover-img5');

img5.addEventListener('mouseenter', function(e) {
	img5.setAttribute('src', e.target.getAttribute('data-hover-src'));
});
img5.addEventListener('mouseleave', function(e) {
	img5.setAttribute('src', e.target.getAttribute('data-default-src'));
});

//image 6
let img6 = document.querySelector('#hover-img6');

img6.addEventListener('mouseenter', function(e) {
	img6.setAttribute('src', e.target.getAttribute('data-hover-src'));
});
img6.addEventListener('mouseleave', function(e) {
	img6.setAttribute('src', e.target.getAttribute('data-default-src'));
});

//image 7
let img7 = document.querySelector('#hover-img7');

img7.addEventListener('mouseenter', function(e) {
	img7.setAttribute('src', e.target.getAttribute('data-hover-src'));
});
img7.addEventListener('mouseleave', function(e) {
	img7.setAttribute('src', e.target.getAttribute('data-default-src'));
});

//image 8
let img8 = document.querySelector('#hover-img8');

img8.addEventListener('mouseenter', function(e) {
	img8.setAttribute('src', e.target.getAttribute('data-hover-src'));
});
img8.addEventListener('mouseleave', function(e) {
	img8.setAttribute('src', e.target.getAttribute('data-default-src'));
});

//image 9
let img9 = document.querySelector('#hover-img9');

img9.addEventListener('mouseenter', function(e) {
	img9.setAttribute('src', e.target.getAttribute('data-hover-src'));
});
img9.addEventListener('mouseleave', function(e) {
	img9.setAttribute('src', e.target.getAttribute('data-default-src'));
});



	// Scrolly.
		$('.scrolly').scrolly();

	// Forms.
		var $form = $('form');

		// Auto-resizing textareas.
			$form.find('textarea').each(function() {

				var $this = $(this),
					$wrapper = $('<div class="textarea-wrapper"></div>'),
					$submits = $this.find('input[type="submit"]');

				$this
					.wrap($wrapper)
					.attr('rows', 1)
					.css('overflow', 'hidden')
					.css('resize', 'none')
					.on('keydown', function(event) {

						if (event.keyCode == 13
						&&	event.ctrlKey) {

							event.preventDefault();
							event.stopPropagation();

							$(this).blur();

						}

					})
					.on('blur focus', function() {
						$this.val($.trim($this.val()));
					})
					.on('input blur focus --init', function() {

						$wrapper
							.css('height', $this.height());

						$this
							.css('height', 'auto')
							.css('height', $this.prop('scrollHeight') + 'px');

					})
					.on('keyup', function(event) {

						if (event.keyCode == 9)
							$this
								.select();

					})
					.triggerHandler('--init');

			});

	// Menu.
		var $menu = $('#menu');

		$menu.wrapInner('<div class="inner"></div>');

		$menu._locked = false;

		$menu._lock = function() {

			if ($menu._locked)
				return false;

			$menu._locked = true;

			window.setTimeout(function() {
				$menu._locked = false;
			}, 350);

			return true;

		};

		$menu._show = function() {

			if ($menu._lock())
				$body.addClass('is-menu-visible');

		};

		$menu._hide = function() {

			if ($menu._lock())
				$body.removeClass('is-menu-visible');

		};

		$menu._toggle = function() {

			if ($menu._lock())
				$body.toggleClass('is-menu-visible');

		};

		$menu
			.appendTo($body)
			.on('click', function(event) {
				event.stopPropagation();
			})
			.on('click', 'a', function(event) {

				var href = $(this).attr('href');

				event.preventDefault();
				event.stopPropagation();

				// Hide.
					$menu._hide();

				// Redirect.
					if (href == '#menu')
						return;

					window.setTimeout(function() {
						window.location.href = href;
					}, 350);

			})
			.append('<a class="close" href="#menu">Close</a>');

		$body
			.on('click', 'a[href="#menu"]', function(event) {

				event.stopPropagation();
				event.preventDefault();

				// Toggle.
					$menu._toggle();

			})
			.on('click', function(event) {

				// Hide.
					$menu._hide();

			})
			.on('keydown', function(event) {

				// Hide on escape.
					if (event.keyCode == 27)
						$menu._hide();

			});
			
			$(function() {
				$('#travelitMenu').on('click', function() {
					var target = $(this.hash);
					target = $('#travelitContent');
					if (target.length) {
						$menu._hide();
						$('html,body').animate({
							scrollTop: target.offset().top
						}, 0);
						return false;
					}
				});
			});

			$(function() {
				$('#howItWorksMenu').on('click', function() {
					var target = $(this.hash);
					target = $('#howItWorksContent');
					if (target.length) {
						$menu._hide();
						$('html,body').animate({
							scrollTop: target.offset().top
						}, 0);
						return false;
					}
				});
			});

			$(function() {
				$('#testimonialsMenu').on('click', function() {
					var target = $(this.hash);
					target = $('#testimonialsContent');
					if (target.length) {
						$menu._hide();
						$('html,body').animate({
							scrollTop: target.offset().top
						}, 0);
						return false;
					}
				});
			});

			$(function() {
				$('#epicStoriesMenu').on('click', function() {
					var target = $(this.hash);
					target = $('#epicStoriesContent');
					if (target.length) {
						$menu._hide();
						$('html,body').animate({
							scrollTop: target.offset().top
						}, 0);
						return false;
					}
				});
			});

			$(function() {
				$('#aboutUsMenu').on('click', function() {
					var target = $(this.hash);
					target = $('#aboutUsContent');
					if (target.length) {
						$menu._hide();
						$('html,body').animate({
							scrollTop: target.offset().top
						}, 0);
						return false;
					}
				});
			});
})