from setuptools import setup


setup(
    name='quandl-py',
    packages = ['quandl-py'],
    description='simple Quandl python wrapper',
    version = 0.1.1,
    author = 'Alex Takata',
    url = 'https://github.com/ack8006/quandl-py',
    license = 'MIT',
    keywords = 'Quandl Python Wrapper',
    install_requires = [
        'pandas >= 0.14',
        'requests',
    ]
)
