from django import forms
from django.contrib.auth.forms import AuthenticationForm
from auth_app import models as AuthAppModels

class LoginForm(AuthenticationForm):
    class Meta:
        model = AuthAppModels.User
        fields = ["username", "password"]

        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'input-group-text form-field'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-field'})