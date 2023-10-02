from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:  
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais')  
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve ter mais de 6 caracteres')  
            return redirect('/usuarios/cadastro')
        
        try:
            # Username deve ser único!
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, 'Usuário salvo com sucesso!')  

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/usuarios/cadastro')


        return redirect('/usuarios/cadastro')