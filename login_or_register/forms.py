from django import forms


class UserRegistrationForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nombre completo',
                'name': 'nombre',
            }),
        label='',
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                'name': 'correo',
            }),
        label='',
        required=True
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Usuario',
                'name': 'usuario',
            }),
        label='',
        required=True
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'name': 'contrasena',
            }),
        label='',
        required=True
    )


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Usuario',
                'name': 'usuario',
            }),
        label='',
        required=True
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'name': 'contrasena',
            }),
        label='',
        required=True
    )
    # FIXME: el checkbox no se está mostrando correctamente
    employee = forms.BooleanField(
        label='Empleado',
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'name': 'empleado',
                'class': 'checkbox',
                'id': 'empleado',
            }
        )
    )
