from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Manga
import json

# --- Página inicial de boas-vindas ---
def home(request):
    return HttpResponse(
        "<h1>Bem-vindo ao gerenciador de mangás!</h1>"
        "<p>Vá para <a href='/mangas/interface/'>/mangas/interface/</a> para usar a interface.</p>"
    )

# --- Interface HTML/JS ---
def pagina_mangas(request):
    return render(request, 'app/index.html')

# --- GET /mangas/ e POST /mangas/ ---
@csrf_exempt
def manga_list(request):
    if request.method == 'GET':
        # Busca todos os registros no banco
        mangas = list(Manga.objects.values())
        if not mangas:
            return JsonResponse({'mensagem': 'Nenhum mangá cadastrado.'})
        return JsonResponse(mangas, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        # Cria um novo objeto no banco
        manga = Manga.objects.create(
            titulo=data['titulo'],
            autor=data['autor'],
            volumes=data['volumes'],
            preco=data['preco']
        )
        # Retorna o objeto criado
        return JsonResponse({
            'id': manga.id,
            'titulo': manga.titulo,
            'autor': manga.autor,
            'volumes': manga.volumes,
            'preco': manga.preco
        }, status=201)

# --- GET/PUT/DELETE /mangas/<id>/ ---
@csrf_exempt
def manga_detail(request, id):
    try:
        manga = Manga.objects.get(pk=id)
    except Manga.DoesNotExist:
        return JsonResponse({'erro': 'Mangá não encontrado'}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            'id': manga.id,
            'titulo': manga.titulo,
            'autor': manga.autor,
            'volumes': manga.volumes,
            'preco': manga.preco,
            'atualizado_em': manga.atualizado_em.isoformat()
        })

    elif request.method == 'DELETE':
        manga.delete()
        return JsonResponse({'mensagem': 'Mangá removido'}, status=204)

    elif request.method == 'PUT':
        data = json.loads(request.body)

        titulo = data.get('titulo')
        autor = data.get('autor')
        volumes = data.get('volumes')
        preco = data.get('preco')

        # Só atualiza se vier algo não vazio ou None
        if titulo is not None and titulo.strip() != "":
            manga.titulo = titulo
        if autor is not None and autor.strip() != "":
            manga.autor = autor
        if volumes is not None:
            manga.volumes = volumes
        if preco is not None:
            manga.preco = preco

        manga.save()

        return JsonResponse({
            'id': manga.id,
            'titulo': manga.titulo,
            'autor': manga.autor,
            'volumes': manga.volumes,
            'preco': manga.preco
        })
