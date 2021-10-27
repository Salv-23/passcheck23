import setuptools


setuptools.setup(
    name='passcheck',
    version='0.0.1',
    author='Salvador Estrella',
    description='Simple program to check whether passwords are safe to use.',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['requests'],
)