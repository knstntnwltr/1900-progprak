from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=160)
    date = forms.CharField(max_length=30)
    percent = forms.IntegerField(max_value=100, min_value=0)
