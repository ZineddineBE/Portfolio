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

