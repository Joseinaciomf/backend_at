// Variável para controlar se a lista de mangás está sendo exibida ou não
let mostrandoLista = false;

// Função para listar todos os mangás
async function listarMangas() {
    const ul = document.getElementById('manga-list'); // Seleciona a <ul> onde os mangás serão listados

    // Se já estiver mostrando, limpa a lista e oculta
    if (mostrandoLista) {
        ul.innerHTML = '';
        mostrandoLista = false;
        return;
    }

    // Requisição GET para obter todos os mangás
    const res = await fetch('/mangas/');
    const data = await res.json(); // Converte a resposta para JSON
    ul.innerHTML = ''; // Limpa o conteúdo da lista antes de exibir

    // Se houver mangás, cria elementos <li> com os dados
    if (Array.isArray(data)) {
        data.forEach(m => {
            ul.innerHTML += `<li>
                <strong>${m.titulo}</strong> - ${m.autor} (${m.volumes} volumes, R$ ${m.preco})
                <button onclick="deletarManga(${m.id})">Excluir</button>
            </li>`;
        });
    } else {
        // Caso não haja mangás cadastrados, exibe a mensagem retornada
        ul.innerHTML = `<li>${data.mensagem}</li>`;
    }

    mostrandoLista = true; // Marca que a lista está visível
}

// Função para adicionar um novo mangá
async function adicionarManga() {
    // Coleta os valores digitados nos inputs
    const titulo = document.getElementById('titulo').value;
    const autor = document.getElementById('autor').value;
    const volumes = parseInt(document.getElementById('volumes').value);
    const preco = parseFloat(document.getElementById('preco').value);

    // Envia os dados via POST para a API
    await fetch('/mangas/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ titulo, autor, volumes, preco })
    });

    listarMangas(); // Atualiza a lista após cadastrar
}

// Função para deletar um mangá com base no ID
async function deletarManga(id) {
    await fetch(`/mangas/${id}/`, { method: 'DELETE' }); // Requisição DELETE
    listarMangas(); // Atualiza a lista após exclusão
}

// Função para buscar um mangá por ID e exibir detalhes
async function buscarMangaPorId() {
    const id = document.getElementById('buscar-id').value; // Pega o ID digitado
    const div = document.getElementById('manga-detalhe'); // Elemento onde será exibido o resultado

    const res = await fetch(`/mangas/${id}/`);
    
    // Se o mangá não for encontrado, mostra aviso
    if (res.status === 404) {
        div.innerHTML = "Mangá não encontrado.";
    } else {
        // Exibe os dados formatados
        const manga = await res.json();
        div.innerHTML = `
            <p><strong>${manga.titulo}</strong><br>
            Autor: ${manga.autor}<br>
            Volumes: ${manga.volumes}<br>
            Preço: R$ ${manga.preco}</p>
        `;
    }
}

// Função para atualizar um mangá com base no ID
async function atualizarManga() {
    // Coleta o ID e os novos valores dos campos
    const id = parseInt(document.getElementById('id-atualizar').value);
    const titulo = document.getElementById('titulo-atualizar').value;
    const autor = document.getElementById('autor-atualizar').value;
    const volumes = parseInt(document.getElementById('volumes-atualizar').value);
    const preco = parseFloat(document.getElementById('preco-atualizar').value);

    // Monta o objeto com os dados a serem atualizados
    const dados = {
        titulo,
        autor,
        volumes,
        preco
    };

    // Envia os dados atualizados via PUT
    await fetch(`/mangas/${id}/`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados)
    });

    listarMangas(); // Atualiza a lista após a alteração
}
