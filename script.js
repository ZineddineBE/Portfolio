var scrollToTopButton = document.getElementById("scrollToTopButton");
var linkArrow = document.getElementById("link-arrow");
var presentation = document.getElementById("top");

// Add a scroll event listener
window.addEventListener("scroll", function() {
    // If user has scrolled down more than 100px, show the button
    if(document.body.scrollTop >= 100 || document.documentElement.scrollTop >= 100) {
        scrollToTopButton.classList.add("show-scroll-to-top");
    }
     else {
        scrollToTopButton.classList.remove("show-scroll-to-top");
        linkArrow.classList.add('disabled');
    }
});

// Add a click event listener to scroll back to the top
scrollToTopButton.addEventListener("click", function(e) {
    e.preventDefault();
    // Scroll to the top smoothly
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});

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
    // close your menu here
    navLinks.classList.remove("mobile-menu");    
    });
};
