from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from chat.models import Mensajes
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contasena', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma contasena', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {k:''  for k in fields}

class MessagesForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2,
                                                                    'placeholder':'Escribe tu mensaje',
                                                                }))
    class Meta:
        model = Mensajes
        fields = ('content',)
    
