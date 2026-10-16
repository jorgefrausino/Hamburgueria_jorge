from django import forms

from .models import Hamburguer


class HamburguerForm(forms.ModelForm):
    class Meta:
        model = Hamburguer
        fields = ["nome", "descricao"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex.: X-Bacon"}),
            "descricao": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "placeholder": "Ex.: Pão brioche, blend 180g, bacon crocante e cheddar"}
            ),
        }
