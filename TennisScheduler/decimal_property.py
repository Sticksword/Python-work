__author__ = 'Michael'
from google.appengine.ext import ndb
from decimal import *


class DecimalProperty(ndb.IntegerProperty):
    # Decimal property ideal to store currency values, such as $20.34
    # See https://developers.google.com/appengine/docs/python/ndb/subclassprop
    def _validate(self, value):
        if not isinstance(value, (Decimal, str, unicode, int, long)):
            raise TypeError('Expected a Decimal, str, unicode, int or long an got instead %s' % repr(value))

    def _to_base_type(self, value):
        return int(Decimal(value) * 100)

    def _from_base_type(self, value):
        return Decimal(value)/Decimal(100)