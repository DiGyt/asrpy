# ASRpy
Artifact Subspace Reconstruction for Python


- [Introduction](#introduction)
- [Installation](#installation)
- [Examples](#examples)
- [Documentation](#documentation)


## Introduction

Artifact subspace reconstruction (ASR) is an automated, online,
component-based artifact removal method for removing transient or
large-amplitude artifacts in multi-channel EEG recordings (Kothe & Jung, 
2016). This repository provides a Python implementation of the standard 
ASR algorithm, similar to the original MATLAB implementation in EEGLab's 
[`clean_rawdata`](https://github.com/sccn/clean_rawdata) plugin.
As of now, this repository only implements the standard version of 
the ASR algorithm. A valid version of the improved _riemannian_ ASR 
(Blum et al., 2019) might be added in the future.

This implementation aims to follow the original ASR algorithm as close 
as possible. Using the according parameters, it should be perfectly 
equivalent to the original implementation, except for a few imprecisions
introduced by different solvers implemented in Python and MATLAB, e.g. 
when calculating the eigenspace. However, this implementation is 
based on [python_meegkit](https://github.com/nbara/python-meegkit). 
For an alternative implementation check their repository.

#### References

- Kothe, C. A. E., & Jung, T. P. (2016). U.S. Patent Application No. 
14/895,440. https://patents.google.com/patent/US20160113587A1/en
- Blum, S., Jacobsen, N. S. J., Bleichner, M. G., & Debener, S. (2019). 
A Riemannian Modification of Artifact Subspace Reconstruction for EEG 
Artifact Handling. Frontiers in Human Neuroscience, 13. 
https://doi.org/10.3389/fnhum.2019.00141
   
   
## Installation

You can install the latest ASRpy release using:
```
pip install asrpy
```
or install the current working version directly from GitHub, using:
```
pip install git+https://github.com/DiGyt/asrpy.git
```


## Examples

ASRpy applies the Artifact Subspace Reconstruction method directly to MNE-Python's `mne.io.Raw` objects. It's usage should be as simple as:
```python
import asrpy
asr = asrpy.ASR(sfreq=raw.info["sfreq"], cutoff=20)
asr.fit(raw)
raw = asr.transform(raw)
```

To get started, we recommend going through the [example notebook](https://github.com/DiGyt/asrpy/blob/main/example.ipynb). You can simply run them via your internet browser (on Google Colab's hosted runtime) by clicking the  button below.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DiGyt/asrpy/blob/main/example.ipynb)


## Documentation

The ASRpy documentation is created using [pdoc3](https://pdoc3.github.io/pdoc/) and [GitHub Pages](https://pages.github.com/). Click on the link below to view the documentation.

[Documentation](https://digyt.github.io/asrpy/)

In most Python IDEs, you can also read them by e.g. typing `asrpy.ASR?`


<!-- 
Note for myself: build the documentation with:
cd . #asrpy head dir
pdoc3 --html --output-dir docs asrpy -f -c sort_identifiers=False

Second Note: Deploy on PyPI like:
git clone https://github.com/DiGyt/asrpy.git
pip install asrpy/.
rm -rf dist
python asrpy/setup.py sdist
python asrpy/setup.py bdist_wheel
pip install twine
twine check dist/*
twine upload dist/*
-->





