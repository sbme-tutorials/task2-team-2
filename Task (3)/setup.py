# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:25:14 2019

@author: manog
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('functionsForTask3.pyx'))