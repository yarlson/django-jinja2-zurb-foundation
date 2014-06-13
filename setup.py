#/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name="django-jinja2-zurb-foundation",
    version="5.1.1",
    description="Django Jinja2 Zurb Foundation package.",
    author="Yar Kravtsov",
    author_email="yarlson@gmail.com",
    url="https://github.com/yarlson/django-jinja2-zurb-foundation",
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
    install_requires=[

    ],
    dependency_links=[
        "git+git://github.com/yarlson/django-jinja2-zurb-foundation.git#egg=django-jinja2-zurb-foundation"
    ]
)
