# -*- coding: utf-8 -*-

# Third
from setuptools import find_packages, setup
from __version__ import version

__description__ = 'Api Flask'
__long_description__ = 'API de usuario usando FLASK'

__author__ = 'Jonas A.'
__author_email__ = 'jonasalmeidasaraiva@gmail.com'

testing_extras = [
    'pytest',
    'pytest-cov',
]

setup(
    name='api',
    version=version,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/JASaraiva/FlaskAPI.git',
    keywords='API, MongoDB',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
)
