from django import forms

class ItemForm(forms.Form):
    quantity = forms.IntegerField(min_value=0)
