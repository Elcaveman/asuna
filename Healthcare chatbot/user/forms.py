from django import forms
from .models import Patient

class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.

    """
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={
        'class':"validate",
        'name':"",
        'placeholder':"Email",
        'autofocus': True
        }))
    password = forms.CharField(max_length=128,
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class':"validate",
            'placeholder':"Password",
            'autocomplete': 'current-password'}),
    )

class RegistrationForm(forms.ModelForm):
    # name = forms.CharField(max_length=150)
    # email = forms.EmailField(label="Email")
    # birthday = forms.DateTimeField()
    # weight = forms.DecimalField(max_value=300,min_value=1)
    
    # is_male = forms.BooleanField()
    # is_smoker = forms.BooleanField()
    # is_obese = forms.BooleanField()
    # is_pregnant = forms.BooleanField()

    class Meta:
        model = Patient
        fields = ('client_name', 'email', 'password')
