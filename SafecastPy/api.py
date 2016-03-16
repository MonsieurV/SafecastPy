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

from .endpoints import EndpointsMixin
from .exceptions import SafecastPyError, SafecastPyAuthError

PRODUCTION_API_URL = 'https://api.safecast.org'
DEVELOPMENT_API_URL = 'http://dev.safecast.org'

class SafecastPy(EndpointsMixin, object):
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

    def _request(self, url, method='GET', params=None, api_call=None):
        """Internal request method"""
        method = method.lower()
        params = params or {}

        func = getattr(requests, method)
        print(func)
        print(params)

        requests_args = {}

        if method == 'get':
            requests_args['params'] = params
        else:
            requests_args['json'] = params.get('json')
        print(requests_args)
        try:
            response = func(url, **requests_args)
        except requests.RequestException as e:
            raise SafecastPyError(str(e))

        # greater than 304 (not modified) is an error
        if response.status_code > 304:
            raise SafecastPyError(response.text)
            # TODO 401, Bad Request
        try:
            if response.status_code == 204:
                content = response.content
            else:
                content = response.json()
        except ValueError:
            raise SafecastPyError('Response was not valid JSON. \
                               Unable to decode.')
        return content

    def request(self, endpoint, method='GET', params=None):
        """Return dict of response received from Safecast's API
        :param endpoint: (required) Full url or Safecast API endpoint
                         (e.g. measurements/users)
        :type endpoint: string
        :param method: (optional) Method of accessing data, either
                       GET, POST or DELETE. (default GET)
        :type method: string
        :param params: (optional) Dict of parameters (if any) accepted
                       the by Safecast API endpoint you are trying to
                       access (default None)
        :type params: dict or None
        :rtype: dict
        """

        # In case they want to pass a full Safecast URL
        # i.e. https://api.safecast.org/measurements.json
        if endpoint.startswith('http'):
            url = endpoint
        else:
            url = '%s/%s.json' % (self.api_url, endpoint)

        if method != 'GET':
            if self.api_key is None:
                raise SafecastPyAuthError('Require an api_key')
            url = url + '?api_key={0}'.format(self.api_key)

        content = self._request(url, method=method, params=params,
                                api_call=url)
        return content

    def get(self, endpoint, params=None):
        """Shortcut for GET requests via :class:`request`"""
        return self.request(endpoint, params=params)

    def post(self, endpoint, params=None):
        """Shortcut for POST requests via :class:`request`"""
        return self.request(endpoint, 'POST', params=params)

    def delete(self, endpoint, params=None):
        """Shortcut for DELETE requests via :class:`request`"""
        return self.request(endpoint, 'DELETE', params=params)
