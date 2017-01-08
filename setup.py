from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(
    # Basic package information:
    name='basicauth-py3',
    version='0.4',
    py_modules=('basicauth',),

    # Packaging options:
    zip_safe=False,
    include_package_data=True,

    # Package dependencies:
    install_requires=[],

    # Metadata for PyPI:
    author='Roman Levin',
    author_email='romanlevin@gmail.com',
    license='UNLICENSE',
    url='https://github.com/romanlevin/python-basicauth',
    keywords='python security basicauth http',
    description='An incredibly simple HTTP basic auth implementation.',
    long_description=open(normpath(join(dirname(abspath(__file__)), 'README.md'))).read()
)
