from setuptools import setup

setup(
    name='snapshotalyzer-5000',
    version='0.1',
    author='Karla Valcárcel Martínez',
    author_email='karla.valcarcel@gmail.com',
    description='SnapshotAlyzer 5000 is a tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/valkarls/snapshotalyzer-5000',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
