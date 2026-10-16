# 🍔 Hamburgueria — Hackathon Django

CRUD de hambúrgueres (nome e descrição) com autenticação de usuário (cadastro, login e logout).

## Como rodar

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse http://127.0.0.1:8000/ — você será levado ao login. Clique em **Criar conta** para se cadastrar.


## Estrutura

- `accounts/` — cadastro, login e logout
- `crud/` — CRUD de hambúrgueres (todas as telas exigem login)
- `templates/` — base, login, cadastro e telas do CRUD (Bootstrap 5)
