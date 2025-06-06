"""`eds.solid_tumor` pipeline"""

from typing import List, Optional

from spacy.tokens import Doc, Span

from edsnlp.core import PipelineProtocol
from edsnlp.pipes.base import SpanSetterArg
from edsnlp.pipes.core.contextual_matcher.models import FullConfig
from edsnlp.utils.numbers import parse_digit

from ..base import DisorderMatcher
from .patterns import default_patterns, metastasis_ct_scan


class SolidTumorMatcher(DisorderMatcher):
    """
    The `eds.solid_tumor` pipeline component extracts mentions of solid tumors. It will
    notably match:

    ??? info "Details of the used patterns"
        ```{ .python .no-check }
        # fmt: off
        --8<-- "edsnlp/pipes/ner/disorders/solid_tumor/patterns.py"
        # fmt: on
        ```

    Extensions
    ----------
    On each span `span` that match, the following attributes are available:

    - `span._.detailed_status`: set to either
        - `"METASTASIS"` for tumors at the metastatic stage
        - `"LOCALIZED"` else
    - `span._.assigned`: dictionary with the following keys, if relevant:
        - `stage`: stage of the tumor

    Examples
    --------
    ```python
    import edsnlp, edsnlp.pipes as eds

    nlp = edsnlp.blank("eds")
    nlp.add_pipe(eds.sentences())
    nlp.add_pipe(
        eds.normalizer(
            accents=True,
            lowercase=True,
            quotes=True,
            spaces=True,
            pollution=dict(
                information=True,
                bars=True,
                biology=True,
                doctors=True,
                web=True,
                coding=True,
                footer=True,
            ),
        ),
    )
    nlp.add_pipe(eds.solid_tumor())
    ```

    Below are a few examples:

    --8<-- "docs/assets/fragments/solid-tumor-examples.md"

    Parameters
    ----------
    nlp : Optional[PipelineProtocol]
        The pipeline
    name : Optional[str]
        The name of the component
    patterns: FullConfig
        The patterns to use for matching
    label : str
        The label to use for the `Span` object and the extension
    span_setter : SpanSetterArg
        How to set matches on the doc
    use_tnm : bool
        Whether to use TNM scores matching as well
    use_patterns_metastasis_ct_scan : bool
        Whether to use the metastasis patterns developed for the CT-Scans

    Authors and citation
    --------------------
    The `eds.solid_tumor` component was developed by AP-HP's Data Science team with a
    team of medical experts, following the insights of the algorithm proposed
    by [@petitjean_2024] and [@kempf:hal-03519085].

    """

    def __init__(
        self,
        nlp: Optional[PipelineProtocol],
        name: str = "solid_tumor",
        *,
        patterns: FullConfig = default_patterns,
        use_tnm: bool = False,
        use_patterns_metastasis_ct_scan: bool = False,
        label: str = "solid_tumor",
        span_setter: SpanSetterArg = {"ents": True, "solid_tumor": True},
    ):
        if use_patterns_metastasis_ct_scan:
            patterns.append(metastasis_ct_scan)

        super().__init__(
            nlp=nlp,
            name=name,
            patterns=patterns,
            detailed_status_mapping={
                1: "LOCALIZED",
                2: "METASTASIS",
            },
            label=label,
            span_setter=span_setter,
        )

        self.use_tnm = use_tnm

        if use_tnm:
            from edsnlp.pipes.ner.tnm.tnm import TNMMatcher

            self.tnm = TNMMatcher(nlp=nlp, attr="TEXT")

    def process_tnm(self, doc):
        spans = self.tnm.process(doc)
        spans = self.tnm.parse(spans)

        for span in spans:
            span.label_ = "solid_tumor"
            span._.source = "tnm"
            metastasis = span._.value.model_dump().get("metastasis", "0")
            if metastasis == "1":
                span._.status = 2
            yield span

    def process(self, doc: Doc) -> List[Span]:
        for span in super().process(doc):
            if (span._.source in ["metastasis", "metastasis_ct_scan"]) or (
                "metastasis" in span._.assigned.keys()
            ):
                span._.status = 2

            if "stage" in span._.assigned.keys():
                stage = parse_digit(
                    span._.assigned["stage"],
                    attr="NORM",
                    ignore_excluded=True,
                )
                if stage == 4:
                    span._.status = 2

            yield span

        if self.use_tnm:
            yield from self.process_tnm(doc)
