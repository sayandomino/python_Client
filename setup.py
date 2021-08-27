from setuptools import setup
import re

PACKAGE_NAME = 'Client'

setup(
    name='python_client',
    version='1.0.0',
    author='Domino Data Lab',
    author_email='support@dominodatalab.com',
    packages=[PACKAGE_NAME],
    scripts=[],
    url='http://www.dominodatalab.com',
    license='LICENSE.txt',
    description='Python Client',
    long_description='',
    install_requires=[
        'requests>=2.4.2',
        'bs4==0.*,>=0.0.1',
        'polling2'
    ],
    extras_require={
        "airflow":  ['apache-airflow==1.*,>=1.10'],
    }
)
