from django.utils.hashcompat import md5_constructor
from django.utils.encoding import smart_str

HASH_PARAMS = ('mid', 'aid', 'portalid', 'mode', 'request', 'responsetype',
    'reference', 'userid', 'customerid', 'param', 'narrative_text',
    'successurl', 'errorurl', 'backurl', 'exiturl', 'clearingtype', 'encoding',
    'amount', 'currency', 'due_type', 'storecarddata', 'checktype',
    'addresschecktype', 'consumerscoretype', 'invoiceid', 'invoiceappendix',
    'eci', 'id[]', 'pr[]', 'no[]', 'de[]', 'ti[]', 'va[]', 'productid',
    'accessname', 'accesscode', 'access_expiretime', 'access_canceltime',
    'access_starttime', 'access_period', 'access_aboperiod', 'access_price',
    'access_aboprice', 'access_vat', 'settleperiod', 'settletime',
    'vaccountname', 'vreference',)

def secure_hash(key, params):
    hash_str = ''
    for i in sorted(params):
        if i in HASH_PARAMS:
            hash_str += smart_str(params[i])
    hash_str += key
    return md5_constructor(hash_str).hexdigest()

