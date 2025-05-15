# 📚 Gerenciador de Mangás (AT1 - AT2 - AT3)

Este é um projeto de back-end em Django com integração front-end, desenvolvido ao longo de três etapas evolutivas. A aplicação tem como objetivo o gerenciamento de mangás em uma livraria fictícia, permitindo operações de listagem, cadastro, busca, atualização e remoção de registros.

## 🚀 Como rodar localmente

### 🔧 Requisitos
- Python 3.10+
- Git
- Django (recomendado instalar via ambiente virtual)
- Navegador moderno (para abrir a interface)

### 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/Joseinaciomf/backend_at.git
cd backend_at

# Crie e ative o ambiente virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Instale as dependências
pip install django

# Aplique as migrações do banco de dados
python manage.py migrate

# Rode o servidor local
python manage.py runserver

Acesse no navegador: http://127.0.0.1:8000
```

🗂️ Estrutura do Projeto:

app/views.py: lógica das rotas da API e renderização HTML

app/templates/app/index.html: interface HTML com Tailwind CSS

app/static/app/script.js: integração com a API via fetch

db.sqlite3: banco de dados SQLite gerado pelo Django


📌 Entidade: Mangá
Campos do modelo:
```bash
{
  "id": 1,
  "titulo": "One Piece",
  "autor": "Eiichiro Oda",
  "volumes": 105,
  "preco": 39.90,
  "atualizado_em": "2025-05-15T17:30:00"
}
```

🔄 Rotas REST implementadas:

| Método | Rota            | Descrição                           |
|--------|-----------------|-------------------------------------|
| GET    | /mangas/        | Lista todos os mangás               |
| GET    | /mangas/<id>/   |Retorna mangá específico por id      |
| POST   | /mangas/        | Adiciona novo mangá                 |
| PUT    | /mangas/<id>/   | Atualiza dados do mangá             |
| DELETE | /mangas/<id>/   | Remove mangá do sistema             |



🧠 Evolução por Atividade

- **AT1 – API REST + Front-end básico**
  - Implementação das rotas `GET`, `POST` e `DELETE`
  - Dados armazenados apenas em memória
  - Front-end HTML + JS consumindo a API com `fetch()`

- **AT2 – CRUD com persistência em JSON**
  - Persistência dos dados no arquivo `mangas.json`
  - Implementado método `PUT`
  - Validação parcial de campos
  - Melhorias visuais e comportamentais na interface

- **AT3 – CRUD com banco de dados relacional (SQLite)**
  - Uso do Django ORM com modelo `Manga`
  - Migração dos dados para banco SQLite (`db.sqlite3`)
  - Campo `atualizado_em` adicionado automaticamente
  - Estilização da interface com Tailwind CSS
  - Cartões com informações detalhadas ao buscar por ID
  - Exibição do ID na listagem
  - Correções no comportamento do botão de exclusão (sem recarregar lista)


🖼️ Funcionalidades da Interface
| Função         | Implementado? | Observação                                                    |
|----------------|---------------|--------------------------------------------------------------|
| Listar         | ✅             | Alternância mostrar/ocultar, com ID visível                   |
| Adicionar      | ✅             | Via formulário com `fetch POST`                              |
| Buscar por ID  | ✅             | Exibe cartão detalhado com data de atualização                |
| Atualizar (PUT)| ✅             | Atualização parcial (mantém valores anteriores se não preenchido) |
| Remover        | ✅             | Botão com destaque em vermelho, lista continua aberta         |


📌 Considerações Finais

- O projeto foi desenvolvido de forma incremental ao longo de três atividades (AT1, AT2, AT3), com evolução contínua nas funcionalidades e na persistência dos dados.

- A aplicação iniciou com dados em memória (AT1), passou para persistência em arquivo JSON (AT2) e evoluiu para persistência em banco de dados relacional SQLite com o uso do Django ORM (AT3).

- A interface HTML foi aprimorada progressivamente, até receber uma versão estilizada com Tailwind CSS, melhorando a usabilidade e visual do sistema.

- Foram aplicadas boas práticas de organização de código e separação entre front-end e back-end, utilizando JavaScript puro para a comunicação com a API REST.

- O projeto possui suporte completo para as operações CRUD (Create, Read, Update, Delete), permitindo inclusive atualizações parciais de campos e exibição detalhada por ID.

- O repositório Git mantém um histórico limpo com branches separados para as versões de cada atividade (`main` com AT3, `at2` com AT2), facilitando a rastreabilidade do progresso do sistema.

- O projeto pode ser facilmente executado localmente por qualquer desenvolvedor, conforme descrito nas instruções do `README.md`.




💡 Dica
Você pode alternar entre as versões das atividades pelas branches (nas duas versões possui o commit da AT1):

main: versão final com banco de dados (AT3)

at2: versão com persistência em JSON (AT2)
