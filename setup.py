from setuptools import setup, find_packages

def parse_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name = 'csgoprices',
    version = '0.1.0',
    packages = find_packages(),
    install_requires = parse_requirements(),
    author = 'Kyle Stevenson',
    author_email = 'kyle@kylestevenson.me',
    description = 'This package can be used to resolve CS:GO item prices from the Steam Market.',
    keywords = 'csgo item prices steam api',
    license = 'MIT',
    url = 'https://github.com/kylestev/csgoprices'
)
