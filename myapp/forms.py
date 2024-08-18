from django import forms
from .models import UserComments

class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComments
        fields = ['first_name', 'last_name', 'comment']