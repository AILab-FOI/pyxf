#!/usr/bin/env python

from distutils.core import setup
import pyxf

setup(name='PyXF',
      version=pyxf.__version__,
      description='Python interface to XSB, SWI, ECLiPSe Prolog and Flora-2/Ergo Lite',
      author='Markus Schatten',
      author_email='markus.schatten@foi.hr',
      url='https://github.com/AILab-FOI/pyxf',
      packages=['pyxf'],
     )
