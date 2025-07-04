from django import forms
from .models import Review, Contact  

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'profession', 'message', 'photo', 'rating']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Write your review here...', 'class': 'form-control'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
