from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django_recaptcha.fields import ReCaptchaField


class NoticiaForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Noticia
        #fields = ['rut','nombre','apellido']
        fields = '__all__'
        

class NoticiaClienteForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Noticia
        #fields = ['rut','nombre','apellido']
        fields = ['titulo','contenido','fecha','ciudad','imagen','nombre_periodista','tipo','comentario']

class NoticiasoladdForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Noticia
        #fields = ['rut','nombre','apellido']
        fields = ['titulo','contenido','fecha','ciudad','imagen','nombre_periodista','tipo']



class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class PeriodistaForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Periodista
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']