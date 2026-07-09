from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'note']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '* نام',
                'id': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': '* ایمیل',
                'dir': 'ltr',
                'id': 'email'
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'پیام شما',
                'id': 'note'
            }),
        }
