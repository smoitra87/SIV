try : 
    from setuptools import setup
except ImportError :
    from distutils.core import setup


config = {
    'description' : 'SIV Project JKS group CMU',
    'author' : 'Subhodeep Moitra',
    'url' : 'https://github.com/smoitra87/siv.git' ,
    'download_url' : 'https://github.com/smoitra87/.../downloads',
    'author_email' : 'subho@cmu.edu',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['siv'],
    'scripts' : [],
    'name' : 'siv'
}

setup(**config)

