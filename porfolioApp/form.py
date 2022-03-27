from django import forms

class FormularioContato(forms.Form):
    asunto = forms.CharField()
    email = forms.EmailField(max_length=100)
    mensaje= forms.CharField() 