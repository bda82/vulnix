# This should be only one line. If it must be multi-line, indent the second
# line onwards to keep the PKG-INFO file format intact.
"""Scans a Nix store for derivations that are affected by vulnerabilities."""

from setuptools import setup, find_packages
import os.path


def project_path(*names):
    return os.path.join(os.path.dirname(__file__), *names)

with open(project_path('VERSION')) as f:
    version = f.read().strip()

long_description = []

for rst in ['README.rst', 'HACKING.rst', 'CHANGES.rst']:
    with open(project_path(rst)) as f:
        long_description.append(f.read())

setup(
    name='vulnix',
    version=version,
    install_requires=[
        'click==6.7',
        'colorama==0.3.9',
        'lxml==3.8.0',
        'pyyaml==3.12',
        'requests==2.18.3',
        'ZODB==5.2.4',
    ],
    extras_require={
        'test': [
            'flake8>=2.5',
            'pytest>=3.2',
            'pytest-catchlog>=1.2',
            'pytest-codecheckers>=0.2',
            'pytest-cov>=2.5',
            'pytest-timeout>=1.2',
        ],
    },
    entry_points="""
        [console_scripts]
            vulnix = vulnix.main:main
    """,
    author='Flying Circus Internet Operations GmbH',
    author_email='mail@flyingcircus.io',
    license='BSD-3-Clause',
    url='https://github.com/flyingcircusio/vulnix',
    keywords='security',
    classifiers="""\
License :: OSI Approved :: BSD License
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3 :: Only
"""[:-1].split('\n'),
    description=__doc__.strip(),
    long_description='\n\n'.join(long_description),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False
)
