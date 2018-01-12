#!/usr/bin/env python
from setuptools import setup

setup(name='dlnap',
      version='0.14',
      description='Python over the network media player to playback on DLNA UPnP devices',
      author='cherezov',
      author_email='cherezov.pavel@gmail.com',
      url='https://github.com/cherezov/dlnap',
      license='MIT',
      platforms=['all'],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.5',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: Jython',
          'Programming Language :: Python :: Implementation :: PyPy',
      ],
      py_modules=['dlnap'],
      install_requires=[
          'xmltodict>=0.11.0',
      ],
)
