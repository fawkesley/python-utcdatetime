# encoding: utf-8

from setuptools import setup, find_packages

import codecs
import os
import re


try:
    # Workaround for https://bugs.python.org/issue15881#msg170215
    # See: https://groups.google.com/forum/#!topic/nose-users/fnJ-kAUbYHQ
    # If this can be removed and the tests pass on Python 2.6, hooray!
    import multiprocessing
except ImportError:
    pass
else:
    del multiprocessing


def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    here = os.path.abspath(os.path.dirname(__file__))

    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

VERSION = find_version('utcdatetime', '__init__.py')


def get_install_requires():
    # This is a good place to do conditional requirements, for example
    # on Python 2.6 there's no OrderedDict class, so we could detect that
    # and add the `ordereddict` dependency.
    dependencies = []
    return dependencies

setup(
    name='utcdatetime',
    packages=find_packages(),
    version=VERSION,
    description='Simple UTC datetimes using RFC3339 subset of ISO8601.',
    author='Paul M Furley',
    author_email='paul@paulfurley.com',
    url='https://github.com/paulfurley/utcdatetime',
    download_url=('https://github.com/paulfurley/utcdatetime/tarball/{0}'
                  .format(VERSION)),
    install_requires=get_install_requires(),
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
