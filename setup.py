from setuptools import setup

setup(
    name='Flask Chart',
    version='1.0',
    long_description=__doc__,
    packages=['flask-chart'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)
