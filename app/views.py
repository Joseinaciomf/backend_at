from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import os

# 🗂 Define o caminho absoluto até o arquivo JSON onde os dados serão armazenados
DATA_FILE = os.path.join(os.path.dirname(__file__), 'mangas.json')

# 📖 Função para ler os dados do arquivo JSON
def ler_dados():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)  # Converte o conteúdo do arquivo em lista Python
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Retorna lista vazia se o arquivo não existir ou estiver inválido

# 💾 Função para salvar os dados no arquivo JSON
def salvar_dados(mangas):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(mangas, f, indent=4, ensure_ascii=False)  # Escreve os dados com formatação

# 🏠 View da página inicial — exibe uma mensagem simples com link para a interface
def home(request):
    return HttpResponse(
        "<h1>Bem-vindo ao gerenciador de mangás!</h1>"
        "<p>Vá para <a href='/mangas/interface/'>/mangas/interface/</a> para acessar a interface.</p>"
    )

# 🌐 View para renderizar o HTML da interface gráfica
def pagina_mangas(request):
    return render(request, 'app/index.html')  # Carrega o template HTML

# 📥📤 View para lidar com a lista de mangás
# - GET: retorna todos os mangás cadastrados
# - POST: adiciona um novo mangá
@csrf_exempt
def manga_list(request):
    mangas = ler_dados()  # Carrega a lista atual de mangás

    if request.method == 'GET':
        if not mangas:
            return JsonResponse({"mensagem": "Nenhum mangá cadastrado."})
        return JsonResponse(mangas, safe=False)  # safe=False permite retornar listas

    elif request.method == 'POST':
        data = json.loads(request.body)  # Converte o JSON da requisição para dicionário

        # Gera um novo ID sequencial
        novo_id = max([m["id"] for m in mangas], default=0) + 1

        # Cria o novo objeto mangá
        novo = {
            "id": novo_id,
            "titulo": data["titulo"],
            "autor": data["autor"],
            "volumes": data["volumes"],
            "status": data.get("status", "Disponível"),  # Pode ser removido no futuro
            "preco": data["preco"]
        }

        mangas.append(novo)           # Adiciona à lista
        salvar_dados(mangas)          # Salva a nova lista no JSON
        return JsonResponse(novo, status=201)  # Retorna o novo mangá criado

# 🔍📝❌ View para detalhes de um mangá específico
# - GET: retorna os dados do mangá pelo ID
# - PUT: atualiza os dados
# - DELETE: remove o mangá
@csrf_exempt
def manga_detail(request, id):
    mangas = ler_dados()
    manga = next((m for m in mangas if m["id"] == id), None)  # Busca o mangá pelo ID

    if not manga:
        return JsonResponse({'erro': 'Mangá não encontrado'}, status=404)

    if request.method == 'GET':
        return JsonResponse(manga)  # Retorna o mangá encontrado

    elif request.method == 'DELETE':
        mangas = [m for m in mangas if m["id"] != id]  # Remove o mangá da lista
        salvar_dados(mangas)                           # Salva a nova lista
        return JsonResponse({'mensagem': 'Mangá removido'}, status=204)

    elif request.method == 'PUT':
        data = json.loads(request.body)  # Converte JSON do corpo da requisição

        # Atualiza os dados do mangá encontrado
        for i in range(len(mangas)):
            if mangas[i]["id"] == id:
                mangas[i].update({
                    "titulo": data.get("titulo", mangas[i]["titulo"]),
                    "autor": data.get("autor", mangas[i]["autor"]),
                    "volumes": data.get("volumes", mangas[i]["volumes"]),
                    "status": data.get("status", mangas[i]["status"]),
                    "preco": data.get("preco", mangas[i]["preco"]),
                })
                salvar_dados(mangas)  # Salva as alterações no JSON
                return JsonResponse(mangas[i], status=200)

        return JsonResponse({'erro': 'Erro ao atualizar'}, status=400)
