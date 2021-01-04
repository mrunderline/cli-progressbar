from distutils.core import setup
from importlib import import_module


setup(
    name='cli_progressbar',
    packages=['cli_progressbar'],
    version=import_module('cli_progressbar').__version__,
    license='MIT',
    description='lightweight library to print progress bar in cli',
    author='Ali Madihi (mrunderline)',
    author_email='alimadihib@gmail.com',
    url='https://github.com/mrunderline/cli-progressbar',
    keywords=['cli', 'progressbar', 'console'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities'
    ],
)
