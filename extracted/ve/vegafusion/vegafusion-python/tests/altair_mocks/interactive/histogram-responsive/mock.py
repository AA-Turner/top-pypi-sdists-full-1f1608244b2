# https://altair-viz.github.io/gallery/histogram_responsive.html

import altair as alt
from vega_datasets import data

source = data.flights_5k.url

brush = alt.selection_interval(encodings=["x"])

base = (
    alt.Chart(source)
    .transform_calculate(time="hours(datum.date) + minutes(datum.date) / 60")
    .mark_bar()
    .encode(y="count():Q")
    .properties(width=600, height=100)
)

alt.vconcat(
    base.encode(
        alt.X(
            "time:Q",
            bin=alt.Bin(maxbins=30, extent=brush),
            scale=alt.Scale(domain=brush),
        )
    ),
    base.encode(
        alt.X("time:Q", bin=alt.Bin(maxbins=30)),
    ).add_selection(brush),
)
