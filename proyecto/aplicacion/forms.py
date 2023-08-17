from django import forms

class empresaForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    nit = forms.IntegerField(required=True)
