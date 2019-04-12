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
        return self.get("/measurements", params=params)

    def get_user_measurements(self, **params):
        return self.get(
            "/users/{0}/measurements".format(params.get("id")), params=params
        )

    def get_device_measurements(self, **params):
        return self.get(
            "/devices/{0}/measurements".format(params.get("id")), params=params
        )

    def get_measurement(self, **params):
        return self.get("/measurements/{0}".format(params.get("id")), params=params)

    def add_measurement(self, **params):
        return self.post("/measurements", params=params)

    def delete_measurement(self, **params):
        return self.delete("/measurements/{0}".format(params.get("id")), params=params)

    def get_bgeigie_imports(self, **params):
        return self.get("/bgeigie_imports", params=params)

    def get_bgeigie_import(self, **params):
        return self.get("/bgeigie_imports/{0}".format(params.get("id")), params=params)

    def upload_bgeigie_import(self, **params):
        return self.post("/bgeigie_imports", params=params)

    def get_users(self, **params):
        return self.get("/users", params=params)

    def get_user(self, **params):
        return self.get("/users/{0}".format(params.get("id")), params=params)

    def get_devices(self, **params):
        return self.get("/devices", params=params)

    def get_device(self, **params):
        return self.get("/devices/{0}".format(params.get("id")), params=params)

    def add_device(self, **params):
        return self.post("/devices", params=params)
