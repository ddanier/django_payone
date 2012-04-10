import urllib
import urlparse
from django.conf import settings
from django.utils.datastructures import MultiValueDict
from django.utils.encoding import smart_unicode, smart_str
from django.utils.hashcompat import md5_constructor
from django_payone.exceptions import PayoneServerException

PAYONE_URL = 'https://api.pay1.de/post-gateway/'
ENCODING_MAP = {
    'utf-8': 'UTF-8',
    'utf8': 'UTF-8',
}

PAYONE_DEBUG = getattr(settings, 'PAYONE_DEBUG', False)

class PayoneServerChannelMethod(object):
    def __init__(self, channel, method):
        self.channel = channel
        self.method = method
    
    def parse_response(self, response):
        values = []
        for line in self.channel._to_unicode(response).split('\n'):
            if '=' in line:
                values.append(line.split('=', 1))
        return dict(values)
    
    def __call__(self, **kwargs):
        params = {
            'mid': self.channel.merchant_id,
            'portalid': self.channel.portal_id,
            'key': self.channel.md5_key,
            'mode': self.channel.mode,
            'encoding': ENCODING_MAP.get(self.channel.encoding, self.channel.encoding),
        }
        params.update(kwargs)
        params.update({ # you cannot override the method!
            'request': self.method,
        })
        if PAYONE_DEBUG:
            print '-' * 79
            print 'Payone request:'
            print params
            print '-' * 79
        
        data = urllib.urlencode([
            (
                self.channel._to_str(k),
                self.channel._to_str(v)
            )
            for k, v
            in params.iteritems()
        ])
        response = urllib.urlopen(PAYONE_URL, data).read()
        
        results = self.parse_response(response)
        if PAYONE_DEBUG:
            print '-' * 79
            print 'Payone response:'
            print results
            print '-' * 79

        status = results.get('status')
        if status == 'ERROR':
            raise PayoneServerException(
                results.get('errormessage', ''),
                results.get('errorcode', None),
            )

        return results

class PayoneServerChannel(object):
    def __init__(self, merchant_id, portal_id, key, mode='live', encoding='utf8'):
        self.merchant_id = merchant_id
        self.portal_id = portal_id
        self.key = key
        self.md5_key = md5_constructor(key).hexdigest()
        self.mode = mode
        self.encoding = encoding
    
    def __getattr__(self, name):
        return PayoneServerChannelMethod(self, name)
    
    def _to_str(self, value):
        try:
            return smart_str(value, encoding=self.encoding)
        except UnicodeEncodeError:
            return smart_str(value, encoding=self.encoding, errors='replace')
    
    def _to_unicode(self, value):
        try:
            return smart_unicode(value, encoding=self.encoding)
        except UnicodeDecodeError:
            return smart_unicode(value, encoding=self.encoding, errors='replace')

