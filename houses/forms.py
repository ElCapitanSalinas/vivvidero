from django import forms
from .models import Apartamentos

CUSTOMERS =(
    (1, "Persona"),
    (2, "Empresa"),
)

TYPE =(
    (1, "Vendedor"),
    (2, "Comprador"),
    (3, "Remodelador"),
)

class NameForm(forms.Form):
    customer = forms.TypedChoiceField(choices = CUSTOMERS, coerce = int)
    type = forms.TypedChoiceField(choices = TYPE, coerce = int)
    fullname = forms.CharField(label='Name:', max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(label='Phone number:', max_length=100)

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()

class ImgForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Apartamentos
        fields = ('ktc',)