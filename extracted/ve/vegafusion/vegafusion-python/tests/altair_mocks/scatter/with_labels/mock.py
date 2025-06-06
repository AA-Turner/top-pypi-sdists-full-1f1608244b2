# https://altair-viz.github.io/gallery/scatter_with_labels.html

import altair as alt
import pandas as pd

source = pd.DataFrame(
    {"x": [1, 3, 5, 7, 9], "y": [1, 3, 5, 7, 9], "label": ["A", "B", "C", "D", "E"]}
)

points = alt.Chart(source).mark_point().encode(x="x:Q", y="y:Q")

text = points.mark_text(align="left", baseline="middle", dx=7).encode(text="label")

points + text
