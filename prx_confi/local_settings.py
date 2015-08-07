# -*- coding: utf-8 -*-
ADMINS = (
     ('Narbe', 'narbelys@gmail.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'audit', #'audit',#'APS', #'PCAFarmaJulio', #'APS', #'Farma15-4', #'APSAon', #'IntegracionAPS', #'APS', #''pcaaudit0508', #'PCAfarma', # 'PCAaudit14-02-14',#'caroni11-11-13',#'aon05-12-13',#' ''backupaon', #sanitas',#, #,  # #'pcaaudit0508',#'pcaaudit',#'prxsys',                          # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.                      # Set to empty string for default. Not used with sqlite3.
    }
}

 # Desactivar sentry local: Unset your DSN value
RAVEN_CONFIG = {}

ADMIN_MEDIA_PREFIX = '/home/narbe/Documentos/prx/admin/'
#STATIC_ROOT = '/home/narbe/Documentos/PCAaudit/PRXAnalyzer/static/'
STATIC_ROOT = '/home/narbe/Documentos/prx/PRX/static/'

# URL prefix for static files.
STATIC_URL  = '/static/'
#STATIC_URL  = 'http://pcaaudit.com/static/'

MEDIA_ROOT = '/home/narbe/vademecum/'

TEMPLATE_DIRS = (
    '/home/narbe/Documentos/prx/my_templates'
)

#MEDIA_ROOT = '/home/narbe/vademecum'

LOG_PATH = '/home/narbe/Documentos/logs/'
CODIGOS_PATH = '/home/narbe/Documentos/codigosBR/'
INFORMES_URL = 'http://localhost:8081/static/informes/'
#INFORMES_PATH = '/home/narbe/Documentos/PCAaudit/static/informes/'

#EMAIL_HOST = 'smtp.sendgrid.net'
#EMAIL_HOST_USER = 'prxsolutions'
#EMAIL_HOST_PASSWORD = 'prx400881390'
ALT_EMAIL_HOST = 'smtp.sendgrid.net'
ALT_EMAIL_HOST_PASSWORD = 'prx400881390'
ALT_EMAIL_HOST_USER = 'prxsolutions'

DEBUG = True

APIKEY_MERCANTIL = 'd3822d68357ccf6284e2a9c1bb874baa'
APIKEY_PCA_MERCANTIL = '8dc9a76d227626ebae23c266b56699db'



#LOGIN_CARONI = True#False#

URL_CARONI = "http://extranet.seguroscaroni.com/framework_prueba/lib/index.php"

