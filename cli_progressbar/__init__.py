# -*- coding: utf-8 -*-
"""
lightweight library to print progress bar in cli
"""
import sys
from cli_progressbar.progressbar import Progress

__author__ = 'Ali Madihi (mrunderline)'
__version__ = '1.0.2'
__date__ = '2021-01-04'

_DEBUG_MODE = False

if _DEBUG_MODE:
    print('Python ' + '.'.join(map(str, sys.version_info[:3])))
