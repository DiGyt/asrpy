# asrpy
Artifact Subspace Reconstruction for Python

___
### Simplified Categorization for Eye Tracking in Python

- [Introduction](#introduction)
- [Installation](#installation)
- [Examples](#examples)
- [Documentation](#documentation)


## Introduction

#TODO


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
