document.addEventListener("DOMContentLoaded", () => {
    // Animasi fade-in kartu
    const cards = document.querySelectorAll(".book-card");
    cards.forEach((card, i) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(10px)";
        card.style.transition = "opacity 0.4s, transform 0.4s";
        setTimeout(() => {
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, i * 40);
    });

    // Auto-hide flash message
    document.querySelectorAll(".flash").forEach((el) => {
        setTimeout(() => {
            el.style.transition = "opacity 0.5s";
            el.style.opacity = "0";
            setTimeout(() => el.remove(), 500);
        }, 4000);
    });

    // Fitur Scroll to Top
    const topBtn = document.createElement("button");
    topBtn.innerHTML = "↑";
    topBtn.style.cssText = `
        position: fixed; bottom: 30px; right: 30px; z-index: 999;
        width: 50px; height: 50px; border-radius: 50%;
        background: var(--accent); color: white; border: none;
        font-size: 1.5rem; cursor: pointer; display: none;
        box-shadow: 0 4px 15px rgba(124, 92, 255, 0.4);
        transition: opacity 0.3s, transform 0.3s;
    `;
    document.body.appendChild(topBtn);

    window.addEventListener("scroll", () => {
        if (window.scrollY > 300) {
            topBtn.style.display = "block";
        } else {
            topBtn.style.display = "none";
        }
    });

    topBtn.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
});