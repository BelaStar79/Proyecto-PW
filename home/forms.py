from django import forms


class CustomerOpinionForm(forms.Form):
    name = forms.CharField(label='Nombre o alias', max_length=100, required=True)
    email = forms.EmailField(label='Correo electrónico', required=True)
    submission = forms.CharField(label='Agradecemos su opinión', widget=forms.Textarea)
