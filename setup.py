#!/usr/bin/env python

### this is inspired by Pyglet file

from setuptools import setup, find_packages

VERSION = '1.0.0'

long_description = '''pdftex backend for matplotlib (Linux only)'''

excluded = []


def exclude_package(pkg):
    for exclude in excluded:
        if pkg.startswith(exclude):
            return True
    return False


def create_package_list(base_package):
    return ([base_package] +
            [base_package + '.' + pkg
             for pkg
             in find_packages(base_package)
             if not exclude_package(pkg)])


setup_info = dict(
    # Metadata
    name='pdftex',
    version=VERSION,
    author='Farshid Varno',
    author_email='fr.varno@gmail.com',
    url='https://github.com/fvarno/PDFTex',
    download_url='https://github.com/fvarno/PDFTex.git',
    description='pdftex backend for matplotlib',
    long_description=long_description,
    license='GNU General Public License v3.0',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha ',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Text Processing :: Markup :: LaTeX',
        'Framework :: Matplotlib',
    ],

    # Package info
    packages=create_package_list('pdftex'),

    install_requires=[
        'matplotlib',
        'pillow'
      ],

    # Add _ prefix to the names of temporary build dirs
    options={
        'build': {'build_base': '_build'},
        #        'sdist': {'dist_dir': '_dist'},
    },
    zip_safe=True,
)

setup(**setup_info)