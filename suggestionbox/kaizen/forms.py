from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea, max_length=1000, label='Leave a Comment')
    idea_id = forms.IntegerField(widget=forms.HiddenInput)
