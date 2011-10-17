from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

MERCHANT_ID = getattr(settings, 'PAYONE_MERCHANT_ID', None)
if MERCHANT_ID is None:
    raise ImproperlyConfigured('PAYONE_MERCHANT_ID not set')

PORTAL_ID = getattr(settings, 'PAYONE_PORTAL_ID', None)
if PORTAL_ID is None:
    raise ImproperlyConfigured('PAYONE_PORTAL_ID not set')

SUBACCOUNT_ID = getattr(settings, 'PAYONE_SUBACCOUNT_ID', None)
if SUBACCOUNT_ID is None:
    raise ImproperlyConfigured('PAYONE_SUBACCOUNT_ID not set')

KEY = getattr(settings, 'PAYONE_KEY', None)
if KEY is None:
    raise ImproperlyConfigured('PAYONE_KEY not set')

MODE = getattr(settings, 'PAYONE_MODE', 'live')

