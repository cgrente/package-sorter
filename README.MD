# Package Sorter

Solution to Smarter Technology's robotic package dispatch challenge.

## Problem

Given a package's dimensions (width, height, length in cm) and mass (kg), dispatch it to the correct stack:

- **STANDARD**: not bulky and not heavy
- **SPECIAL**: bulky or heavy (but not both)
- **REJECTED**: both bulky and heavy

A package is **bulky** if its volume is >= 1,000,000 cm3 or any single dimension is >= 150cm.
A package is **heavy** if its mass is >= 20 kg.

## Requirements

- Python 3.10+
- pytest (for running tests)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install pytest
```

## Usage

```python
from package_sorter import sort

sort(10, 10, 10, 5)     # "STANDARD"
sort(200, 10, 10, 5)    # "SPECIAL" (bulky by dimension)
sort(10, 10, 10, 25)    # "SPECIAL" (heavy)
sort(200, 200, 200, 25) # "REJECTED" (both)
```

## Running Tests

```bash
pytest
```

## Project structure
```
package-sorter/
|-- README.MD
|-- package_sorter.py
|-- tests/
    |-- test_package_sorter.py
```

## Design notes

- Thresholds are extracted as module-level constants for clarity and easy adjustment.
- Input validation rejects non-positive dimensions and negative mass with descriptive errors.
- The sorting logic checks the most restrictive case (REJECTED) first, then falls through.