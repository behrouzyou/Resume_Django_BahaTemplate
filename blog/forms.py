from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام *'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '* ایمیل', 'dir': 'ltr'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'پیام شما', 'rows': 5}),
        }

class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'جستجو ...'}))