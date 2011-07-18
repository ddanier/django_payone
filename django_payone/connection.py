from django_payone import settings as payone_settings
from django_payone.channel.server import PayoneServerChannel

server = PayoneServerChannel(
    merchant_id = payone_settings.MERCHANT_ID,
    portal_id = payone_settings.PORTAL_ID,
    key = payone_settings.KEY,
    mode = payone_settings.MODE,
)

