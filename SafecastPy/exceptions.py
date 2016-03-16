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
    def __init__(self, msg):
        super(SafecastPyError, self).__init__(msg)


class SafecastPyAuthError(SafecastPyError):
    """Raised when you try to access a protected resource and it fails due to
    some issue with your authentication.
    """
    pass
