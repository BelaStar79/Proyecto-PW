from django.shortcuts import render, redirect
from .forms import CustomerOpinionForm
from .models import Opinion

import re


def new_guest(request):
    return redirect('home/')


# Create your views here.
def home(request):
    msg = ''  # se usará para mostrar mensajes...
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        submit = request.POST['submission']

        # Expresión regular para validar un email
        patron = r'^[\w\.-]+@[a-zA-Z0-9\.-]+\.[a-zA-Z]{2,}$'

        if not username:
            msg += 'Por favor, introduzca un nombre o un alias'
        elif not re.match(patron, email):
            msg += 'Email inválido\n'
        elif not submit:
            msg += 'Por favor, escriba algo en la caja de la opinión...'
        else:
            # guardar los datos en la BD
            Opinion.objects.create(name=username, email=email, submission=submit)
    return render(request, 'index.html', {
        'form': CustomerOpinionForm(),
        'msg': msg
    })
