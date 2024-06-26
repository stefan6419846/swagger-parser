#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    name='swagger_parser',
    version='1.0.2.post1',
    description="Swagger parser giving useful informations about your swagger files",
    long_description=readme + '\n\n' + history,
    author="Cyprien Guillemot",
    author_email='cyprien.guillemot@gmail.com',
    url='https://github.com/Trax-air/swagger-parser',
    packages=[
        'swagger_parser',
    ],
    package_dir={'swagger_parser':
                 'swagger_parser'},
    include_package_data=True,
    install_requires=[
        'swagger-spec-validator>=2.0.2',
        'jsonschema>=2.5.1',
        'requests',
        'PyYAML>=5.2',
        'jinja2>=2.8',
    ],
    extras_require={
        'dev': [
            'pytest>=2.7.0',
            'flake8>=2.4.1',
            'Sphinx>=1.4.6',
            'furo',
        ],
    },
    license="MIT",
    zip_safe=False,
    keywords='swagger, parser, API, REST, swagger-parser',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ],
)
