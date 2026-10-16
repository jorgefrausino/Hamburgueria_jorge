from django.urls import include, path

urlpatterns = [
    path("contas/", include("accounts.urls")),
    path("", include("crud.urls")),
]
