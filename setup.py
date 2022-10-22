from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

with open('LICENSE', 'r') as f:
    license_text = f.read()

setup(
    name='nclcmaps',
    version='0.3',
    author='Andreas Kvas',
    description='Use NCL color tables in Python',
    install_requires=['matplotlib'],
    packages=['nclcmaps'],
    package_data={'nclcmaps': ['data/ncl_colormaps.tar']},
    license=license_text
)
