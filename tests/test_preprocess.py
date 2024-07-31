import os
import pyopenms as oms
from preprocessmzML.preprocess import preprocess_spectrum, merge_preprocessed_spectra
from preprocessmzML.utils import get_param_combinations

def test_preprocess_spectrum():
    file_path = "/Users/bharathnair/Downloads/mzml/202_1.mzML"
    param_combination = {
        "MorphologicalFilter": {"struc_elem_length": 3.0, "struc_elem_unit": "Thomson", "method": "tophat"},
        "SavitzkyGolayFilter": {"polynomial_order": 2, "frame_length": 11},
        "PeakPickerHiRes": {"signal_to_noise": 2.0},
        "Normalizer": {"method": "to_TIC"}
    }
    output_dir = "/Users/bharathnair/Downloads/mzml"
    preprocessed_exp = preprocess_spectrum(file_path, param_combination, output_dir)
    assert preprocessed_exp is not None
    assert len(preprocessed_exp.getSpectra()) > 0

def test_get_param_combinations():
    param_grid = {
        'MorphologicalFilter': [{"struc_elem_length": 3.0, "struc_elem_unit": "Thomson", "method": "tophat"}],
        'SavitzkyGolayFilter': [{'polynomial_order': 2, 'frame_length': 7}],
        'PeakPickerHiRes': [{'signal_to_noise': 1.0}],
        'Normalizer': [{'method': 'to_one'}]
    }
    combinations = get_param_combinations(param_grid)
    assert len(combinations) == 1
