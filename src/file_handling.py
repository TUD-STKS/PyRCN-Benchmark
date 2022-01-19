"""
File handling utilities required to reproduce the results in the paper
'Template Repository for Research Papers with Python Code'.
"""
# Authors: Peter Steiner <peter.steiner@tu-dresden.de>,
# License: BSD 3 clause

import pandas as pd
from joblib import dump, load


def load_data(filename):
    return pd.read_csv(filename)


def export_results(results, filename):
    """Store the results as a csv file."""
    df = pd.DataFrame.from_dict(results)
    df.to_csv(filename, sep=',', index=False)
