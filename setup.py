#!/usr/bin/env python

"""
setup.py for cmocean

"""
# import shutil
import sys
from setuptools import setup # to support "develop" mode
from setuptools.command.test import test as TestCommand
import versioneer
# from numpy.distutils.core import setup, Extension

# cmocean_mod = Extension(name = "cmocean",
#                          sources=['rgb/*',
#                                   ],
#                       )

# print cmocean_mod

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.verbose = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    version = versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    name = "cmocean",
    author = "Kristen Thyng",
    author_email = "kthyng@gmail.com",
    url = 'https://github.com/matplotlib/cmocean',
    download_url = 'https://github.com/matplotlib/cmocean/tarball/0.2.1',
    description = ("Colormaps for Oceanography"),
    long_description=open('README.rst').read(),
    classifiers=[
                 "Development Status :: 3 - Alpha",
    #             "Topic :: Utilities",
                 ],
    package_data={
        'cmocean': ['rgb/*.txt'],
    },
    packages = ["cmocean"],
    # py_modules = cmocean_mod,
    ext_package='cmocean',
    # ext_modules = [cmocean_mod],
    scripts = [],
    keywords = ['colormaps', 'oceanography', 'plotting', 'visualization'],
    tests_require=['pytest']
    )
