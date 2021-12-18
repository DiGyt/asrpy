import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "asrpy",
    version = "0.0.1",

    author = "Dirk Gütlin",
    author_email = "dirk.guetlin@gmail.com",
    description = ("Artifact Subspace Reconstruction in Python."),
    license = "BSD-3",
    keywords = "EEG MEG Signal Processing",
    url = "https://github.com/DiGyt/asrpy",
    packages=['asr'],
    include_package_data=True,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        "numpy",
        "scipy",
        "mne",
    ],
)
