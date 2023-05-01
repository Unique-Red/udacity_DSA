try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Noah Useghan',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'vnoah410@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['gothons'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)