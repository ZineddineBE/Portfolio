AOS.init({
  disable: function() {
    var maxWidth = 992;
    return window.innerWidth < maxWidth;
  }
});

var scrollToTopButton = document.getElementById("scrollToTopButton");
var linkArrow = document.getElementById("link-arrow");

// Fonction pour gérer le défilement
function handleScroll() {
    // Vérifie si on a défilé de plus de 150px
    if (document.documentElement.scrollTop >= 150) {
        scrollToTopButton.classList.add("show-scroll-to-top");
    } else {
        scrollToTopButton.classList.remove("show-scroll-to-top");
    }
}

// Ajoute l'écouteur d'événement pour le défilement
window.addEventListener("scroll", handleScroll);

// Exécuter immédiatement pour l'état initial
handleScroll();

// Add a click event listener to scroll back to the top
scrollToTopButton.addEventListener("click", function(e) {
    e.preventDefault();
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});

var presentation = document.getElementById("top");

presentation.addEventListener("click", function(f) {
    f.preventDefault();
    // Scroll to the top smoothly
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});

// Burger menu
const menuHamburger = document.querySelector(".burger-menu")
const navLinks = document.querySelector(".nav-links")
 
menuHamburger.addEventListener('click',()=>{
navLinks.classList.toggle('mobile-menu')
})

var links = document.querySelectorAll('a');

for( var i=links.length; i--; ) {
    links[i].addEventListener("click", function(){
    navLinks.classList.remove("mobile-menu");    
    });
};


// Add class "active" of nav-item when one is selected
const navMenu = document.getElementById('nav-links');
const navItems = document.querySelectorAll('.nav-item');

for(var i = 0; i < navItems.length; i++){
    navItems[i].addEventListener("click", function(){
        var current = document.querySelector(".active")

        if(current){
          current.classList.remove('active')
        }
        this.classList.add('active')
    })
}

