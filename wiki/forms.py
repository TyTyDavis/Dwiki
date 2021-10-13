from django import forms
from models import Article, Comment

class ArticleForm(ModelForm):
    text = forms.CharField(widget=forms.TextArea, label='Entry')
    class Meta:
        model = Article
        exclude = ['updated_on','created_on']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['article','created_on']
