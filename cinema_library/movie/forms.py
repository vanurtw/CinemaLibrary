from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):

    text = forms.CharField(label='Ваш комментарий*', widget=forms.Textarea(attrs={'class': 'form-control border'}))
    name = forms.CharField(label='Имя*', widget=forms.TextInput(attrs={'class': 'form-control border'}))
    email = forms.EmailField(label='Email*', widget=forms.EmailInput(attrs={'class': 'form-control border'}))

    class Meta:
        model = Reviews
        fields = ['name', 'email', 'rating', 'text']
