from tkinter.ttk import Label
from django import forms
from datetime import date

class CommentForm(forms.Form):
    name = forms.CharField(label="Escribe tu nombre", max_length=100, help_text="100 Caracteres máximo")
    url = forms.URLField(label="Tu sitio web", required=False, initial='http://')
    content = forms.CharField(label="Escribe al comentario")
    date = forms.DateField(label = "Fecha")

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre:", max_length=50)
    email = forms.EmailField(label="Email:", max_length=50)
    message = forms.CharField(label="Mensaje:")

