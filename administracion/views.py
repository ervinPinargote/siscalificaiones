from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from administracion.forms import CalificarParametrosCandidatasForm
from administracion.models import usuario_calificador, candidatas, parametros_certamen, calificacion_parametros, \
    metricas_parametros


def index_principal(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)  # verifico el Usuario Logeado y lo envio

    try:
        usuario_certamen = usuario_calificador.objects.get(id_usuario=id_usuario)
        candidata = candidatas.objects.all().filter(id_certamen=usuario_certamen.id_certamen)
    except usuario_calificador.DoesNotExist:
        usuario_certamen = None

    if usuario_certamen is None:
        return render(request, 'panel_usuario/notmain.html', {'user': usuario})
    else:
        return render(request, 'panel_usuario/main.html', {'user': usuario_certamen, 'partic': candidata})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # return render(request, 'panel_usuario/main.html',
                #              {'usuario': user, })
                url = reverse('index', kwargs={'id_usuario': user.id})
                return HttpResponseRedirect(url)
    else:
        form = AuthenticationForm()
    return render(request, 'login/index.html', {'form': form})


def calificacion_parametros_candidata(request, id_candidata):
    user = User.objects.get(username=request.user)  # usuario_Logeadoo
    candidata = candidatas.objects.get(id=id_candidata)  # obtenemos la Candidata
    parametros = parametros_certamen.objects.all().filter(id_certamen=candidata.id_certamen.id)  # Parametros para FORM

    #parmetros_calificados = calificacion_parametros.objects.all()  # todos los parametros ya calificados
    ck=id_candidata
    metricas = metricas_parametros.objects.all().filter(idparametrof=3)

    if request.method == 'POST':
        form = CalificarParametrosCandidatasForm(request.POST)
        if form.is_valid():
            if form.save():
                mensaje = "Guardado con exito"
            return JsonResponse({'content': {'message': mensaje, 'color': '1', }})
        else:
            return JsonResponse({'content': {'message': "Error al Guardar", 'color': '0', }})
    else:
        form = CalificarParametrosCandidatasForm()
        contexto = {'message': 'Guardado con Exito',
                    'user': user,
                    'candidata': candidata,
                    'parametros': parametros,
                    'form': form,
                    'metricas':metricas,
                    }
    return render(request, 'panel_usuario/calificarparametro.html', contexto)
