from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

# 1) Página inicial de boas-vindas
def home(request):
    return HttpResponse(
        "<h1>Bem-vindos ao gerenciador de mangás!</h1>"
        "<p>Vá para <a href='/mangas/interface/'>/mangas/interface/</a> "
        "para abrir a interface completa.</p>"
    )

# 2) Página HTML+JS de interface
def pagina_mangas(request):
    return render(request, 'app/index.html')

# 3) API REST — lista e cria
mangas = []
next_id = 1

@csrf_exempt
def manga_list(request):
    global mangas, next_id

    if request.method == 'GET':
        if not mangas:
            return JsonResponse({"mensagem": "Nenhum mangá cadastrado."})
        return JsonResponse(mangas, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        novo = {
            "id": next_id,
            "titulo": data["titulo"],
            "autor": data["autor"],
            "volumes": data["volumes"],
            "status": data.get("status", "Disponível"),
            "preco": data["preco"]
        }
        mangas.append(novo)
        next_id += 1
        return JsonResponse(novo, status=201)

# 4) API REST — detalhes e delete
@csrf_exempt
def manga_detail(request, id):
    global mangas

    manga = next((m for m in mangas if m["id"] == id), None)
    if not manga:
        return JsonResponse({'erro': 'Mangá não encontrado'}, status=404)

    if request.method == 'GET':
        return JsonResponse(manga)

    elif request.method == 'DELETE':
        mangas = [m for m in mangas if m["id"] != id]
        return JsonResponse({'mensagem': 'Mangá removido'}, status=204)
