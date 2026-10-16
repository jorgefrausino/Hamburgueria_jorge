from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import CadastroView, EntrarView

urlpatterns = [
    path("login/", EntrarView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("cadastro/", CadastroView.as_view(), name="cadastro"),
]
