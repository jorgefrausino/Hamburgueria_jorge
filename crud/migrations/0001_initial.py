from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hamburguer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                ("descricao", models.TextField(verbose_name="Descrição")),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Hambúrguer",
                "verbose_name_plural": "Hambúrgueres",
                "ordering": ["nome"],
            },
        ),
    ]
