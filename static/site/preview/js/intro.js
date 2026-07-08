$(function() {
    "use strict";
	
	
    $(window).on("load", function() {
        // 1. preloader
        $("#preloader").fadeOut(600);
        $(".preloader-bg").delay(400).fadeOut(600);
		
        // 2. fadeIn.element
        setTimeout(function() {
            $(".fadeIn-element").delay(600).css({
                display: "none"
            }).fadeIn(800);
        }, 0);
    });
	
    // 3. navigation
    // 3.1. page scroll
    $(".page-scroll").on("click", function(e) {
        var $anchor = $(this);
        $("html, body").stop().animate({
            scrollTop: $($anchor.attr("href")).offset().top - 55
        }, 1500, 'easeInOutExpo');
        e.preventDefault();
    });
    // 3.2. highlight navigation
    $("body").scrollspy({
        target: ".navbar",
        offset: 65
    });
    // 3.3. close mobile menu
    $(".navbar-collapse ul li a").on("click", function() {
        $(".navbar-toggle:visible").click();
    });
    // 3.4. highlight navigation
    $(".link-underline-menu").on("click", function() {
        $(".link-underline-menu").removeClass("active");
        $(this).addClass("active");
    });
	
    $(window).on("scroll load resize", function() {
        // 3.5. collapse navigation
        if ($(".navbar").offset().top > 50) {
            $(".navbar-bg-switch").addClass("main-navigation-bg");
        } else {
            $(".navbar-bg-switch").removeClass("main-navigation-bg");
        }
		
        // 4. to top arrow animation
        if ($(this).scrollTop() > 400) {
            $(".to-top-arrow").addClass("show");
        } else {
            $(".to-top-arrow").removeClass("show");
        }
		
        // 5. home fadeOut animation
        $("h1.home-page-title, h2.home-page-title, .the-button, .the-button-light").css("opacity", 1 - $(window).scrollTop() / 500);
    });
	
    // 7. facts counter
    $(".facts-counter-number").appear(function() {
        var count = $(this);
        count.countTo({
            from: 0,
            to: count.html(),
            speed: 1200,
            refreshInterval: 60
        });
    });

});