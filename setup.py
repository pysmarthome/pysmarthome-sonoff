from setuptools import setup, find_packages

setup(
    name='pysmarthome-sonoff',
    description='Sonoff plugin for pysmarthome',
    version='1.0.3',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'pysmarthome~=3.0',
        'sonoffreq',
    ],
    packages=find_packages(),
    url='https://github.com/filipealvesdef/pysmarthome-sonoff',
    zip_zafe=False,
)
