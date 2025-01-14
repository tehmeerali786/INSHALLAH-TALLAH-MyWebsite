from django import forms
from django.forms import MultiWidget, Textarea, TextInput
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(help_text="A valid email address, please.", required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'contactus'}))
    content = forms.CharField(widget=Textarea(attrs={'placeholder': 'Message', 'class': 'textarea'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise forms.ValidationError("Invalid email")
        return email
