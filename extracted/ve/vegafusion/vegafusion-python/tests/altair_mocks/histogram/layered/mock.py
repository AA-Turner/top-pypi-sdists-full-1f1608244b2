# https://altair-viz.github.io/gallery/layered_histogram.html

import altair as alt
import numpy as np
import pandas as pd

np.random.seed(42)

# Generating Data
source = pd.DataFrame(
    {
        "Trial A": np.random.normal(0, 0.8, 1000),
        "Trial B": np.random.normal(-2, 1, 1000),
        "Trial C": np.random.normal(3, 2, 1000),
    }
)

alt.Chart(source).transform_fold(
    ["Trial A", "Trial B", "Trial C"], as_=["Experiment", "Measurement"]
).mark_bar(opacity=0.3, binSpacing=0).encode(
    alt.X("Measurement:Q", bin=alt.Bin(maxbins=100)),
    alt.Y("count()", stack=None),
    alt.Color("Experiment:N"),
)
