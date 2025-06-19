# -*- coding: utf-8 -*-
# (c) Dirk Gütlin, 2021. <dirk.guetlin@gmail.com>
#
# License: BSD-3-Clause
"""
Welcome to the ASRpy documentation.

ASR (Artefact Subspace Reconstruction) is a widely used automated cleaning
algorithm for EEG data. This version of ASR is implemented to easily
integrate with the MNE-Python toolbox for M/EEG analysis.

You find the documentation to all available functions by clicking on
the respective submodules.

"""

__version__ = "0.0.5"

from .asr import ASR, asr_calibrate, asr_process, clean_windows  # noqa: F401
