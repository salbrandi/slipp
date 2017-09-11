from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='slipp',
    packages=find_packages(),
    version='0.0.1',
    author='Salvador Brandi',
    author_email='salbrandi@gmail.com',
    url='https://github.com/salbrandi/slipp',
    download_url='https://github.com/salbrandi/slipp/archive/0.1.tar.gz',
    py_modules=['auth_fetcher', 'cli.py', 'updater.py'],
    description='A package for updating a playlist with songs from your "Song" list on Spotify',
    long_description=long_description,
    install_requires=[
                     'click',
                     'spotipy',
                     ],
    entry_points='''
        [console_scripts]
        slipp=slipp.cli:slipp
        ''',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='spotify song list play list public private music users'
)
