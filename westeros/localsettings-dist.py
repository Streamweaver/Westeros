# Django settings for asoiaf project.

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'du@*4v0-vgbnm9rciefamw1=8sg5i-feg%6y1z=!0=#e89)on2'

# Everything here related to django-social-auth
#TWITTER_CONSUMER_KEY              = ''
#TWITTER_CONSUMER_SECRET           = ''
FACEBOOK_APP_ID                   = ''
FACEBOOK_API_SECRET               = ''
GOOGLE_CONSUMER_KEY          = ''
GOOGLE_CONSUMER_SECRET       = ''
#GOOGLE_OAUTH2_CLIENT_KEY          = ''
#GOOGLE_OAUTH2_CLIENT_SECRET       = ''
SOCIAL_AUTH_CREATE_USERS          = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
SOCIAL_AUTH_DEFAULT_USERNAME      = 'socialauth_user'
SOCIAL_AUTH_COMPLETE_URL_NAME     = 'socialauth_complete'
LOGIN_ERROR_URL                   = '/login/error/'
#SOCIAL_AUTH_USER_MODEL            = 'app.CustomUser'
SOCIAL_AUTH_ERROR_KEY             = 'socialauth_error'
