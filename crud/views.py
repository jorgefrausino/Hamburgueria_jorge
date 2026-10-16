from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import HamburguerForm
from .models import Hamburguer


class HamburguerListView(LoginRequiredMixin, ListView):  # READ
    model = Hamburguer
    context_object_name = "hamburgueres"


class HamburguerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):  # CREATE
    model = Hamburguer
    form_class = HamburguerForm
    success_url = reverse_lazy("hamburguer_list")
    success_message = "Hambúrguer cadastrado com sucesso!"
    extra_context = {"titulo": "Novo hambúrguer"}


class HamburguerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):  # UPDATE
    model = Hamburguer
    form_class = HamburguerForm
    success_url = reverse_lazy("hamburguer_list")
    success_message = "Hambúrguer atualizado com sucesso!"
    extra_context = {"titulo": "Editar hambúrguer"}


class HamburguerDeleteView(LoginRequiredMixin, DeleteView):  # DELETE
    model = Hamburguer
    success_url = reverse_lazy("hamburguer_list")

    def form_valid(self, form):
        messages.success(self.request, "Hambúrguer excluído com sucesso!")
        return super().form_valid(form)
