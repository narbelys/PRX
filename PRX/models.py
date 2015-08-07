# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, m2m_changed
from django.core.files.storage import FileSystemStorage
from django.contrib.localflavor.us.forms import USPhoneNumberField

#from PIL import Image as img
import math


#FORMULARIOS
	
class ContactoForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'inputbox05 submit','placeholder':'Nombre y Apellido'}), max_length=150,)
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'inputbox05 submit','placeholder':'Correo Electrónico'}), max_length=150,)
	comentario = forms.CharField(widget=forms.Textarea(attrs={'class':'inputbox06','cols':'25', 'rows':'2','placeholder':'Comentarios'}), max_length=150,)

	
class ContactForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'inputbox05 submit','placeholder':'Name and Last name'}), max_length=150,)
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'inputbox05 submit','placeholder':'Email'}), max_length=150,)
	comentario = forms.CharField(widget=forms.Textarea(attrs={'class':'inputbox06','cols':'25', 'rows':'2','placeholder':'Comments'}), max_length=150,)

	
	
#from captcha.fields import ReCaptchaField
#from django.contrib.auth.forms import AuthenticationForm
#class MyAdminLoginForm(AuthenticationForm):
    #captcha = ReCaptchaField(attrs={'theme' : 'white'})
