#
# ,---.     ,---.                    |    ,---.
# `---.,---.|__. ,---.,---.,---.,---.|--- |---',   .
#     |,---||    |---'|    ,---|`---.|    |    |   |
# `---'`---^`    `---'`---'`---^`---'`---'`    `---|
#                                              `---'

"""
SafecastPy
-------
SafecastPy is a library for Python that wraps the Safecast API.
Questions, comments? yoan@ytotech.com
"""

__author__ = 'Yoan Tournade <yoan@ytotech.com>'
__version__ = '0.1.0'

from .api import SafecastPy, PRODUCTION_API_URL, DEVELOPMENT_API_URL
from .api import UNIT_CPM, UNIT_USV
from .exceptions import (
    SafecastPyError, SafecastPyAuthError
)
