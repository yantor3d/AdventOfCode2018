from setuptools import setup


setup(
    name='Advent of Code 2018',
    version='0.1.0',
    description='Solutions to the 2018 Advent of Code programming challenge',
    long_description='Solutions to the 2018 Advent of Code programming challenge',
    author='Ryan Porter',
    url='https://adventofcode.com/2018',
    download_url='https://github.com/yantor3d/AdventOfCode2018',
    license='License :: Free For Educational Use ',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Other Audience',
        'Programming Language :: Python :: 3.7',
        'License :: Free For Educational Use ',
    ],
    keywords='',
    packages=['aoc'],
    package_data={
        'aoc': ['data/*.bat']
    },
    include_package_data=True,
    install_requires=['']
)
