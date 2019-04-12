# -*- coding: utf-8 -*-

"""
SafecastPy.exceptions
~~~~~~~~~~~~~~~~~~
This module contains SafecastPy specific Exception classes.
"""


class SafecastPyError(Exception):
    """Generic error class, catch-all for most SafecastPy issues.
    Special cases are handled by TwythonAuthError & TwythonRateLimitError.
    """

    def __init__(self, message, error_code=None):
        if error_code is not None:
            self.html = message
            message = "Safecast API returned a {0} error".format(error_code)
        super(SafecastPyError, self).__init__(message)


class SafecastPyAuthError(SafecastPyError):
    """Raised when you try to access a protected resource and it fails due to
    some issue with your authentication.
    """

    pass
