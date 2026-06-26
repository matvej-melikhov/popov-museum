function toggleNavbar() {
    let navbar = document.querySelector(".mobile-navbar");
    navbar.classList.toggle("mobile-navbar_active");
}

document.querySelectorAll(".mobile-navbar__item a").forEach(function(link) {
    link.addEventListener("click", function() {
        document.querySelector(".mobile-navbar").classList.remove("mobile-navbar_active");
    });
});