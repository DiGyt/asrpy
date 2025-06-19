# Authors:  Dirk Gütlin <dirk.guetlin@gmail.com>
#
# License: BSD (3-clause)
import os.path as op

import numpy as np
from scipy.io import loadmat

from asrpy import ASR, asr_calibrate, asr_process
from mne.io import read_raw_eeglab
from mne.datasets import testing

# set paths
current_dir = op.dirname(__file__)
data_path = op.join(testing.data_path(download=True), 'EEGLAB')
eeg_fname = op.join(data_path, 'test_raw.set')
valid_data_path = op.abspath(op.join(current_dir, 'data',
                                     'matlab_asr_data.mat'))


def tes_asr():  # TODO: MNE DATA HAS CHANGED; SO THIS TEST DOESNT WORK ANYMORE
    """Test whether ASR correlates sufficiently with original version."""
    valid_data = loadmat(valid_data_path)["data"][0][0][0]
    raw = read_raw_eeglab(eeg_fname, preload=True)

    # calculate clean data using ASR
    asr = ASR(sfreq=raw.info["sfreq"], cutoff=2.5, blocksize=10, win_len=0.5,
              win_overlap=0.66, max_dropout_fraction=0.1,
              min_clean_fraction=0.25, ab=None)
    asr.fit(raw)
    cleaned = asr.transform(raw, lookahead=0.25, stepsize=32,
                            maxdims=0.66)

    # check if the data is highly equal to the MATLAB data
    corrs = [np.corrcoef(i, j)[0, 1] for (i, j) in zip(cleaned.get_data(), valid_data)]
    assert np.mean(corrs) > 0.94

def test_asr_calibrate():
    # Generate some random data
    X = np.random.randn(10, 1000)
    
    # Run the calibration
    M, T = asr_calibrate(X, sfreq=100)
    
    # Ensure the output shapes are correct
    assert M.shape == (10, 10)
    assert T.shape == (10, 10)

def test_asr_process():
    # Generate some random data
    X = np.random.randn(10, 1000)
    
    # Calibrate the ASR
    M, T = asr_calibrate(X, sfreq=100)
    
    # Run the ASR processing
    cleaned = asr_process(X, sfreq=100, M=M, T=T)
    
    # Ensure the output shape is correct
    assert cleaned.shape == X.shape

