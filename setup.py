from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='hostel_management',
    version=version,
    description='Boys Hostel',
    author='Webnotes',
    author_email='rohit.w@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
