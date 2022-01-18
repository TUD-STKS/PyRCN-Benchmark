"""
Preprocessing utilities required to reproduce the results in the paper
'Template Repository for Research Papers with Python Code'.
"""
# Authors: Peter Steiner <peter.steiner@tu-dresden.de>,
# License: BSD 3 clause

import pandas as pd
from pandas import DataFrame


def ts2super(ts: DataFrame, n_lags: int, h: int):
    """
    Construction of supervised learning dataset (2D) from tim series (1D)
    ts: a dataframe with datetime index and a column with numeric values
    n_lags: number of lags to be used as inputs
    h: forecasting horizon
    """
    # Creating dataframe with lags
    lags = range(1, n_lags)
    data_super_lags = ts.assign(**{'{} (t-{})'.format(col, t): ts[col].shift(t)
                                   for t in lags for col in ts})
    # Reversing column orders in dataframe with lags
    data_super_lags = data_super_lags[data_super_lags.columns[::-1]]
    # Slicing dataframe with legs to get a single column with current values
    ts_at_zero = pd.DataFrame(data_super_lags.iloc[:, -1])
    # Creating dataframe with future values
    future = range(1, h + 1)
    data_super_future = ts_at_zero.assign(**{
        '{} (t+{})'.format(col, t): ts_at_zero[col].shift(-t)
        for t in future for col in ts_at_zero})
    # Joining lags and future values
    data_super = data_super_lags.join(data_super_future.iloc[:, 1:]).dropna()
    data_super = data_super.reset_index(drop=True)
    return data_super
