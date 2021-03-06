
from decimal import Decimal


_SCALE = 1000000


def _clean_up(value):

	v = str(value)
	if '.' in v:
		v = v.rstrip('0')
		if v[-1] == '.':
			v = v[:-1]
	return v


def create_amount(native):

	class Amount(object):

		def __init__(self, value, currency=native, issuer=None):
			self.value		= _clean_up(value)
			self.currency	= currency
			self.issuer		= issuer

		@staticmethod
		def from_json(amount):
			if type(amount) != dict:
				return Amount(str(Decimal(amount) / _SCALE))
			else:
				assert 'value' in amount
				assert 'currency' in amount
				assert 'issuer' in amount
				return Amount(**amount)

		def to_json(self):
			if self.currency == native:
				return str(int(Decimal(self.value) * _SCALE))
			else:
				return {
					'value':	self.value,
					'currency':	self.currency,
					'issuer':	self.issuer
				}

	return Amount
