# -*- encoding: utf-8 -*-
import string
import json

# Django libs
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.db.models import Q, Count, Sum
from django.http import HttpResponse, Http404
from django.utils import simplejson
from django.core import serializers
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

# Forms (models)
from PRX.models import ContactoForm, ContactForm
import smtplib
from email.mime.multipart import MIMEMultipart
from django.core.mail import EmailMessage
from django.core import mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from email.MIMEText import MIMEText


# HOME
def idioma(request):	
	return render_to_response('idioma.html', {}, context_instance=RequestContext(request))
	
	
def index(request):   
	contacto = ContactoForm()
	#user = request.user
	if request.method == 'POST':
		#print "ESPANIOL"
		#return render_to_response('espaniol/contacto_done.html', RequestContext(request))
		contacto = ContactoForm(request.POST)
		if contacto.is_valid():
			#if user.is_authenticated():
				#contacto = ContactoForm(initial={'nombre':user.get_full_name,'email':user.email})
			#else:
			contacto = ContactoForm()
			
			nombre = request.POST.get('nombre',None)
			email = request.POST.get('email',None)
			comentario = request.POST.get('comentario',None)
			combinado = 'Mensaje de Contacto \r\n\r\nNombre: '+nombre+' \r\n'+'Email: '+email+' \r\n'+'Comentario: '+comentario
			msg = MIMEText(combinado.encode('utf-8'), 'plain', 'UTF-8')
			#msg['From']= nombre
			#msg['MIME-Version']="1.0"
			Subject="Mensaje de Contacto - "+nombre+" - "+email
			#msg['Content-Type'] = "text/html; charset=utf-8"
			#msg['Content-Transfer-Encoding'] = "quoted-printable"
			#msg['Reply-To'] = email
			#msg = 'From: '+nombre+' <'+email+'>\r\nTo: miguelmiguel19@gmail.com\r\n\r\n'+comentario
			if nombre and email and comentario:
				try:
					#send_mail('(Comentario) PCA-Audit', nombre+' <'+email+'>. Comentario: '+comentario, email,['miguel.ambrosio@pcaaudit.com'], fail_silently=False)
					conexion = mail.get_connection()
					conexion.password = settings.ALT_EMAIL_HOST_PASSWORD
					conexion.username = settings.ALT_EMAIL_HOST_USER
					conexion.host = settings.ALT_EMAIL_HOST
					conexion.port = settings.EMAIL_PORT	
					conexion.use_tls = settings.EMAIL_USE_TLS
					conexion.open()

					#\"url\": \"https://pcafarma.com\" Si se quiere agregar landing page poner esto dentro del settings del header
					correo = EmailMessage(Subject, combinado, 'contacto@prxcontrolsolutions.com', ['contacto@prxcontrolsolutions.com'], connection=conexion )

					correo.send()
					conexion.close()
	
	
	
					#server = smtplib.SMTP_SSL('smtp.gmail.com',465)
					#server.login('info@pcaaudit.com', 'prxinfo2012')
					#server.sendmail(email,['contacto@prxcontrolsolution.com'], str(msg))
					#server.quit()
					print "holaaaaa"
					return render_to_response('espaniol/contacto_done.html', RequestContext(request))
				except (smtplib.SMTPAuthenticationError):#BadHeaderError:
					print 'Error de header'

	return render_to_response('espaniol/home.html', { 'contacto':contacto }, context_instance=RequestContext(request))
	
def quienesSomos(request):	
	contacto = ContactoForm()
	#user = request.user
	if request.method == 'POST':
		#print "ESPANIOL"
		#return render_to_response('espaniol/contacto_done.html', RequestContext(request))
		contacto = ContactoForm(request.POST)
		if contacto.is_valid():
			#if user.is_authenticated():
				#contacto = ContactoForm(initial={'nombre':user.get_full_name,'email':user.email})
			#else:
			contacto = ContactoForm()
			
			nombre = request.POST.get('nombre',None)
			email = request.POST.get('email',None)
			comentario = request.POST.get('comentario',None)
			combinado = 'Mensaje de Contacto \r\n\r\nNombre: '+nombre+' \r\n'+'Email: '+email+' \r\n'+'Comentario: '+comentario
			msg = MIMEText(combinado.encode('utf-8'), 'plain', 'UTF-8')
			#msg['From']= nombre
			#msg['MIME-Version']="1.0"
			Subject="Mensaje de Contacto - "+nombre+" - "+email
			#msg['Content-Type'] = "text/html; charset=utf-8"
			#msg['Content-Transfer-Encoding'] = "quoted-printable"
			#msg['Reply-To'] = email
			#msg = 'From: '+nombre+' <'+email+'>\r\nTo: miguelmiguel19@gmail.com\r\n\r\n'+comentario
			if nombre and email and comentario:
				try:
					#send_mail('(Comentario) PCA-Audit', nombre+' <'+email+'>. Comentario: '+comentario, email,['miguel.ambrosio@pcaaudit.com'], fail_silently=False)
					conexion = mail.get_connection()
					conexion.password = settings.ALT_EMAIL_HOST_PASSWORD
					conexion.username = settings.ALT_EMAIL_HOST_USER
					conexion.host = settings.ALT_EMAIL_HOST
					conexion.port = settings.EMAIL_PORT	
					conexion.use_tls = settings.EMAIL_USE_TLS
					conexion.open()

					#\"url\": \"https://pcafarma.com\" Si se quiere agregar landing page poner esto dentro del settings del header
					correo = EmailMessage(Subject, combinado, 'contacto@prxcontrolsolutions.com', ['contacto@prxcontrolsolutions.com'], connection=conexion )

					correo.send()
					conexion.close()
	
	
	
					#server = smtplib.SMTP_SSL('smtp.gmail.com',465)
					#server.login('info@pcaaudit.com', 'prxinfo2012')
					#server.sendmail(email,['contacto@prxcontrolsolution.com'], str(msg))
					#server.quit()
					print "holaaaaa"
					return render_to_response('espaniol/contacto_done.html', RequestContext(request))
				except (smtplib.SMTPAuthenticationError):#BadHeaderError:
					print 'Error de header'
	return render_to_response('espaniol/quienesSomos.html', {'contacto':contacto}, context_instance=RequestContext(request))
	
def contacto(request):
	contacto = ContactoForm()
	#user = request.user
	if request.method == 'POST':
		#print "ESPANIOL"
		#return render_to_response('espaniol/contacto_done.html', RequestContext(request))
		contacto = ContactoForm(request.POST)
		if contacto.is_valid():
			#if user.is_authenticated():
				#contacto = ContactoForm(initial={'nombre':user.get_full_name,'email':user.email})
			#else:
			contacto = ContactoForm()
			
			nombre = request.POST.get('nombre',None)
			email = request.POST.get('email',None)
			comentario = request.POST.get('comentario',None)
			combinado = 'Mensaje de Contacto \r\n\r\nNombre: '+nombre+' \r\n'+'Email: '+email+' \r\n'+'Comentario: '+comentario
			msg = MIMEText(combinado.encode('utf-8'), 'plain', 'UTF-8')
			#msg['From']= nombre
			#msg['MIME-Version']="1.0"
			Subject="Mensaje de Contacto - "+nombre+" - "+email
			#msg['Content-Type'] = "text/html; charset=utf-8"
			#msg['Content-Transfer-Encoding'] = "quoted-printable"
			#msg['Reply-To'] = email
			#msg = 'From: '+nombre+' <'+email+'>\r\nTo: miguelmiguel19@gmail.com\r\n\r\n'+comentario
			if nombre and email and comentario:
				try:
					#send_mail('(Comentario) PCA-Audit', nombre+' <'+email+'>. Comentario: '+comentario, email,['miguel.ambrosio@pcaaudit.com'], fail_silently=False)
					conexion = mail.get_connection()
					conexion.password = settings.ALT_EMAIL_HOST_PASSWORD
					conexion.username = settings.ALT_EMAIL_HOST_USER
					conexion.host = settings.ALT_EMAIL_HOST
					conexion.port = settings.EMAIL_PORT	
					conexion.use_tls = settings.EMAIL_USE_TLS
					conexion.open()

					#\"url\": \"https://pcafarma.com\" Si se quiere agregar landing page poner esto dentro del settings del header
					correo = EmailMessage(Subject, combinado, 'contacto@prxcontrolsolutions.com', ['contacto@prxcontrolsolutions.com'], connection=conexion )

					correo.send()
					conexion.close()
	
	
	
					#server = smtplib.SMTP_SSL('smtp.gmail.com',465)
					#server.login('info@pcaaudit.com', 'prxinfo2012')
					#server.sendmail(email,['contacto@prxcontrolsolution.com'], str(msg))
					#server.quit()
					return render_to_response('espaniol/contacto_done.html', RequestContext(request))
				except (smtplib.SMTPAuthenticationError):#BadHeaderError:
					print 'Error de header'
	#else:
		#return render_to_response('espaniol/contacto.html',{ 'contacto':contacto }, RequestContext(request))
	return render_to_response('espaniol/contacto.html',{ 'contacto':contacto }, RequestContext(request))

#-----------------------------------------------------------Ingles------------------------------------------------------------------------
	
# HOME
def indexI(request):	
 	contacto = ContactForm()
	#user = request.user
	if request.method == 'POST':
		contacto = ContactForm(request.POST)
		if contacto.is_valid():
			#if user.is_authenticated():
				#contacto = ContactoForm(initial={'nombre':user.get_full_name,'email':user.email})
			#else:
			contacto = ContactForm()
			
			nombre = request.POST.get('nombre',None)
			email = request.POST.get('email',None)
			comentario = request.POST.get('comentario',None)
			combinado = 'Mensaje de Contacto \r\n\r\nNombre: '+nombre+' \r\n'+'Email: '+email+' \r\n'+'Comentario: '+comentario
			msg = MIMEText(combinado.encode('utf-8'), 'plain', 'UTF-8')
			#msg['From']= nombre
			#msg['MIME-Version']="1.0"
			Subject="Mensaje de Contacto - "+nombre+" - "+email
			#msg['Content-Type'] = "text/html; charset=utf-8"
			#msg['Content-Transfer-Encoding'] = "quoted-printable"
			#msg['Reply-To'] = email
			#msg = 'From: '+nombre+' <'+email+'>\r\nTo: miguelmiguel19@gmail.com\r\n\r\n'+comentario
			if nombre and email and comentario:
				try:
					#send_mail('(Comentario) PCA-Audit', nombre+' <'+email+'>. Comentario: '+comentario, email,['miguel.ambrosio@pcaaudit.com'], fail_silently=False)
					conexion = mail.get_connection()
					conexion.password = settings.ALT_EMAIL_HOST_PASSWORD
					conexion.username = settings.ALT_EMAIL_HOST_USER
					conexion.host = settings.ALT_EMAIL_HOST
					conexion.port = settings.EMAIL_PORT	
					conexion.use_tls = settings.EMAIL_USE_TLS
					conexion.open()

					#\"url\": \"https://pcafarma.com\" Si se quiere agregar landing page poner esto dentro del settings del header
					correo = EmailMessage(Subject, combinado, 'contacto@prxcontrolsolutions.com', ['contacto@prxcontrolsolutions.com'], connection=conexion )

					correo.send()
					conexion.close()
	
	
	
					#server = smtplib.SMTP_SSL('smtp.gmail.com',465)
					#server.login('info@pcaaudit.com', 'prxinfo2012')
					#server.sendmail(email,['contacto@prxcontrolsolution.com'], str(msg))
					#server.quit()
					return render_to_response('ingles/contacto_done.html', RequestContext(request))
				except (smtplib.SMTPAuthenticationError):#BadHeaderError:
					print 'Error de header'
                    
	return render_to_response('ingles/home.html', { 'contacto':contacto }, context_instance=RequestContext(request))
	
def quienesSomosI(request):	
	contacto = ContactForm()
	#user = request.user
	if request.method == 'POST':
		contacto = ContactForm(request.POST)
		if contacto.is_valid():
			#if user.is_authenticated():
				#contacto = ContactoForm(initial={'nombre':user.get_full_name,'email':user.email})
			#else:
			contacto = ContactForm()
			
			nombre = request.POST.get('nombre',None)
			email = request.POST.get('email',None)
			comentario = request.POST.get('comentario',None)
			combinado = 'Mensaje de Contacto \r\n\r\nNombre: '+nombre+' \r\n'+'Email: '+email+' \r\n'+'Comentario: '+comentario
			msg = MIMEText(combinado.encode('utf-8'), 'plain', 'UTF-8')
			#msg['From']= nombre
			#msg['MIME-Version']="1.0"
			Subject="Mensaje de Contacto - "+nombre+" - "+email
			#msg['Content-Type'] = "text/html; charset=utf-8"
			#msg['Content-Transfer-Encoding'] = "quoted-printable"
			#msg['Reply-To'] = email
			#msg = 'From: '+nombre+' <'+email+'>\r\nTo: miguelmiguel19@gmail.com\r\n\r\n'+comentario
			if nombre and email and comentario:
				try:
					#send_mail('(Comentario) PCA-Audit', nombre+' <'+email+'>. Comentario: '+comentario, email,['miguel.ambrosio@pcaaudit.com'], fail_silently=False)
					conexion = mail.get_connection()
					conexion.password = settings.ALT_EMAIL_HOST_PASSWORD
					conexion.username = settings.ALT_EMAIL_HOST_USER
					conexion.host = settings.ALT_EMAIL_HOST
					conexion.port = settings.EMAIL_PORT	
					conexion.use_tls = settings.EMAIL_USE_TLS
					conexion.open()

					#\"url\": \"https://pcafarma.com\" Si se quiere agregar landing page poner esto dentro del settings del header
					correo = EmailMessage(Subject, combinado, 'contacto@prxcontrolsolutions.com', ['contacto@prxcontrolsolutions.com'], connection=conexion )

					correo.send()
					conexion.close()
	
	
	
					#server = smtplib.SMTP_SSL('smtp.gmail.com',465)
					#server.login('info@pcaaudit.com', 'prxinfo2012')
					#server.sendmail(email,['contacto@prxcontrolsolution.com'], str(msg))
					#server.quit()
					return render_to_response('ingles/contacto_done.html', RequestContext(request))
				except (smtplib.SMTPAuthenticationError):#BadHeaderError:
					print 'Error de header'
	return render_to_response('ingles/quienesSomos.html', {'contacto':contacto }, context_instance=RequestContext(request))
	
def contactoI(request):
	contacto = ContactForm()
	#user = request.user
	if request.method == 'POST':
		contacto = ContactForm(request.POST)
		if contacto.is_valid():
			#if user.is_authenticated():
				#contacto = ContactoForm(initial={'nombre':user.get_full_name,'email':user.email})
			#else:
			contacto = ContactForm()
			
			nombre = request.POST.get('nombre',None)
			email = request.POST.get('email',None)
			comentario = request.POST.get('comentario',None)
			combinado = 'Mensaje de Contacto \r\n\r\nNombre: '+nombre+' \r\n'+'Email: '+email+' \r\n'+'Comentario: '+comentario
			msg = MIMEText(combinado.encode('utf-8'), 'plain', 'UTF-8')
			#msg['From']= nombre
			#msg['MIME-Version']="1.0"
			Subject="Mensaje de Contacto - "+nombre+" - "+email
			#msg['Content-Type'] = "text/html; charset=utf-8"
			#msg['Content-Transfer-Encoding'] = "quoted-printable"
			#msg['Reply-To'] = email
			#msg = 'From: '+nombre+' <'+email+'>\r\nTo: miguelmiguel19@gmail.com\r\n\r\n'+comentario
			if nombre and email and comentario:
				try:
					#send_mail('(Comentario) PCA-Audit', nombre+' <'+email+'>. Comentario: '+comentario, email,['miguel.ambrosio@pcaaudit.com'], fail_silently=False)
					conexion = mail.get_connection()
					conexion.password = settings.ALT_EMAIL_HOST_PASSWORD
					conexion.username = settings.ALT_EMAIL_HOST_USER
					conexion.host = settings.ALT_EMAIL_HOST
					conexion.port = settings.EMAIL_PORT	
					conexion.use_tls = settings.EMAIL_USE_TLS
					conexion.open()

					#\"url\": \"https://pcafarma.com\" Si se quiere agregar landing page poner esto dentro del settings del header
					correo = EmailMessage(Subject, combinado, 'contacto@prxcontrolsolutions.com', ['contacto@prxcontrolsolutions.com'], connection=conexion )

					correo.send()
					conexion.close()
	
	
	
					#server = smtplib.SMTP_SSL('smtp.gmail.com',465)
					#server.login('info@pcaaudit.com', 'prxinfo2012')
					#server.sendmail(email,['contacto@prxcontrolsolution.com'], str(msg))
					#server.quit()
					return render_to_response('ingles/contacto_done.html', RequestContext(request))
				except (smtplib.SMTPAuthenticationError):#BadHeaderError:
					print 'Error de header'
	else:
		#if user.is_authenticated():
			#contacto = ContactoForm(initial={'nombre':user.get_full_name,'email':user.email})
		return render_to_response('ingles/contacto.html',{ 'contacto':contacto }, RequestContext(request))
	return render_to_response('ingles/contacto.html',{ 'contacto':contacto }, RequestContext(request))
	
	
def inversionistas(request):	
	return render_to_response('ingles/inversionistas.html', {}, context_instance=RequestContext(request))
	
def license(request):	
	return render_to_response('espaniol/license.html', {}, context_instance=RequestContext(request))
	#return render_to_response('ingles/license.html', {}, context_instance=RequestContext(request))
