#!/usr/bin/env python3
# shaystack module
# See the accompanying LICENSE file.
# (C) 2016 VRT Systems
# (C) 2021 Engie Digital
#
# vim: set ts=4 sts=4 et tw=78 sw=4 si:
import os
from Cython.Build import cythonize
from setuptools import setup
from setuptools import Extension

# See setup.cfg
if 'CFLAGS' not in os.environ:
    os.environ['CFLAGS'] = '-O3'

setup(
    setup_requires=['pbr', 'cythonpackage[build]'],
    pbr=True,
    # cythonpackage=True,
    # cythonpackage={
    #     "inject_ext_modules": True,
    #     "inject_init": True,
    #     "remove_source": True,
    #     "compile_pyc": True,
    #     "optimize": 1,
    #     "exclude":[]
    # },
    ext_modules=cythonize(
        [
            Extension("shaytstack.*", ["shaystack/*.py"]),
            Extension("shaytstack.providers.*", ["shaystack/providers/*.py"]),
         ],
        compiler_directives={'language_level': 3},
        build_dir="build/cythonpackage",
    )
)
