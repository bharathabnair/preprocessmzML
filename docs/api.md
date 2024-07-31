# API Documentation

## Functions
#### set_filter_parameters
```python
set_filter_parameters(filter, parameters)
```
Set the parameters for a given filter.

**Args:**
- `filter (oms.Filter)`: The filter object to set parameters for.
- `parameters (dict)`: A dictionary of parameters where the key is the parameter name and the value is the parameter value.

**Example:**
```python
import pyopenms as oms
from preprocessmzML.filters import set_filter_parameters
filter = oms.MorphologicalFilter()
params = {"struc_elem_length": 3.0, "struc_elem_unit": "Thomson", "method": "tophat"}
set_filter_parameters(filter, params)
```

#### preprocess_spectrum
```python
preprocess_spectrum(file_path, param_combination, output_dir)
```
Preprocess an MS spectrum given a parameter combination and save output to a directory.

**Args:**
- `file_path (str)`: Path to the mzML file.
- `param_combination (dict)`: Dictionary of parameters for different filters.
- `output_dir (str)`: Directory to save the processed spectrum.

**Returns:**
- oms.MSExperiment: The preprocessed MS experiment.

**Example:**
```python
from preprocessmzML.preprocess import preprocess_spectrum

file_path = "path/to/file.mzML"
param_combination = {
    "MorphologicalFilter": {"struc_elem_length": 3.0, "struc_elem_unit": "Thomson", "method": "tophat"},
    "SavitzkyGolayFilter": {"polynomial_order": 2, "frame_length": 11},
    "PeakPickerHiRes": {"signal_to_noise": 2.0},
    "Normalizer": {"method": "to_TIC"}
}
output_dir = "path/to/output"
preprocessed_exp = preprocess_spectrum(file_path, param_combination, output_dir)
```

#### merge_preprocessed_spectra
```python
merge_preprocessed_spectra(preprocessed_experiments)
```
Merge multiple preprocessed spectra (within the three replicates) from a sample into one.

**Args:**
- `preprocessed_experiments (list)`: List of preprocessed MS experiments per sample. This assumes that the spectra for a sample is in the format (*sample01_1.mzML, sample01_2.mzML, sample01_3.mzML*).

**Returns:**
- `oms.MSExperiment`: The merged MS experiment.

**Example:**
```python
from preprocessmzML.preprocess import preprocess_spectrum

file_path = "path/to/file.mzML"
param_combination = {
    "MorphologicalFilter": {"struc_elem_length": 3.0, "struc_elem_unit": "Thomson", "method": "tophat"},
    "SavitzkyGolayFilter": {"polynomial_order": 2, "frame_length": 11},
    "PeakPickerHiRes": {"signal_to_noise": 2.0},
    "Normalizer": {"method": "to_TIC"}
}
output_dir = "path/to/output"
preprocessed_exp = preprocess_spectrum(file_path, param_combination, output_dir)
```

#### plot_spectrum
```python
plot_spectrum(spectrum, title, save_path)
```
Plot a spectrum and save as an image (.png format).

**Args:**
- `spectrum (oms.MSSpectrum)`: The spectrum to plot.
- `title (str)`: Plot title.
- `save_path (str)`: Path to save the plot image.

#### get_param_combinations
```python
get_param_combinations(param_grid)
```

Generate all combinations of parameters from a parameter grid.

**Args:**
- `param_grid (dict)`: Dictionary of parameters to combine.

**Returns:**
- `list`: List of parameter combinations.

**Example:**
```python
from preprocessmzML.utils import get_param_combinations

param_grid = {
    'MorphologicalFilter': [{"struc_elem_length": 3.0, "struc_elem_unit": "Thomson", "method": "tophat"}],
    'SavitzkyGolayFilter': [{'polynomial_order': 2, 'frame_length': 7}],
    'PeakPickerHiRes': [{'signal_to_noise': 1.0}],
    'Normalizer': [{'method': 'to_one'}]
}
combinations = get_param_combinations(param_grid)
```