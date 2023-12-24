function toggleNavbar() {
    let navbar = document.querySelector(".mobile-navbar");
    
    if (navbar.classList.contains("mobile-navbar_active")) {
        navbar.classList.remove("mobile-navbar_active");
    }
    else {
        navbar.classList.add("mobile-navbar_active")
    }
}