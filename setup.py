#!/usr/bin/env python

from distutils.core import setup
from pyxf import _version_

setup(name='PyXF',
      version=_version_,
      description='Python interface to XSB, SWI, ECLiPSe Prolog and Flora-2/Ergo Lite',
      author='Markus Schatten',
      author_email='markus.schatten@foi.hr',
      url='https://github.com/AILab-FOI/pyxf',
      packages=['pyxf'],
     )
