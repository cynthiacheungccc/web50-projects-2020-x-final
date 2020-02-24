from django import forms
from .models import Article
from django import forms

class ArticleForm(forms.ModelForm):

	body = forms.CharField(widget=forms.Textarea(
		attrs={
		'id':'bod',
		'rows':10, 'cols':150,
		'placeholder' :'Write an article...',
		}

		))
	class Meta:
		model = Article
		fields = ['title', 'body', 'pic']