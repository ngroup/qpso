from setuptools import setup, find_packages
import codecs
import os
import re


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


long_description = read('README.md')


setup(
    name='qpso',

    version=find_version('qpso/__init__.py'),

    description='A Python implementation of quantum particle swarm optimization (QPSO).',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/ngroup/qpso',

    author='Chun Nien',

    author_email='contact@chunnien.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='optimization qpso swarm',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['numpy'],

)
