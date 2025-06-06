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

import sys, os.path, xml, xml.parsers.expat
#from urllib.parse import urljoin
from collections import defaultdict

from owlready2.base import OwlReadyOntologyParsingError

INT_DATATYPES   = { "http://www.w3.org/2001/XMLSchema#integer", "http://www.w3.org/2001/XMLSchema#byte", "http://www.w3.org/2001/XMLSchema#short", "http://www.w3.org/2001/XMLSchema#int", "http://www.w3.org/2001/XMLSchema#long", "http://www.w3.org/2001/XMLSchema#unsignedByte", "http://www.w3.org/2001/XMLSchema#unsignedShort", "http://www.w3.org/2001/XMLSchema#unsignedInt", "http://www.w3.org/2001/XMLSchema#unsignedLong", "http://www.w3.org/2001/XMLSchema#negativeInteger", "http://www.w3.org/2001/XMLSchema#nonNegativeInteger", "http://www.w3.org/2001/XMLSchema#positiveInteger" }
FLOAT_DATATYPES = { "http://www.w3.org/2001/XMLSchema#decimal", "http://www.w3.org/2001/XMLSchema#double", "http://www.w3.org/2001/XMLSchema#float", "http://www.w3.org/2002/07/owl#real" }

cdef str urljoin(str base, str name): # Reimplement because urllib.parse.urljoin remove trailing ?
  cdef str protocol
  cdef str empty
  cdef str server
  cdef str rest
  if name.startswith(("http://", "https://")): return name
  if name.startswith("/"):
    protocol, empty, server, rest = base.split("/", 3)
    return "%s//%s%s" % (protocol, server, name)
  while name.startswith("."):
    if   name.startswith( "./"): name = name[2:]
    elif name.startswith("../"): name = name[3:]; base = os.path.dirname(base[:-1] if base.endswith("/") else base)
  if base.endswith("/"): return "%s%s" % (base, name)
  return "%s/%s" % (base, name)

def parse_ntriples(object f, object queue, str default_base, int batch_size):
  import re
  cdef object splitter = re.compile("\s")
  
  cdef str line = f.readline().decode("utf8")
  cdef str s, p, o
  
  cdef list objs  = []
  cdef list datas = []
  
  while line:
    if (not line.startswith("#")) and (not line.startswith("\n")):
      if not line.endswith("\n"): s,p,o = splitter.split(line[:-2], 2)
      else:                       s,p,o = splitter.split(line[:-3], 2)
      
      if s.startswith("<"): s = s[1:-1]
      
      p = p[1:-1]
      
      if   o.startswith("<"):
        objs.append((s, p, o[1:-1]))
        if len(objs) > batch_size:
          queue.put(("objs", objs))
          objs = []
          
      elif o.startswith("_"):
        objs.append((s, p, o))
        
      else: #if o.startswith('"'):
        o, d = o.rsplit('"', 1)
        if d.startswith("^"):
          d = d[3:-1]
          if   d in INT_DATATYPES:   datas.append((s, p, int  (o[1:]), d))
          elif d in FLOAT_DATATYPES: datas.append((s, p, float(o[1:]), d))
          else:                      datas.append((s, p, o[1:].encode("raw-unicode-escape").decode("unicode-escape"), d))
        elif d.startswith("@"):      datas.append((s, p, o[1:].encode("raw-unicode-escape").decode("unicode-escape"), d))
        else:                        datas.append((s, p, o[1:].encode("raw-unicode-escape").decode("unicode-escape"), ""))
        if len(datas) > batch_size:
          queue.put(("datas", datas))
          datas = []
          
    line = f.readline().decode("utf8")

  if objs:  queue.put(("objs", objs))
  if datas: queue.put(("datas", datas))


cdef str new_list2(list l, list objs, object new_blank):
  cdef str bn
  cdef str bn0
  cdef str bn_next
  cdef int i
  
  bn = bn0 = new_blank()
  
  if l:
    for i in range(len(l) - 1):
      objs.append((bn, "http://www.w3.org/1999/02/22-rdf-syntax-ns#first", l[i]))
      bn_next = new_blank()
      objs.append((bn, "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest", bn_next))
      bn = bn_next
    objs.append((bn, "http://www.w3.org/1999/02/22-rdf-syntax-ns#first", l[-1]))
    objs.append((bn, "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest" , "http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"))
    
  else:
    objs.append((bn, "http://www.w3.org/1999/02/22-rdf-syntax-ns#first", "http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"))
    objs.append((bn, "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest" , "http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"))
    
  return bn0

cdef str new_data_list2(list l, list objs, list datas, object new_blank):
  cdef str bn
  cdef str bn0
  cdef str bn_next
  cdef int i
  
  bn = bn0 = new_blank()
  
  if l:
    for i in range(len(l) - 1):
      datas.append((bn, "http://www.w3.org/1999/02/22-rdf-syntax-ns#first", l[i][0], l[i][1]))
      bn_next = new_blank()
      objs.append((bn, "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest", bn_next))
      bn = bn_next
    datas.append((bn, "http://www.w3.org/1999/02/22-rdf-syntax-ns#first", l[-1][0], l[-1][1]))
    objs .append((bn, "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest" , "http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"))
    
  else:
    objs.append((bn, "http://www.w3.org/1999/02/22-rdf-syntax-ns#first", "http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"))
    objs.append((bn, "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest" , "http://www.w3.org/1999/02/22-rdf-syntax-ns#nil"))
    
  return bn0

cdef void add_to_bn2(object bns, set known_nodes, str bn, str type, str rel, object value, object d = None):
    if not bn in bns: bns[bn] = set()
    if type == "COL":
      value = tuple(frozenset(bns.get(v) or set())
                    if v.startswith("_") and (not v in known_nodes)
                    else v
                    for v in value)
      bns[bn].add((type, rel) + value)
    else:
      if type == "DAT":
        bns[bn].add((type, rel, value, d))
      else:
        if value.startswith("_") and (not value in known_nodes): value = frozenset(bns.get(value) or set())
        bns[bn].add((type, rel, value))

    
def parse_rdfxml(object f, object queue, str default_base, int batch_size):
  cdef object parser = xml.parsers.expat.ParserCreate(None, "")
  try:
    parser.buffer_text          = True
    parser.specified_attributes = True
  except: pass
  
  cdef int next_blank = 0
  def new_blank():
    nonlocal next_blank
    next_blank += 1
    return "_:owlready_blank_%s" % next_blank
    
  cdef list objs                      = []
  cdef list datas                     = []
  cdef list stack                     = [[0, ""]] # List of [parse type, value] pairs
  cdef dict prefixes                  = {}
  cdef list prefixess                 = [prefixes]
  cdef bint tag_is_predicate          = False
  cdef str current_content            = ""
  cdef dict current_attrs             = None
  cdef dict bns                       = {}
  cdef bint dont_create_unnamed_bn    = False
  cdef dict axiom_annotation_sources  = {}
  cdef dict axiom_annotation_props    = {}
  cdef dict axiom_annotation_targets  = {}
  cdef dict triples_with_unnamed_bn   = {}
  
  cdef str xml_base
  cdef str xml_dir
  
  if default_base:
    xml_base = default_base
    if xml_base.endswith("#") or xml_base.endswith("/"): xml_base = xml_base[:-1]
    xml_dir  = xml_base.rsplit("/", 1)[0] + "/"
  else:
    xml_base                 = ""
    xml_dir                  = ""
    
  cdef set known_nodes      = set()
  cdef set fake_blanks      = set()
  
  def startNamespace(str prefix, str uri):
    nonlocal prefixess, prefixes
    prefixes = prefixes.copy()
    prefixess.append(prefixes)
    
    if prefix: prefixes[prefix] = uri
    else:      prefixes[""    ] = uri
      
  def endNamespace(str prefix):
    nonlocal prefixess, prefixes
    prefixess.pop()
    prefixes = prefixess[-1]
    
  def startElement(str tag, dict attrs):
    nonlocal tag_is_predicate, stack, current_content, current_attrs, dont_create_unnamed_bn, xml_base, xml_dir, known_nodes
    cdef str iri
    cdef str iri2 = ""
    cdef str namespace_base
    
    tag_is_predicate = not tag_is_predicate
    if tag_is_predicate:
      
      if   attrs.get("http://www.w3.org/1999/02/22-rdf-syntax-ns#parseType") == "Collection":
        stack.append(["Collection", []])
        
      elif tag == "http://www.w3.org/1999/02/22-rdf-syntax-ns#RDF":
        stack.append(["RDF", 0])
        
        namespace_base = attrs.get("http://www.w3.org/XML/1998/namespacebase")
        if namespace_base:
          xml_base = namespace_base
          if "/" in namespace_base:
            xml_dir  = namespace_base.rsplit("/", 1)[0] + "/"
            
      else:
        iri = attrs.get("http://www.w3.org/1999/02/22-rdf-syntax-ns#resource")
        if not iri is None:
          if   iri.startswith("#"): iri = xml_base + iri
          elif iri.startswith("/"): iri = xml_dir  + iri[1:]
          elif not iri:             iri = xml_base
          elif not ":" in iri:      iri = urljoin(xml_dir, iri)
          if iri.endswith("/"): iri = iri[:-1]
          stack.append(["Resource", iri])
          
        else:
          iri = attrs.get("http://www.w3.org/1999/02/22-rdf-syntax-ns#nodeID")
          
          if iri:
            iri = iri2 = "_:%s" % iri
            known_nodes.add(iri2)
            stack.append(["Resource", iri2])
          else:
            stack.append(["Literal", ""])
            current_content = ""
            current_attrs   = attrs
            
          if (tag == "http://www.w3.org/2002/07/owl#annotatedSource") or (tag == "http://www.w3.org/2002/07/owl#annotatedTarget"):
            dont_create_unnamed_bn = True
            
    else:
      iri = attrs.get("http://www.w3.org/1999/02/22-rdf-syntax-ns#about", None)
      if iri is None:
        iri = attrs.get("http://www.w3.org/1999/02/22-rdf-syntax-ns#ID", None)
        if not iri is None: iri = "#%s" % iri
      if iri is None:
        iri = attrs.get("http://www.w3.org/1999/02/22-rdf-syntax-ns#nodeID")
        if iri:
          iri = iri2 = "_:%s" % iri
          known_nodes.add(iri2)
        else:
          iri2 = new_blank()
          if dont_create_unnamed_bn: fake_blanks.add(iri2)
      else:
        if   iri.startswith("#"): iri = xml_base + iri
        elif iri.startswith("/"): iri = xml_dir  + iri[1:]
        elif not iri:             iri = xml_base
        elif not ":" in iri:      iri = urljoin(xml_dir, iri)
        if iri.endswith("/"): iri = iri[:-1]
        iri2 = iri
          
      if tag != "http://www.w3.org/1999/02/22-rdf-syntax-ns#Description":
        if not iri2 in fake_blanks:
          objs.append((iri2, "http://www.w3.org/1999/02/22-rdf-syntax-ns#type", tag))
        if iri2.startswith("_"):
          add_to_bn2(bns, known_nodes,  iri2, "REL", "http://www.w3.org/1999/02/22-rdf-syntax-ns#type", tag)
          
      if stack[-1][0] == "Collection":
        stack[-1][1].append(iri2)
        
      else:
        if stack[-1][0] == "Literal": stack[-1][0] = "Resource"
        stack[-1][1] = iri2
        
        
  def endElement(str tag):
    nonlocal objs, datas, tag_is_predicate, dont_create_unnamed_bn,  stack, axiom_annotation_sources, axiom_annotation_props, axiom_annotation_targets, triples_with_unnamed_bn
    cdef str iri2
    cdef str parse_type
    cdef object value
    cdef object o
    cdef str d
    cdef list triples
    
    if tag_is_predicate:
      parse_type, value = stack.pop()
      
      if stack[-1][0] == "Collection": iri2 = stack[-1][1][-1]
      else:                            iri2 = stack[-1][1]
      
      if   tag == "http://www.w3.org/2002/07/owl#annotatedSource":
        dont_create_unnamed_bn = False
        axiom_annotation_sources[iri2] = value
        if isinstance(value, str) and (value in fake_blanks):
          if not iri2 in triples_with_unnamed_bn: triples_with_unnamed_bn[iri2] = []
          triples_with_unnamed_bn[iri2].insert(0, (tag, value, parser.CurrentLineNumber, parser.CurrentColumnNumber))
          tag_is_predicate = not tag_is_predicate
          return
        
      elif tag == "http://www.w3.org/2002/07/owl#annotatedProperty":
        axiom_annotation_props[iri2] = value
      
      elif tag == "http://www.w3.org/2002/07/owl#annotatedTarget":
        dont_create_unnamed_bn = False
        axiom_annotation_targets[iri2] = value
        if isinstance(value, str) and (value in fake_blanks):
          if not iri2 in triples_with_unnamed_bn: triples_with_unnamed_bn[iri2] = []
          triples_with_unnamed_bn[iri2].append((tag, value, parser.CurrentLineNumber, parser.CurrentColumnNumber))
          tag_is_predicate = not tag_is_predicate
          return
        
      
      if   parse_type == "Resource":
        if not iri2 in fake_blanks:
          objs.append((iri2, tag, value))
          
        if iri2.startswith("_"):
          add_to_bn2(bns, known_nodes,  iri2, "REL", tag, value)
          
        if value.startswith("_"):
          add_to_bn2(bns, known_nodes,  value, "INV", tag, iri2)
          
          
      elif parse_type == "Literal":
        o = current_content
        d = current_attrs.get("http://www.w3.org/XML/1998/namespacelang")
        if d is None:
          d = current_attrs.get("http://www.w3.org/1999/02/22-rdf-syntax-ns#datatype", "")
          if   d in INT_DATATYPES:   o = int  (o)
          elif d in FLOAT_DATATYPES: o = float(o)
        else:
          d = "@%s" % d
          
        if not iri2 in fake_blanks:
          datas.append((iri2, tag, o, d))
        if iri2.startswith("_"):
          add_to_bn2(bns, known_nodes,  iri2, "DAT", tag, o, d)
          
      elif parse_type == "Collection":
        if not iri2 in fake_blanks:
          objs.append((iri2, tag, new_list2(value, objs, new_blank)))
        if iri2.startswith("_"):
          add_to_bn2(bns, known_nodes,  iri2, "COL", tag, value)
          
          
    if   len(objs)  > batch_size:
      queue.put(("objs", objs))
      objs = []
    elif len(datas) > batch_size:
      queue.put(("datas", datas))
      datas = []
      
    tag_is_predicate = not tag_is_predicate
    
  def characters(str content):
    nonlocal current_content,  stack
    if stack[-1][0] == "Literal": current_content += content
    
    
  parser.StartNamespaceDeclHandler = startNamespace
  parser.EndNamespaceDeclHandler   = endNamespace
  parser.StartElementHandler       = startElement
  parser.EndElementHandler         = endElement
  parser.CharacterDataHandler      = characters
  
  try:
    if isinstance(f, str):
      f = open(f, "rb")
      parser.ParseFile(f)
      f.close()
    else:
      parser.ParseFile(f)
  except Exception as e:
    raise OwlReadyOntologyParsingError("RDF/XML parsing error in file %s, line %s, column %s." % (getattr(f, "name", getattr(f, "url", "???")), parser.CurrentLineNumber, parser.CurrentColumnNumber)) from e
  
  cdef dict content_2_bns
  cdef str bn
  cdef set content
  cdef str axiom_iri
  cdef object k
  cdef list candidates_bn
  
  if triples_with_unnamed_bn:
    content_2_bns = {}
    for bn, content in bns.items():
      if not bn in fake_blanks:
        k = frozenset(content)
        if not k in content_2_bns: content_2_bns[k] = [bn]
        else:                      content_2_bns[k].append(bn)
        
    def rebuild_bn(object content):
      nonlocal content_2_bns
      cdef str bn = new_blank()
      k = frozenset(content)
      if not k in content_2_bns: content_2_bns[k] = [bn]
      else:                      content_2_bns[k].append(bn)
      cdef tuple i
      cdef object drop
      cdef str p
      cdef object d
      cdef object o
      cdef list l
      for i in content:
        if   i[0] == "REL":
          drop, p, o = i
          if not isinstance(o, (str, int)): o = rebuild_bn(o)
          objs.append((bn, p, o))
        elif i[0] == "DAT":
          drop, p, o, d = i
          if not isinstance(o, (str, int)): o = rebuild_bn(o)
          datas.append((bn, p, o, d))
        elif i[0] == "INV":
          drop, p, o = i
          if not isinstance(o, (str, int)): o = rebuild_bn(o)
          objs.append((o, p, bn))
        elif i[0] == "COL":
          drop, p, *l = i
          l = [(isinstance(x, (str, int)) and x) or rebuild_bn(x) for x in l]
          objs.append((bn, p, new_list2(l, objs, new_blank)))
        else:
          print(i)
          raise ValueError
      return bn
    
    for axiom_iri, triples in triples_with_unnamed_bn.items():
      for p, o, line, column in triples:
        try:
          content = bns[o]
          if p == "http://www.w3.org/2002/07/owl#annotatedSource":
            target = axiom_annotation_targets[axiom_iri]
            if target.startswith("_"): target = frozenset(bns[target])
            candidates_bn = content_2_bns.get(frozenset(content | { ("REL", axiom_annotation_props[axiom_iri], target) })) or []
            
          else:
            source = axiom_annotation_sources[axiom_iri]
            if source.startswith("_"):
              source = frozenset(bns[source] | { ("REL", axiom_annotation_props[axiom_iri], target) })
            candidates_bn = (content_2_bns.get(frozenset(content | { ("INV", axiom_annotation_props[axiom_iri], source) })) or
                             content_2_bns.get(frozenset(content)) or [])
            
          if candidates_bn: o = candidates_bn[-1]
          else:             o = rebuild_bn(content)
          objs.append((axiom_iri, p, o))
          
        except Exception as e:
          raise OwlReadyOntologyParsingError("RDF/XML parsing error in file %s, line %s, column %s." % (getattr(f, "name", getattr(f, "url", "???")), line, column)) from e
        
  if objs:  queue.put(("objs", objs))
  if datas: queue.put(("datas", datas))








cdef str rdf_type = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"

cdef dict types = {
  "http://www.w3.org/2002/07/owl#Class"              : "http://www.w3.org/2002/07/owl#Class",
  "http://www.w3.org/2002/07/owl#NamedIndividual"    : "http://www.w3.org/2002/07/owl#NamedIndividual",
  "http://www.w3.org/2002/07/owl#ObjectProperty"     : "http://www.w3.org/2002/07/owl#ObjectProperty",
  "http://www.w3.org/2002/07/owl#DataProperty"       : "http://www.w3.org/2002/07/owl#DatatypeProperty",
  "http://www.w3.org/2002/07/owl#AnnotationProperty" : "http://www.w3.org/2002/07/owl#AnnotationProperty",
}

cdef dict prop_types = {
  "http://www.w3.org/2002/07/owl#FunctionalObjectProperty"        : "http://www.w3.org/2002/07/owl#FunctionalProperty",
  "http://www.w3.org/2002/07/owl#FunctionalDataProperty"          : "http://www.w3.org/2002/07/owl#FunctionalProperty",
  "http://www.w3.org/2002/07/owl#InverseFunctionalObjectProperty" : "http://www.w3.org/2002/07/owl#InverseFunctionalProperty",
  "http://www.w3.org/2002/07/owl#InverseFunctionalDataProperty"   : "http://www.w3.org/2002/07/owl#InverseFunctionalProperty",
  "http://www.w3.org/2002/07/owl#IrreflexiveObjectProperty"       : "http://www.w3.org/2002/07/owl#IrreflexiveProperty",
  "http://www.w3.org/2002/07/owl#IrreflexiveDataProperty"         : "http://www.w3.org/2002/07/owl#IrreflexiveProperty",
  "http://www.w3.org/2002/07/owl#ReflexiveObjectProperty"         : "http://www.w3.org/2002/07/owl#ReflexiveProperty",
  "http://www.w3.org/2002/07/owl#ReflexiveDataProperty"           : "http://www.w3.org/2002/07/owl#ReflexiveProperty",
  "http://www.w3.org/2002/07/owl#SymmetricObjectProperty"         : "http://www.w3.org/2002/07/owl#SymmetricProperty",
  "http://www.w3.org/2002/07/owl#SymmetricDataProperty"           : "http://www.w3.org/2002/07/owl#SymmetricProperty",
  "http://www.w3.org/2002/07/owl#AsymmetricObjectProperty"        : "http://www.w3.org/2002/07/owl#AsymmetricProperty",
  "http://www.w3.org/2002/07/owl#AsymmetricDataProperty"          : "http://www.w3.org/2002/07/owl#AsymmetricProperty",
  "http://www.w3.org/2002/07/owl#TransitiveObjectProperty"        : "http://www.w3.org/2002/07/owl#TransitiveProperty",
  "http://www.w3.org/2002/07/owl#TransitiveDataProperty"          : "http://www.w3.org/2002/07/owl#TransitiveProperty",
}

cdef dict sub_ofs = {
  "http://www.w3.org/2002/07/owl#SubClassOf"              : "http://www.w3.org/2000/01/rdf-schema#subClassOf",
  "http://www.w3.org/2002/07/owl#SubPropertyOf"           : "http://www.w3.org/2000/01/rdf-schema#subPropertyOf",
  "http://www.w3.org/2002/07/owl#SubObjectPropertyOf"     : "http://www.w3.org/2000/01/rdf-schema#subPropertyOf",
  "http://www.w3.org/2002/07/owl#SubDataPropertyOf"       : "http://www.w3.org/2000/01/rdf-schema#subPropertyOf",
  "http://www.w3.org/2002/07/owl#SubAnnotationPropertyOf" : "http://www.w3.org/2000/01/rdf-schema#subPropertyOf",
  }

cdef dict equivs = {
  "http://www.w3.org/2002/07/owl#EquivalentClasses" : "http://www.w3.org/2002/07/owl#equivalentClass",
  "http://www.w3.org/2002/07/owl#EquivalentProperties" : "http://www.w3.org/2002/07/owl#equivalentProperty",
  "http://www.w3.org/2002/07/owl#EquivalentObjectProperties" : "http://www.w3.org/2002/07/owl#equivalentProperty",
  "http://www.w3.org/2002/07/owl#EquivalentDataProperties" : "http://www.w3.org/2002/07/owl#equivalentProperty",
  "http://www.w3.org/2002/07/owl#EquivalentAnnotationProperties" : "http://www.w3.org/2002/07/owl#equivalentProperty",
  "http://www.w3.org/2002/07/owl#SameIndividual" : "http://www.w3.org/2002/07/owl#sameAs",
  }

cdef dict restrs = {
  "http://www.w3.org/2002/07/owl#ObjectSomeValuesFrom" : "http://www.w3.org/2002/07/owl#someValuesFrom",
  "http://www.w3.org/2002/07/owl#ObjectAllValuesFrom"  : "http://www.w3.org/2002/07/owl#allValuesFrom",
  "http://www.w3.org/2002/07/owl#DataSomeValuesFrom"   : "http://www.w3.org/2002/07/owl#someValuesFrom",
  "http://www.w3.org/2002/07/owl#DataAllValuesFrom"    : "http://www.w3.org/2002/07/owl#allValuesFrom",
  "http://www.w3.org/2002/07/owl#ObjectHasValue"       : "http://www.w3.org/2002/07/owl#hasValue",
  "http://www.w3.org/2002/07/owl#DataHasValue"         : "http://www.w3.org/2002/07/owl#hasValue",
  }

cdef dict qual_card_restrs = {
  "http://www.w3.org/2002/07/owl#ObjectExactCardinality" : "http://www.w3.org/2002/07/owl#qualifiedCardinality",
  "http://www.w3.org/2002/07/owl#ObjectMinCardinality"   : "http://www.w3.org/2002/07/owl#minQualifiedCardinality",
  "http://www.w3.org/2002/07/owl#ObjectMaxCardinality"   : "http://www.w3.org/2002/07/owl#maxQualifiedCardinality",
  "http://www.w3.org/2002/07/owl#DataExactCardinality"   : "http://www.w3.org/2002/07/owl#qualifiedCardinality",
  "http://www.w3.org/2002/07/owl#DataMinCardinality"     : "http://www.w3.org/2002/07/owl#minQualifiedCardinality",
  "http://www.w3.org/2002/07/owl#DataMaxCardinality"     : "http://www.w3.org/2002/07/owl#maxQualifiedCardinality",
  }

cdef dict card_restrs = {
  "http://www.w3.org/2002/07/owl#ObjectExactCardinality" : "http://www.w3.org/2002/07/owl#cardinality",
  "http://www.w3.org/2002/07/owl#ObjectMinCardinality"   : "http://www.w3.org/2002/07/owl#minCardinality",
  "http://www.w3.org/2002/07/owl#ObjectMaxCardinality"   : "http://www.w3.org/2002/07/owl#maxCardinality",
  "http://www.w3.org/2002/07/owl#DataExactCardinality"   : "http://www.w3.org/2002/07/owl#cardinality",
  "http://www.w3.org/2002/07/owl#DataMinCardinality"     : "http://www.w3.org/2002/07/owl#minCardinality",
  "http://www.w3.org/2002/07/owl#DataMaxCardinality"     : "http://www.w3.org/2002/07/owl#maxCardinality",
  }

cdef dict disjoints = {
  "http://www.w3.org/2002/07/owl#DisjointClasses"              : ("http://www.w3.org/2002/07/owl#AllDisjointClasses"   , "http://www.w3.org/2002/07/owl#disjointWith", "http://www.w3.org/2002/07/owl#members"),
  "http://www.w3.org/2002/07/owl#DisjointObjectProperties"     : ("http://www.w3.org/2002/07/owl#AllDisjointProperties", "http://www.w3.org/2002/07/owl#propertyDisjointWith", "http://www.w3.org/2002/07/owl#members"),
  "http://www.w3.org/2002/07/owl#DisjointDataProperties"       : ("http://www.w3.org/2002/07/owl#AllDisjointProperties", "http://www.w3.org/2002/07/owl#propertyDisjointWith", "http://www.w3.org/2002/07/owl#members"),
  "http://www.w3.org/2002/07/owl#DisjointAnnotationProperties" : ("http://www.w3.org/2002/07/owl#AllDisjointProperties", "http://www.w3.org/2002/07/owl#propertyDisjointWith", "http://www.w3.org/2002/07/owl#members"),
  "http://www.w3.org/2002/07/owl#DifferentIndividuals"         : ("http://www.w3.org/2002/07/owl#AllDifferent"         , None, "http://www.w3.org/2002/07/owl#distinctMembers"),
}

    
cdef int _rindex(list l):
  i = len(l) - 1
  while l[i] != "(": i -= 1
  return i



def parse_owlxml(object f, object queue, str default_base, int batch_size):
  cdef object parser = xml.parsers.expat.ParserCreate(None, "")
  try:
    parser.buffer_text          = True
    parser.specified_attributes = True
  except: pass

  cdef str ontology_iri_str       = ""
  cdef str ontology_iri           = ""
  cdef list objs                  = []
  cdef list datas                 = []
  cdef list stack                 = []
  cdef list annots                = []
  cdef dict prefixes              = {}
  cdef str current_content        = ""
  cdef dict current_attrs         = None
  cdef bint in_declaration        = False
  cdef bint in_prop_chain         = False
  cdef bint before_declaration    = True
  cdef int last_cardinality       = 0
  cdef set datatypes              = INT_DATATYPES | FLOAT_DATATYPES
  cdef str lang
  
  cdef int next_blank = 0
  def new_blank():
    nonlocal next_blank
    next_blank += 1
    return "_:owlready_blank_%s" % next_blank
    
  def _unabbreviate_IRI(str _abbreviated_iri):
    cdef str prefix, name
    prefix, name = _abbreviated_iri.split(":", 1)
    return prefixes[prefix] + name
  
  def get_IRI(dict attrs):
    nonlocal ontology_iri, ontology_iri_str
    cdef str iri
    if "IRI" in attrs:
      iri = attrs["IRI"]
      if not iri: return ontology_iri
      if iri.startswith("#") or iri.startswith("/"): iri = "%s%s" % (ontology_iri_str, iri)
      if iri.endswith("/"): iri = iri[:-1]
      if not "//" in iri: iri = urljoin(prefixes[""], iri)
      return iri
    return _unabbreviate_IRI(attrs["abbreviatedIRI"])
  
  def startElement(str tag, dict attrs):
    nonlocal current_content, current_attrs, in_declaration, before_declaration, last_cardinality, in_prop_chain, ontology_iri, ontology_iri_str
    cdef str iri
    cdef str version_iri
    
    current_content = ""
    if   (tag == "http://www.w3.org/2002/07/owl#Prefix"):
      prefixes[attrs["name"]] = attrs["IRI"]
    
    elif (tag == "http://www.w3.org/2002/07/owl#Declaration"):
      in_declaration     = True
      before_declaration = False
      
    elif (tag in types):
      iri = get_IRI(attrs)
      if in_declaration: objs.append((iri, rdf_type, types[tag]))
      stack.append(iri)
      
    elif (tag == "http://www.w3.org/2002/07/owl#Datatype"): stack.append(get_IRI(attrs))
    
    elif (tag == "http://www.w3.org/2002/07/owl#Literal"):  current_attrs = attrs
    
    elif((tag == "http://www.w3.org/2002/07/owl#ObjectIntersectionOf") or (tag == "http://www.w3.org/2002/07/owl#ObjectUnionOf") or
         (tag == "http://www.w3.org/2002/07/owl#ObjectOneOf") or (tag == "http://www.w3.org/2002/07/owl#DataOneOf") or
         (tag == "http://www.w3.org/2002/07/owl#DataIntersectionOf") or (tag == "http://www.w3.org/2002/07/owl#DataUnionOf") or
         (tag == "http://www.w3.org/2002/07/owl#DisjointClasses") or (tag == "http://www.w3.org/2002/07/owl#DisjointObjectProperties") or (tag == "http://www.w3.org/2002/07/owl#DisjointDataProperties") or (tag == "http://www.w3.org/2002/07/owl#DifferentIndividuals")):
      stack.append("(")
      
    elif((tag == "http://www.w3.org/2002/07/owl#ObjectExactCardinality") or (tag == "http://www.w3.org/2002/07/owl#ObjectMinCardinality") or (tag == "http://www.w3.org/2002/07/owl#ObjectMaxCardinality") or
         (tag == "http://www.w3.org/2002/07/owl#DataExactCardinality"  ) or (tag == "http://www.w3.org/2002/07/owl#DataMinCardinality"  ) or (tag == "http://www.w3.org/2002/07/owl#DataMaxCardinality"  )):
      stack.append("(")
      last_cardinality = int(attrs["cardinality"])
      
    elif (tag == "http://www.w3.org/2002/07/owl#AnonymousIndividual"): stack.append(new_blank())
    
    elif (tag == "http://www.w3.org/2002/07/owl#SubObjectPropertyOf"): in_prop_chain = False
    
    elif (tag == "http://www.w3.org/2002/07/owl#ObjectInverseOf") or (tag == "http://www.w3.org/2002/07/owl#DataInverseOf") or (tag == "http://www.w3.org/2002/07/owl#inverseOf"): stack.append(new_blank())
    
    elif (tag == "http://www.w3.org/2002/07/owl#ObjectPropertyChain"): stack.append("(")
    
    elif (tag == "http://www.w3.org/2002/07/owl#DatatypeRestriction"): stack.append("(")
    
    elif (tag == "http://www.w3.org/2002/07/owl#FacetRestriction"): stack.append(attrs["facet"])
    
    elif (tag == "http://www.w3.org/2002/07/owl#DisjointUnion"): stack.append("(")
    
    elif (tag == "http://www.w3.org/2002/07/owl#Ontology"):
      ontology_iri_str = attrs["ontologyIRI"]
      if ontology_iri_str.endswith("/"): ontology_iri = ontology_iri_str[:-1]
      else:                              ontology_iri = ontology_iri_str
      objs.append((ontology_iri, rdf_type, "http://www.w3.org/2002/07/owl#Ontology"))
      version_iri = attrs.get("versionIRI")
      if version_iri: objs.append((ontology_iri, "http://www.w3.org/2002/07/owl#versionIRI", version_iri))
        
    elif (tag == "RDF") or (tag == "rdf:RDF"): raise ValueError("Not an OWL/XML file! (It seems to be an OWL/RDF file)")
    
    
  def endElement(str tag):
    nonlocal in_declaration, stack, in_prop_chain, current_content, objs, datas
    cdef str iri, list_iri

    if   (tag == "http://www.w3.org/2002/07/owl#Declaration"):
      in_declaration = False
      stack = [] # Purge stack
      
    elif (tag == "http://www.w3.org/2002/07/owl#Literal"):
      lang = current_attrs.get("http://www.w3.org/XML/1998/namespacelang", "")
      if lang != "": stack.append((current_content, "@%s" % lang))
      else:
        d = current_attrs.get("datatypeIRI", "")
        if   d in INT_DATATYPES:   stack.append((int  (current_content), d))
        elif d in FLOAT_DATATYPES: stack.append((float(current_content), d))
        elif d:
          iri = d
          stack.append((current_content, iri))
          datatypes.add(iri)
        else:
          stack.append((current_content, 0))
        
    elif (tag == "http://www.w3.org/2002/07/owl#SubClassOf") or (tag == "http://www.w3.org/2002/07/owl#SubObjectPropertyOf") or (tag == "http://www.w3.org/2002/07/owl#SubDataPropertyOf") or (tag == "http://www.w3.org/2002/07/owl#SubAnnotationPropertyOf"):
      parent = stack.pop()
      child  = stack.pop()
      if (tag == "http://www.w3.org/2002/07/owl#SubObjectPropertyOf") and in_prop_chain:
        relation = "http://www.w3.org/2002/07/owl#propertyChainAxiom"
        parent, child = child, parent
      else:
        relation = sub_ofs[tag]
      objs.append((child, relation, parent))
      if annots: purge_annotations((child, relation, parent))
      
    elif (tag == "http://www.w3.org/2002/07/owl#ClassAssertion"):
      child  = stack.pop() # Order is reversed compared to SubClassOf!
      parent = stack.pop()
      objs.append((child, rdf_type, parent))
      if annots: purge_annotations((child, rdf_type, parent))
      
    elif (tag == "http://www.w3.org/2002/07/owl#EquivalentClasses") or (tag == "http://www.w3.org/2002/07/owl#EquivalentObjectProperties") or (tag == "http://www.w3.org/2002/07/owl#EquivalentDataProperties"):
      o1 = stack.pop()
      o2 = stack.pop()
      if o1.startswith("_"): o1, o2 = o2, o1 # Swap in order to have blank node at third position -- rapper seems to do that
      objs.append((o1, equivs[tag], o2))
      if annots: purge_annotations((o1, equivs[tag], o2))
      
    elif (tag == "http://www.w3.org/2002/07/owl#ObjectPropertyDomain") or (tag == "http://www.w3.org/2002/07/owl#DataPropertyDomain") or (tag == "http://www.w3.org/2002/07/owl#AnnotationPropertyDomain"):
      val = stack.pop(); obj = stack.pop();
      objs.append((obj, "http://www.w3.org/2000/01/rdf-schema#domain", val))
      if annots: purge_annotations((obj, "http://www.w3.org/2000/01/rdf-schema#domain", val))
      
    elif (tag == "http://www.w3.org/2002/07/owl#ObjectPropertyRange") or (tag == "http://www.w3.org/2002/07/owl#DataPropertyRange") or (tag == "http://www.w3.org/2002/07/owl#AnnotationPropertyRange"):
      val = stack.pop(); obj = stack.pop();
      objs.append((obj, "http://www.w3.org/2000/01/rdf-schema#range", val))
      if annots: purge_annotations((obj, "http://www.w3.org/2000/01/rdf-schema#range", val))
      
    elif (tag in prop_types):
      obj = stack.pop()
      objs.append((obj, rdf_type, prop_types[tag]))
      
    elif (tag == "http://www.w3.org/2002/07/owl#InverseObjectProperties") or (tag == "http://www.w3.org/2002/07/owl#InverseDataProperties"):
      a, b = stack.pop(), stack.pop()
      objs.append((b, "http://www.w3.org/2002/07/owl#inverseOf", a))
      
    elif (tag == "http://www.w3.org/2002/07/owl#ObjectPropertyChain"):
      start          = _rindex(stack)
      in_prop_chain  = True
      stack[start :] = [new_list2(stack[start + 1 : ], objs, new_blank)]
      
    elif (tag in disjoints):
      start    = _rindex(stack)
      list_obj = stack[start + 1 : ]
      tag, rel, member = disjoints[tag]
      if rel and (len(list_obj) == 2):
        objs.append((list_obj[0], rel, list_obj[1]))
        if annots: purge_annotations((list_obj[0], rel, list_obj[1]))
        
      else:
        list_iri = new_list2(list_obj, objs, new_blank)
        iri = new_blank()
        objs.append((iri, rdf_type, tag))
        objs.append((iri, member, list_iri))
        if annots: purge_annotations((iri, rdf_type, tag))
        
      del stack[start :]
      
    elif (tag == "http://www.w3.org/2002/07/owl#ObjectPropertyAssertion"):
      p,s,o = stack[-3 :]
      objs.append((s, p, o))
      if annots: purge_annotations((s,p,o))
      del stack[-3 :]
      
    elif (tag == "http://www.w3.org/2002/07/owl#DataPropertyAssertion"):
      p,s,o = stack[-3 :]
      datas.append((s, p, o[0], o[1]))
      if annots: purge_annotations((s,p,o))
      del stack[-3 :]
      
    elif (tag == "http://www.w3.org/2002/07/owl#ObjectComplementOf") or (tag == "http://www.w3.org/2002/07/owl#DataComplementOf"):
      iri = new_blank()
      objs.append((iri, rdf_type, "http://www.w3.org/2002/07/owl#Class"))
      objs.append((iri, "http://www.w3.org/2002/07/owl#complementOf", stack[-1]))
      stack[-1] = iri
    
    elif (tag in restrs):
      iri = new_blank()
      objs.append((iri, rdf_type, "http://www.w3.org/2002/07/owl#Restriction"))
      objs.append((iri, "http://www.w3.org/2002/07/owl#onProperty", stack.pop(-2)))
      if isinstance(stack[-1], tuple): datas.append((iri, restrs[tag], stack[-1][0], stack[-1][1]))
      else:                            objs.append ((iri, restrs[tag], stack[-1]))
      stack[-1] = iri
      
    elif (tag == "http://www.w3.org/2002/07/owl#ObjectHasSelf"):
      iri = new_blank()
      objs.append((iri, rdf_type, "http://www.w3.org/2002/07/owl#Restriction"))
      objs.append((iri, "http://www.w3.org/2002/07/owl#onProperty", stack[-1]))
      datas.append((iri, "http://www.w3.org/2002/07/owl#hasSelf", "true", "http://www.w3.org/2001/XMLSchema#boolean"))
      stack[-1] = iri
      
    elif (tag in card_restrs):
      iri = new_blank()
      objs.append((iri, rdf_type, "http://www.w3.org/2002/07/owl#Restriction"))
      start = _rindex(stack)
      values = stack[start + 1 : ]
      del stack[start :]
      
      if len(values) == 2: # Qualified
        tag = qual_card_restrs[tag]
        objs.append((iri, "http://www.w3.org/2002/07/owl#onProperty", values[-2]))
        if stack[-1] in datatypes:
          objs.append((iri, "http://www.w3.org/2002/07/owl#onDataRange", values[-1]))
        else:
          objs.append((iri, "http://www.w3.org/2002/07/owl#onClass", values[-1]))
      else: # Non qualified
        tag = card_restrs[tag]
        objs.append((iri, "http://www.w3.org/2002/07/owl#onProperty", values[-1]))
      datas.append((iri, tag, last_cardinality, "http://www.w3.org/2001/XMLSchema#nonNegativeInteger"))
      stack.append(iri)
      
    elif (tag == "http://www.w3.org/2002/07/owl#ObjectOneOf"):
      start    = _rindex(stack)
      list_iri = new_list2(stack[start + 1 : ], objs, new_blank)
      iri      = new_blank()
      objs.append((iri, rdf_type, "http://www.w3.org/2002/07/owl#Class"))
      objs.append((iri, "http://www.w3.org/2002/07/owl#oneOf", list_iri))
      stack[start :] = [iri]
      
    elif (tag == "http://www.w3.org/2002/07/owl#DataOneOf"):
      start    = _rindex(stack)
      list_iri = new_data_list2(stack[start + 1 : ], objs, datas, new_blank)
      iri      = new_blank()
      objs.append((iri, rdf_type, "http://www.w3.org/2000/01/rdf-schema#Datatype"))
      objs.append((iri, "http://www.w3.org/2002/07/owl#oneOf", list_iri))
      stack[start :] = [iri]
      
    elif (tag == "http://www.w3.org/2002/07/owl#ObjectIntersectionOf") or (tag == "http://www.w3.org/2002/07/owl#ObjectUnionOf") or (tag == "http://www.w3.org/2002/07/owl#DataIntersectionOf") or (tag == "http://www.w3.org/2002/07/owl#DataUnionOf"):
      start    = _rindex(stack)
      list_iri = new_list2(stack[start + 1 : ], objs, new_blank)
      iri      = new_blank()
      
      if stack[start + 1 : ][0] in datatypes:
        objs.append((iri, rdf_type, "http://www.w3.org/2000/01/rdf-schema#Datatype"))
      else:
        objs.append((iri, rdf_type, "http://www.w3.org/2002/07/owl#Class"))
      if (tag == "http://www.w3.org/2002/07/owl#ObjectIntersectionOf") or (tag == "http://www.w3.org/2002/07/owl#DataIntersectionOf"):
        objs.append((iri, "http://www.w3.org/2002/07/owl#intersectionOf", list_iri))
      else:
        objs.append((iri, "http://www.w3.org/2002/07/owl#unionOf", list_iri))
      stack[start :] = [iri]
      
    elif (tag == "http://www.w3.org/2002/07/owl#Import"):
      objs.append((ontology_iri, "http://www.w3.org/2002/07/owl#imports", current_content))
      
    elif (tag == "http://www.w3.org/2002/07/owl#IRI"):
      #current_content is IRI !
      if not current_content: current_content = ontology_iri_str
      else:
        if current_content.startswith("#") or current_content.startswith("/"): current_content = ontology_iri_str + current_content
      stack.append(current_content)
      
    elif (tag == "http://www.w3.org/2002/07/owl#AbbreviatedIRI"):
      stack.append(_unabbreviate_IRI(current_content))
      
    elif (tag == "http://www.w3.org/2002/07/owl#AnnotationAssertion"):
      if isinstance(stack[-1], tuple): datas.append((stack[-2], stack[-3], stack[-1][0], stack[-1][1]))
      else:                            objs .append((stack[-2], stack[-3], stack[-1]))
      if annots: purge_annotations((stack[-2], stack[-3], stack[-1]))
      
    elif (tag == "http://www.w3.org/2002/07/owl#Annotation"):
      if before_declaration: # On ontology
        if isinstance(stack[-1], tuple): datas.append((ontology_iri, stack[-2], stack[-1][0], stack[-1][1]))
        else:                            objs .append((ontology_iri, stack[-2], stack[-1]))
      else:
        annots.append((stack[-2], stack[-1]))
      del stack[-2:]
      
    elif (tag == "http://www.w3.org/2002/07/owl#DatatypeRestriction"):
      start               = _rindex(stack)
      datatype, *list_bns = stack[start + 1 : ]
      list_bns            = new_list2(list_bns, objs, new_blank)
      bn                  = new_blank()
      stack[start :]  = [bn]
      objs.append((bn, rdf_type, "http://www.w3.org/2000/01/rdf-schema#Datatype"))
      objs.append((bn, "http://www.w3.org/2002/07/owl#onDatatype", datatype))
      objs.append((bn, "http://www.w3.org/2002/07/owl#withRestrictions", list_bns))
      
    elif (tag == "http://www.w3.org/2002/07/owl#FacetRestriction"):
      facet, literal = stack[-2:]
      bn = new_blank()
      if isinstance(literal, tuple): datas.append((bn, facet, literal[0], literal[1]))
      else:                          objs .append((bn, facet, literal))
      stack[-2:] = [bn]
      
    elif (tag == "http://www.w3.org/2002/07/owl#ObjectInverseOf") or (tag == "http://www.w3.org/2002/07/owl#DataInverseOf") or (tag == "http://www.w3.org/2002/07/owl#inverseOf"):
      bn, prop = stack[-2:]
      objs.append((bn, "http://www.w3.org/2002/07/owl#inverseOf", prop))
      
      stack[-2:] = [bn]
      
    elif (tag == "http://www.w3.org/2002/07/owl#SameIndividual"):
      objs.append((stack[-2], "http://www.w3.org/2002/07/owl#sameAs", stack[-1]))
      del stack[-2:]
      
    elif (tag == "http://www.w3.org/2002/07/owl#DisjointUnion"):
      start    = _rindex(stack)
      list_obj = stack[start + 1 : ]
      list_iri = new_list2(list_obj[1:], objs, new_blank)
      objs.append((list_obj[0], "http://www.w3.org/2002/07/owl#disjointUnionOf", list_iri))
      del stack[start:]
      
    if   len(objs)  > batch_size:
      queue.put(("objs", objs))
      objs = []
    elif len(datas) > batch_size:
      queue.put(("datas", datas))
      datas = []
      
  def characters(str content):
    nonlocal current_content
    current_content += content
    
  def purge_annotations(on_iri):
    nonlocal annots
    cdef str s, p, prop_iri, bn
    cdef object value, o
    
    if isinstance(on_iri, tuple):
      s,p,o = on_iri
      bn    = new_blank()
      objs.append((bn, rdf_type, "http://www.w3.org/2002/07/owl#Axiom"))
      objs.append((bn, "http://www.w3.org/2002/07/owl#annotatedSource", s))
      objs.append((bn, "http://www.w3.org/2002/07/owl#annotatedProperty", p))
      if isinstance(o, tuple): datas.append((bn, "http://www.w3.org/2002/07/owl#annotatedTarget", o[0], o[1]))
      else:                    objs .append((bn, "http://www.w3.org/2002/07/owl#annotatedTarget", o))
    else:
      bn = on_iri
      
    for prop_iri, value in annots:
      if isinstance(value, tuple): datas.append((bn, prop_iri, value[0], value[1]))
      else:                        objs .append((bn, prop_iri, value))
    annots = []
    
    
  parser.StartElementHandler  = startElement
  parser.EndElementHandler    = endElement
  parser.CharacterDataHandler = characters

  try:
    if isinstance(f, str):
      f = open(f, "rb")
      parser.ParseFile(f)
      f.close()
    else:
      parser.ParseFile(f)
      
  except Exception as e:
    raise OwlReadyOntologyParsingError("OWL/XML parsing error in file %s, line %s, column %s." % (getattr(f, "name", getattr(f, "url", "???")), parser.CurrentLineNumber, parser.CurrentColumnNumber)) from e
  
  if objs:  queue.put(("objs", objs))
  if datas: queue.put(("datas", datas))

