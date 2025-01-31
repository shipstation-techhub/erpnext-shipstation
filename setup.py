# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpnext_shipping/__init__.py
from erpnext_shipstation import __version__ as version

setup(
	name='erpnext_shipstation',
	version=version,
	description='Shipstation Integration for ERPNext',
	author='Frappe',
	author_email='didals0521@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
