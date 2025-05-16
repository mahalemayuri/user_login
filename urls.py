from user_portal.user_portal.settings import BASE_DIR


AUTH_USER_MODEL = 'accounts.CustomUser'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
