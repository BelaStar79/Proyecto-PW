from django.shortcuts import render, redirect

from .forms import CustomerOpinionForm
from .models import Opinion

from re import match


def new_guest(request):
    return redirect('home')


# Create your views here.
def home(request):
    messages = ''  # se usará para mostrar mensajes...
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        submit = request.POST['submission']
        # Expresión regular para validar un email
        email_pattern = r'^[\w\.-]+@[a-zA-Z0-9\.-]+\.[a-zA-Z]{2,}$'
        if not username or not email or not submit:  # validar que los campos están llenos...
            messages += '- Rellene todos los campos'
        elif not match(email_pattern, email):  # validar email usando expresión regular
            messages += '- Email inválido'

        else:
            # guardar los datos en la BD
            Opinion.objects.create(name=username, email=email, submission=submit)
    return render(request, 'index.html', {
        'form': CustomerOpinionForm(),
        'messages': messages,
    })
