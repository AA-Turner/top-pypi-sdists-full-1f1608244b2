/**
 * @file    SBase.h
 * @brief   Definition of SBase, the base object of all SBML objects
 * @author  Ben Bornstein
 * 
 * <!--------------------------------------------------------------------------
 * This file is part of libSBML.  Please visit http://sbml.org for more
 * information about SBML, and the latest version of libSBML.
 *
 * Copyright (C) 2020 jointly by the following organizations:
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. University of Heidelberg, Heidelberg, Germany
 *     3. University College London, London, UK
 *
 * Copyright (C) 2019 jointly by the following organizations:
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. University of Heidelberg, Heidelberg, Germany
 *
 * Copyright (C) 2013-2018 jointly by the following organizations:
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. EMBL European Bioinformatics Institute (EMBL-EBI), Hinxton, UK
 *     3. University of Heidelberg, Heidelberg, Germany
 *
 * Copyright (C) 2009-2013 jointly by the following organizations: 
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. EMBL European Bioinformatics Institute (EMBL-EBI), Hinxton, UK
 *  
 * Copyright (C) 2006-2008 by the California Institute of Technology,
 *     Pasadena, CA, USA 
 *  
 * Copyright (C) 2002-2005 jointly by the following organizations: 
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. Japan Science and Technology Agency, Japan
 * 
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation.  A copy of the license agreement is provided
 * in the file named "LICENSE.txt" included with this software distribution
 * and also available online as http://sbml.org/software/libsbml/license.html
 * ------------------------------------------------------------------------ -->
 * 
 * @class SBase
 * @sbmlbrief{core} SBML's <em>%SBase</em> class, base class of most SBML objects.
 *
 * Most components in SBML are derived from a single abstract base type,
 * SBase.  In addition to serving as the parent class for most other
 * classes of objects in SBML, this base type is designed to allow a
 * modeler or a software package to attach arbitrary information to each
 * major element or list in an SBML model.
 *
 * SBase has an optional subelement called "notes".  It is intended to
 * serve as a place for storing optional information intended to be seen by
 * humans.  An example use of the "notes" element would be to contain
 * formatted user comments about the model element in which the "notes"
 * element is enclosed.  There are certain conditions on the XHTML content
 * permitted inside the "notes" element; please consult the <a
 * target="_blank" href="http://sbml.org/Documents/Specifications">SBML
 * specification document</a> corresponding to the SBML Level and Version
 * of your model for more information about the requirements for "notes"
 * content.
 *
 * SBase has another optional subelement called "annotation".  Whereas the
 * "notes" element described above is a container for content to be shown
 * directly to humans, the "annotation" element is a container for optional
 * software-generated content @em not meant to be shown to humans.  The
 * element's content type is <a target="_blank"
 * href="http://www.w3.org/TR/2004/REC-xml-20040204/#elemdecls">XML type
 * "any"</a>, allowing essentially arbitrary data content.  SBML places
 * only a few restrictions on the organization of the content; these are
 * intended to help software tools read and write the data as well as help
 * reduce conflicts between annotations added by different tools.  As is
 * the case with "notes", it is important to refer to the <a
 * target="_blank" href="http://sbml.org/Documents/Specifications">SBML
 * specification document</a> corresponding to the SBML Level and Version
 * of your model for more information about the requirements for
 * "annotation" content.
 * 
 * It is worth pointing out that the "annotation" element in the definition
 * of SBase exists in order that software developers may attach optional
 * application-specific data to the elements in an SBML model.  However, it
 * is important that this facility not be misused.  In particular, it is
 * <em>critical</em> that data essential to a model definition or that can
 * be encoded in existing SBML elements is <em>not</em> stored in
 * "annotation". Parameter values, functional dependencies between model
 * elements, etc., should not be recorded as annotations.  It is crucial to
 * keep in mind the fact that data placed in annotations can be freely
 * ignored by software applications.  If such data affects the
 * interpretation of a model, then software interoperability is greatly
 * impeded.
 *
 * SBML Level 2 introduced an optional SBase attribute named "metaid" for
 * supporting metadata annotations using RDF (<a target="_blank"
 * href="http://www.w3.org/RDF/">Resource Description Format</a>). The
 * attribute value has the data type <a
 * href="http://www.w3.org/TR/REC-xml/#id">XML ID</a>, the XML identifier
 * type, which means each "metaid" value must be globally unique within an
 * SBML file.  (Importantly, this uniqueness criterion applies across any
 * attribute with type <a href="http://www.w3.org/TR/REC-xml/#id">XML
 * ID</a>, not just the "metaid" attribute used by SBML---something to
 * be aware of if your application-specific XML content inside the
 * "annotation" subelement happens to use <a
 * href="http://www.w3.org/TR/REC-xml/#id">XML ID</a>.)  The "metaid" value
 * serves to identify a model component for purposes such as referencing
 * that component from metadata placed within "annotation" subelements.
 *
 * Beginning with SBML Level 2 Version 2, SBase has an optional
 * attribute named "sboTerm" for supporting the use of the Systems Biology
 * Ontology.  In SBML proper, the data type of the attribute is a string of
 * the form "SBO:NNNNNNN", where "NNNNNNN" is a seven digit integer number;
 * libSBML simplifies the representation by only storing the "NNNNNNN"
 * integer portion.  Thus, in libSBML, the "sboTerm" attribute on SBase has
 * data type @c int, and SBO identifiers are stored simply as integers.
 * (For convenience, SBase offers methods for returning both the integer
 * form and a text-string form of the SBO identifier.)  SBO terms are a
 * type of optional annotation, and each different class of SBML object
 * derived from SBase imposes its own requirements about the values
 * permitted for "sboTerm".  More details can be found in SBML specifications
 * for Level&nbsp;2 Version&nbsp;2 and above.
 *
 * Finally, note that, in the list of methods on SBase, there is no public
 * constructor because SBase is an abstract class.  The constructors reside
 * in the subclasses derived from SBase.
 *
 *
 * @section sbase-miriam Standard format for annotations linking data resources
 *
 * SBML Level 2 Versions 2, 3 and 4, and Level&nbsp;3, define a proposed
 * regular format for encoding two particular categories of annotations:
 * (a) references to controlled vocabulary terms and database identifiers
 * which define and describe biological and biochemical entities in a
 * model; and (b) descriptions of the provenance of a model, including its
 * author(s) and modification history.
 */

/**
 * <!-- ~ ~ ~ ~ ~ Start of common documentation strings ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 * The following text is used as common documentation blocks copied multiple
 * times elsewhere in this file.  The use of @class is a hack needed because
 * Doxygen's @copydetails command has limited functionality.  Symbols
 * beginning with "doc_" are marked as ignored in our Doxygen configuration.
 * ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  -->
 *
 */

#ifndef SBase_h
#define SBase_h


#include <sbml/common/extern.h>
#include <sbml/common/sbmlfwd.h>
#include <sbml/SBMLTypeCodes.h>
#ifndef LIBSBML_USE_STRICT_INCLUDES
#include <sbml/annotation/RDFAnnotation.h>
#endif
#include <sbml/annotation/CVTerm.h>
#include <sbml/util/List.h>
#include <sbml/SBMLNamespaces.h>
#include <sbml/SyntaxChecker.h>
#include <sbml/SBMLConstructorException.h>
#include <sbml/ExpectedAttributes.h>
#include <sbml/xml/XMLNode.h>
#include <sbml/xml/XMLError.h>

#ifdef __cplusplus


#include <string>
#include <stdexcept>
#include <algorithm>

LIBSBML_CPP_NAMESPACE_BEGIN

class SBMLErrorLog;
class SBMLVisitor;
class SBMLDocument;
class Model;

class List;

class XMLAttributes;
class XMLInputStream;
class XMLNamespaces;
class XMLOutputStream;
class XMLToken;

class SBasePlugin;
class IdentifierTransformer;
class ElementFilter;

class LIBSBML_EXTERN SBase
{
public:

  /**
   * Destroys this object.
   */
  virtual ~SBase ();


  /**
   * Assignment operator for SBase.
   *
   * @param rhs the object whose values are used as the basis of the
   * assignment.
   */
  SBase& operator=(const SBase& rhs);


  /** @cond doxygenLibsbmlInternal */
  /**
   * Accepts the given SBMLVisitor for this SBase object.
   *
   * @param v the SBMLVisitor instance to be used.
   *
   * @return the result of calling <code>v.visit()</code>.
   */
  virtual bool accept (SBMLVisitor& v) const = 0;
  /** @endcond */


  /**
   * Creates and returns a deep copy of this SBase object.
   *
   * @return the (deep) copy of this SBase object.
   */
  virtual SBase* clone () const = 0;


  /**
   * Returns the first child element found that has the given @p id in the
   * model-wide @c SId namespace, or @c NULL if no such object is found.
   *
   * @param id string representing the "id" attribute value of the object
   * to find.
   *
   * @return pointer to the first element found with the given identifier.
   */
  virtual SBase* getElementBySId(const std::string& id);
  
  /**
   * Returns the first child element found that has the given @p id in the
   * model-wide @c SId namespace, or @c NULL if no such object is found.
   *
   * @param id string representing the "id" attribute value of the object
   * to find.
   *
   * @return pointer to the first element found with the given identifier.
   */
  virtual const SBase* getElementBySId(const std::string& id) const;
  
  /**
   * Returns the first child element it can find with a specific "metaid"
   * attribute value, or @c NULL if no such object is found.
   *
   * @copydetails doc_what_is_metaid
   *
   * @param metaid string representing the "metaid" attribute value of the
   * object to find.
   *
   * @return pointer to the first element found with the given meta-identifier.
   */
  virtual SBase* getElementByMetaId(const std::string& metaid);

  /**
   * Returns the first child element it can find with a specific "metaid"
   * attribute value, or @c NULL if no such object is found.
   *
   * @copydetails doc_what_is_metaid
   *
   * @param metaid string representing the "metaid" attribute value of the
   * object to find.
   *
   * @return pointer to the first element found with the given meta-identifier.
   */
  const SBase* getElementByMetaId(const std::string& metaid) const;

  /**
   * Returns a List of all child SBase objects, including those nested to
   * an arbitrary depth.
   *
   * @param filter a pointer to an ElementFilter, which causes the function 
   * to return only elements that match a particular set of constraints.  
   * If NULL (the default), the function will return all child objects.
   *
   * @return a pointer to a List of pointers to all objects that are children
   * of this object.
   */
  virtual List* getAllElements(ElementFilter* filter=NULL);


  /**
   * @copydoc doc_renamesidref_common
   */
  virtual void renameSIdRefs(const std::string& oldid, const std::string& newid);


  /**
   * @copydoc doc_renamemetasidref_common
   */
  virtual void renameMetaIdRefs(const std::string& oldid, const std::string& newid);


  /**
   * @copydoc doc_renameunitsidref_common
   */
  virtual void renameUnitSIdRefs(const std::string& oldid, const std::string& newid);


  /** @cond doxygenLibsbmlInternal */
  /**
   * If this object has a child 'math' object (or anything with ASTNodes in
   * general), replace all nodes with the name 'id' with the provided
   * function.
   *
   * @note This function does nothing itself---subclasses with ASTNode
   * subelements must override this function.
   */
  virtual void replaceSIDWithFunction(const std::string& id, const ASTNode* function);
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /**
   * If the function of this object is to assign a value has a child 'math'
   * object (or anything with ASTNodes in general), replace the 'math'
   * object with the function (existing/function).
   *
   * @note This function does nothing itself---subclasses with ASTNode
   * subelements must override this function.
   */
  virtual void divideAssignmentsToSIdByFunction(const std::string& id, const ASTNode* function);
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /**
   * If this assignment assigns a value to the 'id' element, replace the 'math' object with the function (existing*function). 
   */
  virtual void multiplyAssignmentsToSIdByFunction(const std::string& id, const ASTNode* function);
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /**
   * Returns the first child element found that has the given @p id in the
   * model-wide SId namespace from all plug-ins associated with this
   * element, or @c NULL if no such object is found.
   *
   * @param id string representing the id of the object to find.
   *
   * @return pointer to the first element found with the given @p id.
   */
  virtual SBase* getElementFromPluginsBySId(const std::string& id);
  /** @endcond */
  
  
  /** @cond doxygenLibsbmlInternal */
  /**
   * Returns the first child element it can find with the given @p metaid from
   * all plug-ins associated with this element, or @c NULL if no such object
   * is found.
   *
   * @param metaid string representing the metaid of the object to find.
   *
   * @return pointer to the first element found with the given @p metaid.
   */
  virtual SBase* getElementFromPluginsByMetaId(const std::string& metaid);
  /** @endcond */

  
  /** @cond doxygenLibsbmlInternal */
  /**
   * Check to see if the given prefix is used by any of the IDs defined by
   * extension elements *excluding* 'id' and 'metaid' attributes (as, for
   * example, the spatial id attributes 'spid').
   */
  virtual bool hasNonstandardIdentifierBeginningWith(const std::string& prefix);
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /**
   * Add the given string to all identifiers (but not identifier references) in the object.  If the string
   * is added to anything other than an id or a metaid, this code is
   * responsible for tracking down and renaming all *idRefs in the package
   * extension that identifier comes from.
   */
  virtual int prependStringToAllIdentifiers(const std::string& prefix);
  /** @endcond */
  
  /** @cond doxygenLibsbmlInternal */
  virtual int transformIdentifiers(IdentifierTransformer* idTransformer);
  /** @endcond */


  /**
   * Returns a List of all child SBase objects contained in SBML package
   * plug-ins.
   *
   * @copydetails doc_what_are_plugins
   *
   * This method walks down the list of all SBML Level&nbsp;3 packages used
   * by this object and returns all child objects defined by those packages.
   *
   * @param filter a pointer to an ElementFilter, which causes the function 
   * to return only elements that match a particular set of constraints.  
   * If NULL (the default), the function will return all child objects.
   *
   * @return a pointer to a List of pointers to all children objects from
   * plug-ins.
   *
   * @ifnot hasDefaultArgs @htmlinclude warn-default-args-in-docs.html @endif@~
   */
  virtual List* getAllElementsFromPlugins(ElementFilter* filter=NULL);


  /**
   * Returns the value of the "metaid" attribute of this SBML object.
   *
   * @copydetails doc_what_is_metaid
   *  
   * @return the meta-identifier of this SBML object.
   *
   * @see isSetMetaId()
   * @see setMetaId(const std::string& metaid)
   */
  const std::string& getMetaId () const;


  /**
   * Returns the value of the "metaid" attribute of this SBML object.
   *
   * @copydetails doc_what_is_metaid
   *  
   * @return the meta-identifier of this SBML object, as a string.
   *
   * @see isSetMetaId()
   * @see setMetaId(const std::string& metaid)
   */
  std::string& getMetaId ();


  /**
   * Returns the value of the "id" attribute of this SBML object, if it has one, 
   * or the "variable" attribute of a Rule, or the "symbol" attribute of
   * an InitialAssignment.
   *
   * @copydetails doc_id_attribute
   *
   * @return the id of this SBML object, or the "variable" if the object is a
   * Rule, or the "symbol" if the object is an InitialAssignment.
   *
   * @note Because of the inconsistent behavior of this function with respect
   * to assignments and rules, callers should use getIdAttribute() instead.
   *
   * @see getIdAttribute()
   * @see setIdAttribute(const std::string& sid)
   * @see isSetIdAttribute()
   * @see unsetIdAttribute()
   */
  virtual const std::string& getId () const;


  /**
   * Returns the value of the "id" attribute of this SBML object.
   *
   * @copydetails doc_id_attribute
   *
   * @return the id of this SBML object, if set and valid for this
   * level and version of SBML; an empty string otherwise.
   *
   * @note Because of the inconsistent behavior of this function with respect
   * to assignments and rules, callers should use getIdAttribute() instead.
   *
   * @see setIdAttribute(const std::string& sid)
   * @see isSetIdAttribute()
   * @see unsetIdAttribute()
   */
  const std::string& getIdAttribute() const;


  /**
   * Returns the value of the "name" attribute of this SBML object.
   *
   * @copydetails doc_get_name
   */
  virtual const std::string& getName () const;


  /**
   * Returns the content of the "notes" subelement of this object as
   * a tree of XMLNode objects.
   *
   * @copydetails doc_what_are_notes 
   *
   * The "notes" element content returned by this method will be in XML
   * form, but libSBML does not provide an object model specifically for
   * the content of notes.  Callers will need to traverse the XML tree
   * structure using the facilities available on XMLNode and related
   * objects.  For an alternative method of accessing the notes, see
   * getNotesString().
   *
   * @return the content of the "notes" subelement of this SBML object as a
   * tree structure composed of XMLNode objects.
   *
   * @see getNotesString()
   * @see getNotesMarkdown()
   * @see isSetNotes()
   * @see setNotes(const XMLNode* notes)
   * @see setNotes(const std::string& notes, bool addXHTMLMarkup)
   * @see setNotesFromMarkdown(const std::string& markdown)
   * @see appendNotes(const XMLNode* notes)
   * @see appendNotes(const std::string& notes)
   * @see unsetNotes()
   * @see SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif)
   */
  XMLNode* getNotes();


  /**
   * Returns the content of the "notes" subelement of this object as
   * a tree of XMLNode objects.
   *
   * @copydetails doc_what_are_notes 
   *
   * The "notes" element content returned by this method will be in XML
   * form, but libSBML does not provide an object model specifically for
   * the content of notes.  Callers will need to traverse the XML tree
   * structure using the facilities available on XMLNode and related
   * objects.  For an alternative method of accessing the notes, see
   * getNotesString().
   *
   * @return the content of the "notes" subelement of this SBML object as a
   * tree structure composed of XMLNode objects.
   *
   * @see getNotesString()
   * @see getNotesMarkdown()
   * @see isSetNotes()
   * @see setNotes(const XMLNode* notes)
   * @see setNotes(const std::string& notes, bool addXHTMLMarkup)
   * @see setNotesFromMarkdown(const std::string& markdown)
   * @see appendNotes(const XMLNode* notes)
   * @see appendNotes(const std::string& notes)
   * @see unsetNotes()
   * @see SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif)
   */
  XMLNode* getNotes() const;


  /**
   * Returns the content of the "notes" subelement of this object as a
   * string.
   *
   * @copydetails doc_what_are_notes 
   *
   * For an alternative method of accessing the notes, see getNotes(),
   * which returns the content as an XMLNode tree structure.  Depending on
   * an application's needs, one or the other method may be more
   * convenient.
   *
   * @return the content of the "notes" subelement of this SBML object as a
   * string.
   *
   * @see getNotes()
   * @see getNotesMarkdown()
   * @see isSetNotes()
   * @see setNotes(const XMLNode* notes)
   * @see setNotes(const std::string& notes, bool addXHTMLMarkup)
   * @see setNotesFromMarkdown(const std::string& markdown)
   * @see appendNotes(const XMLNode* notes)
   * @see appendNotes(const std::string& notes)
   * @see unsetNotes()
   * @see SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif)
   */
  std::string getNotesString ();


  /**
   * Returns the content of the "notes" subelement of this object as a
   * string.
   *
   * @copydetails doc_what_are_notes 
   *
   * For an alternative method of accessing the notes, see getNotes(),
   * which returns the content as an XMLNode tree structure.  Depending on
   * an application's needs, one or the other method may be more
   * convenient.
   *
   * @return the content of the "notes" subelement of this SBML object as a
   * string.
   *
   * @see getNotes()
   * @see getNotesMarkdown()
   * @see isSetNotes()
   * @see setNotes(const XMLNode* notes)
   * @see setNotes(const std::string& notes, bool addXHTMLMarkup)
   * @see setNotesFromMarkdown(const std::string& markdown)
   * @see appendNotes(const XMLNode* notes)
   * @see appendNotes(const std::string& notes)
   * @see unsetNotes()
   * @see SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif)
   */
  std::string getNotesString () const;

  /**
   * Returns the markdown version of the "notes" subelement of this object.
   * The HTML is translated by 'html2md', https://github.com/tim-gromeyer/html2md/
   *
   * @copydetails doc_what_are_notes
   *
   * For an alternative method of accessing the notes, see getNotes(),
   * which returns the content as an XMLNode tree structure.  Depending on
   * an application's needs, one or the other method may be more
   * convenient.
   *
   * @return the string (char*) representing the markdown version of the notes 
   * from this structure.
   *
   * @see getNotes()
   * @see getNotesString()
   * @see isSetNotes()
   * @see setNotes(const XMLNode* notes)
   * @see setNotes(const std::string& notes, bool addXHTMLMarkup)
   * @see appendNotes(const XMLNode* notes)
   * @see appendNotes(const std::string& notes)
   * @see unsetNotes()
   * @see SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif)
   */
  std::string getNotesMarkdown() const;


  /**
   * Returns the content of the "annotation" subelement of this object as
   * a tree of XMLNode objects.
   *
   * @copydetails doc_what_are_annotations 
   *
   * The annotations returned by this method will be in XML form.  LibSBML
   * provides an object model and related interfaces for certain specific
   * kinds of annotations, namely model history information and RDF
   * content.  See the ModelHistory, CVTerm and RDFAnnotationParser classes
   * for more information about the facilities available.
   *
   * @return the annotation of this SBML object as a tree of XMLNode objects.
   *
   * @see getAnnotationString()
   * @see isSetAnnotation()
   * @see setAnnotation(const XMLNode* annotation)
   * @see setAnnotation(const std::string& annotation)
   * @see appendAnnotation(const XMLNode* annotation)
   * @see appendAnnotation(const std::string& annotation)
   * @see unsetAnnotation()
   */
  XMLNode* getAnnotation ();


  /**
   * Returns the content of the "annotation" subelement of this object as
   * a tree of XMLNode objects.
   *
   * @copydetails doc_what_are_annotations 
   *
   * The annotations returned by this method will be in XML form.  LibSBML
   * provides an object model and related interfaces for certain specific
   * kinds of annotations, namely model history information and RDF
   * content.  See the ModelHistory, CVTerm and RDFAnnotationParser classes
   * for more information about the facilities available.
   *
   * @return the annotation of this SBML object as a tree of XMLNode objects.
   *
   * @see getAnnotationString()
   * @see isSetAnnotation()
   * @see setAnnotation(const XMLNode* annotation)
   * @see setAnnotation(const std::string& annotation)
   * @see appendAnnotation(const XMLNode* annotation)
   * @see appendAnnotation(const std::string& annotation)
   * @see unsetAnnotation()
   */
  XMLNode* getAnnotation () const;


  /**
   * Returns the content of the "annotation" subelement of this object as a
   * character string.
   *
   * @copydetails doc_what_are_annotations 
   *
   * The annotations returned by this method will be in string form.  See the
   * method getAnnotation() for a version that returns annotations in XML form.
   *
   * @return the annotation of this SBML object as a character string.
   *
   * @see getAnnotation()
   * @see isSetAnnotation()
   * @see setAnnotation(const XMLNode* annotation)
   * @see setAnnotation(const std::string& annotation)
   * @see appendAnnotation(const XMLNode* annotation)
   * @see appendAnnotation(const std::string& annotation)
   * @see unsetAnnotation()
   */
  std::string getAnnotationString ();


  /**
   * Returns the content of the "annotation" subelement of this object as a
   * character string.
   *
   * @copydetails doc_what_are_annotations
   *
   * The annotations returned by this method will be in string form.  See the
   * method getAnnotation() for a version that returns annotations in XML form.
   *
   * @return the annotation of this SBML object as a character string.
   *
   * @see getAnnotation()
   * @see isSetAnnotation()
   * @see setAnnotation(const XMLNode* annotation)
   * @see setAnnotation(const std::string& annotation)
   * @see appendAnnotation(const XMLNode* annotation)
   * @see appendAnnotation(const std::string& annotation)
   * @see unsetAnnotation()
   */
  std::string getAnnotationString () const;


  /**
   * Returns a list of the XML Namespaces declared on the SBML document
   * owning this object.
   *
   * The SBMLNamespaces object encapsulates SBML Level/Version/namespaces
   * information.  It is used to communicate the SBML Level, Version, and (in
   * Level&nbsp;3) packages used in addition to SBML Level&nbsp;3 Core.
   *
   * @return the XML Namespaces associated with this SBML object, or @c NULL
   * in certain very usual circumstances where a namespace is not set.
   *
   * @see getLevel()
   * @see getVersion()
   */
  virtual XMLNamespaces* getNamespaces() const ;


  /**
   * Returns the SBMLDocument object containing this object instance.
   *
   * @copydetails doc_what_is_SBMLDocument
   *
   * This method allows the caller to obtain the SBMLDocument for the
   * current object.
   * 
   * @return the parent SBMLDocument object of this SBML object.
   *
   * @see getParentSBMLObject()
   * @see getModel()
   */
  const SBMLDocument* getSBMLDocument () const;


  /**
   * Returns the SBMLDocument object containing this object instance.
   *
   * @copydetails doc_what_is_SBMLDocument
   *
   * This method allows the caller to obtain the SBMLDocument for the
   * current object.
   * 
   * @return the parent SBMLDocument object of this SBML object.
   *
   * @see getParentSBMLObject()
   * @see getModel()
   */
  SBMLDocument* getSBMLDocument ();


  /**
   * Returns the parent SBML object containing this object.
   *
   * This returns the immediately-containing object.  This method is
   * convenient when holding an object nested inside other objects in an
   * SBML model.  
   * 
   * @return the parent SBML object of this SBML object.
   *
   * @see getSBMLDocument()
   * @see getModel()
   */
  SBase* getParentSBMLObject();


  /**
   * Returns the parent SBML object containing this object.
   *
   * This returns the immediately-containing object.  This method is
   * convenient when holding an object nested inside other objects in an
   * SBML model.  
   * 
   * @return the parent SBML object of this SBML object.
   *
   * @see getSBMLDocument()
   * @see getModel()
   */
  const SBase* getParentSBMLObject() const;


  /**
   * Returns the first ancestor object that has the given SBML type code from the given package.
   *
   * @if clike LibSBML attaches an identifying code to every kind of SBML
   * object.  These are known as <em>SBML type codes</em>.  The set of
   * possible type codes is defined in the enumeration #SBMLTypeCode_t.
   * The names of the type codes all begin with the characters
   * @c SBML_. @endif@if java LibSBML attaches an identifying code to every
   * kind of SBML object.  These are known as <em>SBML type codes</em>.  In
   * other languages, the set of type codes is stored in an enumeration; in
   * the Java language interface for libSBML, the type codes are defined as
   * static integer constants in the interface class {@link
   * libsbmlConstants}.  The names of the type codes all begin with the
   * characters @c SBML_. @endif@if python LibSBML attaches an identifying
   * code to every kind of SBML object.  These are known as <em>SBML type
   * codes</em>.  In the Python language interface for libSBML, the type
   * codes are defined as static integer constants in the interface class
   * @link libsbml@endlink.  The names of the type codes all begin with the
   * characters @c SBML_. @endif@if csharp LibSBML attaches an identifying
   * code to every kind of SBML object.  These are known as <em>SBML type
   * codes</em>.  In the C# language interface for libSBML, the type codes
   * are defined as static integer constants in the interface class @link
   * libsbmlcs.libsbml libsbml@endlink.  The names of the type codes all begin with
   * the characters @c SBML_. @endif@~
   *
   * This method searches the tree of objects that are parents of this
   * object, and returns the first one that has the given SBML type code from 
   * the given @p pkgName.
   *
   * @param type the SBML type code of the object sought.
   *
   * @param pkgName (optional) the short name of an SBML Level&nbsp;3
   * package to which the sought-after object must belong.
   * 
   * @return the ancestor SBML object of this SBML object that corresponds
   * to the given @if clike #SBMLTypeCode_t value@else SBML object type
   * code@endif, or @c NULL if no ancestor exists.
   *
   * @warning The optional argument @p pkgName must be used for all type codes
   * from SBML Level&nbsp;3 packages.  Otherwise, the function will search the 
   * "core" namespace alone, not find any corresponding elements, and return 
   * NULL.
   *
   * @ifnot hasDefaultArgs @htmlinclude warn-default-args-in-docs.html @endif@~
   */
  SBase* getAncestorOfType(int type, const std::string& pkgName = "core");


  /**
   * Returns the first ancestor object that has the given SBML type code from the given package.
   *
   * @if clike LibSBML attaches an identifying code to every kind of SBML
   * object.  These are known as <em>SBML type codes</em>.  The set of
   * possible type codes is defined in the enumeration #SBMLTypeCode_t.
   * The names of the type codes all begin with the characters
   * @c SBML_. @endif@if java LibSBML attaches an identifying code to every
   * kind of SBML object.  These are known as <em>SBML type codes</em>.  In
   * other languages, the set of type codes is stored in an enumeration; in
   * the Java language interface for libSBML, the type codes are defined as
   * static integer constants in the interface class {@link
   * libsbmlConstants}.  The names of the type codes all begin with the
   * characters @c SBML_. @endif@if python LibSBML attaches an identifying
   * code to every kind of SBML object.  These are known as <em>SBML type
   * codes</em>.  In the Python language interface for libSBML, the type
   * codes are defined as static integer constants in the interface class
   * @link libsbml@endlink.  The names of the type codes all begin with the
   * characters @c SBML_. @endif@if csharp LibSBML attaches an identifying
   * code to every kind of SBML object.  These are known as <em>SBML type
   * codes</em>.  In the C# language interface for libSBML, the type codes
   * are defined as static integer constants in the interface class @link
   * libsbmlcs.libsbml libsbml@endlink.  The names of the type codes all begin with
   * the characters @c SBML_. @endif@~
   *
   * This method searches the tree of objects that are parents of this
   * object, and returns the first one that has the given SBML type code from 
   * the given @p pkgName.
   *
   * @param type the SBML type code of the object sought.
   *
   * @param pkgName (optional) the short name of an SBML Level&nbsp;3
   * package to which the sought-after object must belong.
   * 
   * @return the ancestor SBML object of this SBML object that corresponds
   * to the given @if clike #SBMLTypeCode_t value@else SBML object type
   * code@endif, or @c NULL if no ancestor exists.
   *
   * @warning The optional argument @p pkgName must be used for all type codes
   * from SBML Level&nbsp;3 packages.  Otherwise, the function will search the 
   * "core" namespace alone, not find any corresponding elements, and return 
   * NULL.
   *
   * @ifnot hasDefaultArgs @htmlinclude warn-default-args-in-docs.html @endif@~
   */
  const SBase* getAncestorOfType(int type, const std::string pkgName = "core") const;


  /**
   * Returns the integer portion of the value of the "sboTerm" attribute of
   * this object.
   *
   * @copydetails doc_sbo_terms
   * @copydetails doc_sbo_terms_addendum
   *
   * @return the value of the "sboTerm" attribute as an integer, or @c -1
   * if the value is not set.
   */
  int getSBOTerm () const;


  /**
   * Returns the string representation of the "sboTerm" attribute of
   * this object.
   *
   * @copydetails doc_sbo_terms
   * @copydetails doc_sbo_terms_addendum
   *
   * @return the value of the "sboTerm" attribute as a string (its value
   * will be of the form "SBO:NNNNNNN"), or an empty string if
   * the value is not set.
   */
  std::string getSBOTermID () const;


  /**
   * Returns the URL representation of the "sboTerm" attribute of this
   * object.
   *
   * This method returns the entire SBO identifier as a text string in the
   * form <code style='margin-right:0; padding-right:0'>http</code><code style='margin-left:0; padding-left:0'>://identifiers.org/biomodels.sbo/SBO:NNNNNNN"</code>.
   *
   * @copydetails doc_sbo_terms_addendum
   *
   * @return the value of the "sboTerm" attribute as an identifiers.org URL,
   * or an empty string if the value is not set.
   */
  std::string getSBOTermAsURL () const;


  /**
   * Returns the line number where this object first appears in the XML
   * representation of the SBML document.
   *
   * @return the line number of this SBML object.  If this object was
   * created programmatically and not read from a file, this method will
   * return the value @c 0.
   *
   * @note The line number for each construct in an SBML model is set upon
   * reading the model.  The accuracy of the line number depends on the
   * correctness of the XML representation of the model, and on the
   * particular XML parser library being used.  The former limitation
   * relates to the following problem: if the model is actually invalid
   * XML, then the parser may not be able to interpret the data correctly
   * and consequently may not be able to establish the real line number.
   * The latter limitation is simply that different parsers seem to have
   * their own accuracy limitations, and out of all the parsers supported
   * by libSBML, none have been 100% accurate in all situations. (At this
   * time, libSBML supports the use of <a target="_blank"
   * href="http://xmlsoft.org">libxml2</a>, <a target="_blank"
   * href="http://expat.sourceforge.net/">Expat</a> and <a target="_blank"
   * href="http://xerces.apache.org/xerces-c/">Xerces</a>.)
   *
   * @see getColumn()
   */
  unsigned int getLine () const;


  /**
   * Returns the column number where this object first appears in the XML
   * representation of the SBML document.
   *
   * @return the column number of this SBML object.  If this object was
   * created programmatically and not read from a file, this method will
   * return the value @c 0.
   *
   * @note The column number for each construct in an SBML model is set
   * upon reading the model.  The accuracy of the column number depends on
   * the correctness of the XML representation of the model, and on the
   * particular XML parser library being used.  The former limitation
   * relates to the following problem: if the model is actually invalid
   * XML, then the parser may not be able to interpret the data correctly
   * and consequently may not be able to establish the real column number.
   * The latter limitation is simply that different parsers seem to have
   * their own accuracy limitations, and out of all the parsers supported
   * by libSBML, none have been 100% accurate in all situations. (At this
   * time, libSBML supports the use of <a target="_blank"
   * href="http://xmlsoft.org">libxml2</a>, <a target="_blank"
   * href="http://expat.sourceforge.net/">Expat</a> and <a target="_blank"
   * href="http://xerces.apache.org/xerces-c/">Xerces</a>.)
   * 
   * @see getLine()
   */
  unsigned int getColumn () const;


  /**
   * Returns the ModelHistory object, if any, attached to this object.
   *
   * @return the ModelHistory object attached to this object, or @c NULL if
   * none exist.
   * 
   * @note In SBML Level&nbsp;2, model history annotations were only
   * permitted on the Model element.  In SBML Level&nbsp;3, they are
   * permitted on all SBML components derived from SBase.
   */
  ModelHistory* getModelHistory() const;


  /**
  * Returns the "creation date" portion of the ModelHistory of this object.
  *
  * @return a Date object representing the creation date stored in
  * this ModelHistory object.
  *
  * @note In SBML Level&nbsp;2, model history annotations were only
  * permitted on the Model element.  In SBML Level&nbsp;3, they are
  * permitted on all SBML components derived from SBase.
  */
  Date * getCreatedDate() const;


  /**
   * Returns the ModelHistory object, if any, attached to this object.
   * 
   * @return the ModelHistory object attached to this object, or @c NULL if
   * none exist.
   * 
   * @note In SBML Level&nbsp;2, model history annotations were only
   * permitted on the Model element.  In SBML Level&nbsp;3, they are
   * permitted on all SBML components derived from SBase.
   */
  ModelHistory* getModelHistory();


  /**
  * Returns the "creation date" portion of the ModelHistory of this object.
  *
  * @return a Date object representing the creation date stored in
  * this ModelHistory object.
  *
  * @note In SBML Level&nbsp;2, model history annotations were only
  * permitted on the Model element.  In SBML Level&nbsp;3, they are
  * permitted on all SBML components derived from SBase.
  */
  Date * getCreatedDate();


  /**
  * Get the nth Date object in the list of "modified date" values stored
  * in the ModelHistory of this object.
  *
  * In the MIRIAM format for annotations, there can be multiple
  * modification dates.  The libSBML ModelHistory class supports this by
  * storing a list of "modified date" values.
  *
  * @return the nth Date in the list of ModifiedDates of this
  * ModelHistory or @c NULL if no such object exists.
  */
  Date* getModifiedDate(unsigned int n);


  /**
  * Get the number of Date objects in the ModelHistory of this Iobject's list of
  * "modified dates".
  *
  * In the MIRIAM format for annotations, there can be multiple
  * modification dates.  The libSBML ModelHistory class supports this by
  * storing a list of "modified date" values.
  *
  * @return the number of ModifiedDates in this ModelHistory.
  */
  unsigned int getNumModifiedDates();


  /**
   * Predicate returning @c true if this object's "metaid" attribute is set.
   *
   * @copydetails doc_what_is_metaid 
   *
   * @return @c true if the "metaid" attribute of this SBML object is
   * set, @c false otherwise.
   *
   * @see getMetaId()
   * @see setMetaId(const std::string& metaid)
   */
  bool isSetMetaId () const;


  /**
   * Predicate returning @c true if a call to getId() returns a
   * non-empty string.
   *
   * For most objects, this function will return @c true if its "id"
   * attribute is set, and @c false if it is not, or if the object has no
   * "id" attribute at all.  However, for an EventAssignment or a Rule,
   * isSetId() checks whether the "variable" attribute is set, and for an
   * InitialAssignment, it checks whether the "symbol" attribute is set.
   * Because those elements will also have an "id" attribute in SBML
   * Level&nbsp;3 Version&nbsp;2 which isSetId() will not check, the function
   * itself is deprecated, and it is recommended to use isSetIdAttribute() in
   * all cases where one needs to know whether the "id" attribute is set, and
   * to use EventAssignment::isSetVariable(), Rule::isSetVariable() and
   * InitialAssignment::isSetSymbol() when the status of the "variable" or
   * "symbol" attributes need to be checked.
   *
   * @copydetails doc_isset_id
   */
  virtual bool isSetId () const;


  /**
   * Predicate returning @c true if this object's "id" attribute is set.
   *
   * @copydetails doc_id_attribute
   * 
   * @return @c true if the "id" attribute of this SBML object is
   * set, @c false otherwise.
   *
   * @see getIdAttribute()
   * @see setIdAttribute(const std::string& sid)
   * @see unsetIdAttribute()
   */
  bool isSetIdAttribute() const;


  /**
   * Predicate returning @c true if this
   * object's "name" attribute is set.
   * 
   * @copydetails doc_isset_name
   */
  virtual bool isSetName () const;


  /**
   * Predicate returning @c true if this
   * object's "notes" subelement exists and has content.
   *
   * The optional SBML element named "notes", present on every major SBML
   * component type, is intended as a place for storing optional
   * information intended to be seen by humans.  An example use of the
   * "notes" element would be to contain formatted user comments about the
   * model element in which the "notes" element is enclosed.  Every object
   * derived directly or indirectly from type SBase can have a separate
   * value for "notes", allowing users considerable freedom when adding
   * comments to their models.
   *
   * The format of "notes" elements must be <a target="_blank"
   * href="http://www.w3.org/TR/xhtml1/">XHTML&nbsp;1.0</a>.  To help
   * verify the formatting of "notes" content, libSBML provides the static
   * utility method SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode xhtml@endif); however,
   * readers are urged to consult the appropriate <a target="_blank"
   * href="http://sbml.org/Documents/Specifications">SBML specification
   * document</a> for the Level and Version of their model for more
   * in-depth explanations.  The SBML Level&nbsp;2 and&nbsp;3
   * specifications have considerable detail about how "notes" element
   * content must be structured.
   *
   * @return @c true if a "notes" subelement exists, @c false otherwise.
   * 
   * @see getNotes()
   * @see getNotesString()
   * @see getNotesMarkdown()
   * @see setNotes(const XMLNode* notes)
   * @see setNotes(const std::string& notes, bool addXHTMLMarkup)
   * @see setNotesFromMarkdown(const std::string& markdown)
   * @see appendNotes(const XMLNode* notes)
   * @see appendNotes(const std::string& notes)
   * @see unsetNotes()
   * @see SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif)
   */
  bool isSetNotes () const;


  /**
   * Predicate returning @c true if this
   * object's "annotation" subelement exists and has content.
   *
   * Whereas the SBase "notes" subelement is a container for content to be
   * shown directly to humans, the "annotation" element is a container for
   * optional software-generated content @em not meant to be shown to
   * humans.  Every object derived from SBase can have its own value for
   * "annotation".  The element's content type is <a target="_blank"
   * href="http://www.w3.org/TR/2004/REC-xml-20040204/#elemdecls">XML type
   * "any"</a>, allowing essentially arbitrary well-formed XML data
   * content.
   *
   * SBML places a few restrictions on the organization of the content of
   * annotations; these are intended to help software tools read and write
   * the data as well as help reduce conflicts between annotations added by
   * different tools.  Please see the SBML specifications for more details.
   *
   * @return @c true if a "annotation" subelement exists, @c false
   * otherwise.
   * 
   * @see getAnnotation()
   * @see getAnnotationString()
   * @see setAnnotation(const XMLNode* annotation)
   * @see setAnnotation(const std::string& annotation)
   * @see appendAnnotation(const XMLNode* annotation)
   * @see appendAnnotation(const std::string& annotation)
   * @see unsetAnnotation()
   */
  bool isSetAnnotation () const;


  /**
   * Predicate returning @c true if this
   * object's "sboTerm" attribute is set.
   *
   * @return @c true if the "sboTerm" attribute of this SBML object is
   * set, @c false otherwise.
   */
  bool isSetSBOTerm () const;


  /**
   * Sets the value of the meta-identifier attribute of this SBML object.
   *
   * @copydetails doc_what_is_metaid 
   *
   * The string @p metaid is copied.  
   *
   * @param metaid the identifier string to use as the value of the
   * "metaid" attribute.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_INVALID_ATTRIBUTE_VALUE, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
   * 
   * @see getMetaId()
   * @see isSetMetaId()
   */
  int setMetaId (const std::string& metaid);


  /**
   * Predicate returning @c true if this
   * object has a ModelHistory object attached to it.
   *
   * @return @c true if the ModelHistory of this object is set,
   * @c false otherwise.
   * 
   * @note In SBML Level&nbsp;2, model history annotations were only
   * permitted on the Model element.  In SBML Level&nbsp;3, they are
   * permitted on all SBML components derived from SBase.
   */
  bool isSetModelHistory() const;


  /**
  * Predicate returning @c true if this
  * object has a ModelHistory object attached to it and the created date is set
  *
  * @return @c true if the CreatedDate of the ModelHistory of this object is set,
  * @c false otherwise.
  *
  * @note In SBML Level&nbsp;2, model history annotations were only
  * permitted on the Model element.  In SBML Level&nbsp;3, they are
  * permitted on all SBML components derived from SBase.
  */
  bool isSetCreatedDate() const;


  /**
  * Predicate returning @c true or @c false depending on whether the
  * ModelHistory's "modified date" of this object is set.
  *
  * @return @c true if the modification date value of this ModelHistory
  * object is set, @c false otherwise.
  */
  bool isSetModifiedDate() const;


  /**
   * Sets the value of the "id" attribute of this SBML object.
   *
   * @copydetails doc_set_id
   */
  virtual int setId(const std::string& sid);


  /**
   * Sets the value of the "id" attribute of this SBML object.
   *
   * @copydetails doc_set_id
   */
  virtual int setIdAttribute(const std::string& sid);

  /**
   * Sets the value of the "name" attribute of this SBML object.
   *
   * @copydetails doc_set_name
   */
  virtual int setName (const std::string& name);


  /**
   * Sets the value of the "annotation" subelement of this SBML object.
   *
   * The content of @p annotation is copied, and any previous content of
   * this object's "annotation" subelement is deleted.
   * 
   * Whereas the SBase "notes" subelement is a container for content to be
   * shown directly to humans, the "annotation" element is a container for
   * optional software-generated content @em not meant to be shown to
   * humans.  Every object derived from SBase can have its own value for
   * "annotation".  The element's content type is <a target="_blank"
   * href="http://www.w3.org/TR/2004/REC-xml-20040204/#elemdecls">XML type
   * "any"</a>, allowing essentially arbitrary well-formed XML data
   * content.
   *
   * SBML places a few restrictions on the organization of the content of
   * annotations; these are intended to help software tools read and write
   * the data as well as help reduce conflicts between annotations added by
   * different tools.  Please see the SBML specifications for more details.
   *
   * Call this method will result in any existing content of the
   * "annotation" subelement to be discarded.  Unless you have taken steps
   * to first copy and reconstitute any existing annotations into the @p
   * annotation that is about to be assigned, it is likely that performing
   * such wholesale replacement is unfriendly towards other software
   * applications whose annotations are discarded.  An alternative may be
   * to use SBase::appendAnnotation(const XMLNode* annotation) or
   * SBase::appendAnnotation(const std::string& annotation).
   *
   * @param annotation an XML structure that is to be used as the new content
   * of the "annotation" subelement of this object.
   *
   * @copydetails doc_returns_one_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   *
   * @see getAnnotationString()
   * @see isSetAnnotation()
   * @see setAnnotation(const std::string& annotation)
   * @see appendAnnotation(const XMLNode* annotation)
   * @see appendAnnotation(const std::string& annotation)
   * @see unsetAnnotation()
   */
  virtual int setAnnotation (const XMLNode* annotation);


  /**
   * Sets the value of the "annotation" subelement of this SBML object.
   *
   * The content of @p annotation is copied, and any previous content of
   * this object's "annotation" subelement is deleted.
   * 
   * Whereas the SBase "notes" subelement is a container for content to be
   * shown directly to humans, the "annotation" element is a container for
   * optional software-generated content @em not meant to be shown to
   * humans.  Every object derived from SBase can have its own value for
   * "annotation".  The element's content type is <a target="_blank"
   * href="http://www.w3.org/TR/2004/REC-xml-20040204/#elemdecls">XML type
   * "any"</a>, allowing essentially arbitrary well-formed XML data
   * content.
   *
   * SBML places a few restrictions on the organization of the content of
   * annotations; these are intended to help software tools read and write
   * the data as well as help reduce conflicts between annotations added by
   * different tools.  Please see the SBML specifications for more details.
   *
   * Call this method will result in any existing content of the
   * "annotation" subelement to be discarded.  Unless you have taken steps
   * to first copy and reconstitute any existing annotations into the @p
   * annotation that is about to be assigned, it is likely that performing
   * such wholesale replacement is unfriendly towards other software
   * applications whose annotations are discarded.  An alternative may be
   * to use SBase::appendAnnotation(const XMLNode* annotation) or
   * SBase::appendAnnotation(const std::string& annotation).
   *
   * @param annotation an XML string that is to be used as the content
   * of the "annotation" subelement of this object.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   *
   * @see getAnnotationString()
   * @see isSetAnnotation()
   * @see setAnnotation(const XMLNode* annotation)
   * @see appendAnnotation(const XMLNode* annotation)
   * @see appendAnnotation(const std::string& annotation)
   * @see unsetAnnotation()
   */
  virtual int setAnnotation (const std::string& annotation);


  /**
   * Appends the given @p annotation to the "annotation" subelement of this
   * object.
   * 
   * Whereas the SBase "notes" subelement is a container for content to be
   * shown directly to humans, the "annotation" element is a container for
   * optional software-generated content @em not meant to be shown to
   * humans.  Every object derived from SBase can have its own value for
   * "annotation".  The element's content type is <a
   * target="_blank"
   * href="http://www.w3.org/TR/2004/REC-xml-20040204/#elemdecls">XML type "any"</a>,
   * allowing essentially arbitrary well-formed XML data content.
   *
   * SBML places a few restrictions on the organization of the content of
   * annotations; these are intended to help software tools read and write
   * the data as well as help reduce conflicts between annotations added by
   * different tools.  Please see the SBML specifications for more details.
   *
   * Unlike SBase::setAnnotation(const XMLNode* annotation) or
   * SBase::setAnnotation(const std::string& annotation), this method
   * allows other annotations to be preserved when an application adds its
   * own data.
   *
   * @param annotation an XML structure that is to be copied and appended
   * to the content of the "annotation" subelement of this object.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
   * (if the parent element does not have the 'metaid' attribute set)
   * @li @sbmlconstant{LIBSBML_DUPLICATE_ANNOTATION_NS, OperationReturnValues_t}
   * (if the parent was already annotated with the annotation in question)
   *
   * @see getAnnotationString()
   * @see isSetAnnotation()
   * @see setAnnotation(const XMLNode* annotation)
   * @see setAnnotation(const std::string& annotation)
   * @see appendAnnotation(const std::string& annotation)
   * @see unsetAnnotation()
   */
  virtual int appendAnnotation (const XMLNode* annotation);


  /**
   * Appends the given @p annotation to the "annotation" subelement of this
   * object.
   *
   * Whereas the SBase "notes" subelement is a container for content to be
   * shown directly to humans, the "annotation" element is a container for
   * optional software-generated content @em not meant to be shown to
   * humans.  Every object derived from SBase can have its own value for
   * "annotation".  The element's content type is <a
   * target="_blank"
   * href="http://www.w3.org/TR/2004/REC-xml-20040204/#elemdecls">XML type "any"</a>,
   * allowing essentially arbitrary well-formed XML data content.
   *
   * SBML places a few restrictions on the organization of the content of
   * annotations; these are intended to help software tools read and write
   * the data as well as help reduce conflicts between annotations added by
   * different tools.  Please see the SBML specifications for more details.
   *
   * Unlike SBase::setAnnotation(const XMLNode* annotation) or
   * SBase::setAnnotation(const std::string& annotation), this method
   * allows other annotations to be preserved when an application adds its
   * own data.
   *
   * @param annotation an XML string that is to be copied and appended
   * to the content of the "annotation" subelement of this object.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
   * (if the parent element does not have the 'metaid' attribute set)
   * @li @sbmlconstant{LIBSBML_DUPLICATE_ANNOTATION_NS, OperationReturnValues_t}
   * (if the parent was already annotated with the annotation in question)
   *
   * @see getAnnotationString()
   * @see isSetAnnotation()
   * @see setAnnotation(const XMLNode* annotation)
   * @see setAnnotation(const std::string& annotation)
   * @see appendAnnotation(const XMLNode* annotation)
   * @see unsetAnnotation()
   */
  virtual int appendAnnotation (const std::string& annotation);


  /**
   * Removes the top-level element within the "annotation" subelement of this
   * SBML object with the given name and optional URI.
   *
   * SBML places a few restrictions on the organization of the content of
   * annotations; these are intended to help software tools read and write
   * the data as well as help reduce conflicts between annotations added by
   * different tools.  Please see the SBML specifications for more details.
   *
   * Calling this method allows a particular annotation element to be removed
   * whilst the remaining annotations remain intact.
   *
   * @param elementName a string representing the name of the top level
   * annotation element that is to be removed.
   * @param elementURI an optional string that is used to check both the name
   * and URI of the top level element to be removed.
   * @param removeEmpty if after removing of the element, the annotation is 
   * empty, and the removeEmpty argument is true, the annotation node will be 
   * deleted (default). 
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_ANNOTATION_NAME_NOT_FOUND, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_ANNOTATION_NS_NOT_FOUND, OperationReturnValues_t}
   *
   * @see replaceTopLevelAnnotationElement(const XMLNode *)
   * @see replaceTopLevelAnnotationElement(const std::string&)
   */
  int removeTopLevelAnnotationElement(const std::string& elementName, 
    const std::string elementURI = "", bool removeEmpty = true);


  /**
   * Replaces the given top-level element within the "annotation" 
   * subelement of this SBML object and with the annotation element supplied.
   *
   * SBML places a few restrictions on the organization of the content of
   * annotations; these are intended to help software tools read and write
   * the data as well as help reduce conflicts between annotations added by
   * different tools.  Please see the SBML specifications for more details.
   *
   * This method determines the name of the element to be replaced from the
   * annotation argument. Functionally it is equivalent to calling <code>
   * removeTopLevelAnnotationElement(name)</code> followed by calling
   * <code>appendAnnotation(annotation_with_name)</code>, with the exception
   * that the placement of the annotation element remains the same.
   *
   * @param annotation XMLNode representing the replacement top level annotation.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
   *
   * @see removeTopLevelAnnotationElement(const std::string elementName, const std::string elementURI, bool removeEmpty)
   * @see replaceTopLevelAnnotationElement(const std::string&)
   */
  int replaceTopLevelAnnotationElement(const XMLNode* annotation);


  /**
   * Replaces the given top-level element within the "annotation" 
   * subelement of this SBML object and with the annotation element supplied.
   *
   * SBML places a few restrictions on the organization of the content of
   * annotations; these are intended to help software tools read and write
   * the data as well as help reduce conflicts between annotations added by
   * different tools.  Please see the SBML specifications for more details.
   *
   * This method determines the name of the element to be replaced from the
   * annotation argument. Functionally it is equivalent to calling <code>
   * removeTopLevelAnnotationElement(name)</code> followed by calling
   * <code>appendAnnotation(annotation_with_name)</code>, with the exception
   * that the placement of the annotation element remains the same.
   *
   * @param annotation string representing the replacement top level annotation.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
   *
   * @see removeTopLevelAnnotationElement(const std::string elementName, const std::string elementURI)
   * @see replaceTopLevelAnnotationElement(const XMLNode*)
   */
  int replaceTopLevelAnnotationElement(const std::string& annotation);


  /**
   * Sets the value of the "notes" subelement of this SBML object.
   *
   * The content of @p notes is copied, and any existing content of this
   * object's "notes" subelement is deleted.
   *
   * The optional SBML element named "notes", present on every major SBML
   * component type, is intended as a place for storing optional
   * information intended to be seen by humans.  An example use of the
   * "notes" element would be to contain formatted user comments about the
   * model element in which the "notes" element is enclosed.  Every object
   * derived directly or indirectly from type SBase can have a separate
   * value for "notes", allowing users considerable freedom when adding
   * comments to their models.
   *
   * The format of "notes" elements must be <a target="_blank"
   * href="http://www.w3.org/TR/xhtml1/">XHTML&nbsp;1.0</a>.  To help
   * verify the formatting of "notes" content, libSBML provides the static
   * utility method SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode xhtml@endif); however,
   * readers are urged to consult the appropriate <a target="_blank"
   * href="http://sbml.org/Documents/Specifications">SBML specification
   * document</a> for the Level and Version of their model for more
   * in-depth explanations.  The SBML Level&nbsp;2 and&nbsp;3
   * specifications have considerable detail about how "notes" element
   * content must be structured.
   *
   * @param notes an XML structure that is to be used as the content of the
   * "notes" subelement of this object.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
   *
   * @see getNotesString()
   * @see getNotesMarkdown()
   * @see isSetNotes()
   * @see setNotes(const std::string& notes, bool addXHTMLMarkup)
   * @see setNotesFromMarkdown(const std::string& markdown)
   * @see appendNotes(const XMLNode* notes)
   * @see appendNotes(const std::string& notes)
   * @see unsetNotes()
   * @see SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif)
   */
  int setNotes(const XMLNode* notes);


  /**
   * Sets the value of the "notes" subelement of this SBML object to a copy
   * of the string @p notes.
   *
   * The content of @p notes is copied, and any existing content of this
   * object's "notes" subelement is deleted.
   *
   * The optional SBML element named "notes", present on every major SBML
   * component type, is intended as a place for storing optional
   * information intended to be seen by humans.  An example use of the
   * "notes" element would be to contain formatted user comments about the
   * model element in which the "notes" element is enclosed.  Every object
   * derived directly or indirectly from type SBase can have a separate
   * value for "notes", allowing users considerable freedom when adding
   * comments to their models.
   *
   * The format of "notes" elements must be <a target="_blank"
   * href="http://www.w3.org/TR/xhtml1/">XHTML&nbsp;1.0</a>.  To help
   * verify the formatting of "notes" content, libSBML provides the static
   * utility method SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif); however,
   * readers are urged to consult the appropriate <a target="_blank"
   * href="http://sbml.org/Documents/Specifications">SBML specification
   * document</a> for the Level and Version of their model for more
   * in-depth explanations.  The SBML Level&nbsp;2 and&nbsp;3
   * specifications have considerable detail about how "notes" element
   * content must be structured.
   *
   * The following code illustrates a very simple way of setting the notes
   * using this method.  Here, the object being annotated is the whole SBML
   * document, but that is for illustration purposes only; you could of
   * course use this same approach to annotate any other SBML component.
   * @if cpp
@code{.cpp}
SBMLDocument* s = new SBMLDocument(3, 1);
s->setNotes("<body xmlns='http://www.w3.org/1999/xhtml'><p>here is my note</p></body>");
@endcode
@endif
@if java
@code{.java}
SBMLDocument s = new SBMLDocument(3, 1);
s.setNotes("<body xmlns='http://www.w3.org/1999/xhtml'><p>here is my note</p></body>");
@endcode
@endif
@if python
@code{.py}
try:
  sbmlDoc = SBMLDocument(3, 1)
except ValueError:
  print('Could not create SBMLDocument object')
  sys.exit(1)

note = "<body xmlns='http://www.w3.org/1999/xhtml'><p>here is my note</p></body>"

status = sbmlDoc.setNotes(note)
if status != LIBSBML_OPERATION_SUCCESS:
  # Do something to handle the error here.
  print("Unable to set notes on the SBML document object")
  sys.exit(1)
@endcode
@endif
@if csharp
@code
SBMLDocument s = new SBMLDocument(3, 1);
s.setNotes("<body xmlns='http://www.w3.org/1999/xhtml'><p>here is my note</p></body>");
@endcode
@endif@~
   *
   * @param notes an XML string that is to be used as the content of the
   * "notes" subelement of this object.
   *
   * @param addXHTMLMarkup a boolean indicating whether to wrap the contents
   * of the @p notes argument with XHTML paragraph (<code>&lt;p&gt;</code>)
   * tags.  This is appropriate when the string in @p notes does not already
   * containg the appropriate XHTML markup.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   *
   * @see getNotesString()
   * @see getNotesMarkdown()
   * @see isSetNotes()
   * @see setNotes(const XMLNode* notes)
   * @see setNotesFromMarkdown(const std::string& markdown)
   * @see appendNotes(const XMLNode* notes)
   * @see appendNotes(const std::string& notes)
   * @see unsetNotes()
   * @see SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif)
   */
  int setNotes(const std::string& notes, bool addXHTMLMarkup = false);


  /**
   * Sets the value of the "notes" subelement of this SBML object using a 
   * markdown-formatted string.
   *
   * The content of @p notes is translated to HTML, and any existing 
   * content of this object's "notes" subelement is deleted.
   *
   * The optional SBML element named "notes", present on every major SBML
   * component type, is intended as a place for storing optional
   * information intended to be seen by humans.  An example use of the
   * "notes" element would be to contain formatted user comments about the
   * model element in which the "notes" element is enclosed.  Every object
   * derived directly or indirectly from type SBase can have a separate
   * value for "notes", allowing users considerable freedom when adding
   * comments to their models.
   *
   * The markdown input is translated using the 'maddy' library.  A
   * description of how the text is translated to HTML can be found at
   * https://github.com/progsource/maddy/blob/master/docs/definitions.md
   */
int setNotesFromMarkdown(const std::string& markdown);


  /**
   * Appends the given @p notes to the "notes" subelement of this object.
   *
   * The content of @p notes is copied.
   *
   * The optional SBML element named "notes", present on every major SBML
   * component type, is intended as a place for storing optional
   * information intended to be seen by humans.  An example use of the
   * "notes" element would be to contain formatted user comments about the
   * model element in which the "notes" element is enclosed.  Every object
   * derived directly or indirectly from type SBase can have a separate
   * value for "notes", allowing users considerable freedom when adding
   * comments to their models.
   *
   * The format of "notes" elements must be <a target="_blank"
   * href="http://www.w3.org/TR/xhtml1/">XHTML&nbsp;1.0</a>.  To help
   * verify the formatting of "notes" content, libSBML provides the static
   * utility method SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif); however,
   * readers are urged to consult the appropriate <a target="_blank"
   * href="http://sbml.org/Documents/Specifications">SBML specification
   * document</a> for the Level and Version of their model for more
   * in-depth explanations.  The SBML Level&nbsp;2 and&nbsp;3
   * specifications have considerable detail about how "notes" element
   * content must be structured.
   * 
   * @param notes an XML node structure that is to appended to the content
   * of the "notes" subelement of this object.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   *
   * @see getNotesString()
   * @see getNotesMarkdown()
   * @see isSetNotes()
   * @see setNotes(const XMLNode* notes)
   * @see setNotes(const std::string& notes, bool addXHTMLMarkup)
   * @see setNotesFromMarkdown(const std::string& markdown)
   * @see appendNotes(const std::string& notes)
   * @see unsetNotes()
   * @see SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif)
   */
  int appendNotes(const XMLNode* notes);


  /**
   * Appends the given @p notes to the "notes" subelement of this object.
   *
   * The content of the parameter @p notes is copied.
   *
   * The optional SBML element named "notes", present on every major SBML
   * component type, is intended as a place for storing optional
   * information intended to be seen by humans.  An example use of the
   * "notes" element would be to contain formatted user comments about the
   * model element in which the "notes" element is enclosed.  Every object
   * derived directly or indirectly from type SBase can have a separate
   * value for "notes", allowing users considerable freedom when adding
   * comments to their models.
   *
   * The format of "notes" elements must be <a target="_blank"
   * href="http://www.w3.org/TR/xhtml1/">XHTML&nbsp;1.0</a>.  To help
   * verify the formatting of "notes" content, libSBML provides the static
   * utility method SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif); however,
   * readers are urged to consult the appropriate <a target="_blank"
   * href="http://sbml.org/Documents/Specifications">SBML specification
   * document</a> for the Level and Version of their model for more
   * in-depth explanations.  The SBML Level&nbsp;2 and&nbsp;3
   * specifications have considerable detail about how "notes" element
   * content must be structured.
   *
   * @param notes an XML string that is to appended to the content of
   * the "notes" subelement of this object.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   *
   * @see getNotesString()
   * @see getNotesMarkdown()
   * @see isSetNotes()
   * @see setNotes(const XMLNode* notes)
   * @see setNotes(const std::string& notes, bool addXHTMLMarkup)
   * @see setNotesFromMarkdown(const std::string& markdown)
   * @see appendNotes(const XMLNode* notes)
   * @see unsetNotes()
   * @see SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif)
   */
  int appendNotes(const std::string& notes);


  /**
   * Sets the ModelHistory of this object.
   *
   * The content of @p history is copied, and this object's existing model
   * history content is deleted.
   *
   * @param history ModelHistory of this object.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
   * 
   * @note In SBML Level&nbsp;2, model history annotations were only
   * permitted on the Model element.  In SBML Level&nbsp;3, they are
   * permitted on all SBML components derived from SBase.
   */
  int setModelHistory(ModelHistory * history);


  /**
  * Sets the creation date of the ModelHistory of this object.
  *
  * @param date a Date object representing the date to which the "created
  * date" portion of this ModelHistory should be set.
  *
  * @copydetails doc_returns_success_code
  * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
  * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
  */
  int setCreatedDate(Date* date);


  /**
  * Adds a modified date to the ModelHistory of this object.
  *
  * @param date a Date object representing the date to which the "modified
  * date" portion of this ModelHistory should be set.
  *
  * @copydetails doc_returns_success_code
  * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
  * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
  */
  int addModifiedDate(Date* date);


  /** @cond doxygenLibsbmlInternal */
  /**
   * Sets the parent SBMLDocument of this SBML object.
   *
   * @copydetails doc_what_is_SBMLDocument
   * 
   * @param d the SBMLDocument object to use.
   *
   * @see connectToChild()
   * @if clike
   * @see enablePackageInternal()
   * @endif@~
   */
  virtual void setSBMLDocument (SBMLDocument* d);
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /**
   * Sets the parent SBML object of this SBML object.
   * (Creates a child-parent relationship by the child)
   * This function is called when a child element is
   * set/added/created by its parent element (e.g. by setXXX,
   * addXXX, createXXX, and connectToChild functions of the
   * parent element).
   *
   * @param parent the SBML object to use.
   */
  virtual void connectToParent (SBase* parent);


  /**
   * Sets this SBML object to child SBML objects (if any).
   * (Creates a child-parent relationship by the parent)
   *
   * Subclasses must override this function if they define
   * one ore more child elements.
   * Basically, this function needs to be called in
   * constructor, copy constructor, assignment operator.
   *
   * @if clike
   * @see setSBMLDocument()
   * @see enablePackageInternal()
   * @endif@~
   */
  virtual void connectToChild ();

  /** @endcond */


  /**
   * Sets the value of the "sboTerm" attribute.
   *
   * @copydetails doc_sbo_terms
   * @copydetails doc_sbo_terms_addendum
   *
   * @param value the NNNNNNN integer portion of the SBO identifier.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_INVALID_ATTRIBUTE_VALUE, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
   *
   * @see setSBOTerm(const std::string &sboid)
   */
  virtual int setSBOTerm (int value);


  /**
   * Sets the value of the "sboTerm" attribute by string.
   *
   * @copydetails doc_sbo_terms
   * @copydetails doc_sbo_terms_addendum
   *
   * @param sboid the SBO identifier string of the form "SBO:NNNNNNN".
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_INVALID_ATTRIBUTE_VALUE, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
   *
   * @see setSBOTerm(int value)
   */
  virtual int setSBOTerm (const std::string &sboid);


  /**
   * Sets the namespaces relevant of this SBML object.
   *
   * The content of @p xmlns is copied, and this object's existing
   * namespace content is deleted.
   *
   * The SBMLNamespaces object encapsulates SBML Level/Version/namespaces
   * information.  It is used to communicate the SBML Level, Version, and
   * (in Level&nbsp;3) packages used in addition to SBML Level&nbsp;3 Core.
   * 
   * @param xmlns the namespaces to set.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   */
  int setNamespaces(XMLNamespaces* xmlns);


  /**
   * Unsets the value of the "metaid" attribute of this SBML object.
   *
   * @copydetails doc_what_is_metaid 
   *  
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  int unsetMetaId ();


  /**
   * Unsets the value of the "id" attribute of this SBML object.
   *
   * @copydetails doc_unset_id
   */
  virtual int unsetId ();


  /**
   * Unsets the value of the "id" attribute of this SBML object.
   *
   * Most (but not all) objects in SBML include two common attributes: "id"
   * and "name".  The identifier given by an object's "id" attribute value
   * is used to identify the object within the SBML model definition.
   * Other objects can refer to the component using this identifier.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   *
   * @see getIdAttribute()
   * @see setIdAttribute(const std::string& sid)
   * @see isSetIdAttribute()
   */
  int unsetIdAttribute();


  /**
   * Unsets the value of the "name" attribute of this SBML object.
   *
   * @copydetails doc_unset_name
   */
  virtual int unsetName ();


  /**
   * Unsets the value of the "notes" subelement of this SBML object.
   *
   * The optional SBML element named "notes", present on every major SBML
   * component type, is intended as a place for storing optional
   * information intended to be seen by humans.  An example use of the
   * "notes" element would be to contain formatted user comments about the
   * model element in which the "notes" element is enclosed.  Every object
   * derived directly or indirectly from type SBase can have a separate
   * value for "notes", allowing users considerable freedom when adding
   * comments to their models.
   *
   * The format of "notes" elements must be <a target="_blank"
   * href="http://www.w3.org/TR/xhtml1/">XHTML&nbsp;1.0</a>.  To help
   * verify the formatting of "notes" content, libSBML provides the static
   * utility method SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif); however,
   * readers are urged to consult the appropriate <a target="_blank"
   * href="http://sbml.org/Documents/Specifications">SBML specification
   * document</a> for the Level and Version of their model for more
   * in-depth explanations.  The SBML Level&nbsp;2 and&nbsp;3
   * specifications have considerable detail about how "notes" element
   * content must be structured.
   *
   * @copydetails doc_returns_one_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   *
   * @see getNotesString()
   * @see getNotesMarkdown()
   * @see isSetNotes()
   * @see setNotes(const XMLNode* notes)
   * @see setNotes(const std::string& notes, bool addXHTMLMarkup)
   * @see setNotesFromMarkdown(const std::string& markdown)
   * @see appendNotes(const XMLNode* notes)
   * @see appendNotes(const std::string& notes)
   * @see SyntaxChecker::hasExpectedXHTMLSyntax(@if java XMLNode@endif)
   */
  int unsetNotes ();


  /**
   * Unsets the value of the "annotation" subelement of this SBML object.
   *
   * Whereas the SBase "notes" subelement is a container for content to be
   * shown directly to humans, the "annotation" element is a container for
   * optional software-generated content @em not meant to be shown to
   * humans.  Every object derived from SBase can have its own value for
   * "annotation".  The element's content type is <a target="_blank"
   * href="http://www.w3.org/TR/2004/REC-xml-20040204/#elemdecls">XML type
   * "any"</a>, allowing essentially arbitrary well-formed XML data
   * content.
   *
   * SBML places a few restrictions on the organization of the content of
   * annotations; these are intended to help software tools read and write
   * the data as well as help reduce conflicts between annotations added by
   * different tools.  Please see the SBML specifications for more details.
   *
   * @copydetails doc_returns_one_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   *
   * @see getAnnotation()
   * @see getAnnotationString()
   * @see isSetAnnotation()
   * @see setAnnotation(const XMLNode* annotation)
   * @see setAnnotation(const std::string& annotation)
   * @see appendAnnotation(const XMLNode* annotation)
   * @see appendAnnotation(const std::string& annotation)
   */
  int unsetAnnotation ();


  /**
   * Unsets the value of the "sboTerm" attribute of this SBML object.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
   */
  int unsetSBOTerm ();


  /**
   * Adds a copy of the given CVTerm object to this SBML object.
   *
   * @param term the CVTerm to assign.
   *
   * @param newBag if @c true, creates a new RDF bag with the same identifier
   * as a previous bag, and if @c false, adds the term to an existing
   * RDF bag with the same type of qualifier as the term being added.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}, if
   * this object lacks a "metaid" attribute
   * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
   *
   * @note Since the CV Term uses the "metaid" attribute of the object as a
   * reference, if the object has no "metaid" attribute value set, then the
   * CVTerm will not be added.
   *
   * @copydetails doc_note_object_is_copied
   * 
   * @ifnot hasDefaultArgs @htmlinclude warn-default-args-in-docs.html @endif@~
   */
  int addCVTerm(CVTerm * term, bool newBag = false);


  /**
   * Returns a list of CVTerm objects in the annotations of this SBML
   * object.
   * 
   * @return the list of CVTerms for this SBML object.
   */
  List* getCVTerms();


  /**
   * Returns a list of CVTerm objects in the annotations of this SBML
   * object.
   * 
   * @return the list of CVTerms for this SBML object.
   */
  List* getCVTerms()  const;


  /**
   * Returns the number of CVTerm objects in the annotations of this SBML
   * object.
   * 
   * @return the number of CVTerms for this SBML object.
   */
  unsigned int getNumCVTerms() const;


  /**
   * Returns the nth CVTerm in the list of CVTerms of this SBML
   * object.
   * 
   * @param n unsigned int the index of the CVTerm to retrieve.
   *
   * @return the nth CVTerm in the list of CVTerms for this SBML object.
   * If the index @p n is invalid, @c NULL is returned.
   */
  CVTerm* getCVTerm(unsigned int n);


  /**
   * Clears the list of CVTerm objects attached to this SBML object.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  int unsetCVTerms();


  /**
   * Unsets the ModelHistory object attached to this object.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   * 
   * @note In SBML Level&nbsp;2, model history annotations were only
   * permitted on the Model element.  In SBML Level&nbsp;3, they are
   * permitted on all SBML components derived from SBase.
   */
  int unsetModelHistory();


  /**
  * Unsets the created date of the ModelHistory object attached to this object.
  *
  * @copydetails doc_returns_success_code
  * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
  * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
  * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
  *
  * @note In SBML Level&nbsp;2, model history annotations were only
  * permitted on the Model element.  In SBML Level&nbsp;3, they are
  * permitted on all SBML components derived from SBase.
  */
  int unsetCreatedDate();


  /**
  * Unsets the modified dates of the ModelHistory object attached to this object.
  *
  * @copydetails doc_returns_success_code
  * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
  * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
  * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
  *
  * @note In SBML Level&nbsp;2, model history annotations were only
  * permitted on the Model element.  In SBML Level&nbsp;3, they are
  * permitted on all SBML components derived from SBase.
  */
  int unsetModifiedDates();


  /**
   * Returns the MIRIAM <em>biological qualifier</em> associated with the
   * given resource.
   *
   * In <a target="_blank" href="http://biomodels.net/miriam">MIRIAM</a>,
   * qualifiers are an optional means of indicating the relationship
   * between a model component and its annotations.  There are two broad
   * kinds of annotations: <em>model</em> and <em>biological</em>.  The
   * latter kind is used to qualify the relationship between a model
   * component and a biological entity which it represents.  Examples of
   * relationships include "is" and "has part", but many others are
   * possible.  MIRIAM defines <a target="_blank"
   * href="http://www.ebi.ac.uk/miriam/main/qualifiers/">numerous
   * relationship qualifiers</a> to enable different software tools to
   * qualify biological annotations in the same standardized way.  In
   * libSBML, the MIRIAM controlled-vocabulary annotations on an SBML model
   * element are represented using lists of CVTerm objects, and the
   * the MIRIAM biological qualifiers are represented using
   * values @if clike from the enumeration
   * type #BiolQualifierType_t.@endif@if python whose
   * names begin with <code>BQB_</code> in the interface class
   * @link libsbml libsbml@endlink.@endif@if java whose
   * names begin with <code>BQB_</code> in the interface class
   * {@link libsbmlConstants}.@endif@if csharp whose
   * names begin with <code>BQB_</code> in the interface class
   * @link libsbmlcs.libsbml libsbml@endlink.@endif@~
   *
   * This method searches the controlled-vocabulary annotations
   * (i.e., the list of CVTerm objects) on the present object, then out of
   * those that have biological qualifiers, looks for an annotation to the
   * given @p resource.  If such an annotation is found, it returns the
   * type of biological qualifier associated with that resource as a 
   * value @if clike from the enumeration type
   * #BiolQualifierType_t.@endif@if python whose name begins with
   * <code>BQB_</code> from the interface
   * class @link libsbml libsbml@endlink.@endif@if java whose name
   * begins with <code>BQB_</code> from the interface
   * class {@link libsbmlConstants}.@endif@if csharp whose
   * names begin with <code>BQB_</code> in the interface class
   * @link libsbmlcs.libsbml libsbml@endlink.@endif@~
   *
   * @param resource string representing the resource; e.g.,
   * <code>"http://www.geneontology.org/#GO:0005892"</code>.
   *
   * @return the qualifier associated with the resource,
   * or @sbmlconstant{BQB_UNKNOWN, BiolQualifierType_t} if the
   * resource does not exist.
   *
   * @if clike
   * @note The set of MIRIAM biological qualifiers grows over
   * time, although relatively slowly.  The values in the enumeration
   * #BiolQualifierType_t are up to date with MIRIAM at the time of a given
   * libSBML release.  The set of values may be expanded in later libSBML
   * releases, to match the values defined by MIRIAM at that later time.
   * @endif@if python
   * @note The set of MIRIAM biological qualifiers grows over
   * time, although relatively slowly.  The values are up to date with
   * MIRIAM at the time of a given libSBML release.  The set of values in
   * list of <code>BQB_</code> constants defined in @link libsbml
   * libsbml@endlink may be expanded in later libSBML releases, to match
   * the values defined by MIRIAM at that later time.
   * @endif@if java
   * @note The set of MIRIAM biological qualifiers grows over
   * time, although relatively slowly.  The values are up to date with
   * MIRIAM at the time of a given libSBML release.  The set of values in
   * list of <code>BQB_</code> constants defined in {@link libsbmlConstants}
   * may be expanded in later libSBML releases, to match
   * the values defined by MIRIAM at that later time.
   * @endif@if csharp
   * @note The set of MIRIAM biological qualifiers grows over
   * time, although relatively slowly.  The values are up to date with
   * MIRIAM at the time of a given libSBML release.  The set of values in
   * list of <code>BQB_</code> constants defined in @link libsbmlcs.libsbml libsbml@endlink
   * may be expanded in later libSBML releases, to match
   * the values defined by MIRIAM at that later time.
   * @endif@~
   */
  BiolQualifierType_t getResourceBiologicalQualifier(std::string resource) const;


  /**
   * Returns the MIRIAM <em>model qualifier</em> associated with the
   * given resource.
   *
   * In <a target="_blank" href="http://biomodels.net/miriam">MIRIAM</a>,
   * qualifiers are an optional means of indicating the relationship
   * between a model component and its annotations.  There are two broad
   * kinds of annotations: <em>model</em> and <em>biological</em>.  The
   * former kind is used to qualify the relationship between a model
   * component and another modeling object.  An example qualifier is
   * "isDerivedFrom", to indicate that a given component of the model is
   * derived from the modeling object represented by the referenced
   * resource.  MIRIAM defines <a target="_blank"
   * href="http://www.ebi.ac.uk/miriam/main/qualifiers/">numerous
   * relationship qualifiers</a> to enable different software tools to
   * qualify model annotations in the same standardized way.  In libSBML,
   * the MIRIAM controlled-vocabulary annotations on an SBML model element
   * are represented using lists of CVTerm objects, and the 
   * the MIRIAM model qualifiers are represented using
   * values @if clike from the enumeration
   * type #ModelQualifierType_t.@endif@if python whose
   * names begin with <code>BQM_</code> in the interface class
   * @link libsbml libsbml@endlink.@endif@if java whose
   * names begin with <code>BQM_</code> in the interface class
   * {@link libsbmlConstants}.@endif@if csharp whose
   * names begin with <code>BQB_</code> in the interface class
   * @link libsbmlcs.libsbml libsbml@endlink.@endif@~
   *
   * This method method searches the controlled-vocabulary annotations
   * (i.e., the list of CVTerm objects) on the present object, then out of
   * those that have model qualifiers, looks for an annotation to the given
   * @p resource.  If such an annotation is found, it returns the type of
   * type of model qualifier associated with that resource as a 
   * value @if clike from the enumeration type
   * #ModelQualifierType_t.@endif@if python whose name begins with
   * <code>BQM_</code> from the interface
   * class @link libsbml libsbml@endlink.@endif@if java whose name
   * begins with <code>BQM_</code> from the interface
   * class {@link libsbmlConstants}.@endif@if csharp whose
   * names begin with <code>BQB_</code> in the interface class
   * @link libsbmlcs.libsbml libsbml@endlink.@endif@~
   *
   * @param resource string representing the resource; e.g.,
   * <code>"http://www.geneontology.org/#GO:0005892"</code>.
   *
   * @return the @if clike #ModelQualifierType_t value@else model qualifier
   * type@endif@~ associated with the resource, or @sbmlconstant{BQM_UNKNOWN,
   * ModelQualifierType_t} if the resource does not exist.
   *
   * @if clike
   * @note The set of MIRIAM biological qualifiers grows over
   * time, although relatively slowly.  The values in the enumeration
   * #ModelQualifierType_t are up to date with MIRIAM at the time of a given
   * libSBML release.  The set of values may be expanded in later libSBML
   * releases, to match the values defined by MIRIAM at that later time.
   * @endif@if python
   * @note The set of MIRIAM model qualifiers grows over
   * time, although relatively slowly.  The values are up to date with
   * MIRIAM at the time of a given libSBML release.  The set of values in
   * list of <code>BQM_</code> constants defined in @link libsbml
   * libsbml@endlink may be expanded in later libSBML releases, to match
   * the values defined by MIRIAM at that later time.
   * @endif@if java
   * @note The set of MIRIAM model qualifiers grows over
   * time, although relatively slowly.  The values are up to date with
   * MIRIAM at the time of a given libSBML release.  The set of values in
   * list of <code>BQM_</code> constants defined in {@link libsbmlConstants}
   * may be expanded in later libSBML releases, to match
   * the values defined by MIRIAM at that later time.
   * @endif@if csharp
   * @note The set of MIRIAM model qualifiers grows over
   * time, although relatively slowly.  The values are up to date with
   * MIRIAM at the time of a given libSBML release.  The set of values in
   * list of <code>BQM_</code> constants defined in @link libsbmlcs.libsbml libsbml@endlink
   * may be expanded in later libSBML releases, to match
   * the values defined by MIRIAM at that later time.
   * @endif@~
   */
  ModelQualifierType_t getResourceModelQualifier(std::string resource) const;


  /**
   * Returns the Model object for the SBML Document in which the current object is located.
   * 
   * @return the Model object for the SBML Document of this SBML object.
   *
   * @see getParentSBMLObject()
   * @see getSBMLDocument()
   */
  const Model* getModel () const;


  /**
   * Returns the SBML Level of the SBMLDocument object containing @em this
   * object.
   * 
   * @copydetails doc_what_is_SBMLDocument
   * 
   * @return the SBML level of this SBML object.
   * 
   * @see getVersion()
   * @see getNamespaces()
   * @see getPackageVersion()
   */
  unsigned int getLevel () const;


  /**
   * Returns the Version within the SBML Level of the SBMLDocument object
   * containing @em this object.
   * 
   * @copydetails doc_what_is_SBMLDocument
   * 
   * @return the SBML version of this SBML object.
   *
   * @see getLevel()
   * @see getNamespaces()
   */
  unsigned int getVersion () const;


  /**
  * Returns the SBML Core Version within the SBML Level of the actual object.
  *
  * @copydetails doc_what_is_SBMLDocument
  *
  * @return the SBML core version of this SBML object.
  */
  unsigned int getPackageCoreVersion() const;


  /**
   * Returns the Version of the SBML Level&nbsp;3 package to which this
   * element belongs to.
   *
   * @return the version of the SBML Level&nbsp;3 package to which this
   * element belongs. The value @c 0 will be returned if this element
   * belongs to the SBML Level&nbsp;3 Core package.
   *
   * @see getLevel()
   * @see getVersion()
   */
  unsigned int getPackageVersion () const;


  /**
   * Returns the name of the SBML Level&nbsp;3 package in which this element
   * is defined.
   *
   * @return the name of the SBML package in which this element is defined.
   * The string <code>&quot;core&quot;</code> will be returned if this
   * element is defined in SBML Level&nbsp;3 Core. The string
   * <code>&quot;unknown&quot;</code> will be returned if this element is
   * not defined in any SBML package.
   */
  const std::string& getPackageName () const;


  /**
   * Returns the libSBML type code for this object.
   *
   * @copydetails doc_what_are_typecodes
   *
   * @copydetails doc_additional_typecode_details
   *
   * @return the @if clike #SBMLTypeCode_t value@else SBML object type
   * code@endif@~ of this SBML object, or @sbmlconstant{SBML_UNKNOWN,
   * SBMLTypeCode_t} (the default).  The latter is possible because
   * subclasses of SBase are not required to implement this method to return
   * a type code.
   *
   * @copydetails doc_warning_typecodes_not_unique
   *
   * @see getPackageName()
   * @see getElementName()
   */
  virtual int getTypeCode () const;


  /**
   * Predicate returning @c true if this object's level/version and namespace
   * values correspond to a valid SBML specification.
   *
   * The valid combinations of SBML Level, Version and Namespace as of this
   * release of libSBML are the following:
   * <ul>
   * <li> Level&nbsp;1 Version&nbsp;2: &quot;<code style='margin-right:0; padding-right:0'>http</code><code style='margin-left:0; padding-left:0'>://www.sbml.org/sbml/level1</code>&quot;
   * <li> Level&nbsp;2 Version&nbsp;1: &quot;<code style='margin-right:0; padding-right:0'>http</code><code style='margin-left:0; padding-left:0'>://www.sbml.org/sbml/level2</code>&quot;
   * <li> Level&nbsp;2 Version&nbsp;2: &quot;<code style='margin-right:0; padding-right:0'>http</code><code style='margin-left:0; padding-left:0'>://www.sbml.org/sbml/level2/version2</code>&quot;
   * <li> Level&nbsp;2 Version&nbsp;3: &quot;<code style='margin-right:0; padding-right:0'>http</code><code style='margin-left:0; padding-left:0'>://www.sbml.org/sbml/level2/version3</code>&quot;
   * <li> Level&nbsp;2 Version&nbsp;4: &quot;<code style='margin-right:0; padding-right:0'>http</code><code style='margin-left:0; padding-left:0'>://www.sbml.org/sbml/level2/version4</code>&quot;
   * <li> Level&nbsp;2 Version&nbsp;5: &quot;<code style='margin-right:0; padding-right:0'>http</code><code style='margin-left:0; padding-left:0'>://www.sbml.org/sbml/level2/version5</code>&quot;
   * <li> Level&nbsp;3 Version&nbsp;1 Core: &quot;<code style='margin-right:0; padding-right:0'>http</code><code style='margin-left:0; padding-left:0'>://www.sbml.org/sbml/level3/version1/core</code>&quot;
   * <li> Level&nbsp;3 Version&nbsp;2 Core: &quot;<code style='margin-right:0; padding-right:0'>http</code><code style='margin-left:0; padding-left:0'>://www.sbml.org/sbml/level3/version2/core</code>&quot;
   * </ul>
   *
   * @return @c true if the level, version and namespace values of this 
   * SBML object correspond to a valid set of values, @c false otherwise.
   */
  bool hasValidLevelVersionNamespaceCombination();

  
  /**
   * Returns the XML element name of this object.
   *
   * This is overridden by subclasses to return a string appropriate to the
   * SBML component.  For example, Model defines it as returning
   * @c "model", CompartmentType defines it as returning @c "compartmentType",
   * and so on.
   */
  virtual const std::string& getElementName () const;


  /**
   * Returns a string consisting of a partial SBML corresponding to just
   * this object.
   * 
   * @return the partial SBML that describes this SBML object.
   *
   * @warning <span class="warning">This is primarily provided for testing
   * and debugging purposes.  It may be removed in a future version of
   * libSBML.</span>
   */
  char* toSBML();


  /**
   * Returns this element as an XMLNode.
   *
   * @return this element as an XMLNode.
   *
   * @warning <span class="warning">This operation is computationally
   * expensive, because the element has to be fully serialized to a string
   * and then parsed into the XMLNode structure.  Attempting to convert a
   * large tree structure (e.g., a large Model) may consume significant
   * computer memory and time.</span>
   */
   XMLNode* toXMLNode();


  /**
   * Reads (initializes) this SBML object by reading from the given XMLNode.
   * 
   * @param node the XMLNode to read from.
   *
   * @param flag an optional flag that determines how how errors are logged
   * during the reading process.
   *
   * @warning <span class="warning">This method is computationally expensive,
   * because the given node has to be serialized to a string first.
   * Attempting to serialize a large tree structure (e.g., a large Model) may
   * consume significant computer memory and time.</span>
   */
   void read(const XMLNode& node, XMLErrorSeverityOverride_t flag = LIBSBML_OVERRIDE_DISABLED);


#ifndef SWIG
   /** @cond doxygenLibsbmlInternal */

  // ------------------------------------------------------------------
  //
  //  functions to faciliate matlab binding

   virtual int getAttribute(const std::string& attributeName, double& value) const;

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual int getAttribute(const std::string& attributeName, bool& value) const;

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual int getAttribute(const std::string& attributeName, int& value) const;

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual int getAttribute(const std::string& attributeName, unsigned int& value) const;

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual int getAttribute(const std::string& attributeName, std::string& value) const;

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual bool isSetAttribute(const std::string& attributeName) const;

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual int setAttribute(const std::string& attributeName, double value);

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual int setAttribute(const std::string& attributeName, bool value);

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual int setAttribute(const std::string& attributeName, int value);

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual int setAttribute(const std::string& attributeName, unsigned int value);

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual int setAttribute(const std::string& attributeName, const std::string& value);

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual int unsetAttribute(const std::string& attributeName);

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual SBase* createChildObject(const std::string& elementName);

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual int addChildObject(const std::string& elementName, const SBase* element);

   /** @endcond */

   /** @cond doxygenLibsbmlInternal */

   virtual SBase* removeChildObject(const std::string& elementName, const std::string& id);

   /** @endcond */

   /** @cond doxygenLibsbmlInternal */

   virtual unsigned int getNumObjects(const std::string& objectName);

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

   virtual SBase* getObject(const std::string& objectName, unsigned int index);

  /** @endcond */

     /** @cond doxygenLibsbmlInternal */

  virtual int setMessage (const std::string& message, bool addXHTMLMarkup = false);

  /** @endcond */

  /** @cond doxygenLibsbmlInternal */
  /**
   * Returns @c NULL.  SBase subclasses that define a child Math object
   * will override this function to return that child.
   * 
   * @return @c NULL.
   */
  virtual const ASTNode* getMath () const;
  /** @endcond */

  /** @cond doxygenLibsbmlInternal */
  /**
   * Returns @c false.  SBase subclasses that define a child Math object
   * will override this function and return whether or not that Math
   * object is set.
   *
   * @return @c false.
   */
  virtual bool isSetMath () const;
  /** @endcond */

  /** @cond doxygenLibsbmlInternal */
  /**
   * Does nothing and returns @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}.
   * SBase subclasses that define a child Math object
   * will override this function to set that Math child.
   *
   * @param math an ASTNode representing a formula tree.
   *
   * @copydetails doc_returns_one_success_code
   * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
   */
  virtual int setMath (const ASTNode* math);
  /** @endcond */

   /** @cond doxygenLibsbmlInternal */
   virtual std::string getMessageString () const;

   /** @endcond */

#endif

  /** @cond doxygenLibsbmlInternal */

#ifndef SWIG

  template<typename T> T getAttribute(const std::string& attributeName)
  {
    T result;
    getAttribute(attributeName, result);
    return result;
  }

#endif /* SWIG */

   /** @endcond */

  // ------------------------------------------------------------------
  //
  // public functions for EXTENSION
  //
  // ------------------------------------------------------------------

  /**
   * Returns a plug-in object (extension interface) for an SBML Level&nbsp;3
   * package extension with the given package name or URI.
   * The returned plug-in will be the appropriate type of plugin requested:
   * calling Model::getPlugin("fbc") will return an FbcModelPlugin; calling
   * Parameter::getPlugin("comp") will return CompSBasePlugin, etc.
   *
   * If no such plugin exists, NULL is returned.
   *
   * @copydetails doc_what_are_plugins
   *
   * @param package the name or URI of the package.
   *
   * @return the plug-in object (the libSBML extension interface) of
   * a package extension with the given package name or URI.
   *
   * @see getPlugin(unsigned int n)
   */
  SBasePlugin* getPlugin(const std::string& package);


  /**
   * Returns a plug-in object (extension interface) for an SBML Level&nbsp;3
   * package extension with the given package name or URI.
   * The returned plug-in will be the appropriate type of plugin requested:
   * calling Model::getPlugin("fbc") will return an FbcModelPlugin; calling
   * Parameter::getPlugin("comp") will return CompSBasePlugin, etc.
   *
   * If no such plugin exists, NULL is returned.
   *
   * @copydetails doc_what_are_plugins
   *
   * @param package the name or URI of the package.
   *
   * @return the plug-in object (the libSBML extension interface) of a
   * package extension with the given package name or URI.
   *
   * @see getPlugin(unsigned int n)
   */
  const SBasePlugin* getPlugin(const std::string& package) const;


  /**
   * Returns the nth plug-in object (extension interface) for an SBML Level&nbsp;3
   * package extension.
   * The returned plug-in will be the appropriate type of plugin requested:
   * calling Model::getPlugin("fbc") will return an FbcModelPlugin; calling
   * Parameter::getPlugin("comp") will return CompSBasePlugin, etc.
   *
   * If no such plugin exists, NULL is returned.
   *
   * @copydetails doc_what_are_plugins
   *
   * @param n the index of the plug-in to return.
   *
   * @return the nth plug-in object (the libSBML extension interface) of a
   * package extension.
   * If the index @p n is invalid, @c NULL is returned.
   *
   * @see getNumPlugins()
   * @see getPlugin(const std::string& package)
   */
  SBasePlugin* getPlugin(unsigned int n);


  /**
   * Returns the nth plug-in object (extension interface) for an SBML Level&nbsp;3
   * package extension.
   * The returned plug-in will be the appropriate type of plugin requested:
   * calling Model::getPlugin("fbc") will return an FbcModelPlugin; calling
   * Parameter::getPlugin("comp") will return CompSBasePlugin, etc.
   *
   * If no such plugin exists, NULL is returned.
   *
   * @copydetails doc_what_are_plugins
   *
   * @param n the index of the plug-in to return.
   *
   * @return the nth plug-in object (the libSBML extension interface) of a
   * package extension.
   * If the index @p n is invalid, @c NULL is returned.
   *
   * @see getNumPlugins()
   * @see getPlugin(const std::string& package)
   */
  const SBasePlugin* getPlugin(unsigned int n) const;


  /**
   * Returns the nth disabled plug-in object (extension interface) for an SBML Level&nbsp;3
   * package extension.  If no such plugin exists, NULL is returned.
   *
   * @copydetails doc_what_are_plugins
   *
   * @copydetails doc_what_are_disabled_plugins
   *
   * @param n the index of the disabled plug-in to return.
   *
   * @return the nth disabled plug-in object (the libSBML extension interface) of a
   * package extension.
   * If the index @p n is invalid, @c NULL is returned.
   *
   * @see getNumDisabledPlugins()
   * @see getPlugin(const std::string& package)
   */
  SBasePlugin* getDisabledPlugin(unsigned int n);


  /**
   * Returns the nth disabled plug-in object (extension interface) for an SBML Level&nbsp;3
   * package extension.  If no such plugin exists, NULL is returned.
   *
   * @copydetails doc_what_are_plugins
   *
   * @copydetails doc_what_are_disabled_plugins
   *
   * @param n the index of the disabled plug-in to return.
   *
   * @return the nth disabled plug-in object (the libSBML extension interface) of a
   * package extension.
   * If the index @p n is invalid, @c NULL is returned.
   *
   * @see getNumDisabledPlugins()
   * @see getPlugin(const std::string& package)
   */
  const SBasePlugin* getDisabledPlugin(unsigned int n) const;


  /**
   * Returns the number of plug-in objects (extenstion interfaces) for SBML
   * Level&nbsp;3 package extensions known.
   *
   * @copydetails doc_what_are_plugins
   *
   * @return the number of plug-in objects (extension interfaces) of
   * package extensions known by this instance of libSBML.
   *
   * @see getPlugin(unsigned int n)
   */
  unsigned int getNumPlugins() const;


  /**
   * Returns the number of disabled plug-in objects (extension interfaces) 
   * for SBML Level&nbsp;3 package extensions known.
   *
   * @copydetails doc_what_are_plugins
   *
   * @copydetails doc_what_are_disabled_plugins
   *
   * @return the number of disabled plug-in objects (extension interfaces) 
   * of package extensions known by this instance of libSBML.
   *
   */
  unsigned int getNumDisabledPlugins() const;


  /**
   * Deletes all information stored in disabled plugins.  If the plugin is 
   * re-enabled later, it will then not have any previously-stored information.
   *
   * @copydetails doc_what_are_plugins
   *
   * @copydetails doc_what_are_disabled_plugins
   *
   * @param recursive if @c true, the disabled information will be deleted
   * also from all child elements, otherwise only from this SBase element.
   *
   * @see getNumDisabledPlugins()
   */
  void deleteDisabledPlugins(bool recursive=true);


  /**
   * Enables or disables the given SBML Level&nbsp;3 package on this object.
   *
   * This method enables the specified package on this object and other
   * objects connected by child-parent links in the same SBMLDocument object.
   * This method is the converse of
   * SBase::disablePackage(const std::string& pkgURI, const std::string& pkgPrefix).
   *
   * @param pkgURI the URI of the package.
   * 
   * @param pkgPrefix the XML prefix of the package.
   * 
   * @param flag whether to enable (@c true) or disable (@c false) the package.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_PKG_UNKNOWN, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_PKG_VERSION_MISMATCH, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_PKG_CONFLICTED_VERSION, OperationReturnValues_t}
   *
   * @see disablePackage(const std::string& pkgURI, const std::string& pkgPrefix)
   */
  int enablePackage(const std::string& pkgURI, const std::string& pkgPrefix, bool flag);


  /**
   * Disables the given SBML Level&nbsp;3 package on this object.
   *
   * This method disables the specified package on this object
   * and other objects connected by child-parent links in the same
   * SBMLDocument object.
   * 
   * An example of when this may be useful is during construction of model
   * components when mixing existing and new models.  Suppose your
   * application read an SBML document containing a model that used the SBML
   * Hierarchical %Model Composition (&ldquo;comp&rdquo;) package, and
   * extracted parts of that model in order to construct a new model in
   * memory.  The new, in-memory model will not accept a component drawn from
   * an other SBMLDocument with different package namespace declarations.
   * You could reconstruct the same namespaces in the in-memory model first,
   * but as a shortcut, you could also disable the package namespace on the
   * object being added.  Here is a code example to help clarify this:
   * @if cpp
@code{.cpp}
// We read in an SBML L3V1 model that uses the 'comp'
// package namespace.
doc = readSBML("sbml-file-with-comp-elements.xml");

// We extract one of the species from the model.
Species* s1 = doc->getModel()->getSpecies(0);

// We construct a new model.  This model does not use the
// 'comp' package.
Model * newModel = new Model(3,1);

// The following will fail with an error, because addSpecies()
// will first check that the parent of the given object has
// namespaces declared, and will discover that s1 does but
// newModel does not.

// newModel->addSpecies(s1);

// However, if we disable the 'comp' package on s1, then
// the call to addSpecies will work.

s1->disablePackage("http://www.sbml.org/sbml/level3/version1/comp/version1",
                   "comp");
newModel->addSpecies(s1);
@endcode
@endif
@if python
@code{.py}
import sys
import os.path
from libsbml import *

# We read an SBML L3V1 model that uses the 'comp' package.

doc = readSBML("sbml-file-with-comp-elements.xml");
if doc.getNumErrors() > 0:
  print('readSBML encountered errors while reading the file.')
  doc.printErrors()
  sys.exit(1)

# We extract one of the species from the model.

model = doc.getModel()
if model == None:
  print('Unable to retrieve Model object')
  sys.exit(1)

s1 = model.getSpecies(0)
if s1 == None:
  print('Unable to retrieve Species object')
  sys.exit(1)

# We construct a new model.
# This model does not use the 'comp' package.

try:
  newDoc = SBMLDocument(3, 1)
except ValueError:
  print('Could not create SBMLDocument object')
  sys.exit(1)

newModel = newDoc.createModel()
if newModel == None:
  print('Unable to create new Model object')
  sys.exit(1)

# The following would normally fail with an error, because
# addSpecies() would first check that the parent of the given
# object has namespaces declared, and will discover that s1
# does but newModel does not.

#   newModel.addSpecies(s1)

# However, if we disable the 'comp' package on s1, then the
# call to addSpecies will work.

compNS = "http://www.sbml.org/sbml/level3/version1/comp/version1"
status = s1.disablePackage(compNS, "comp")
if status != LIBSBML_OPERATION_SUCCESS:
  print('Unable to disable package.')
  sys.exit(1)

newSpecies = newModel.addSpecies(s1)   # This will work now.
if newSpecies == None:
  print('Could not add Species')       # (This will not happen,
  sys.exit(1)                          # but always check errors.)
@endcode
@endif
@if java
@code{.java}
// We read in an SBML L3V1 model that uses the 'comp' package namespace
SBMLReader reader = new SBMLReader();
SBMLDocument doc = reader.readSBML("sbml-file-with-comp-elements.xml");

// We extract one of the species from the model we just read in.
Species s1 = doc.getModel().getSpecies(0);

// We construct a new model.  This model does not use the 'comp' package.
Model newModel = new Model(3,1);

// The following will fail with an error, because addSpecies() will
// first check that the parent of the given object has namespaces
// declared, and will discover that s1 does but newModel does not.

// newModel->addSpecies(s1);

// However, if we disable the 'comp' package on s1, then the call
// to addSpecies will work.

s1->disablePackage("http://www.sbml.org/sbml/level3/version1/comp/version1",
                   "comp");
newModel.addSpecies(s1);
@endcode
@endif
   *
   * @param pkgURI the URI of the package.
   * 
   * @param pkgPrefix the XML prefix of the package.
   * 
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_PKG_UNKNOWN, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_PKG_VERSION_MISMATCH, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_PKG_CONFLICTED_VERSION, OperationReturnValues_t}
   *
   * @see enablePackage(const std::string& pkgURI, const std::string& pkgPrefix, bool flag)
   */
  int disablePackage(const std::string& pkgURI, const std::string& pkgPrefix);
  

  /** @cond doxygenLibsbmlInternal */
  /**
   * Enables/Disables the given package with this element and child
   * elements (if any).
   * (This is an internal implementation for enablePackage function)
   *
   * @note Subclasses in which one or more child elements are defined 
   * must override this function.
   *
   * @if clike
   * @see setSBMLDocument()
   * @endif@~
   * @see connectToChild()
   */
  virtual void enablePackageInternal(const std::string& pkgURI, const std::string& pkgPrefix, bool flag);
  /** @endcond */


  /**
   * Predicate returning @c true if an SBML Level&nbsp;3 package with the
   * given URI is enabled with this object.
   *
   * @param pkgURI the URI of the package.
   *
   * @return @c true if the given package is enabled within this object, @c 
   * false otherwise.
   *
   * @see isPackageEnabled(@if java String@endif)
   */
  bool isPackageURIEnabled(const std::string& pkgURI) const;


  /**
   * Predicate returning @c true if the given SBML Level&nbsp;3 package is
   * enabled with this object.
   *
   * The search ignores the package version.
   *
   * @param pkgName the name of the package.
   *
   * @return @c true if the given package is enabled within this object,
   * @c false otherwise.
   *
   * @see isPackageURIEnabled(@if java String@endif)
   */
  bool isPackageEnabled(const std::string& pkgName) const;


  /**
   * Predicate returning @c true if an SBML Level&nbsp;3 package with the
   * given URI is enabled with this object.
   *
   * @param pkgURI the URI of the package.
   *
   * @return @c true if the given package is enabled within this object, @c 
   * false otherwise.
   *
   * @deprecated Replaced in libSBML 5.2.0 by
   * SBase::isPackageURIEnabled(@if java String@endif).
   *
   * @see isPkgEnabled(@if java String@endif)
   */
  bool isPkgURIEnabled(const std::string& pkgURI) const;


  /**
   * Predicate returning @c true if the given SBML Level&nbsp;3 package is
   * enabled with this object.
   *
   * The search ignores the package version.
   *
   * @param pkgName the name of the package.
   *
   * @return @c true if the given package is enabled within this object,
   * @c false otherwise.
   *
   * @deprecated Replaced in libSBML 5.2.0 by
   * SBase::isPackageEnabled(@if java String@endif).
   *
   * @see isPkgURIEnabled(@if java String@endif)
   */
  bool isPkgEnabled(const std::string& pkgName) const;


  /** @cond doxygenLibsbmlInternal */
  /**
   * Writes out contained SBML objects of package extensions (if any)
   * as XML elements.
   *
   */
  virtual void writeExtensionElements (XMLOutputStream& stream) const;
  /** @endcond */

  // ------------------------------------------------------------------


  /** @cond doxygenLibsbmlInternal */
  /**
   * Reads (initializes) this SBML object by reading from XMLInputStream.
   */
  void read (XMLInputStream& stream);
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /**
   * Writes (serializes) this SBML object by writing it to XMLOutputStream.
   */
  virtual void write (XMLOutputStream& stream) const;
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /**
   * Subclasses should override this method to write out their contained
   * SBML objects as XML elements.  Be sure to call your parent's
   * implementation of this method as well.  For example:@if clike
   * <pre>
   *   SBase::writeElements();
   *   mReactants.write(stream);
   *   mProducts.write(stream);
   *   ...
   * </pre>@endif@~
   */
  virtual void writeElements (XMLOutputStream& stream) const;
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /* function returns true if component has all the required
   * attributes
   * needs to be overloaded for each component
   */
  virtual bool hasRequiredAttributes() const ;
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /* function returns true if component has all the required
   * elements
   * needs to be overloaded for each component
   */
  virtual bool hasRequiredElements() const ;
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /* function returns value if the object matches level/version/namespace
   */
  int checkCompatibility(const SBase * object) const ;
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /* sets the SBMLnamespaces - internal use only*/
  int setSBMLNamespaces(const SBMLNamespaces * sbmlns);

  /* sets the SBMLNamaepaces and owns the given object - internal use only */
  void setSBMLNamespacesAndOwn(SBMLNamespaces * disownedNs);
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /* gets the SBMLnamespaces - internal use only*/
  virtual SBMLNamespaces * getSBMLNamespaces() const;
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /* removes duplicate top level annotations*/
  void removeDuplicateAnnotations();
  std::string checkMathMLNamespace(const XMLToken &elem);
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /* returns the derived units of the object
   * needs to be on SBase so that comp can use it for unit checking
   * but may also need to be implemented for other packages
   */
  virtual UnitDefinition* getDerivedUnitDefinition();
  /** @endcond */


  /** @cond doxygenLibsbmlInternal */
  /* returns boolean indicating object has undeclared units
   * needs to be on SBase so that comp can use it for unit checking
   * but may also need to be implemented for other packages
   */
  virtual bool containsUndeclaredUnits();
  /** @endcond */


  /**
   * Removes this object from its parent.
   *
   * If the parent was storing this object as a pointer, it is deleted.  If
   * not, it is simply cleared (as in ListOf objects).  This is a pure
   * virtual method, as every SBase element has different parents, and
   * therefore different methods of removing itself.  Will fail (and not
   * delete itself) if it has no parent object.  This function is designed to
   * be overridden, but for all objects whose parent is of the class ListOf,
   * the default implementation will work.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  virtual int removeFromParentAndDelete();


  /**
   * Returns @c true if this object's set of XML namespaces are the same
   * as the given object's XML namespaces.
   *
   * @copydetails doc_what_are_sbmlnamespaces
   *
   * @param sb an object to compare with respect to namespaces.
   *
   * @return boolean, @c true if this object's collection of namespaces is
   * the same as @p sb's, @c false otherwise.
   */
  bool matchesSBMLNamespaces(const SBase * sb);


  /**
   * Returns @c true if this object's set of XML namespaces are the same
   * as the given object's XML namespaces.
   *
   * @copydetails doc_what_are_sbmlnamespaces
   *
   * @param sb an object to compare with respect to namespaces.
   *
   * @return boolean, @c true if this object's collection of namespaces is
   * the same as @p sb's, @c false otherwise.
   */
  bool matchesSBMLNamespaces(const SBase * sb) const;


  /**
   * Returns @c true if this object's set of XML namespaces are a subset
   * of the given object's XML namespaces.
   *
   * @copydetails doc_what_are_sbmlnamespaces
   *
   * @param sb an object to compare with respect to namespaces.
   *
   * @return boolean, @c true if this object's collection of namespaces is
   * a subset of @p sb's, @c false otherwise.
   */
  bool matchesRequiredSBMLNamespacesForAddition(const SBase * sb);
  
  
  /**
   * Returns @c true if this object's set of XML namespaces are a subset
   * of the given object's XML namespaces.
   *
   * @copydetails doc_what_are_sbmlnamespaces
   *
   * @param sb an object to compare with respect to namespaces.
   *
   * @return boolean, @c true if this object's collection of namespaces is
   * a subset of @p sb's, @c false otherwise.
   */
  bool matchesRequiredSBMLNamespacesForAddition(const SBase * sb) const;


  /**
   * Sets the user data of this element.
   *
   * @copydetails doc_what_is_user_data
   *
   * @param userData specifies the new user data.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  int setUserData(void *userData);


  /**
   * Returns the user data that has been previously set via setUserData().
   *
   * @copydetails doc_what_is_user_data
   *
   * @return the user data of this node, or @c NULL if no user data has been set.
   *
   * @if clike
   * @see ASTNode::setUserData(void *userData)
   * @endif@~
   */
  void *getUserData() const;


  /**
   * Predicate returning true or false depending on whether
   * the user data of this element has been set.
   *
   * @copydetails doc_what_is_user_data
   *
   * @return boolean, @c true if this object's user data has been set,
   * @c false otherwise.
   */
  bool isSetUserData() const;


  /**
   * Unsets the user data of this element.
   *
   * @copydetails doc_what_is_user_data
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  int unsetUserData();


  /**
   * Returns the namespace URI to which this element belongs to.
   *
   * For example, all elements that belong to SBML Level&nbsp;3 Version&nbsp;1 Core
   * must would have the URI <code>"http://www.sbml.org/sbml/level3/version1/core"</code>;
   * all elements that belong to Layout Extension Version 1 for SBML Level&nbsp;3
   * Version&nbsp;1 Core must would have the URI
   * <code>"http://www.sbml.org/sbml/level3/version1/layout/version1"</code>.
   *
   * This function first returns the URI for this element by looking into the
   * SBMLNamespaces object of the document with the its package name.  If not
   * found, it will then look for the namespace associated with the element
   * itself.
   *
   * @return the URI of this element, as a text string.
   *
   * @see getSBMLDocument()
   * @see getPackageName()
   */
  std::string getURI() const;


  /**
   * Returns the XML namespace prefix of this element.
   *
   * This reports the XML namespace prefix chosen for this class of object in
   * the current SBML document.  This may be an empty string if the component
   * has no explicit prefix (for instance, if it is a core SBML object placed
   * in the default SBML namespace of the document).  If it is not empty, then
   * it corresponds to the XML namespace prefix used set the object, whatever
   * that may be in a given SBML document.
   *
   * @return a text string representing the XML namespace prefix.
   */
  std::string getPrefix() const;

  /** @cond doxygenLibsbmlInternal */


  virtual bool hasOptionalAttributes() const;


  /** @endcond */

  
  /** @cond doxygenLibsbmlInternal */


  virtual bool hasOptionalElements() const;


  /** @endcond */

  /** @cond doxygenLibsbmlInternal */

  virtual void updateSBMLNamespace(const std::string& package, unsigned int level,
    unsigned int version);
  /** @endcond */




protected:

  /** 
   * When overridden allows SBase elements to use the text included in between
   * the elements tags. The default implementation does nothing.
   * 
   * @param text the text string found between the element tags.
   */
  virtual void setElementText(const std::string &text);


  /** @cond doxygenLibsbmlInternal */
  bool matchesCoreSBMLNamespace(const SBase * sb);

  bool matchesCoreSBMLNamespace(const SBase * sb) const;
  
  /**
   * Creates a new SBase object with the given SBML level, version.
   */
  SBase (unsigned int level, unsigned int version);


  /**
   * Creates a new SBase object with the given SBMLNamespaces.
   * Only subclasses may create SBase objects.
   */
  SBase (const SBMLNamespaces* sbmlns);


  /**
  * Copy constructor. Creates a copy of this SBase object.
   *
   * @param orig the object to copy.
  */
  SBase(const SBase& orig);


  /**
   * Subclasses should override this method to create, store, and then
   * return an SBML object corresponding to the next XMLToken in the
   * XMLInputStream.
   *
   * @return the SBML object corresponding to next XMLToken in the
   * XMLInputStream or @c NULL if the token was not recognized.
   */
  virtual SBase* createObject (XMLInputStream& stream);


  /**
   * Predicate returning @c true if this
   * object's level/version and namespace values correspond to a valid
   * SBML specification.
   *
   * The valid combinations of SBML Level, Version and Namespace as of this
   * release of libSBML are the following:
   * <ul>
   * <li> Level&nbsp;1 Version&nbsp;2: <code>"http://www.sbml.org/sbml/level1"</code>
   * <li> Level&nbsp;2 Version&nbsp;1: <code>"http://www.sbml.org/sbml/level2"</code>
   * <li> Level&nbsp;2 Version&nbsp;2: <code>"http://www.sbml.org/sbml/level2/version2"</code>
   * <li> Level&nbsp;2 Version&nbsp;3: <code>"http://www.sbml.org/sbml/level2/version3"</code>
   * <li> Level&nbsp;2 Version&nbsp;4: <code>"http://www.sbml.org/sbml/level2/version4"</code>
   * <li> Level&nbsp;2 Version&nbsp;5: <code>"http://www.sbml.org/sbml/level2/version5"</code>
   * <li> Level&nbsp;3 Version&nbsp;1 Core: <code>"http://www.sbml.org/sbml/level3/version1/core"</code>
   * <li> Level&nbsp;3 Version&nbsp;2 Core: <code>"http://www.sbml.org/sbml/level3/version2/core"</code>
   * </ul>
   *
   * @param typecode the typecode for this element.
   * @param xmlns the namespaces used by this element.
   *
   * @return @c true if the level, version and namespace values of this 
   * SBML object correspond to a valid set of values, @c false otherwise.
   *
   * @note This function is provided as convenience method to be called from
   * constructors. This allows to use it in scenarios where the namespaces or
   * typecode have not yet been initialized.
   */
  bool hasValidLevelVersionNamespaceCombination(int typecode, const XMLNamespaces *xmlns);


  /**
   * Subclasses should override this method to read (and store) XHTML,
   * MathML, etc. directly from the XMLInputStream.
   *
   * @return @c true if the subclass read from the stream, @c false otherwise.
   */
  virtual bool readOtherXML (XMLInputStream& stream);


  /**
   * The SBML XML Schema is written such that the order of child elements
   * is significant.  LibSBML can read elements out of order.  If you
   * override this method to indicate the ordinal position of element with
   * respect to its siblings, libSBML will log an error if the element is
   * read out of order.
   *
   * @return the ordinal position of the element with respect to its
   * siblings or @c -1 (the default) to indicate the position is not
   * significant.
   */
  virtual int getElementPosition () const;


  /**
   * Returns the SBMLErrorLog used to log errors while reading and
   * validating SBML.
   *
   * @return the SBMLErrorLog used to log errors while reading and
   * validating SBML.
   */
  SBMLErrorLog* getErrorLog ();


  /**
   * Convenience method for easily logging problems from within method
   * implementations.
   *
   * This is essentially a short form of getErrorLog()->logError(...)
   *
   * @ifnot hasDefaultArgs @htmlinclude warn-default-args-in-docs.html @endif@~
   */
  void logError (  unsigned int       id
                 , const unsigned int level   = 2
                 , const unsigned int version = 3
                 , const std::string details = "" );


  /**
   * Helper to log a common type of error.
   */
  void logUnknownAttribute( const std::string& attribute,
          const unsigned int level,
          const unsigned int version,
          const std::string& element,
          const std::string prefix="");


  /**
   * Helper to log a common type of error.
   */
  void logUnknownElement( const std::string& element,
        const unsigned int level,
        const unsigned int version );

 
  /**
   * Helper to log a common type of error.
   */
  void logEmptyString( const std::string& attribute,
                       const unsigned int level,
                       const unsigned int version,
                       const std::string& element);


  /**
   * Subclasses should override this method to add the list of
   * expected attributes. Be sure to call your parent's implementation 
   * of this method as well.
   */
  virtual void addExpectedAttributes(ExpectedAttributes& attributes);

  /**
   * Subclasses should override this method to read values from the given
   * XMLAttributes set into their specific fields.  Be sure to call your
   * parent's implementation of this method as well.
   */
  virtual void readAttributes (const XMLAttributes& attributes, 
                               const ExpectedAttributes& expectedAttributes);


  /**
   * Subclasses should override this method to write their XML attributes
   * to the XMLOutputStream.  Be sure to call your parent's implementation
   * of this method as well.  For example:
   *
   *   SBase::writeAttributes(stream);
   *   stream.writeAttribute( "id"  , mId   );
   *   stream.writeAttribute( "name", mName );
   *   ...
   *
   * (NOTICE) this function doesn't write xmlns attributes.
   * Be sure to implement wirteXMLNS() function to write xmlns attributes.
   *
   */
  virtual void writeAttributes (XMLOutputStream& stream) const;


  /**
   *
   * Subclasses should override this method to write their xmlns attriubutes
   * (if any) to the XMLOutputStream. 
   *
   */
  virtual void writeXMLNS (XMLOutputStream& stream) const;


  /**
   * Synchronizes the annotation of this SBML object.
   *
   * Annotation element (XMLNode* mAnnotation) is synchronized with the 
   * current CVTerm objects (List* mCVTerm).
   * Currently, this method is called in getAnnotation, isSetAnnotation,
   * and writeElements methods.
   */
  virtual void syncAnnotation();

  void reconstructRDFAnnotation();


  /**
   * Checks that the SBML element appears in the expected order.
   *
   * If @p object is not in the expected position, an error is logged.
   */
  void checkOrderAndLogError (SBase* object, int expected);


  /**
   * Checks that an SBML ListOf element is populated.  
   * If a listOf element has been declared with no elements, 
   * an error is logged.
   */
  void checkListOfPopulated(SBase* object);

#if 0
  /**
   * Checks the syntax of the unit attribute.
   * The syntax of an unit is of type UnitSId which is defined as:
   *
   *  - letter ::= 'a'..'z','A'..'Z'
   *  - digit  ::= '0'..'9'
   *  - idChar ::= letter | digit | '_'
   *  - UnitSId    ::= ( letter | '_' ) idChar*
   *
   * If the syntax of the unit attribute of this object is incorrect, 
   * an error is logged
   *
   * @ifnot hasDefaultArgs @htmlinclude warn-default-args-in-docs.html @endif@~
   */
  void checkUnitSyntax(unsigned int flag = 0);
#endif

  /**
   * Checks that the given default namespace in the given element is valid.
   * If the given default namespace is not valid, an error is logged.
   */
  void checkDefaultNamespace(const XMLNamespaces* xmlns, 
    const std::string& elementName, const std::string prefix = "");

  /**
   * Checks the annotation does not declare an sbml namespace.
   * If the annotation declares an sbml namespace an error is logged.
   */
  void checkAnnotation();


  /**
   * Checks that the XHTML is valid.
   * If the xhtml does not conform to the specification of valid xhtml within
   * an sbml document, an error is logged.
   */
  void checkXHTML(const XMLNode *);

  
  // ------------------------------------------------------------------
  //
  // protected functions for EXTENSION
  //
  // ------------------------------------------------------------------

  /*
   * Checks if one or more package extensions (defined in the given 
   * SBMLNamespaces) are bound with this SBase derived object, and
   * loads the corresponding SBasePlugin derived objects (if any).
   *
   * (NOTE) 
   *
   *  Each constructor of SBase derived class (except for an abstract class)
   *  which accepts an SBMLNamespaces must invoke this function for 
   *  supporting package extensions.
   *
   */
  void loadPlugins(SBMLNamespaces *sbmlns);


  /**
   * Create, store, and then return an SBML object of package extensions
   * corresponding to the next XMLToken in the XMLInputStream.
   *
   * @return the SBML object of package extensions corresponding to next 
   * XMLToken in the XMLInputStream or @c NULL if the token was not recognized.
   */
  virtual SBase* createExtensionObject (XMLInputStream& stream);


  /**
   * Sets the XML namespace to which this element belongs to.
   * For example, all elements that belong to SBML Level&nbsp;3 Version&nbsp;1 Core
   * must set the namespace to <code>"http://www.sbml.org/sbml/level3/version1/core"</code>; 
   * all elements that belong to Layout Extension Version 1 for SBML Level&nbsp;3
   * Version&nbsp;1 Core must set the namespace to 
   * <code>"http://www.sbml.org/sbml/level3/version1/layout/version1"</code>.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_INVALID_ATTRIBUTE_VALUE, OperationReturnValues_t}
   */
  int setElementNamespace(const std::string& uri);


  /**
   * Returns the XML namespace (URI) to which this element belongs to.
   */
  const std::string& getElementNamespace() const;


  /**
   * Read attributes of package extensions from the given XMLAttributes 
   * set into their specific fields. 
   * 
   * Be sure to call your parent's implementation of this function as well.  
   * For example:
   * @if clike
@verbatim
SBase::readExtensionAttributes(attributes, expectedAttributes);
@endverbatim
   * @endif@if java
@verbatim
SBase.readExtensionAttributes(attributes, expectedAttributes);
@endverbatim
   * @endif@if java
@verbatim
SBase.readExtensionAttributes(attributes, expectedAttributes);
@endverbatim
   * @endif@if python
@verbatim
SBase.readExtensionAttributes(attributes, expectedAttributes);
@endverbatim
   * @endif@~
   */
  virtual void readExtensionAttributes (const XMLAttributes& attributes, 
    const ExpectedAttributes* expectedAttributes = NULL);


  /**
   * Write attributes of package extensions to the XMLOutputStream.  
   *
   * Be sure to call your parent's implementation of this function as well.  
   * For example:
   *
   *   SBase::writeExtensionAttributes(stream);
   *
   */
  virtual void writeExtensionAttributes (XMLOutputStream& stream) const;


  /**
   * Stores the given attribute to the list of ignored attributes if
   * the given attribute belongs to some unknown package extension.
   * Unknown attribute error will be logged if the "required" attribute
   * of the package is "true" in SBMLDocument element.
   *
   * The stored attributes will be written out as-is when writing the 
   * SBMLDocument to a string or a file (i.e. Attributes and elements of 
   * unknown package extensions will not be lost when reading/writing 
   * a file/sting containing them.)
   *
   * @param element the string of element which contains the given attribute.
   * @param xattr the XMLAttributes object which is contained in the given 
   * element.
   * @param index the index of the target attribute in the given XMLAttributes
   * object.
   *
   * @return @c true will be returned if the given attribute belongs
   * to some unknown package extension, otherwise @c false will be returned.
   */
  void storeUnknownExtAttribute(const std::string& element, 
                                const XMLAttributes& xattr, 
                                unsigned int index);


  /**
   * Stores the element of next token if the element belongs to some 
   * unknown package extension. Unknown element error will be logged if
   * the "required" attribute of the package is "true" in SBMLDocument 
   * element.
   *
   * The stored elements will be written out as-is when writing the 
   * SBMLDocument to a string or a file (i.e. Attributes and elements of 
   * unknown package extensions will not be lost when reading/writing 
   * a file/sting containing them.)
   *
   * @return @c true will be returned if the element of next token belongs
   * to some unknown package extension, otherwise @c false will be returned.
   */
  bool storeUnknownExtElement(XMLInputStream &stream);


  /**
   * Return the SBML XML namespace prefix of this element.
   *
   * This will be the same as getPrefix() unless the element in question is
   * an element of an SBML extension class.
   *
   * @return the XML namespace prefix.
   */
  std::string getSBMLPrefix() const;


  /**
   * Returns the root element of the node tree to which this element is connected.
   *
   * @note The root element may not be an SBMLDocument element. For example,
   * this element is the root element if this element doesn't have a parent
   * SBML object (i.e. mParentSBMLObject is @c NULL)
   *
   * @see enablePackageInternal
   */
  SBase* getRootElement();


  // ------------------------------------------------------------------


  std::string     mId;
  std::string     mName;
  std::string     mMetaId;
  XMLNode*        mNotes;
  XMLNode*        mAnnotation;
  SBMLDocument*   mSBML;
  SBMLNamespaces* mSBMLNamespaces;
  void*           mUserData;

  int mSBOTerm;

  unsigned int mLine;
  unsigned int mColumn;

  /* store the parent SBML object */
  SBase* mParentSBMLObject;

  /* storing annotations */
  List * mCVTerms;
  ModelHistory*   mHistory;

  /* flag that allows object to know its been deleted
   * for OS where the memory is still readable after a delete
   */
  bool mHasBeenDeleted;

  std::string mEmptyString;

  //----------------------------------------------------------------------
  //
  // Additional data members for Extension
  //
  //----------------------------------------------------------------------

  //
  // SBasePlugin derived classes will be stored in mPlugins.
  //
  // An object of corresponding SBasePlugin derived class will be added 
  // to this variable if the corresponding XMLNamespace is given when creating 
  // an SBase derived object.
  //
  std::vector<SBasePlugin*> mPlugins;

  //
  // In case an SBasePlugin is disabled, we still store it here in case it 
  // will be re-enabled later on. 
  //
  std::vector<SBasePlugin*> mDisabledPlugins;


  //
  // namespace to which this SBase object belongs.
  // This variable can be publicly accessible by getElementNamespace function.
  //
  // For example, mURI of elements defined in L3 Core (or defined in Level 2 
  // or before) will be the URI defined in the corresponding SBML specification
  // (e.g. "http://www.sbml.org/sbml/level3/version1" for L3V1 Core); and mURI
  // will be "http://www.sbml.org/sbml/level3/version1/layout/version1" for 
  // elements defined in layout extension L3V1-V1.
  // The purpuse of this data member is to explicitly distinguish elements in core 
  // package and extension packages.
  // 
  // From the implementation point of view, this variable is needed to identify
  // if the prefix needs to be added when printing elements in some package extension.
  // (i.e. used in getPrefix function)
  //
  std::string mURI;

  bool            mHistoryChanged;
  bool            mCVTermsChanged;

  //
  // XMLAttributes object containing attributes of unknown packages
  //
  XMLAttributes mAttributesOfUnknownPkg;
  XMLAttributes mAttributesOfUnknownDisabledPkg;

  //
  // XMLNode object containing elements of unknown packages
  //
  XMLNode       mElementsOfUnknownPkg;
  XMLNode       mElementsOfUnknownDisabledPkg;

  //-----------------------------------------------------------------------------

  
  bool getHasBeenDeleted() const;
  
  /** @endcond */

private:
  /** @cond doxygenLibsbmlInternal */
  /**
   * Stores the location (line and column) and any XML namespaces (for
   * roundtripping) declared on this SBML (XML) element.
   */
  void setSBaseFields (const XMLToken& element);


  /**
   * Reads an annotation from the stream and returns true if successful.
   *
   * @return @c true if read an <annotation> element from the stream.
   */
  bool readAnnotation (XMLInputStream& stream);


  /**
   * removes resources from the term object that alread exist on this object 
   */
  void removeDuplicatedResources(CVTerm *term, QualifierType_t type);
  
 /**
  * adds the given term to an existing bag. Returns 1 if added, 0 otherwise. 
  */
  int addTermToExistingBag(CVTerm *term, QualifierType_t type) const;

  /**
   * Reads the notes from the stream and returns true if successful.
   *
   * @return @c true if read a &lt;notes&gt; element from the stream.
   */
  bool readNotes (XMLInputStream& stream);


  /** @endcond */
};

LIBSBML_CPP_NAMESPACE_END

#endif  /* __cplusplus */



#ifndef SWIG

LIBSBML_CPP_NAMESPACE_BEGIN
BEGIN_C_DECLS

/**
 * Returns the value of the "metaid" attribute of the given SBase_t
 * structure.
 *
 * @param sb the SBase_t structure.
 *
 * @return the value of the "metaid" attribute of @p sb
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
const char *
SBase_getMetaId (SBase_t *sb);


/**
 * Returns the value of the "id" attribute of the given SBase_t
 * structure.
 *
 * @param sb the SBase_t structure
 *
 * @return the value of the "id" attribute of @p sb
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
const char * 
SBase_getIdAttribute(const SBase_t * sb);


/**
 * Returns the value of the "name" attribute of the given SBase_t
 * structure.
 *
 * @param sb the SBase_t structure
 *
 * @return the value of the "name" attribute of @p sb
 *
 * @memberof SBase_t
  */
LIBSBML_EXTERN
const char * 
SBase_getName(const SBase_t * sb);


/**
 * Returns the parent SBMLDocument_t structure of the given SBase_t
 * structure.
 *
 * @param sb the SBase_t structure.
 *
 * @return the parent SBMLDocument of this SBML structure.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
const SBMLDocument_t *
SBase_getSBMLDocument (SBase_t *sb);


/**
 * Returns the parent SBase_t structure of the given SBase_t
 * structure.
 *
 * @param sb the SBase_t structure.
 *
 * @return the parent SBase  of this SBML structure.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
const SBase_t *
SBase_getParentSBMLObject (SBase_t *sb);


/**
 * Returns the ancestor SBase_t structure of the given SBase_t
 * structure that corresponds to the given type.
 *
 * This function allows any structure to determine its exact
 * location/function within a model. For example a
 * StoichiometryMath_t structure has ancestors of type SpeciesReference_t,
 * ListOf_t(Products/Reactants), Reaction_t, ListOfReactions_t and Model_t;
 * any of which can be accessed via this function.
 *
 * @param sb the SBase_t structure.
 * @param type the typecode (int) of the structure to be returned.
 * @param pkgName the name of the package that defines the @p type .
 *
 * @return the ancestor SBase_t structure of this SBML structure with
 * the corresponding typecode (int), NULL if there is no ancestor of
 * this type.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
const SBase_t *
SBase_getAncestorOfType (SBase_t *sb, int type, const char* pkgName);

/**
 * Returns the integer portion of the value of the "sboTerm" attribute of
 * the given SBase_t structure.
 *
 * @copydetails doc_sbo_terms
 * @copydetails doc_sbo_terms_addendum
 *
 * @param sb the SBase_t structure.
 *
 * @return the value of the "sboTerm" attribute as an integer, or @c -1
 * if the value is not set.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_getSBOTerm (const SBase_t *sb);


/**
 * Returns the string representation of the "sboTerm" attribute of
 * this structure.
 *
 * @copydetails doc_sbo_terms
 * @copydetails doc_sbo_terms_addendum
 *
 * @return the value of the "sboTerm" attribute as a string of the form
 * SBO:NNNNNNN, or @c NULL if the value is not set.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
char*
SBase_getSBOTermID (const SBase_t *sb);


/**
 * Returns the identifiers.org URL  representation of the "sboTerm" attribute of
 * this structure.
 *
 * @return the value of the "sboTerm" attribute as a string of the form
 * <code>http://identifiers.org/biomodels.sbo/SBO:NNNNNNN</code>, or @c NULL if the value is not set.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
char*
SBase_getSBOTermAsURL (const SBase_t *sb);




/**
 * Returns the line number on which the given structure first appears in the
 * XML representation of the SBML document, or <code>0</code> if the object was created,
 * not read from a file.
 *
 * @param sb the SBase_t structure.
 *
 * @return the line number of the given structure, or <code>0</code> if no such value.
 *
 * @see SBase_getColumn().
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
unsigned int
SBase_getLine (const SBase_t *sb);


/**
 * Returns the column number on which the given structure first appears in the
 * XML representation of the SBML document, or <code>0</code> if the object was created,
 * not read from a file.
 *
 * @param sb the SBase_t structure.
 *
 * @return the column number of this SBML structure, or <code>0</code> if no such value.
 *
 * @see SBase_getLine().
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
unsigned int
SBase_getColumn (const SBase_t *sb);


/**
 * Returns the notes from given SBML structure.
 *
 * @param sb the given SBML structure.
 *
 * @return the XMLNode_t structure representing the notes from this structure.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
XMLNode_t *
SBase_getNotes (SBase_t *sb);


/**
 * Returns the notes string from given SBML structure.
 * The string is owned by the caller and should be freed
 * (with free()) when no longer needed.
 *
 * @param sb the given SBML structure.
 *
 * @return the string (char*) representing the notes from this structure.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
char*
SBase_getNotesString (SBase_t *sb);


/**
 * Returns the markdown version of the notes string from given SBML structure.
 * The string is owned by the caller and should be freed
 * (with free()) when no longer needed.  The HTML is translated
 * by 'html2md', https://github.com/tim-gromeyer/html2md/
 *
 * @param sb the given SBML structure.
 *
 * @return the string (char*) representing the markdown version of the notes from this structure.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
char*
SBase_getNotesMarkdown(SBase_t* sb);


/**
 * Returns the annotation from given SBML structure.
 *
 * @param sb the given SBML structure.
 *
 * @return the XMLNode_t structure representing the annotation from this structure.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
XMLNode_t *
SBase_getAnnotation (SBase_t *sb);


/**
 * Returns the annotation string from given SBML structure.
 * The string is owned by the caller and should be freed
 * (with free()) when no longer needed.
 *
 * @param sb the given SBML structure.
 *
 * @return the string (char*) representing the annotation from this structure.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
char*
SBase_getAnnotationString (SBase_t *sb);


/**
 * Predicate returning @c 1 (true) or @c 0 (false) depending on whether the given
 * structure's "metaid" attribute is set.
 *
 * @param sb the SBase_t structure to query.
 *
 * @return @c 1 (true) if the "metaid" attribute of this SBML structure
 * is set, @c 0 (false) otherwise.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_isSetMetaId (const SBase_t *sb);


/**
 * Predicate returning @c 1 (true) or @c 0 (false) depending on whether the given
 * structure's "id" attribute is set.
 *
 * @param sb the SBase_t structure to query
 *
 * @return @c 1 (true) if the "id" attribute of this SBML structure
 * is set, @c 0 (false) otherwise.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_isSetIdAttribute (const SBase_t *sb);


/**
 * Predicate returning @c 1 (true) or @c 0 (false) depending on whether the given
 * structure's "name" attribute is set.
 *
 * @param sb the SBase_t structure to query
 *
 * @return @c 1 (true) if the "name" attribute of this SBML structure
 * is set, @c 0 (false) otherwise.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_isSetName (const SBase_t *sb);


/**
 * Predicate returning @c 1 (true) or @c 0 (false) depending on whether the given
 * structure's "notes" subelement is set.
 *
 * @param sb the SBase_t structure to query.
 *
 * @return @c 1 (true) if the "notes" subelement of this SBML structure
 * is set, @c 0 (false) otherwise.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_isSetNotes (const SBase_t *sb);


/**
 * Predicate returning @c 1 (true) or @c 0 (false) depending on whether the given
 * structure's "annotation" subelement is set.
 *
 * @param sb the SBase_t structure to query.
 *
 * @return @c 1 (true) if the "annotation" subelement of this SBML structure
 * is set, @c 0 (false) otherwise.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_isSetAnnotation (const SBase_t *sb);


/**
 * Predicate returning @c 1 (true) or @c 0 (false) depending on whether the given
 * structure's "sboTerm" attribute is set.
 *
 * @param sb the SBase_t structure to query.
 *
 * @return @c 1 (true) if the "sboTerm" attribute of this SBML structure
 * is set, @c 0 (false) otherwise.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_isSetSBOTerm(const SBase_t *sb);


/**
 * Sets the value of the "metaid" attribute of the given structure.
 *
 * The string @p metaid is copied.  The value of @p metaid must be an
 * identifier conforming to the syntax defined by the XML 1.0 data type
 * ID.  Among other things, this type requires that a value is unique
 * among all the values of type XML ID in an SBMLDocument_t.  Although SBML
 * only uses XML ID for the "metaid" attribute, callers should be careful
 * if they use XML ID's in XML portions of a model that are not defined
 * by SBML, such as in the application-specific content of the
 * "annotation" subelement.
 *
 * @param sb the SBase_t structure.
 *
 * @param metaid the identifier string to use as the value of the
 * "metaid" attribute.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_ATTRIBUTE_VALUE, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
 *
 * @note Using this function with the metaid set to NULL is equivalent to
 * unsetting the "metaid" attribute.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_setMetaId (SBase_t *sb, const char *metaid);


/**
 * Sets the value of the "id" attribute of the given structure.
 *
 * The string @p id is copied.  The value of @p metaid must be an
 * identifier conforming to the syntax defined by SBML.
 *
 * @param sb the SBase_t structure
 *
 * @param id the identifier string to use as the value of the
 * "metaid" attribute
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_ATTRIBUTE_VALUE, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
 *
 * @note Using this function with the id set to NULL is equivalent to
 * unsetting the "id" attribute.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_setIdAttribute (SBase_t *sb, const char *id);


/**
 * Sets the value of the "name" attribute of the given structure.
 *
 * The string @p name is copied.  
 *
 * @param sb the SBase_t structure
 *
 * @param name the string to use as the value of the
 * "name" attribute
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_ATTRIBUTE_VALUE, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
 *
 * @note Using this function with the name set to NULL is equivalent to
 * unsetting the "name" attribute.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_setName (SBase_t *sb, const char *name);


/**
 * Sets the value of the "sboTerm" attribute.
 *
 * @copydetails doc_sbo_terms
 * @copydetails doc_sbo_terms_addendum
 *
 * @param sb the SBase_t structure.
 * @param value the NNNNNNN integer portion of the SBO identifier.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_ATTRIBUTE_VALUE, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_setSBOTerm (SBase_t *sb, int value);


/**
 * Sets the value of the "sboTerm" attribute by string.
 *
 * @copydetails doc_sbo_terms
 * @copydetails doc_sbo_terms_addendum
 *
 * @param sb the SBase_t structure.
 *
 * @param sboid the SBO identifier string of the form SBO:NNNNNNN.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_ATTRIBUTE_VALUE, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_setSBOTermID (SBase_t *sb, const char* sboid);


/**
 * Sets the namespaces relevant of this SBML structure.
 *
 * @param sb the SBase_t structure.
 *
 * @param xmlns the namespaces to set.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_setNamespaces (SBase_t *sb, XMLNamespaces_t *xmlns);


/**
 * Sets the notes for the given SBML structure.
 *
 * @param sb the given SBML structure.
 * @param notes the XMLNode_t structure representing the notes.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_setNotes (SBase_t *sb, const XMLNode_t *notes);

/**
 * Sets the notes for the given SBML structure from markdown input.
 *
 * Markdown parser is 'maddy' (https://github.com/progsource/maddy).
 * 
 * @param sb the given SBML structure.
 * @param markdown the markdown version of the notes.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int 
SBase_setNotesFromMarkdown(SBase_t* sb, const char* markdown);


/**
 * Sets the notes for the given SBML structure.
 *
 * @param sb the given SBML structure.
 * @param notes the string representing the notes.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_setNotesString (SBase_t *sb, const char *notes);


/**
 * Sets the notes for the given SBML structure.
 *
 * @param sb the given SBML structure.
 * @param notes the string representing the notes.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_setNotesStringAddMarkup (SBase_t *sb, const char *notes);


/**
 * Appends the notes for the given SBML structure.
 *
 * @param sb the given SBML structure.
 * @param notes the XMLNode_t structure representing the notes.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_appendNotes (SBase_t *sb, const XMLNode_t *notes);


/**
 * Appends the notes for the given SBML structure.
 *
 * @param sb the given SBML structure.
 * @param notes the string representing the notes.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_appendNotesString (SBase_t *sb, const char *notes);


/**
 * Sets the annotation for the given SBML structure.
 *
 * @param sb the given SBML structure.
 * @param annotation the XMLNode_t structure representing the annotation.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_setAnnotation (SBase_t *sb, const XMLNode_t *annotation);


/**
 * Sets the annotation for the given SBML structure.
 *
 * @param sb the given SBML structure.
 * @param annotation the string representing the annotation.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_setAnnotationString (SBase_t *sb, const char *annotation);


/**
 * Appends the annotation for the given SBML structure.
 *
 * @param sb the given SBML structure.
 * @param annotation the XMLNode_t structure representing the annotation.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_appendAnnotation (SBase_t *sb, const XMLNode_t *annotation);


/**
 * Appends the annotation for the given SBML structure.
 *
 * @param sb the given SBML structure.
 * @param annotation the string representing the annotation.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_appendAnnotationString (SBase_t *sb, const char *annotation);


/**
 * Removes the top-level element within the "annotation"
 * subelement of this SBML structure with the given name.
 *
 * SBML places a few restrictions on the organization of the content of
 * annotations; these are intended to help software tools read and write
 * the data as well as help reduce conflicts between annotations added by
 * different tools.  Please see the SBML specifications for more details.
 *
 * Calling this method allows a particular annotation element to be removed
 * whilst the remaining annotations remain intact.
 *
 * @param sb SBase_t structure containing the annotation to be altered.
 * @param name a string representing the name of the top level
 * annotation element that is to be removed.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_ANNOTATION_NAME_NOT_FOUND, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_ANNOTATION_NS_NOT_FOUND, OperationReturnValues_t}
 *
 * @see SBase_removeTopLevelAnnotationElementWithURI (SBase_t *,
 *  const char *, const char *)
 * @see SBase_replaceTopLevelAnnotationElement (SBase_t *, XMLNode_t *)
 * @see SBase_replaceTopLevelAnnotationElementString (SBase_t *, char *)
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_removeTopLevelAnnotationElement (SBase_t *sb, const char *name);


/**
 * Removes the top-level element within the "annotation"
 * subelement of this SBML structure with the given name and URI.
 *
 * SBML places a few restrictions on the organization of the content of
 * annotations; these are intended to help software tools read and write
 * the data as well as help reduce conflicts between annotations added by
 * different tools.  Please see the SBML specifications for more details.
 *
 * Calling this method allows a particular annotation element to be removed
 * whilst the remaining annotations remain intact.
 *
 * @param sb SBase_t structure containing the annotation to be altered.
 * @param name a string representing the name of the top level
 * annotation element that is to be removed.
 * @param uri a string that is used to check both the name
 * and URI of the top level element to be removed.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_ANNOTATION_NAME_NOT_FOUND, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_ANNOTATION_NS_NOT_FOUND, OperationReturnValues_t}
 *
 * @see SBase_removeTopLevelAnnotationElement (SBase_t *, const char *)
 * @see SBase_replaceTopLevelAnnotationElement (SBase_t *, XMLNode_t *)
 * @see SBase_replaceTopLevelAnnotationElementString (SBase_t *, char *)
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_removeTopLevelAnnotationElementWithURI (SBase_t *sb, const char *name, 
                                              const char *uri);


/**
 * Replaces the given top-level element within the "annotation"
 * subelement of this SBML structure and with the annotation element supplied.
 *
 * SBML places a few restrictions on the organization of the content of
 * annotations; these are intended to help software tools read and write
 * the data as well as help reduce conflicts between annotations added by
 * different tools.  Please see the SBML specifications for more details.
 *
 * This method determines the name of the element to be replaced from the
 * annotation argument. Functionally it is equivalent to calling
 * <code> SBase_removeTopLevelAnnotationElement(sb, name);
 * SBase_appendAnnotation(sb, annotation_with_name);
 * </code> with the exception that the placement of the annotation element remains
 * the same.
 *
 * @param sb SBase_t structure containing the annotation to be altered.
 * @param annotation XMLNode representing the replacement top level annotation.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 *
 * @see SBase_removeTopLevelAnnotationElement (SBase_t *, const char *)
 * @see SBase_removeTopLevelAnnotationElementWithURI (SBase_t *,
 *  const char *, const char *)
 * @see SBase_replaceTopLevelAnnotationElementString (SBase_t *, char *)
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_replaceTopLevelAnnotationElement (SBase_t *sb, const XMLNode_t *annotation);


/**
 * Replaces the given top-level element within the "annotation"
 * subelement of this SBML structure and with the annotation element supplied.
 *
 * SBML places a few restrictions on the organization of the content of
 * annotations; these are intended to help software tools read and write
 * the data as well as help reduce conflicts between annotations added by
 * different tools.  Please see the SBML specifications for more details.
 *
 * This method determines the name of the element to be replaced from the
 * annotation argument. Functionally it is equivalent to calling
 * <code> SBase_removeTopLevelAnnotationElement(sb, name);
 * SBase_appendAnnotation(sb, annotation_with_name);
 * </code> with the exception that the placement of the annotation element remains
 * the same.
 *
 * @param sb SBase_t structure containing the annotation to be altered.
 * @param annotation string representing the replacement top level annotation.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 *
 * @see SBase_removeTopLevelAnnotationElement (SBase_t *, const char *)
 * @see SBase_removeTopLevelAnnotationElementWithURI (SBase_t *,
 *  const char *, const char *)
 * @see SBase_replaceTopLevelAnnotationElement (SBase_t *, XMLNode_t *)
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_replaceTopLevelAnnotationElementString (SBase_t *sb, const char *annotation);


/**
 * Unsets the "metaid" attribute of the given structure.
 *
 * @param sb the SBase_t structure.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_unsetMetaId (SBase_t *sb);


/**
 * Unsets the "id" attribute of the given structure.
 *
 * @param sb the SBase_t structure
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_unsetIdAttribute (SBase_t *sb);


/**
 * Unsets the "name" attribute of the given structure.
 *
 * @param sb the SBase_t structure
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_unsetName (SBase_t *sb);


/**
 * Unsets the "notes" subelement of the given structure.
 *
 * @param sb the SBase_t structure.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_unsetNotes (SBase_t *sb);


/**
 * Unsets the "annotation" subelement of the given structure.
 *
 * @param sb the SBase_t structure.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_unsetAnnotation (SBase_t *sb);


/**
 * Unsets the "sboTerm" attribute of the given structure.
 *
 * @param sb the SBase_t structure.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_unsetSBOTerm (SBase_t *sb);


/**
 * Adds a copy of the given CVTerm_t to this SBML structure.
 *
 * @param sb the structure to add the CVTerm_t to.
 * @param term the CVTerm_t to assign.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 *
 * @note The annotation constructed from a CVTerm_t uses the metaid
 * of the structure to identify it.  Adding a CVTerm_t to an structure
 * where the 'metaId' attribute has not been set will fail with the
 * return value @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int 
SBase_addCVTerm(SBase_t *sb, CVTerm_t *term);


/**
 * Adds a copy of the given CVTerm_t to this SBML structure creating
 * a new bBag element with the same identifier.
 *
 * @param sb the structure to add the CVTerm_t to.
 * @param term the CVTerm_t to assign.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 *
 * @note The annotation constructed from a CVTerm_t uses the metaid
 * of the structure to identify it.  Adding a CVTerm_t to an structure
 * where the 'metaId' attribute has not been set will fail with the
 * return value @sbmlconstant{LIBSBML_UNEXPECTED_ATTRIBUTE, OperationReturnValues_t}.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int 
SBase_addCVTermNewBag(SBase_t *sb, CVTerm_t *term);


/**
 * Returns a list of CVTerm structures in the annotations of this SBML
 * structure.
 *
 * @param sb the structure to getCVTerms from.
 *
 * @return the list of CVTerms for this SBML structure.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
List_t* 
SBase_getCVTerms(SBase_t *sb);


/**
 * Returns the number of CVTerm structures in the annotations of this SBML
 * structure.
 *
 * @param sb the structure to getCVTerms from.
 *
 * @return the number of CVTerms for this SBML structure.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
unsigned int 
SBase_getNumCVTerms(SBase_t *sb);


/**
 * Returns the nth CVTerm in the list of CVTerm_t's of this SBML
 * structure.
 *
 * @param sb the structure to get CVTerm_t's from.
 * @param n unsigned int the index of the CVTerm_t to retrieve.
 *
 * @return the nth CVTerm_t in the list of CVTerm_t's for this SBML structure.
 * If the index @p n is invalid, @c NULL is returned.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
CVTerm_t* 
SBase_getCVTerm(SBase_t *sb, unsigned int n);


/**
 * Clears the list of CVTerm_t's of this SBML
 * structure.
 *
 * @param sb the structure to clear CVTerm_t's from.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int 
SBase_unsetCVTerms(SBase_t *sb);


/**
 * Returns the ModelHistory_t of the given SBase_t structure.
 *
 * @return the ModelHistory_t of the given SBase_t structure.
 *
 * @param sb the SBase_t structure.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
ModelHistory_t * 
SBase_getModelHistory(SBase_t *sb);

/**
 * Predicate for testing whether the ModelHistory_t of a given SBase_t structure is
 * assigned.
 *
 * @param sb the SBase_t structure.
 *
 * @return @c 1 (true) if the ModelHistory_t of this SBase_t structure is
 * set, @c 0 (false) otherwise.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int 
SBase_isSetModelHistory(SBase_t *sb);


/**
 * Set the ModelHistory_t of the given SBase_t structure.
 *
 * @param sb the SBase_t structure.
 * @param history the ModelHistory_t structure.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int 
SBase_setModelHistory(SBase_t *sb, ModelHistory_t *history);

/**
 * Unsets the ModelHistory_t of the given SBase_t structure.
 *
 * @param sb the SBase_t structure.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int 
SBase_unsetModelHistory(SBase_t *sb);


/**
 * Returns the Biological Qualifier associated with this resource,
 * @sbmlconstant{BQB_UNKNOWN, BiolQualifierType_t} if the resource does not exist.
 *
 * @param sb the structure to query.
 * @param resource string representing the resource; e.g.,
 * <code>"http://www.geneontology.org/#GO:0005892"</code>.
 *
 * @return the #BiolQualifierType_t associated with the resource
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
BiolQualifierType_t 
SBase_getResourceBiologicalQualifier(SBase_t *sb, const char * resource);


/**
 * Returns the Model Qualifier associated with this resource,
 * @sbmlconstant{BQM_UNKNOWN, ModelQualifierType_t} if the resource does not exist.
 *
 * @param sb the structure to query.
 * @param resource string representing the resource; e.g.,
 * <code>"http://www.geneontology.org/#GO:0005892"</code>.
 *
 * @return the #ModelQualifierType_t associated with the resource
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
ModelQualifierType_t 
SBase_getResourceModelQualifier(SBase_t *sb, const char * resource);


/**
 * Returns the Model_t structure in which the given instance is located.
 *
 * @param sb the SBase_t structure.
 *
 * @return the parent Model_t structure of the given structure.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
const Model_t *
SBase_getModel (const SBase_t *sb);


/**
 * Returns the SBML Level of the overall SBML document.
 *
 * @param sb the SBase_t structure to query.
 *
 * @return the SBML level of the given structure.
 *
 * @see SBase_getVersion()
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
unsigned int
SBase_getLevel (const SBase_t *sb);


/**
 * Returns the Version within the SBML Level of the overall SBML document.
 *
 * @param sb the SBase_t structure to query.
 *
 * @return the SBML version of the given structure.
 *
 * @see SBase_getLevel()
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
unsigned int
SBase_getVersion (const SBase_t *sb);


/**
 * Returns the libSBML type code for this structure.
 *
 * This method MAY return the typecode of this SBML structure or it MAY
 * return @sbmlconstant{SBML_UNKNOWN, SBMLTypeCode_t}.  That is, 
 * subclasses of SBase are not required to
 * implement this method to return a typecode.  This method is meant
 * primarily for the LibSBML C interface where class and subclass
 * information is not readily available.
 *
 * @note In libSBML 5, the type of return value has been changed from
 * typecode (int) to int. The return value is one of enum values defined for
 * each package. For example, return values will be one of typecode (int) if
 * this structure is defined in SBML core package, return values will be one of
 * #SBMLLayoutTypeCode_t if this structure is defined in Layout extension
 * (i.e. similar enum types are defined in each package extension for each
 * SBase subclass) The value of each typecode can be duplicated between those
 * of different packages. Thus, to distinguish the typecodes of different
 * packages, not only the return value of SBase_getTypeCode() but also that of
 * SBase_getPackageName() must be checked.
 *
 * @param sb the SBase_t structure.
 *
 * @return the typecode (int value) of this SBML structure or 
 * @sbmlconstant{SBML_UNKNOWN, SBMLTypeCode_t} (default).
 *
 * @see SBase_getElementName()
 * @see SBase_getPackageName()
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_getTypeCode (const SBase_t *sb);


/**
 * Returns the XML element name of the given structure.
 *
 * This is overridden by subclasses to return a string appropriate to the
 * SBML component.  For example, Model defines it as returning "model",
 * CompartmentType defines it as returning "compartmentType", etc.
 *
 * @param sb the SBase_t structure.
 *
 * @see SBase_getPackageName()
 * @see SBase_getTypeCode()
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
const char *
SBase_getElementName (const SBase_t *sb);


/**
 * Returns the package name for the given SBase_t structure
 *
 * @param sb the SBase_t structure.
 *
 * @return the package name for the given SBase_t structure or
 * NULL.
 *
 * @see SBase_getElementName()
 * @see SBase_getTypeCode()
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
char *
SBase_getPackageName(const SBaseExtensionPoint_t *sb);


/**
 * Predicate returning @c 1 (true) or @c 0 (false) depending on whether the
 * structure's level/version and namespace values correspond to a valid
 * SBML specification.
 *
 * The valid combinations of SBML Level, Version and Namespace as of this release
 * of libSBML are the following:
 * <ul>
 * <li> Level&nbsp;1 Version&nbsp;2 "http://www.sbml.org/sbml/level1"
 * <li> Level&nbsp;2 Version&nbsp;1 "http://www.sbml.org/sbml/level2"
 * <li> Level&nbsp;2 Version&nbsp;2 "http://www.sbml.org/sbml/level2/version2"
 * <li> Level&nbsp;2 Version&nbsp;3 "http://www.sbml.org/sbml/level2/version3"
 * <li> Level&nbsp;2 Version&nbsp;4 "http://www.sbml.org/sbml/level2/version4"
 * <li> Level&nbsp;2 Version&nbsp;5 "http://www.sbml.org/sbml/level2/version5"
 * <li> Level&nbsp;3 Version&nbsp;1 "http://www.sbml.org/sbml/level3/version1"
 * <li> Level&nbsp;3 Version&nbsp;2 "http://www.sbml.org/sbml/level3/version2"
 * </ul>
 *
 * @param sb the SBase_t structure.
 *
 * @return @c 1 (true) if the level, version and namespace values of this
 * SBML structure correspond to a valid set of values, @c 0 (false) otherwise.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_hasValidLevelVersionNamespaceCombination(SBase_t *sb);


/**
 * Returns the number of plug-in structures (extenstion interfaces) for SBML
 * Level&nbsp;3 package extensions known.
 *
 * @copydetails doc_what_are_plugins
 *
 * @param sb the SBase_t structure to query.
 *
 * @return the number of plug-in structures (extension interfaces) of
 * package extensions known by this instance of libSBML.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int
SBase_getNumPlugins(const SBase_t *sb);

/**
 * Returns a plug-in structure (extension interface) for an SBML Level&nbsp;3
 * package extension with the given package name or URI.
 * The returned plug-in will be the appropriate type of plugin requested:
 * calling SBase_getPlugin(model, "fbc") will return an FbcModelPlugin; calling
 * SBase_getPlugin(parameter, "comp") will return CompSBasePlugin, etc.
 *
 * If no such plugin exists, NULL is returned.
 *
 * @copydetails doc_what_are_plugins
 *
 * @param sb the SBase_t structure.
 * @param package the name or URI of the package.
 *
 * @return the plug-in structure (the libSBML extension interface) of
 * a package extension with the given package name or URI.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
SBasePlugin_t* 
SBase_getPlugin(SBase_t *sb, const char *package);


/**
 * Sets the user data of this node. This can be used by the application
 * developer to attach custom information to the node. In case of a deep
 * copy this attribute will passed as it is. The attribute will be never
 * interpreted by this class.
 *
 * @param sb defines the node of which the user data should be set.
 * @param userData specifies the new user data.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int 
SBase_setUserData(SBase_t* sb, void *userData);

/**
 * Returns the user data that has been previously set by setUserData().
 *
 * @param sb the SBase_t structure in question.
 * @return the user data of this node. NULL if no user data has been.
 * @see SBase_setUserData
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
void *
SBase_getUserData(const SBase_t* sb);

/**
 * Predicate returning @c 1 (true) or @c 0 (false) depending on whether the
 * structure's user data object has been set.
 *
 * @param sb defines the node of which the user data should be queried.
 *
 * @return @c 1 (true) if the user data object of this
 * SBML structure has been set, @c 0 (false) otherwise.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int 
SBase_isSetUserData(const SBase_t* sb);

/**
 * Unsets the user data of this node. 
 *
 * @param sb defines the node of which the user data should be unset.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN
int 
SBase_unsetUserData(SBase_t* sb);

/**
 * Returns the first child element found that has the given @p id in the
 * model-wide @c SId namespace, or @c NULL if no such structure is found.
 *
 * @param sb the SBase_t structure in question.
 * @param id string representing the "id" attribute value of the structure
 * to find.
 *
 * @return pointer to the first element found with the given identifier.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN 
SBase_t* 
SBase_getElementBySId(SBase_t* sb, const char* id);

/**
 * Returns the first child element it can find with a specific "metaid"
 * attribute value, or @c NULL if no such structure is found.
 *
 * @copydetails doc_what_is_metaid
 *
 * @param sb the SBase_t structure in question.
 * @param metaid string representing the "metaid" attribute value of the
 * structure to find.
 *
 * @return pointer to the first element found with the given meta-identifier.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN 
SBase_t* 
SBase_getElementByMetaId(SBase_t* sb, const char* metaid);

/**
 * Returns a List_t structure of all child SBase_t structures, including those nested to
 * an arbitrary depth.
 *
 * @param sb the SBase_t structure in question.
 *
 * @return a pointer to a List_t of pointers to all children structures.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN 
List_t* 
SBase_getAllElements(SBase_t* sb);

/**
 * Renames all the @c SIdRef attributes on this element, including any
 * found in MathML content (if such exists).
 *
 * @copydetails doc_what_is_sidref 
 *
 * This method works by looking at all attributes and (if appropriate)
 * mathematical formulas, comparing the identifiers to the value of @p
 * oldid.  If any matches are found, the matching identifiers are replaced
 * with @p newid.  The method does @em not descend into child elements.
 *
 * @param sb the SBase_t structure in question.
 * @param oldid the old identifier.
 * @param newid the new identifier.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN 
void 
SBase_renameSIdRefs(SBase_t* sb, const char* oldid, const char* newid);

/**
 * Renames all the meta-identifier attributes on this element.
 *
 * @copydetails doc_what_is_metaidref
 *
 * This method works by looking at all meta-identifier attribute values,
 * comparing the identifiers to the value of @p oldid.  If any matches are
 * found, the matching identifiers are replaced with @p newid.  The method
 * does @em not descend into child elements.
 *
 * @param sb the SBase_t structure in question.
 * @param oldid the old identifier.
 * @param newid the new identifier.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN 
void 
SBase_renameMetaIdRefs(SBase_t* sb, const char* oldid, const char* newid);

/**
 * Renames all the @c UnitSIdRef attributes on this element.
 *
 * @copydetails doc_what_is_unitsidref 
 *
 * This method works by looking at all unit identifier attribute values
 * (including, if appropriate, inside mathematical formulas), comparing the
 * unit identifiers to the value of @p oldid.  If any matches are found,
 * the matching identifiers are replaced with @p newid.  The method does
 * @em not descend into child elements.
 *
 * @param sb the SBase_t structure in question.
 * @param oldid the old identifier.
 * @param newid the new identifier.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN 
void 
SBase_renameUnitSIdRefs(SBase_t* sb, const char* oldid, const char* newid);

/**
 * Returns the first child element found that has the given @p id in the
 * model-wide SId namespace from all plug-ins associated with this
 * element, or @c NULL if no such structure is found.
 *
 * @param sb the SBase_t structure in question.
 * @param id string representing the id of structures to find.
 *
 * @return pointer to the first element found with the given @p id.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN 
SBase_t* 
SBase_getElementFromPluginsBySId(SBase_t* sb, const char* id);

/**
 * Returns the first child element it can find with the given @p metaid from
 * all plug-ins associated with this element, or @c NULL if no such structure
 * is found.
 *
 * @param sb the SBase_t structure in question.
 * @param metaid string representing the metaid of structures to find.
 *
 * @return pointer to the first element found with the given @p metaid.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN 
SBase_t* 
SBase_getElementFromPluginsByMetaId(SBase_t* sb, const char* metaid);

/**
 * Returns a List_t of all child SBase_t structures contained in SBML package
 * plug-ins.
 *
 * @copydetails doc_what_are_plugins
 *
 * This method walks down the list of all SBML Level&nbsp;3 packages used
 * by this structure and returns all child structures defined by those packages.
 *
 * @param sb the SBase_t structure in question.
 *
 * @return a pointer to a List_t of pointers to all children structures from
 * plug-ins.
 *
 * @memberof SBase_t
 */
LIBSBML_EXTERN 
List_t* 
SBase_getAllElementsFromPlugins(SBase_t* sb);

END_C_DECLS
LIBSBML_CPP_NAMESPACE_END

#endif  /* !SWIG   */
#endif  /* SBase_h */
