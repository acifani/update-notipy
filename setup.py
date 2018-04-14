import io
from setuptools import setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='update-notipy',
    version='0.1.2',
    url='https://github.com/acifani/update-notipy',
    license='BSD',
    author='Alessandro Cifani',
    author_email='alessandro.cifani@gmail.com',
    description='Update notifications for your python app',
    long_description=readme,
    py_modules=['update_notipy'],
    install_requires=['pkg_info', 'boxing>=0.1.4', 'semver', 'colored'],
    classifiers=[
        'Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python'
    ])
