import os
from setuptools import setup, find_packages


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# read version from asrpy/__init__.py
with open("asrpy/__init__.py") as f:
    version = re.search(r'__version__ = "(.*)"', f.read()).group(1)

setup(
    name = "asrpy",
    version = version,

    author = "Dirk Gütlin",
    author_email = "dirk.guetlin@gmail.com",
    description = ("Artifact Subspace Reconstruction in Python."),
    license = "BSD-3",
    keywords = "EEG MEG Signal Processing",
    url = "https://github.com/DiGyt/asrpy",
    package_dir = {"":"."},
    packages = find_packages(),
    include_package_data=True,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
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
