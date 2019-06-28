from django import forms
from .models import Comment


class SharePostForm(forms.Form):
    name=forms.CharField(max_length=50)
    fro=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(widget=forms.Textarea,required=False)

class NewCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','body']

class SearchPostForm(forms.Form):
    keyword=forms.CharField(max_length=50)        
