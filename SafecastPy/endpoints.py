# -*- coding: utf-8 -*-

"""
SafecastPy.endpoints
~~~~~~~~~~~~~~~~~
This module provides a mixin for a :class:`SafecastPy <SafecastPy>` instance.
Parameters that need to be embedded in the API url just need to be passed
as a keyword argument.
e.g. SafecastPy.get_measurement(id='12345')
"""
import requests

class EndpointsMixin(object):
    def get_measurements(self):
        # TODO Paging?
        return requests.get(self.construct_url('/measurements'))

    def get_measurement(self, id):
        return requests.get(self.construct_url('/measurements/{0}'.format(id)))

    def post_measurement(self, measurement):
        return requests.post(self.construct_url('/measurements', True),
            json=measurement)

    def delete_measurement(self, id):
        return requests.delete(self.construct_url(
            '/measurements/{0}'.format(id), True))
