# -*- coding: utf-8 -*-

"""
SafecastPy.api
~~~~~~~~~~~
This module contains functionality for access to Safecast API calls,
Safecast Authentication, and miscellaneous methods that are useful when
dealing with the Safecast API.
"""

import requests
import json

# from .endpoints import EndpointsMixin
# TODO Do like Twython: generic request constructing and handling here,
# then a complete list of available methods in a Mixin.
# https://github.com/ryanmcgrath/twython/blob/master/twython/endpoints.py
# https://github.com/ryanmcgrath/twython/blob/master/twython/api.py
from .exceptions import SafecastPyError, SafecastPyAuthError

PRODUCTION_API_URL = 'https://api.safecast.org'
DEVELOPMENT_API_URL = 'http://dev.safecast.org'

class SafecastPy(object):
    def __init__(self, api_key=None, api_url=None):
        """Instantiates an instance of SafecastPy. Takes an optional api_key
        parameters for authentication.
        """
        if api_url is None:
            self.api_url = PRODUCTION_API_URL
        else:
            self.api_url = api_url
        self.api_key = api_key

    def __repr__(self):
        return '<SafecastPy: %s>' % (self.api_url)

    def construct_url(self, uri, auth=False):
        url = self.api_url + uri + '.json'
        if auth:
            if self.api_key is None:
                raise SafecastPyAuthError('Require an api_key')
            url = url + '?api_key={0}'.format(self.api_key)
        return url

    def get_measurements(self):
        return requests.get(self.construct_url('/measurements'))

    def get_measurement(self, id):
        return requests.get(self.construct_url('/measurements/{0}'.format(id)))

    def post_measurement(self, measurement):
        return requests.post(self.construct_url('/measurements', True),
            json=measurement)
