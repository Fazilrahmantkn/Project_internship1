document.addEventListener("DOMContentLoaded", function(){

    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {

        card.addEventListener("mouseenter", () => {
            card.style.background = "#eef7ff";
        });

        card.addEventListener("mouseleave", () => {
            card.style.background = "white";
        });

    });

});