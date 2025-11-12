from django.urls import path
from .views import (BlocosListCreate, BlocosRetrieverUpdateDestroy,
                    ApartamentosListCreate, ApartamentosRetriverUpdateDestroy,
                    ResidenteListCreate, ResidenteRetrieverUpdateDestroy)


urlpatterns = [
    path("blocos/", BlocosListCreate.as_view(), name="listar__criar_blocos"),
    path("blocos/<int:pk>", BlocosRetrieverUpdateDestroy.as_view(),
         name="visualizar_atualizar_deletar_bloco"),

    path("apartamentos/", ApartamentosListCreate.as_view(),
         name="listar__criar_apartamentos"),
    path("apartamentos/<int:pk>", ApartamentosRetriverUpdateDestroy.as_view(),
         name="visualizar_atualizar_deletar_apartamento"),

    path("residentes/", ResidenteListCreate.as_view(),
         name="listar__criar_residentes"),
    path("residentes/<int:pk>", ResidenteRetrieverUpdateDestroy.as_view(),
         name="visualizar_atualizar_deletar_residente"),

]
