#!/usr/bin/env python
from setuptools import setup, find_packages
import subprocess
import os

__doc__ = ("A collection of helpful add-ons for working with"
           " internationalization in Django")


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


install_requires = [
    'Django>=1.4',
]

version = (0, 1, 0, 'alpha')


def get_version():
    number = '.'.join(map(str, version[:3]))
    stage = version[3]
    if stage == 'final':
        return number
    elif stage == 'alpha':
        process = subprocess.Popen('git rev-parse HEAD'.split(), stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return number + '-' + stdout.decode('utf-8').strip()[:8]

setup(
    name='django-i18ntools',
    version=get_version(),
    author='Fusionbox, Inc.',
    author_email='programmers@fusionbox.com',
    description=__doc__,
    long_description=read('README.rst'),
    url='https://django-i18ntools.readthedocs.org/',
    license='BSD',
    packages=[package for package in find_packages() if package.startswith('i18ntools')],
    install_requires=install_requires,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)
