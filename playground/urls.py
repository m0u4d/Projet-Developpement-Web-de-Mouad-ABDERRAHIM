from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_list, name='data_list'),
    path('equipe/<str:id_equipe>/', views.detail_equipe, name='detail_equipe'),
    path('stade/<str:id_stade>/', views.detail_stade, name='detail_stade'),
    path('create_equipe/', views.create_equipe, name='create_equipe'),
    path('create_stade/', views.create_stade, name='create_stade'),
    path('delete_stade/<str:id_stade>/', views.delete_stade, name='delete_stade'),
    path('delete_equipe/<str:id_equipe>/', views.delete_equipe, name='delete_equipe'),
    path('modify_equipe/<str:id_equipe>/', views.modify_equipe, name='modify_equipe'),
    path('modify_stade/<str:id_stade>/', views.modify_stade, name='modify_stade'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)