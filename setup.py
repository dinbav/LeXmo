"""Setup for the LeXmo package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Dina Bavli",
    author_email="din.bavli@gmail.com",
    name='LeXmo',
    license="Attribution-NonCommercial 4.0 International",
    description='LeXmo is a python package for emotion classification.',
    version='v0.0.1',
    long_description=README,
    url='https://github.com/dinbav/LeXmo',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=["pandas","nltk", "requests"],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers and Researchers',
    ],
)
