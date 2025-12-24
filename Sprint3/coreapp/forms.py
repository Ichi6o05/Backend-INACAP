from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'telefono', 'mensaje', 'origen', 'curso', 'cc_ami']
        widgets = {
            'mensaje': forms.Textarea(),
            'telefono': forms.TextInput(),
            'cc_ami': forms.CheckboxInput(),
        }
        labels = {
            'curso': 'Curso de interés',
            'cc_ami': 'Reenviar a su correo?',
        }