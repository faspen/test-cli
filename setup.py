from setuptools import setup
setup(
    name = 'test-cli',
    version = '0.1.0',
    packages = ['console'],
    entry_points = {
        'console_scripts': [
	    'console = console.__main__:main'
	]
    })
