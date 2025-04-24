# Portfólio Django: 
Portfólio profissional desenvolvido com Django.

![image](https://github.com/user-attachments/assets/11829f45-6ca2-4fbd-8877-6737cadd9692)




## Funcionalidades

- Seção "Sobre Mim" com foto
- Listagem de projetos
- Design responsivo
- Painel administrativo
- Links de redirecionamento para as redes sociais

## Tecnologias

- Python 3.12
- Django 5.2
- Bootstrap 5
- PostgreSQL (opcional)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/portfolio-django.git
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Crie um superusuário:
```bash
python manage.py createsuperuser
```

6. Execute o servidor:
```bash
python manage.py runserver
```

## Configuração

Edite o arquivo `.env` com suas configurações:

```ini
SECRET_KEY=sua_chave_secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```
