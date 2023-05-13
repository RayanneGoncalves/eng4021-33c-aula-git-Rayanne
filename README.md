Linha de comando:
python na aba shell: Utilizado para poder fazer todas as operações que faria quando está no Python normal. 

import secrets: Utilizado para importar o módulo secrets do Python 

secrets.token_urlsafe(32): Gera um token (senha) para o uso em urls

python manage.py startapp appdaray: Cria uma pasta com o nome "appdaray" dentro do projeto Django

python manage.py makemigrations: Criar migrações com base em alterações feitas no modelos criados do projeto 

python manage.py migrate: Aplica as migrações pendentes e atualiza o banco de dados 

python manage.py createsuperuser: Usado para criar um usuário com acesso completo ao admin do django e pode criar, editar ou excluir objetos do banco de dados. 
A partir desse comando há a solicitação para preencher 3 questões:
Username: Um nome para poder entrar no admin do django
Email address: um email 
Password: uma senha para entrar no admin do django 

O comando python3 manage.py runserver 0.0.0.0:3000 inicia um servidor local para uma aplicação web Django na porta 3000. 
