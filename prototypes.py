import sys
import os
from django.conf import settings
from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(__file__)
settings.configure(
    DEBUG=True,
    SECRET_KEY='f91oh8l1dymu)87ejlwbd7-@kac50owy@6^_8$@ky9jvfgma02',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    #ALLOWED_HOSTS = ['127.0.0.1', '207.154.240.36'],
    ALLOWED_HOSTS=[],
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
        'compressor',
        'django_icons',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        },
    ),
    STATIC_URL='/static/',
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
    SITE_OUTPUT_DIRECTORY=os.path.join(BASE_DIR, '_build'),
    STATIC_ROOT=os.path.join(BASE_DIR, '_build', 'static'),
    STATICAFILES_STORAGE='django.contrib.staticfiles.storage.CachedStaticFilesStorage',
    STATICFILES_FINDERS=(
            'django.contrib.staticfiles.finders.FileSystemFinder',
            'django.contrib.staticfiles.finders.AppDirectoriesFinder',
            'compressor.finders.CompressorFinder',
        ),

    # EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend',
    EMAIL_HOST='smtp.gmail.com',
    EMAIL_PORT=587,
    EMAIL_USE_TLS=True,
    EMAIL_HOST_USER='claudio.tubertini@gmail.com',
    EMAIL_HOST_PASSWORD='Matilde1995?'
)

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)