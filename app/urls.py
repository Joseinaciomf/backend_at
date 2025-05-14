from django.urls import path
from .views import home, pagina_mangas, manga_list, manga_detail

urlpatterns = [
    path('', home, name='home'),
    path('mangas/interface/', pagina_mangas, name='mangas-interface'),
    path('mangas/', manga_list, name='manga-list'),
    path('mangas/<int:id>/', manga_detail, name='manga-detail'),
]
