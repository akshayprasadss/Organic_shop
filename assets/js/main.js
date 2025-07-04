(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();

    // Fixed Navbar
    $(window).scroll(function () {
        if ($(window).width() < 992) {
            $('.fixed-top').toggleClass('shadow', $(this).scrollTop() > 55);
        } else {
            if ($(this).scrollTop() > 55) {
                $('.fixed-top').addClass('shadow').css('top', -55);
            } else {
                $('.fixed-top').removeClass('shadow').css('top', 0);
            }
        }
    });

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });

    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });

    // Testimonial carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 2000,
        center: false,
        dots: true,
        loop: true,
        margin: 25,
        nav: true,
        navText: ['<i class="bi bi-arrow-left"></i>', '<i class="bi bi-arrow-right"></i>'],
        responsive: {
            0: { items: 1 },
            576: { items: 1 },
            768: { items: 1 },
            992: { items: 2 },
            1200: { items: 2 }
        }
    });

    // vegetable carousel
    $(".vegetable-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1500,
        center: false,
        dots: true,
        loop: true,
        margin: 25,
        nav: true,
        navText: ['<i class="bi bi-arrow-left"></i>', '<i class="bi bi-arrow-right"></i>'],
        responsive: {
            0: { items: 1 },
            576: { items: 1 },
            768: { items: 2 },
            992: { items: 3 },
            1200: { items: 4 }
        }
    });

    // Modal Video
    $(document).ready(function () {
        let $videoSrc;
        $('.btn-play').click(function () {
            $videoSrc = $(this).data("src");
        });

        $('#videoModal').on('shown.bs.modal', function () {
            $("#video").attr('src', $videoSrc + "?autoplay=1&modestbranding=1&showinfo=0");
        });

        $('#videoModal').on('hide.bs.modal', function () {
            $("#video").attr('src', $videoSrc);
        });
    });

    // Quantity Dropdown Price Update
    $(document).ready(function () {
        document.querySelectorAll('.quantity-select').forEach(select => {
            select.addEventListener('change', function () {
                const quantity = parseInt(this.value);
                const unitPrice = parseFloat(this.dataset.price);
                const totalPriceEl = this.closest('.card-body').querySelector('.total-price');
                totalPriceEl.textContent = '₹' + (quantity * unitPrice).toFixed(2);
            });
        });
    });

    // Product Quantity (plus/minus buttons)
    $('.quantity button').on('click', function () {
        var button = $(this);
        var input = button.closest('.quantity').find('input');
        var oldValue = parseInt(input.val());

        var newVal = button.hasClass('btn-plus') ? oldValue + 1 : Math.max(0, oldValue - 1);
        input.val(newVal);

        // Update price on click
        var unitPrice = parseFloat(input.data('price'));
        var priceContainer = button.closest('.card-body').find('.total-price');
        if (unitPrice && priceContainer.length) {
            priceContainer.text('₹' + (unitPrice * newVal).toFixed(2));
        }
    });

})(jQuery);