# -*- coding: utf-8 -*-
"""
vpo
~~~~~~~~~~~~~~~~~~~

Prueba de paquete Python con cookiecutter plantilla pyvanguard

:copyright: (c) 2015 by xgid
:licence: MIT, see LICENCE for more details
"""
from __future__ import absolute_import, unicode_literals
import logging

# Generate your own AsciiArt at:
# patorjk.com/software/taag/#f=Calvin%20S&t=Vanguard Package One
__banner__ = r"""
╦  ╦┌─┐┌┐┌┌─┐┬ ┬┌─┐┬─┐┌┬┐
╚╗╔╝├─┤││││ ┬│ │├─┤├┬┘ ││  by xgid
 ╚╝ ┴ ┴┘└┘└─┘└─┘┴ ┴┴└──┴┘
"""

__title__ = 'vpo'
__summary__ = 'Prueba de paquete Python con cookiecutter plantilla pyvanguard'
__uri__ = 'https://github.com/xgid/vpo'

__version__ = '0.0.1'

__author__ = 'xgid'
__email__ = 'xgid03@zoho.com'

__license__ = 'MIT'
__copyright__ = 'Copyright 2015 xgid'

# the user should dictate what happens when a logging event occurs
logging.getLogger(__name__).addHandler(logging.NullHandler())
