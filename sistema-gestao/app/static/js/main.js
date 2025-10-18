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

    // --- Lógica do Botão Pegar Cupom (ATUALIZADA) ---
    const btnPegarCupom = document.getElementById('btn-pegar-cupom');

    // Verifica se o botão existe nesta página (index.html)
    if (btnPegarCupom) {
        // Define o código do cupom aqui
        const codigoCupom = "MAGA20OFF"; // Exemplo de código

        btnPegarCupom.addEventListener('click', () => {
            // Tenta copiar o código para a área de transferência
            navigator.clipboard.writeText(codigoCupom).then(() => {
                // Sucesso na cópia!
                
                // 1. Mostra a mensagem de sucesso com o código
                alert(`Cupom "${codigoCupom}" copiado para a área de transferência! Use no checkout.`); 
                
                // 2. Muda o texto do botão
                btnPegarCupom.textContent = 'Cupom Copiado!';
                
                // 3. Desabilita o botão
                btnPegarCupom.disabled = true;
                
                // 4. Adiciona uma classe para mudar o estilo via CSS
                btnPegarCupom.classList.add('cupom-pego');

            }).catch(err => {
                // Erro ao copiar (navegador pode não suportar ou permissão negada)
                console.error('Erro ao copiar cupom: ', err);
                // Mostra mensagem alternativa sem confirmar a cópia
                 alert(`Seu cupom é: ${codigoCupom}. Use no checkout.`); 
                 // Mesmo assim, atualiza o botão
                 btnPegarCupom.textContent = 'Use o Cupom!';
                 btnPegarCupom.disabled = true;
                 btnPegarCupom.classList.add('cupom-pego'); // Ainda aplica o estilo
            });
        });
    }

}); // Fim do addEventListener 'DOMContentLoaded'