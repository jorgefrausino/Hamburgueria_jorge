from django.urls import path

from . import views

urlpatterns = [
    path("", views.HamburguerListView.as_view(), name="hamburguer_list"),
    path("novo/", views.HamburguerCreateView.as_view(), name="hamburguer_create"),
    path("<int:pk>/editar/", views.HamburguerUpdateView.as_view(), name="hamburguer_update"),
    path("<int:pk>/excluir/", views.HamburguerDeleteView.as_view(), name="hamburguer_delete"),
]
