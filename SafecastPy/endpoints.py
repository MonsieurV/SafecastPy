# -*- coding: utf-8 -*-

"""
SafecastPy.endpoints
~~~~~~~~~~~~~~~~~
This module provides a mixin for a :class:`SafecastPy <SafecastPy>` instance.
Parameters that need to be embedded in the API url just need to be passed
as a keyword argument.
e.g. SafecastPy.get_measurement(id='12345')
"""

class EndpointsMixin(object):
    def get_measurements(self, **params):
        return self.get('/measurements', params=params)

    def get_measurement(self, **params):
        return self.get('/measurements/{0}'.format(params.get('id')),
            params=params)

    def post_measurement(self, **params):
        return self.post('/measurements', params=params)

    def delete_measurement(self, **params):
        return self.delete('/measurements/{0}'.format(params.get('id')),
            params=params)
