$(document).ready(function(){
    var swiper = new Swiper(".swiper", {
      autoplay: {
        delay: 5000,
      },
        effect: "coverflow",
        grabCursor: true,
        centeredSlides: true,
        coverflowEffect: {
          rotate: 0,
          stretch: 0,
          depth: 100,
          modifier: 3,
          slideShadows: true,
          autoplay: 5000,
          speed: 1000
        },
        loop: true,
        pagination: {
          el: ".swiper-pagination",
          clickable: true
        },
        
        breakpoints: {
          640: {
            slidesPerView: 2
          },
          768: {
            slidesPerView: 1
          },
          1024: {
            slidesPerView: 2
          },
          1560: {
            slidesPerView: 2
          }
        }
      });
  });

  