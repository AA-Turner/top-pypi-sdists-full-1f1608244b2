import os
from tempfile import mkdtemp, mkstemp

import pytest

from rdflib import RDF, RDFS, BNode, URIRef, Variable, plugin
from rdflib.graph import Dataset, QuotedGraph

implies = URIRef("http://www.w3.org/2000/10/swap/log#implies")
testN3 = """
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix : <http://test/> .
{:a :b :c;a :foo} => {:a :d :c,?y}.
_:foo a rdfs:Class.
:a :d :c."""  # noqa: N816


# Thorough test suite for formula-aware store


def checkFormulaStore(store="default", configString=None):  # noqa: N802, N803
    try:
        g = Dataset(store=store)
    except ImportError:
        pytest.skip("Dependencies for store '%s' not available!" % store)

    if configString:
        g.destroy(configString)
        g.open(configString)
    else:
        if store == "SQLite":
            _, path = mkstemp(prefix="test", dir="/tmp", suffix=".sqlite")
            g.open(path, create=True)
        else:
            g.open(mkdtemp(), create=True)

    g.parse(data=testN3, format="n3")
    try:
        for s, p, o in g.triples((None, implies, None)):
            formulaA = s  # noqa: N806
            formulaB = o  # noqa: N806

        assert type(formulaA) is QuotedGraph and type(formulaB) is QuotedGraph
        # a = URIRef('http://test/a')
        b = URIRef("http://test/b")
        c = URIRef("http://test/c")
        d = URIRef("http://test/d")
        v = Variable("y")

        universe = Dataset(g.store)

        # test formula as terms
        assert len(list(universe.triples((formulaA, implies, formulaB)))) == 1

        # test variable as term and variable roundtrip
        assert len(list(formulaB.triples((None, None, v)))) == 1
        for s, p, o in formulaB.triples((None, d, None)):
            if o != c:
                assert isinstance(o, Variable)
                assert o == v
        s = list(universe.subjects(RDF.type, RDFS.Class))[0]
        assert isinstance(s, BNode)
        assert len(list(universe.triples((None, implies, None)))) == 1
        assert len(list(universe.triples((None, RDF.type, None)))) == 1
        assert len(list(formulaA.triples((None, RDF.type, None)))) == 1
        assert len(list(formulaA.triples((None, None, None)))) == 2
        assert len(list(formulaB.triples((None, None, None)))) == 2
        assert len(list(universe.triples((None, None, None)))) == 3
        assert len(list(formulaB.triples((None, URIRef("http://test/d"), None)))) == 2
        assert len(list(universe.triples((None, URIRef("http://test/d"), None)))) == 1

        # #context tests
        # #test contexts with triple argument
        # assert len(list(universe.contexts((a, d, c)))) == 1, \
        #                     [ct for ct in universe.contexts((a, d, c))]

        # FAIL: test.test_graph_formula.testFormulaStores('SQLite',)
        # --------------------------------------------------------------------
        # Traceback (most recent call last):
        #   File ".../site-packages/nose/case.py", line 197, in runTest
        #     self.test(*self.arg)
        #   File ".../test_graph_formula.py", line 80, in testFormulaStore
        #     [ct for ct in universe.contexts((a, d, c))]
        # AssertionError: [
        #     <Graph identifier=N52fd4417ef7641089b2e4045ef19ad87
        #        (<class 'rdflib.graph.Graph'>)>,
        #     <Graph identifier=_:Formula16 (<class 'rdflib.graph.Graph'>)>
        #     ]

        # Remove test cases
        universe.remove((None, implies, None))
        assert len(list(universe.triples((None, implies, None)))) == 0
        assert len(list(formulaA.triples((None, None, None)))) == 2
        assert len(list(formulaB.triples((None, None, None)))) == 2

        formulaA.remove((None, b, None))
        assert len(list(formulaA.triples((None, None, None)))) == 1
        formulaA.remove((None, RDF.type, None))
        assert len(list(formulaA.triples((None, None, None)))) == 0

        universe.remove((None, RDF.type, RDFS.Class))

        # remove_context tests
        universe.remove_context(formulaB)
        assert len(list(universe.triples((None, RDF.type, None)))) == 0
        assert len(universe) == 1
        assert len(formulaB) == 0

        universe.remove((None, None, None))
        assert len(universe) == 0

        g.close()
        if store == "SQLite":
            os.unlink(path)
        else:
            g.store.destroy(configString)
    except Exception:
        g.close()
        if store == "SQLite":
            os.unlink(path)
        else:
            g.store.destroy(configString)
        raise


def get_formula_stores_tests():
    pluginname = None

    for s in plugin.plugins(pluginname, plugin.Store):
        if s.name in (
            "Auditable",
            "Concurrent",
            "SPARQLStore",
            "SPARQLUpdateStore",
        ):
            continue
        if not s.getClass().formula_aware:
            continue
        yield checkFormulaStore, s.name


@pytest.mark.parametrize("checker, name", get_formula_stores_tests())
def test_formula_stores(checker, name) -> None:
    checker(name)
