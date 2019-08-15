# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
#import pydiderotlib

setup(
    name='pydiderotlib',
    version='0.0.1',
    packages=find_packages(),
    packages_dir = {'' : 'pydiderotlib'},
    author='Professeurs de Mathématiques du lycée Denis Diderot (Marseille)',
    description="Librairies utilisées dans l'enseignement de l'informatique",
    url='',
    download_url='https://github.com/cspaier/',
    license='MIT',
    keywords = ["python", "teaching"],
        classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Topic :: Teaching",
    ],
    install_requires=[
          'pygame',
      ],
    long_description=open('README.md').read(),
    # Active la prise en compte du fichier MANIFEST.in
    include_package_data=True,
    )
