from setuptools import setup
import os
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    long_description = f.read()

setup(
    name='seaborn_table',
    version='1.3.0',
    description='SeabornTable reads and writes tables in '
                'csv and md and acts like a list and dict."',
    long_description=long_description,
    author='Ben Christenson',
    author_email='Python@BenChristenson.com',
    url='https://github.com/SeabornGames/SeabornTable',
    install_requires=[],
    extras_require={
    },
    packages=['seaborn.seaborn_table'],
    license='MIT License',
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'),
    entry_points='''
        [console_scripts]
        seaborn_table=seaborn.seaborn_table:cli_converter
    ''',
)
