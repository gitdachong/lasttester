#coding:utf-8
from setuptools import setup, find_packages
from lasttester import __author__,__version__,__contact__
import sys
import os


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()



with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "lasttester",
    version = __version__,
    keywords = ["lasttester", "automatic test","online monitoring", "test data preparation", "continuous integration"],
    description = "LastTester is a  multiple protocols,powerful and easy to expand test lib,it is applicable to back-end automatic test, test data preparation, online monitoring, continuous integration and other scenarios",
    long_description = long_description,
    long_description_content_type='text/markdown',
    license = "MIT Licence",
    url = "https://github.com/gitdachong/lasttester",
    project_urls={
        "Bug Tracker": "https://github.com/gitdachong/lasttester",
        "Documentation": "https://github.com/gitdachong/lasttester",
        "Source Code": "https://github.com/gitdachong/lasttester",
    },
    author = __author__,
    author_email = __contact__,

    packages = find_packages(),
    package_data={'': ['LICENSE'], 'lasttester': ['*.mo','*.po']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'requests'
    ]
)
