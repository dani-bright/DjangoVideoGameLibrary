from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

class RegisterForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=60, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(label="Nom", max_length=60, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(label="Nom d'utilisateur", max_length=30, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(label="email", max_length=200, widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class' : 'form-control'}))


