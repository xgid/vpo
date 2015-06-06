#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
vpo.__main__
~~~~~~~~~~~~~~~~~~~~~

The main entry point for the command line interface.

Invoke as ``vpo`` (if installed)
or ``python -m vpo`` (no install required).
"""
from __future__ import absolute_import, unicode_literals
import logging
import sys

from vpo.log import configure_stream

logger = logging.getLogger(__name__)


def cli():
    """Add some useful functionality here or import from a submodule."""
    # configure root logger to print to STDERR
    configure_stream(level='DEBUG')

    # launch the command line interface
    logger.debug('Booting up command line interface')

    # ...oops, it wasn't implemented yet!
    logger.error('Please implement the command line interface!')
    raise NotImplementedError('Vanguard Package One CLI not implemented yet')


if __name__ == '__main__':
    # exit using whatever exit code the CLI returned
    sys.exit(cli())
