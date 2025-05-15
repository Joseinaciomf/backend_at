// Variável para controlar se a lista de mangás está sendo exibida ou não
let mostrandoLista = false;

// Função para listar todos os mangás
async function listarMangas() {
    const ul = document.getElementById('manga-list');

    if (mostrandoLista) {
        ul.innerHTML = '';
        mostrandoLista = false;
        return;
    }

    const res = await fetch('/mangas/');
    const data = await res.json();
    ul.innerHTML = '';

    if (Array.isArray(data)) {
        data.forEach(m => {
            ul.innerHTML += `<li id="manga-${m.id}">
                <strong>ID: ${m.id}</strong> - ${m.titulo} - ${m.autor} (${m.volumes} volumes, R$ ${m.preco})
                <button onclick="deletarManga(${m.id})" class="bg-red-100 border border-red-400 hover:bg-red-200 text-red-800 font-semibold px-3 py-1 rounded">
    Excluir</button>
            </li>`;
        });
    } else {
        ul.innerHTML = `<li>${data.mensagem}</li>`;
    }

    mostrandoLista = true;
}

// Função para adicionar um novo mangá
async function adicionarManga() {
    const titulo = document.getElementById('titulo').value;
    const autor = document.getElementById('autor').value;
    const volumes = parseInt(document.getElementById('volumes').value);
    const preco = parseFloat(document.getElementById('preco').value);

    await fetch('/mangas/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ titulo, autor, volumes, preco })
    });

    listarMangas();
}

// Função para deletar um mangá com base no ID (sem recarregar toda a lista)
async function deletarManga(id) {
    await fetch(`/mangas/${id}/`, { method: 'DELETE' });
    const li = document.getElementById(`manga-${id}`);
    if (li) li.remove();
}

// Função para buscar um mangá por ID e exibir detalhes
async function buscarMangaPorId() {
    const id = document.getElementById('buscar-id').value;
    const div = document.getElementById('manga-detalhe');

    const res = await fetch(`/mangas/${id}/`);

    if (res.status === 404) {
        div.innerHTML = "Mangá não encontrado.";
    } else {
        const manga = await res.json();
        const dataFormatada = new Date(manga.atualizado_em).toLocaleString('pt-BR');

        div.innerHTML = `
            <div class="bg-white border border-gray-300 rounded p-4 shadow-sm mt-4">
                <h3 class="text-xl font-bold text-blue-600 mb-2">${manga.titulo}</h3>
                <p><strong>ID:</strong> ${manga.id}</p>
                <p><strong>Autor:</strong> ${manga.autor}</p>
                <p><strong>Volumes:</strong> ${manga.volumes}</p>
                <p><strong>Preço:</strong> R$ ${parseFloat(manga.preco).toFixed(2)}</p>
                <p class="text-sm text-gray-500 mt-2">Última atualização: ${dataFormatada}</p>
            </div>
        `;
    }
}


// Função para atualizar um mangá com base no ID
async function atualizarManga() {
    const id = parseInt(document.getElementById('id-atualizar').value);
    const titulo = document.getElementById('titulo-atualizar').value;
    const autor = document.getElementById('autor-atualizar').value;
    const volumes = document.getElementById('volumes-atualizar').value;
    const preco = document.getElementById('preco-atualizar').value;

    const dados = {};
    if (titulo !== '') dados.titulo = titulo;
    if (autor !== '') dados.autor = autor;
    if (volumes !== '') dados.volumes = parseInt(volumes);
    if (preco !== '') dados.preco = parseFloat(preco);

    await fetch(`/mangas/${id}/`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dados)
    });

    listarMangas();
}
