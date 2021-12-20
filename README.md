# ASRpy
Artifact Subspace Reconstruction for Python

___
### Simplified Categorization for Eye Tracking in Python

- [Introduction](#introduction)
- [Installation](#installation)
- [Examples](#examples)
- [Documentation](#documentation)


## Introduction

Artifact subspace reconstruction (ASR) is an automated, online,
component-based artifact removal method for removing transient or
large-amplitude artifacts in multi-channel EEG recordings [1]. This
repository provides a Python implementation of the standard ASR 
algorithm, similar to the original MATLAB implementation in EEGLab's 
[`clean_rawdata`](https://github.com/sccn/clean_rawdata) plugin.

As of now, this repository only implements the standard version of 
the ASR algorithm. A valid version of the improved _riemannian_ ASR [2] 
might be added in the future.

___

[1] Kothe, C. A. E., & Jung, T. P. (2016). U.S. Patent Application No.
   14/895,440. https://patents.google.com/patent/US20160113587A1/en
   
[2] Blum, S., Jacobsen, N. S. J., Bleichner, M. G., & Debener, S. 
(2019). A Riemannian Modification of Artifact Subspace Reconstruction
   for EEG Artifact Handling. Frontiers in Human Neuroscience, 13.
   https://doi.org/10.3389/fnhum.2019.00141
   
   
## Installation

Currently, the way to install the package is:
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

Please refer to the ASRpy function Docstrings for documentation. In most Python IDEs, you can read them by e.g. typing `asrpy.ASR?`

The following functions/objects are available.

Main API:
```python
asrpy.ASR
asrpy.ASR.fit
asrpy.ASR.transform
```

MATLAB-like functions (similar to EEGLab's clean_rawdata).
```python
asrpy.asr_calibrate
asrpy.asr_process
```

Helper functions.
```python
asrpy.clean_windows
```
