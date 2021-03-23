from setuptools import setup, find_packages

setup(
    name='package1',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    author='Michael',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/samplemod',
    packages=find_packages(exclude=('tests', 'docs'))
)
