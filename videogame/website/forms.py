from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=60)
    last_name = forms.CharField(label="Nom", max_length=60)
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    email = forms.CharField(label="email", max_length=200)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

