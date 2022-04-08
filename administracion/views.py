from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def index_principal(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)  #verifico el Usuario Logeado y lo envio
    return render(request, 'panel_usuario/main.html', {'user': usuario})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #return render(request, 'panel_usuario/main.html',
                #              {'usuario': user, })
                url = reverse('index', kwargs={'id_usuario': user.id})
                return HttpResponseRedirect(url)
    else:
        form = AuthenticationForm()
    return render(request, 'login/index.html', {'form': form})
