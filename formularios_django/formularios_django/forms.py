from tkinter.ttk import Label
from django import forms
from datetime import date

class CommentForm(forms.Form):
    name = forms.CharField(label="Escribe tu nombre", max_length=100, help_text="100 Caracteres máximo")
    url = forms.URLField(label="Tu sitio web", required=False, initial='http://')
    content = forms.CharField(label="Escribe al comentario")
    date = forms.DateField(label = "Fecha")

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre:",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(
        label="Email:", 
        max_length=50,
        widget=forms.EmailInput(attrs={'class': 'form-control'}))

    message = forms.CharField(
        label="Mensaje:",
        widget=forms.Textarea(attrs={'class': 'form-control'}))

    

