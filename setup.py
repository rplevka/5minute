
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()


def get_version():
    VERSIONFILE = path.join('vminute', '__init__.py')
    initfile_lines = open(VERSIONFILE, 'rt').readlines()
    VSRE = r"^__version__ ?= ?['\"]([^'\"]*)['\"]"
    for line in initfile_lines:
        mo = re.search(VSRE, line, re.M)
        if mo:
            return mo.group(1)
    raise RuntimeError('Unable to find version string in %s.' % (VERSIONFILE,))


setup(
    name='5minute',
    version=get_version(),
    description='A tool for quick creation and deployment of Openstack machines used for QA testing.',
    long_description=long_description,
    url='https://github.com/SatelliteQE/5minute',
    author='Martin Korbel',
    author_email='mkorbel@redhat.com',
    license='GNU General Public License v2 (GPLv2)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Quality Assurance',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    keywords='openstack testing deployment',
    install_requires=['python-keystoneclient',
                      'python-cinderclient',
                      'python-heatclient',
                      'python-neutronclient',
                      'python-novaclient',
                      'xmltodict',
                      'prettytable'],
    packages=find_packages(),
    package_data={
        'vminute': ['scenarios/README']
    },
    entry_points={
        'console_scripts': [
            '5minute=vminute:main_main'
        ]
    }
)
