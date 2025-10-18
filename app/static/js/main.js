// Ativa todos os ícones da biblioteca Feather Icons na página
feather.replace();


// --- Lógica do Menu Hamburger ---
document.addEventListener('DOMContentLoaded', () => {

    const menuToggle = document.getElementById('menu-toggle');
    const navLinks = document.getElementById('nav-links');

    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('nav-open');
        });
    }

    // --- LÓGICA DO BOTÃO PEGAR CUPOM FOI REMOVIDA DAQUI ---

}); // Fim do addEventListener 'DOMContentLoaded'