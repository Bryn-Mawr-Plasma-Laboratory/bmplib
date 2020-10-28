
#!/usr/bin/env python3
#
# This file is part of the bmplib package, a Python toolkit for the
# Bryn Mawr Plasma Laboratory at Bryn Mawr College.
#
#
#
#
import os

from setuptools import setup

# find here
here = os.path.abspath(os.path.dirname(__file__))

# ---- Perform setup                                                        ----
setup(use_scm_version=True)