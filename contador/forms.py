from django import forms

class formInput(forms.Form):
    userInput = forms.CharField(label='en que estas pensado?', max_length=120)