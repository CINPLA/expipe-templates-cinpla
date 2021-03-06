# -*- coding: utf-8 -*-
from setuptools import setup
import os


from setuptools import setup, find_packages

long_description = open("README.md").read()

setup(name="expipe_templates_cinpla",
      packages=find_packages(),
      version='1.0',
      include_package_data=True,
      author="CINPLA",
      author_email="",
      maintainer="Mikkel Elle Lepperød",
      maintainer_email="m.e.lepperod@medisin.uio.no",
      long_description=long_description,
      url="https://github.com/CINPLA/expipe-templates-cinpla",
      platforms=['Linux', "Windows"],
      description="",
      classifiers=['Development Status :: Alpha',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: GPLv2 License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 2,3',
                   'Topic :: Scientific/Engineering :: Bio-Informatics'
                   ],
      )
