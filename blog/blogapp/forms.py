from django import forms

class CommentForm(forms.Form):
    name = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
