#!/usr/bin/env python3

from setuptools import setup

setup(
    name='nbp',
    version='0.1.0',
    description='N-Body Physics Simulator',
    author='Stephan Meijer',
    author_email='me@stephanmeijer.com',
    url='https://github.com/N-BodyPhysicsSimulator/Main',
    license='GPL-3.0',
    packages=['nbp'],
    install_requires=[
        'numpy',
        'websockets'
    ],
)
