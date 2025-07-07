from setuptools import setup, find_packages

setup(
    name='carbonswipe',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    author='Raj Budigam',
    description='Track energy, CO2, and water use from local LLM inference.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rajbudigam/CarbonSwipe',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)