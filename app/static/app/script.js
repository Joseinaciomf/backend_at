let mostrandoLista = false;

async function listarMangas() {
    const ul = document.getElementById('manga-list');

    if (mostrandoLista) {
        ul.innerHTML = '';  // limpa a lista
        mostrandoLista = false;
        return;
    }

    const res = await fetch('/mangas/');
    const data = await res.json();
    ul.innerHTML = '';

    if (Array.isArray(data)) {
        data.forEach(m => {
            ul.innerHTML += `<li>
                <strong>${m.titulo}</strong> - ${m.autor} (${m.volumes} volumes, R$ ${m.preco})
                <button onclick="deletarManga(${m.id})">Excluir</button>
            </li>`;
        });
    } else {
        ul.innerHTML = `<li>${data.mensagem}</li>`;
    }

    mostrandoLista = true;
}


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

async function deletarManga(id) {
    await fetch(`/mangas/${id}/`, { method: 'DELETE' });
    listarMangas();
}

async function buscarMangaPorId() {
    const id = document.getElementById('buscar-id').value;
    const div = document.getElementById('manga-detalhe');

    const res = await fetch(`/mangas/${id}/`);
    if (res.status === 404) {
        div.innerHTML = "Mangá não encontrado.";
    } else {
        const manga = await res.json();
        div.innerHTML = `
            <p><strong>${manga.titulo}</strong><br>
            Autor: ${manga.autor}<br>
            Volumes: ${manga.volumes}<br>
            Status: ${manga.status}<br>
            Preço: R$ ${manga.preco}</p>
        `;
    }
}
