from setuptools import setup, find_packages

setup(
        name = 'Crypt0Lib V1',
        version = "0.0.1",
        description = 'Version 1 - Cryptography Lib',
        license = "MIT",
        author = "Hamza Abderrahim - (Crypto)",
        packages = find_packages(),
        install_requires = ['hashlib','requests','cryptography','pycrypto'],
    )
