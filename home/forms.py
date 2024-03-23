from django import forms


class CustomerOpinionForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nombre o alias',
                'name': 'nombre',
                'class': 'campo'
            }),
        label='',
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Correo electrónico',
                'name': 'correo',
                'class': 'campo'
            }),
        label='',
        required=True
    )
    submission = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': "Agredeceríamos tus palabras"
            }),
        label='',
        required=True
    )
