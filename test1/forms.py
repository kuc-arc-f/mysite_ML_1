from django.forms import ModelForm
from django import forms
from test1.models import Book, Impression


class MyForm(forms.Form):
    text = forms.CharField(max_length=100)
#
class BookForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Book
        fields = ('name', 'publisher', 'page', )


class ImpressionForm(ModelForm):
    """感想のフォーム"""
    class Meta:
        model = Impression
        fields = ('comment', )
