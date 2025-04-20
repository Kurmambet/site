from django import forms
from users.models import User
from django.contrib.auth.forms import AuthenticationForm



class UserLoginForm(AuthenticationForm):


    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ("username", "password")
    
    
    # non_field_errors в includes...

    # username = forms.CharField(label="Имя", 
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                                          'class':'form-control',
    #                                                          'placeholder':"Введите ваше имя пользователя"
    #                                                          }))
    # password = forms.CharField(label='Пароль',
    #                            widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                                              'class':'form-control',                                                          
    #                                                              'placeholder': "Введите ваш пароль"}),)






