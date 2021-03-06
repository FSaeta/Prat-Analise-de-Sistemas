from django.urls import path

from .views import *

urlpatterns = [
    path('avaliar/<str:tipo_item>/<int:item_id>', avaliar_item, name='avaliar_item'),
    path('usuario/<int:user_id>/', avaliacoes_usuario, name='avaliacoes_usuario'),
    path('<str:tipo_item>/<int:item_id>/', avaliacoes_item, name='avaliacoes_item'),
    path('<str:tipo_item>/<int:item_id>/<int:av_id>', avaliacao, name='avaliacao'),
]