from django import forms
from .models import Comments
# Creating form class
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name','email', 'body',)