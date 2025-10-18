document.addEventListener('DOMContentLoaded', () => {

    // --- Lógica para mostrar/esconder campo de valor do desconto ---

    const radiosDesconto = document.querySelectorAll('input[name="tem_desconto"]');
    const grupoValorDesconto = document.getElementById('desconto-valor-group');
    const inputValorDesconto = document.getElementById('desconto_valor');

    // Função para verificar qual radio está marcado e mostrar/esconder o campo
    function toggleValorDesconto() {
        const selecionado = document.querySelector('input[name="tem_desconto"]:checked').value;
        
        if (selecionado === 'sim') {
            grupoValorDesconto.style.display = 'block'; // Mostra o campo
            inputValorDesconto.required = true; // Torna obrigatório se "Sim"
        } else {
            grupoValorDesconto.style.display = 'none';  // Esconde o campo
            inputValorDesconto.required = false; // Não é obrigatório se "Não"
            inputValorDesconto.value = ''; // Limpa o valor se esconder
        }
    }

    // Adiciona o evento 'change' para cada botão de radio
    radiosDesconto.forEach(radio => {
        radio.addEventListener('change', toggleValorDesconto);
    });

    // Chama a função uma vez no início para garantir o estado correto
    toggleValorDesconto(); 


    // --- (Futuro) Lógica para adicionar produto (simulação) ---
    const productForm = document.getElementById('product-form');
    if (productForm) {
        productForm.addEventListener('submit', (e) => {
            e.preventDefault(); // Impede o envio real do formulário
            
            // Aqui você pegaria os valores dos campos:
            const nome = document.getElementById('nome').value;
            // ... pegar outros campos
            
            console.log('Produto a ser adicionado:', { nome }); 
            
            // Simulação de sucesso
            alert(`Produto "${nome}" adicionado com sucesso! (Simulação)`);
            productForm.reset(); // Limpa o formulário
            toggleValorDesconto(); // Garante que o campo de desconto volte ao estado inicial
            
            // No futuro, aqui você chamaria a função para atualizar a lista de produtos
            // fetchAndDisplayProducts(); 
        });
    }

});