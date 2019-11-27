from setuptools import setup

setup(
    name='ui-tests',
    version='0.0.2',
    packages=['uitests'],
    install_requires=['behave==1.2.6', 'selenium==3.14.0' ,'PyHamcrest==1.9.0'],
    url='',
    license='',
    author='monte',
    author_email='',
    description='Automated UI tests for google or facebook, selenium needs 3.4 ++'
)
