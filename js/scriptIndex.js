// inicio de la configuracion del menu
let menu = document.querySelector('#menu-bars');
let navbar = document.querySelector('.navbar');


//Menu movile
menu.onclick = () =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
}

let section = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header .navbar a');

window.onscroll = () =>{
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');

   section.forEach(sec =>{  //no funciona 
    let top = window.scrollY;
    let height = sec.offsetHeight;
    let offset = sec.offsetTop - 150;
    let id = sec.getAttribute('id');

    if (top >= offset && top < offset + height){
      navLinks.forEach(links =>{
        links.classList.remove('active');
        //alert(id)
        document.querySelector(`header .navbar a[href="#${id}"]`).classList.add('active');
      });
    };
    //href*=++]
  });

}
// fin de la configuracion del menu


// inicio de la configuracion del boton de busqueda
document.querySelector('#search-icon').onclick = () =>{     // no funciona
    document.querySelector('#search-form').classList.toggle('active');
}

document.querySelector('#close').onclick = () =>{   
    document.querySelector('#search-form').classList.remove('active');
}
// fin de la configuracion del boton de busqueda


// inicio de la configuracion del carrusel inicial
var swiper = new Swiper(".home-slider", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
      delay: 7500,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    loop: true,
  });
  // fin de la configuracion del carrusel inicial


// inicio de la configuracion del carrusel de opiniones
var swiper = new Swiper(".opinion-slider", {
  spaceBetween: 30,
  centeredSlides: true,
  autoplay: {
    delay: 7500,
    disableOnInteraction: false,
  },
  loop: true,
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    640: {
      slidesPerView: 2,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
});
// fin de la configuracion del carrusel de opiniones

