from django.urls import path
from . import views

urlpatterns = [
    path('makeup-artists/', views.makeup_artist_list, name='makeup_artist_list'),
   path('makeup_artist/<int:artist_id>/', views.makeup_artist_details, name='makeup_artist_details'),
    path('Dj/', views.Djs_list, name='Djs_list'), 
   path('dj_details/<int:dj_id>/', views.dj_details, name='Djs_detail'),
    path('Traiteur/', views.caterer_list, name='Traiteur_list'), 
   path('Traiteur_detail/<int:caterer_id>/', views.caterer_details, name='Traiteur_detail'),
   path('dada')
]