# preprocessmzML

A simple python package for preprocessing mzML spectra using various filters and normalization techniques derived from the fantastic `pyopenms` package. This package supports baseline correction, smoothing, centroiding, and normalization of spectra from MALDI-TOF mass spectrometers.

## Features
- **Baseline Correction**: Remove baseline using MorphologicalFilter
- **Smoothing**: Smooth the spectrum using Savitzky-Golay filter
- **Centroiding**: Pick peaks with PeakPickerHiRes
- **Normalization**: Normalize spectra with different methods (TIC, To the most intense peak)

## Installation

### Prerequisites
- Python 3.6 or higher
- `pip` (Python package installer)

### macOS or Linux systems
1. Create and activate a virtual environment:

```bash
python3 -m venv preprocess_mzml
source venv/bin/activate
```

2. Install the package:

```bash
pip install preprocessmzML
``` 

### Windows
1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```
2. Install the package:

```bash
pip install preprocessmzML
```

To install the package, use the following command:

```bash
pip install preprocessmzML
```

## Usage

After installing the package, you can preprocess your mzML files from the command line (in a virtual environment as described above). I highly recommend running this workflow within a virtual environment to tackle version conflicts of modules used in this package.

### Command-Line Interface (CLI)
```bash
preprocess_mzml --data_dir /path/to/mzML/files --output_base_dir /path/to/output/directory
```

## Troubleshooting
If you encounter issues, please check the following:
- Ensure that the mzML files are correctly formatted and accessible.
- Verify that the output directory is writable.
- Check the parameter combinations for any invalid values.

## Contributing
Contributions are always welcome. Feel free to submit a pull request or open an issue on Github.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Bharath Nair
bharath@palaeome.org; bn317@cam.ac.uk

## Acknowledgements
- `pyopenms`
- `pandas`
- `numpy`
- `matplotlib`


This `README.md` includes:

- A brief introduction to the package and its features.
- Installation instructions.
- Usage examples.
- Detailed function documentation.
- Contribution guidelines.
- License information.
- Author information.
- Acknowledgements for dependencies.
