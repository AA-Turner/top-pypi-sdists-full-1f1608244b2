# -*- coding: utf-8 -*-
# Owlready2
# Copyright (C) 2013-2019 Jean-Baptiste LAMY
# LIMICS (Laboratoire d'informatique médicale et d'ingénierie des connaissances en santé), UMR_S 1142
# University Paris 13, Sorbonne paris-Cité, Bobigny, France

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, os, types, tempfile, subprocess, weakref, re, urllib.request, warnings, itertools
from io import StringIO
from collections import defaultdict, OrderedDict
from xml.sax.saxutils import escape
import datetime

from owlready2.util import *

class OwlReadyWarning                     (UserWarning): pass
class OwlReadyUndefinedIRIWarning         (OwlReadyWarning): pass
class OwlReadyOntologyIRIWarning          (OwlReadyWarning): pass
class OwlReadyMROWarning                  (OwlReadyWarning): pass
class OwlReadyGeneratedNameWarning        (OwlReadyWarning): pass
class OwlReadyDupplicatedNameWarning      (OwlReadyWarning): pass

class OwlReadyError(Exception): pass
class OwlReadySharedBlankNodeError(OwlReadyError): pass
class OwlReadyOntologyParsingError(OwlReadyError): pass
class OwlReadyInconsistentOntologyError(OwlReadyError): pass
class OwlReadyJavaError(OwlReadyError): pass




def to_literal(o):
  if isinstance(o, locstr) and o.lang: return str(o), "@%s" % o.lang
  datatype, unparser = _universal_datatype_2_abbrev_unparser.get(o.__class__) or (None, None)
  if datatype is None: raise ValueError("Cannot store literal '%s' of type '%s'!" % (o, type(o)))
  return unparser(o), datatype
  
def from_literal(o, d):
  if isinstance(d, str):
    if d.startswith("@"): return locstr(o, lang = d[1:])
    return o
  if d == 0: return o
  datatype, parser = _universal_abbrev_2_datatype_parser.get(d) or (None, None)
  if parser is None: raise ValueError("Cannot read literal of datatype %s!" % repr(d))
  return parser(o)

_universal_abbrev_2_iri = {}
_universal_iri_2_abbrev = {}
_next_abb = 1
def _universal_abbrev(iri):
  global _next_abb
  abb = _next_abb
  _next_abb += 1
  _universal_abbrev_2_iri[abb] = iri
  _universal_iri_2_abbrev[iri] = abb
  return abb

owlready_python_module    = _universal_abbrev("http://www.lesfleursdunormal.fr/static/_downloads/owlready_ontology.owl#python_module")
owlready_python_name      = _universal_abbrev("http://www.lesfleursdunormal.fr/static/_downloads/owlready_ontology.owl#python_name")

rdf_first                 = _universal_abbrev("http://www.w3.org/1999/02/22-rdf-syntax-ns#first")
rdf_rest                  = _universal_abbrev("http://www.w3.org/1999/02/22-rdf-syntax-ns#rest")
rdf_nil                   = _universal_abbrev("http://www.w3.org/1999/02/22-rdf-syntax-ns#nil")
rdf_type                  = _universal_abbrev("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")
rdf_domain                = _universal_abbrev("http://www.w3.org/2000/01/rdf-schema#domain")
rdf_range                 = _universal_abbrev("http://www.w3.org/2000/01/rdf-schema#range")
rdfs_subclassof           = _universal_abbrev("http://www.w3.org/2000/01/rdf-schema#subClassOf")
rdfs_subpropertyof        = _universal_abbrev("http://www.w3.org/2000/01/rdf-schema#subPropertyOf")
owl_class                 = _universal_abbrev("http://www.w3.org/2002/07/owl#Class")
owl_named_individual      = _universal_abbrev("http://www.w3.org/2002/07/owl#NamedIndividual")
owl_object_property       = _universal_abbrev("http://www.w3.org/2002/07/owl#ObjectProperty")
owl_data_property         = _universal_abbrev("http://www.w3.org/2002/07/owl#DatatypeProperty")
owl_annotation_property   = _universal_abbrev("http://www.w3.org/2002/07/owl#AnnotationProperty")
owl_inverse_property      = _universal_abbrev("http://www.w3.org/2002/07/owl#inverseOf")
owl_restriction           = _universal_abbrev("http://www.w3.org/2002/07/owl#Restriction")
owl_onproperty            = _universal_abbrev("http://www.w3.org/2002/07/owl#onProperty")
owl_onclass               = _universal_abbrev("http://www.w3.org/2002/07/owl#onClass")
owl_ondatarange           = _universal_abbrev("http://www.w3.org/2002/07/owl#onDataRange")
owl_cardinality           = _universal_abbrev("http://www.w3.org/2002/07/owl#cardinality")
owl_min_cardinality       = _universal_abbrev("http://www.w3.org/2002/07/owl#minCardinality")
owl_max_cardinality       = _universal_abbrev("http://www.w3.org/2002/07/owl#maxCardinality")
SOME                      = _universal_abbrev("http://www.w3.org/2002/07/owl#someValuesFrom")
ONLY                      = _universal_abbrev("http://www.w3.org/2002/07/owl#allValuesFrom")
EXACTLY                   = _universal_abbrev("http://www.w3.org/2002/07/owl#qualifiedCardinality")
MIN                       = _universal_abbrev("http://www.w3.org/2002/07/owl#minQualifiedCardinality")
MAX                       = _universal_abbrev("http://www.w3.org/2002/07/owl#maxQualifiedCardinality")
VALUE                     = _universal_abbrev("http://www.w3.org/2002/07/owl#hasValue")
owl_unionof               = _universal_abbrev("http://www.w3.org/2002/07/owl#unionOf")
owl_intersectionof        = _universal_abbrev("http://www.w3.org/2002/07/owl#intersectionOf")
owl_oneof                 = _universal_abbrev("http://www.w3.org/2002/07/owl#oneOf")
owl_equivalentclass       = _universal_abbrev("http://www.w3.org/2002/07/owl#equivalentClass")
owl_thing                 = _universal_abbrev("http://www.w3.org/2002/07/owl#Thing")
owl_alldisjointclasses    = _universal_abbrev("http://www.w3.org/2002/07/owl#AllDisjointClasses")
owl_alldifferent          = _universal_abbrev("http://www.w3.org/2002/07/owl#AllDifferent")
owl_members               = _universal_abbrev("http://www.w3.org/2002/07/owl#members")
owl_distinctmembers       = _universal_abbrev("http://www.w3.org/2002/07/owl#distinctMembers")

_universal_abbrev("http://www.w3.org/2000/01/rdf-schema#comment")
_universal_abbrev("http://www.w3.org/2000/01/rdf-schema#label")
_universal_abbrev("http://www.w3.org/2002/07/owl#FunctionalProperty")
_universal_abbrev("http://www.w3.org/2002/07/owl#InverseFunctionalProperty")

SPECIAL_ATTRS      = { "namespace",  "name", "_name", "iri", "_iri", "storid", "is_a", "equivalent_to", "_equivalent_to", "disjoint_with", "_disjoint_with", "defined_class", "_disjoint_unions", "__class__", "__qualname__", "__module__", "__doc__", "__bases__" }
SPECIAL_PROP_ATTRS = { "namespace",  "name", "_name", "python_name", "_python_name", "_domain", "_property_chain", "_inverse_property", "inverse_property", "inverse", "_range", "iri", "_iri", "storid", "is_a", "equivalent_to", "_equivalent_to", "disjoint_with", "_disjoint_with", "__class__", "__qualname__", "__module__", "__doc__", "__bases__" }


DONT_COPY_BN = Environment()

LOADING = Environment()
LOADING.__enter__() # Avoid creating triple when creating base classes like Thing


_universal_abbrev_2_datatype = {}
_universal_datatype_2_abbrev = {}

_universal_abbrev_2_datatype_parser   = {}
_universal_datatype_2_abbrev_unparser = {}

def _universal_abbrev_datatype(datatype, parser, unparser, *iris):
  abbs = [_universal_abbrev(iri) for iri in iris]
  _universal_datatype_2_abbrev         [datatype] =  abbs[0]
  _universal_datatype_2_abbrev_unparser[datatype] = (abbs[0], unparser or str)
  for abb in abbs:
    _universal_abbrev_2_datatype       [abb] =  datatype
    _universal_abbrev_2_datatype_parser[abb] = (datatype, parser or datatype)


def _bool_parser(s):
  return (s == "true") or (s == 1)
def _bool_unparser(b):
  if b: return "true"
  return "false"
def _number_unparser(x):
  return x

def _parse_date(s):
  try:
    r = datetime.date(*(int(i or "1") or 1 for i in s.rsplit("-", 2)))
  except:
    sys.excepthook(*sys.exc_info())
    return None
  return r

def _parse_datetime(s):
  for format in ["%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S.%f%z"]:
    try:    return datetime.datetime.strptime(s.replace(" ", "T"), format)
    except: pass
  raise ValueError("Cannot parse ISO datetime '%s'!" % s)

_universal_abbrev_datatype(int, None, _number_unparser, "http://www.w3.org/2001/XMLSchema#integer", "http://www.w3.org/2001/XMLSchema#byte", "http://www.w3.org/2001/XMLSchema#short", "http://www.w3.org/2001/XMLSchema#int", "http://www.w3.org/2001/XMLSchema#long", "http://www.w3.org/2001/XMLSchema#unsignedByte", "http://www.w3.org/2001/XMLSchema#unsignedShort", "http://www.w3.org/2001/XMLSchema#unsignedInt", "http://www.w3.org/2001/XMLSchema#unsignedLong", "http://www.w3.org/2001/XMLSchema#negativeInteger", "http://www.w3.org/2001/XMLSchema#nonNegativeInteger", "http://www.w3.org/2001/XMLSchema#positiveInteger")
_universal_abbrev_datatype(bool, _bool_parser, _bool_unparser, "http://www.w3.org/2001/XMLSchema#boolean")
_universal_abbrev_datatype(float, None, _number_unparser, "http://www.w3.org/2001/XMLSchema#decimal", "http://www.w3.org/2001/XMLSchema#double", "http://www.w3.org/2001/XMLSchema#float", "http://www.w3.org/2002/07/owl#real")
_universal_abbrev_datatype(str, None, None, "http://www.w3.org/2001/XMLSchema#string", "http://www.w3.org/2001/XMLSchema#QName", "http://www.w3.org/2001/XMLSchema#NOTATION")
_universal_abbrev_datatype(normstr, None, None, "http://www.w3.org/2001/XMLSchema#normalizedString", "http://www.w3.org/2001/XMLSchema#anyURI", "http://www.w3.org/2001/XMLSchema#Name", "http://www.w3.org/2001/XMLSchema#NCName", "http://www.w3.org/2001/XMLSchema#language", "http://www.w3.org/2001/XMLSchema#token", "http://www.w3.org/2001/XMLSchema#NMTOKEN", "http://www.w3.org/2001/XMLSchema#ID", "http://www.w3.org/2001/XMLSchema#IDREF", "http://www.w3.org/2001/XMLSchema#ENTITY")
_universal_abbrev_datatype(plainliteral, None, None, "http://www.w3.org/1999/02/22-rdf-syntax-ns#PlainLiteral")
_universal_abbrev_datatype(datetime.datetime,
                           _parse_datetime,
                           lambda dt: datetime.datetime.isoformat(dt, timespec='milliseconds'),
                           "http://www.w3.org/2001/XMLSchema#dateTime")
_universal_abbrev_datatype(datetime.date,
                           _parse_date,
                           datetime.date.isoformat, "http://www.w3.org/2001/XMLSchema#date")
_universal_abbrev_datatype(datetime.time,
                           lambda s: datetime.datetime.strptime(s, "%H:%M:%S").time(),
                           datetime.time.isoformat, "http://www.w3.org/2001/XMLSchema#time")
_universal_datatype_2_abbrev_unparser[FTS] = _universal_datatype_2_abbrev_unparser[str]

def _parse_duration(s):
  assert s.startswith("P")
  days = seconds = 0
  in_date = True
  for number, letter in re.findall(r"([0-9.]+)([A-Z]+)", s):
    number = float(number)
    letter0 = letter[0]
    if letter0 == "Y": days     +=  365.0 * number
    if letter0 == "D": days     +=          number
    if letter0 == "H": seconds  += 3600.0 * number
    if letter0 == "S": seconds  +=          number
    if letter0 == "M":
      if in_date:      days     +=   30.0 * number
      else:            seconds  +=   60.0 * number
    if "T" in letter: in_date = False
  return datetime.timedelta(days, seconds)

def _format_duration(td):
  return "P%sD%sS" % (td.days, td.seconds + td.microseconds / 1000000.0)

def _parse_base64(s):
  import base64
  return base64.b64decode(s)

def _format_base64(b):
  import base64
  return base64.b64encode(b).decode()

def set_datatype_iri(datatype, iri):
  unparser = _universal_datatype_2_abbrev_unparser[datatype][1]
  _universal_datatype_2_abbrev         [datatype] =  _universal_iri_2_abbrev[iri]
  _universal_datatype_2_abbrev_unparser[datatype] = (_universal_iri_2_abbrev[iri], unparser)

  
def declare_datatype(datatype, iri, parser, unparser):
  import sqlite3
  if iri in _universal_iri_2_abbrev: storid = _universal_iri_2_abbrev[iri]
  else:                              storid = _universal_abbrev(iri)
  from owlready2 import WORLDS
  for world in WORLDS:
    if (not world.graph.read_only):
      try:
        world.graph.execute("INSERT OR IGNORE INTO resources VALUES (?,?)", (storid, iri))
      except sqlite3.ProgrammingError: # World has been closed
        pass
      
  _universal_datatype_2_abbrev         [datatype] =  storid
  _universal_datatype_2_abbrev_unparser[datatype] = (storid, unparser)
  _universal_abbrev_2_datatype         [storid]   =  datatype
  _universal_abbrev_2_datatype_parser  [storid]   = (datatype, parser)
  return storid

def define_datatype_in_ontology(datatype, iri, ontology):
  storid = ontology.world._abbreviate(iri)
  ontology._add_obj_triple_spo(storid, rdf_type, rdfs_datatype)
  


owl_alldisjointproperties = _universal_abbrev("http://www.w3.org/2002/07/owl#AllDisjointProperties")
owl_equivalentproperty    = _universal_abbrev("http://www.w3.org/2002/07/owl#equivalentProperty")
owl_equivalentindividual  = _universal_abbrev("http://www.w3.org/2002/07/owl#sameAs")
owl_ontology              = _universal_abbrev("http://www.w3.org/2002/07/owl#Ontology")
owl_imports               = _universal_abbrev("http://www.w3.org/2002/07/owl#imports")
owl_nothing               = _universal_abbrev("http://www.w3.org/2002/07/owl#Nothing")
owl_axiom                 = _universal_abbrev("http://www.w3.org/2002/07/owl#Axiom")
owl_annotatedsource       = _universal_abbrev("http://www.w3.org/2002/07/owl#annotatedSource")
owl_annotatedproperty     = _universal_abbrev("http://www.w3.org/2002/07/owl#annotatedProperty")
owl_annotatedtarget       = _universal_abbrev("http://www.w3.org/2002/07/owl#annotatedTarget")
owl_complementof          = _universal_abbrev("http://www.w3.org/2002/07/owl#complementOf")
owl_disjointwith          = _universal_abbrev("http://www.w3.org/2002/07/owl#disjointWith")
owl_propdisjointwith      = _universal_abbrev("http://www.w3.org/2002/07/owl#propertyDisjointWith")
rdfs_datatype             = _universal_abbrev("http://www.w3.org/2000/01/rdf-schema#Datatype")
owl_ondatatype            = _universal_abbrev("http://www.w3.org/2002/07/owl#onDatatype")
owl_withrestrictions      = _universal_abbrev("http://www.w3.org/2002/07/owl#withRestrictions")
xmls_length               = _universal_abbrev("http://www.w3.org/2001/XMLSchema#length")
xmls_minlength            = _universal_abbrev("http://www.w3.org/2001/XMLSchema#minLength")
xmls_maxlength            = _universal_abbrev("http://www.w3.org/2001/XMLSchema#maxLength")
xmls_pattern              = _universal_abbrev("http://www.w3.org/2001/XMLSchema#pattern")
xmls_whitespace           = _universal_abbrev("http://www.w3.org/2001/XMLSchema#whiteSpace")
xmls_maxinclusive         = _universal_abbrev("http://www.w3.org/2001/XMLSchema#maxInclusive")
xmls_maxexclusive         = _universal_abbrev("http://www.w3.org/2001/XMLSchema#maxExclusive")
xmls_mininclusive         = _universal_abbrev("http://www.w3.org/2001/XMLSchema#minInclusive")
xmls_minexclusive         = _universal_abbrev("http://www.w3.org/2001/XMLSchema#minExclusive")
xmls_totaldigits          = _universal_abbrev("http://www.w3.org/2001/XMLSchema#totalDigits")
xmls_fractiondigits       = _universal_abbrev("http://www.w3.org/2001/XMLSchema#fractionDigits")
owl_propertychain         = _universal_abbrev("http://www.w3.org/2002/07/owl#propertyChainAxiom")

_universal_abbrev("http://www.w3.org/2002/07/owl#TransitiveProperty")
_universal_abbrev("http://www.w3.org/2002/07/owl#SymmetricProperty")
_universal_abbrev("http://www.w3.org/2002/07/owl#AsymmetricProperty")
_universal_abbrev("http://www.w3.org/2002/07/owl#ReflexiveProperty")
_universal_abbrev("http://www.w3.org/2002/07/owl#IrreflexiveProperty")
_universal_abbrev("http://www.w3.org/2002/07/owl#backwardCompatibleWith")
_universal_abbrev("http://www.w3.org/2002/07/owl#deprecated")
_universal_abbrev("http://www.w3.org/2002/07/owl#incompatibleWith")
_universal_abbrev("http://www.w3.org/2000/01/rdf-schema#isDefinedBy")
_universal_abbrev("http://www.w3.org/2002/07/owl#priorVersion")
_universal_abbrev("http://www.w3.org/2000/01/rdf-schema#seeAlso")
_universal_abbrev("http://www.w3.org/2002/07/owl#versionInfo")


HAS_SELF = _universal_abbrev("http://www.w3.org/2002/07/owl#hasSelf")

owlready_class_property_type = _universal_abbrev("http://www.lesfleursdunormal.fr/static/_downloads/owlready_ontology.owl#class_property_type")
owlready_defined_class       = _universal_abbrev("http://www.lesfleursdunormal.fr/static/_downloads/owlready_ontology.owl#defined_class")
rdf_property                 = _universal_abbrev("http://www.w3.org/1999/02/22-rdf-syntax-ns#Property")

swrl_variable                = _universal_abbrev("http://www.w3.org/2003/11/swrl#Variable")
swrl_imp                     = _universal_abbrev("http://www.w3.org/2003/11/swrl#Imp")
swrl_body                    = _universal_abbrev("http://www.w3.org/2003/11/swrl#body")
swrl_head                    = _universal_abbrev("http://www.w3.org/2003/11/swrl#head")
swrl_class_atom              = _universal_abbrev("http://www.w3.org/2003/11/swrl#ClassAtom")
swrl_class_predicate         = _universal_abbrev("http://www.w3.org/2003/11/swrl#classPredicate")
swrl_dataprop_atom           = _universal_abbrev("http://www.w3.org/2003/11/swrl#DatavaluedPropertyAtom")
swrl_objprop_atom            = _universal_abbrev("http://www.w3.org/2003/11/swrl#IndividualPropertyAtom")
swrl_property_predicate      = _universal_abbrev("http://www.w3.org/2003/11/swrl#propertyPredicate")
swrl_builtin_atom            = _universal_abbrev("http://www.w3.org/2003/11/swrl#BuiltinAtom")
swrl_builtin                 = _universal_abbrev("http://www.w3.org/2003/11/swrl#builtin")
swrl_datarange_atom          = _universal_abbrev("http://www.w3.org/2003/11/swrl#DataRangeAtom")
swrl_datarange               = _universal_abbrev("http://www.w3.org/2003/11/swrl#dataRange")
swrl_argument1               = _universal_abbrev("http://www.w3.org/2003/11/swrl#argument1")
swrl_argument2               = _universal_abbrev("http://www.w3.org/2003/11/swrl#argument2")
swrl_arguments               = _universal_abbrev("http://www.w3.org/2003/11/swrl#arguments")
swrl_equivalentindividual    = _universal_abbrev("http://www.w3.org/2003/11/swrl#SameIndividualAtom")
swrl_differentfrom           = _universal_abbrev("http://www.w3.org/2003/11/swrl#DifferentIndividualsAtom")

owl_bottomobjectproperty     = _universal_abbrev("http://www.w3.org/2002/07/owl#bottomObjectProperty")
owl_bottomdataproperty       = _universal_abbrev("http://www.w3.org/2002/07/owl#bottomDataProperty")

owl_disjointunion            = _universal_abbrev("http://www.w3.org/2002/07/owl#disjointUnionOf")

#owlready_direct_is_a         = _universal_abbrev("http://www.lesfleursdunormal.fr/static/_downloads/owlready_ontology.owl#direct_is_a")
#owlready_is_a_construct      = _universal_abbrev("http://www.lesfleursdunormal.fr/static/_downloads/owlready_ontology.owl#is_a_construct")
#owlready_context_is_a        = _universal_abbrev("http://www.lesfleursdunormal.fr/static/_downloads/owlready_ontology.owl#context_is_a")
owlready_concrete            = _universal_abbrev("http://www.lesfleursdunormal.fr/static/_downloads/owlready_ontology.owl#concrete")

_universal_abbrev_datatype(locstr, None, None, "http://www.w3.org/1999/02/22-rdf-syntax-ns#langString")
rdf_langstring = _universal_datatype_2_abbrev[locstr]

#xsd_duration                 = _universal_abbrev("http://www.w3.org/2001/XMLSchema#duration")
_universal_abbrev_datatype(datetime.timedelta,
                           _parse_duration,
                           _format_duration,
                           "http://www.w3.org/2001/XMLSchema#duration")

_universal_abbrev_datatype(bytes,
                           _parse_base64,
                           _format_base64,
                           "http://www.w3.org/2001/XMLSchema#base64Binary")

issubclass_python = issubclass



