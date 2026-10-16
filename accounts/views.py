from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CadastroForm, LoginForm


class EntrarView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True


class CadastroView(CreateView):
    template_name = "accounts/cadastro.html"
    form_class = CadastroForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "Conta criada! Agora é só entrar.")
        return super().form_valid(form)
