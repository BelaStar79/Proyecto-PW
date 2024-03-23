from django.shortcuts import render

from .forms import UserRegistrationForm, UserLoginForm


# Create your views here.
def login_or_register(request):
    return render(request, 'login_and_register.html', {
        'form_register': UserRegistrationForm(),
        'form_login': UserLoginForm(),
        # 'messages': messages,
    })
