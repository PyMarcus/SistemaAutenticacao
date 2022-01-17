from django.shortcuts import render, redirect  # render para renderizar os arquivos estáticos, ou seja, rodá-los
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages, auth


# Create your views here.
# funções que serão chamadas em urls.py
def cadastro(request):
    # funcao recebe requisicao do usuario e devolve uma resposta
    if request.method == "GET":
        print('oj')

        # recebe a pág ao informar a url
        return render(request, 'cadastro.html')  # renderiza a pagina pegando a request e especificando o caminho
    elif request.method == "POST":
        # envia informações para o site
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        print(email)
        # validações para testar os métodos:
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            return redirect('/auth/cadastro')  # redireciona a página caso nao seja digitado nada
        # verificar se o usuario ja foi cadastrado:
        user = User.objects.filter(username=username)
        if user.exists():  # se existir, nao permite cadastro
            return redirect('/auth/cadastro')
        else:
            # cadastra bi data base
            try:
                user = User(username=username, email=email, password=senha)
                user.save()  # salva no database
                return redirect('/auth/logar')
            except:
                return redirect('/auth/cadastro')


def logar(request):
    # loga no sistema
    if request.method == "GET":
        return render(request, 'logar.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        usuario = auth.authenticate(username=username, password=senha)
        print(username)
        if not usuario:
            return render(request, 'cadastro.html')
        else:
            print(username, senha)
            auth.login(request, usuario)
            return redirect('/')


def sair(request):
    # faz logout do site
    auth.logout(request)
    return render(request, 'logar.html')
