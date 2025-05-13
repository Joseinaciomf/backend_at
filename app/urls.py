from django.urls import path
from .views import home, pagina_mangas, manga_list, manga_detail

urlpatterns = [
    path('', home, name='home'),                             # "/" → boas-vindas
    path('mangas/interface/', pagina_mangas, name='interface'),  # HTML+JS
    path('mangas/', manga_list, name='manga-list'),          # API GET/POST
    path('mangas/<int:id>/', manga_detail, name='manga-detail'), # API GET/DELETE
]
