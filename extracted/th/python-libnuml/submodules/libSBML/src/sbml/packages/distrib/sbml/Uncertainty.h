/**
 * @file Uncertainty.h
 * @brief Definition of the Uncertainty class.
 * @author SBMLTeam
 *
 * <!--------------------------------------------------------------------------
 * This file is part of libSBML. Please visit http://sbml.org for more
 * information about SBML, and the latest version of libSBML.
 *
 * Copyright (C) 2020 jointly by the following organizations:
 *     1. California Institute of Technology, Pasadena, CA, USA
 *     2. University of Heidelberg, Heidelberg, Germany
 *     3. University College London, London, UK
 *
 * Copyright (C) 2019 jointly by the following organizations:
 * 1. California Institute of Technology, Pasadena, CA, USA
 * 2. University of Heidelberg, Heidelberg, Germany
 *
 * Copyright (C) 2013-2018 jointly by the following organizations:
 * 1. California Institute of Technology, Pasadena, CA, USA
 * 2. EMBL European Bioinformatics Institute (EMBL-EBI), Hinxton, UK
 * 3. University of Heidelberg, Heidelberg, Germany
 *
 * Copyright (C) 2009-2013 jointly by the following organizations:
 * 1. California Institute of Technology, Pasadena, CA, USA
 * 2. EMBL European Bioinformatics Institute (EMBL-EBI), Hinxton, UK
 *
 * Copyright (C) 2006-2008 by the California Institute of Technology,
 * Pasadena, CA, USA
 *
 * Copyright (C) 2002-2005 jointly by the following organizations:
 * 1. California Institute of Technology, Pasadena, CA, USA
 * 2. Japan Science and Technology Agency, Japan
 *
 * This library is free software; you can redistribute it and/or modify it
 * under the terms of the GNU Lesser General Public License as published by the
 * Free Software Foundation. A copy of the license agreement is provided in the
 * file named "LICENSE.txt" included with this software distribution and also
 * available online as http://sbml.org/software/libsbml/license.html
 * ------------------------------------------------------------------------ -->
 *
 * @class Uncertainty
 * @sbmlbrief{spatial} The Uncertainty class is a collection of zero or more
 * statistical measures related to the uncertainty of the parent SBML element. It
 * may only contain one of each type of measurement, which means that each of its
 * UncertParameter children must have a unique type attribute for every ue but
 * externalParameter. Each UncertParameter child with a type of externalParameter
 * must, in turn, have a unique definitionURL ue. If a given SBML element has
 * multiple measures of the same type (for example, as measured from different
 * sources or different experiments), it should be given multiple Uncertainty
 * children. Each Uncertainty child must be a unique set of statistical measures.
 *
 * These statistical measures do not numerically affect simulation of the model.
 * They are, in essence, a controlled annotation format specifically designed for
 * this sort of information. Tools may use this information as they wish, just as
 * they can with other annotation information.
 *
 * Note that for elements that change in ue over time, the described uncertainty
 * applies only to the element's initial state, and not to how it changes in
 * time. For typical simulations, this means the element's initial assignment.
 *
 * The child UncertParameter children are named according to their class, so any
 * UncertSpan child will have the element name uncertSpan, and any
 * UncertParameter base class child will have the element name uncertParameter.
 */


#ifndef Uncertainty_H__
#define Uncertainty_H__


#include <sbml/common/extern.h>
#include <sbml/common/sbmlfwd.h>
#include <sbml/packages/distrib/common/distribfwd.h>


#ifdef __cplusplus


#include <string>


#include <sbml/packages/distrib/sbml/DistribBase.h>
#include <sbml/packages/distrib/extension/DistribExtension.h>
#include <sbml/packages/distrib/sbml/ListOfUncertParameters.h>


LIBSBML_CPP_NAMESPACE_BEGIN


class LIBSBML_EXTERN Uncertainty : public DistribBase
{
protected:

  /** @cond doxygenLibsbmlInternal */

  ListOfUncertParameters mUncertParameters;

  /** @endcond */

public:

  /**
   * Creates a new Uncertainty using the given SBML Level, Version and
   * &ldquo;distrib&rdquo; package version.
   *
   * @param level an unsigned int, the SBML Level to assign to this
   * Uncertainty.
   *
   * @param version an unsigned int, the SBML Version to assign to this
   * Uncertainty.
   *
   * @param pkgVersion an unsigned int, the SBML Distrib Version to assign to
   * this Uncertainty.
   *
   * @copydetails doc_note_setting_lv_pkg
   */
  Uncertainty(unsigned int level = DistribExtension::getDefaultLevel(),
              unsigned int version = DistribExtension::getDefaultVersion(),
              unsigned int pkgVersion =
                DistribExtension::getDefaultPackageVersion());


  /**
   * Creates a new Uncertainty using the given DistribPkgNamespaces object.
   *
   * @copydetails doc_what_are_sbml_package_namespaces
   *
   * @param distribns the DistribPkgNamespaces object.
   *
   * @copydetails doc_note_setting_lv_pkg
   */
  Uncertainty(DistribPkgNamespaces *distribns);


  /**
   * Copy constructor for Uncertainty.
   *
   * @param orig the Uncertainty instance to copy.
   */
  Uncertainty(const Uncertainty& orig);


  /**
   * Assignment operator for Uncertainty.
   *
   * @param rhs the Uncertainty object whose values are to be used as the basis
   * of the assignment.
   */
  Uncertainty& operator=(const Uncertainty& rhs);


  /**
   * Creates and returns a deep copy of this Uncertainty object.
   *
   * @return a (deep) copy of this Uncertainty object.
   */
  virtual Uncertainty* clone() const;


  /**
   * Destructor for Uncertainty.
   */
  virtual ~Uncertainty();


  /**
   * Returns the ListOfUncertParameters from this Uncertainty.
   *
   * @return the ListOfUncertParameters from this Uncertainty.
   *
   * @copydetails doc_returned_unowned_pointer
   *
   * @see addUncertParameter(const UncertParameter* object)
   * @see createUncertParameter()
   * @see getUncertParameter(const std::string& sid)
   * @see getUncertParameter(unsigned int n)
   * @see getNumUncertParameters()
   * @see removeUncertParameter(const std::string& sid)
   * @see removeUncertParameter(unsigned int n)
   */
  const ListOfUncertParameters* getListOfUncertParameters() const;


  /**
   * Returns the ListOfUncertParameters from this Uncertainty.
   *
   * @return the ListOfUncertParameters from this Uncertainty.
   *
   * @copydetails doc_returned_unowned_pointer
   *
   * @see addUncertParameter(const UncertParameter* object)
   * @see createUncertParameter()
   * @see getUncertParameter(const std::string& sid)
   * @see getUncertParameter(unsigned int n)
   * @see getNumUncertParameters()
   * @see removeUncertParameter(const std::string& sid)
   * @see removeUncertParameter(unsigned int n)
   */
  ListOfUncertParameters* getListOfUncertParameters();


  /**
   * Get an UncertParameter from the Uncertainty.
   *
   * @param n an unsigned int representing the index of the UncertParameter to
   * retrieve.
   *
   * @return the nth UncertParameter in the ListOfUncertParameters within this
   * Uncertainty or @c NULL if no such object exists.
   *
   * @copydetails doc_returned_unowned_pointer
   *
   * @see addUncertParameter(const UncertParameter* object)
   * @see createUncertParameter()
   * @see getUncertParameter(const std::string& sid)
   * @see getNumUncertParameters()
   * @see removeUncertParameter(const std::string& sid)
   * @see removeUncertParameter(unsigned int n)
   */
  UncertParameter* getUncertParameter(unsigned int n);


  /**
   * Get an UncertParameter from the Uncertainty.
   *
   * @param n an unsigned int representing the index of the UncertParameter to
   * retrieve.
   *
   * @return the nth UncertParameter in the ListOfUncertParameters within this
   * Uncertainty or @c NULL if no such object exists.
   *
   * @copydetails doc_returned_unowned_pointer
   *
   * @see addUncertParameter(const UncertParameter* object)
   * @see createUncertParameter()
   * @see getUncertParameter(const std::string& sid)
   * @see getNumUncertParameters()
   * @see removeUncertParameter(const std::string& sid)
   * @see removeUncertParameter(unsigned int n)
   */
  const UncertParameter* getUncertParameter(unsigned int n) const;


  /**
   * Get an UncertParameter from the Uncertainty based on the element to which
   * it refers.
   *
   * @param sid a string representing the "var" attribute of the
   * UncertParameter object to retrieve.
   *
   * @return the first UncertParameter in this Uncertainty based on the given
   * var attribute or NULL if no such UncertParameter exists.
   *
   * @copydetails doc_returned_unowned_pointer
   */
  const UncertParameter* getUncertParameterByVar(const std::string& sid) const;

  /**
   * Get an UncertParameter from the Uncertainty based on
   * its type.
   *
   * @param utype the UncertType representing the "type" attribute of the
   * UncertParameter object to retrieve.
   *
   * @return the first UncertParameter in this ListOfUncertParameters based on
   * the given var attribute or NULL if no such UncertParameter exists.
   *
   * Note that while most types must be unique in any ListOfUncertParameters,
   * the exception is external parameters 
   * (@sbmlconstant{DISTRIB_UNCERTTYPE_EXTERNALPARAMETER, UncerType_t}), 
   * which there many be several of.
   *
   * @copydetails doc_returned_unowned_pointer
   */
  const UncertParameter * getUncertParameterByType(UncertType_t utype) const;


  /**
   * Get an UncertParameter from the Uncertainty based on the element to which
   * it refers.
   *
   * @param sid a string representing the "var" attribute of the
   * UncertParameter object to retrieve.
   *
   * @return the first UncertParameter in this Uncertainty based on the given
   * var attribute or NULL if no such UncertParameter exists.
   *
   * @copydetails doc_returned_unowned_pointer
   */
  UncertParameter* getUncertParameterByVar(const std::string& sid);


  /**
   * Get an UncertParameter from the Uncertainty based on
   * its type.
   *
   * @param utype the UncertType representing the "type" attribute of the
   * UncertParameter object to retrieve.
   *
   * @return the first UncertParameter in this ListOfUncertParameters based on
   * the given var attribute or NULL if no such UncertParameter exists.
   *
   * Note that while most types must be unique in any ListOfUncertParameters,
   * the exception is external parameters 
   * (@sbmlconstant{DISTRIB_UNCERTTYPE_EXTERNALPARAMETER, UncerType_t}), 
   * which there many be several of.
   *
   * @copydetails doc_returned_unowned_pointer
   */
  UncertParameter * getUncertParameterByType(UncertType_t utype);


  /**
   * Adds a copy of the given UncertParameter to this Uncertainty.
   *
   * @param up the UncertParameter object to add.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_LEVEL_MISMATCH, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_VERSION_MISMATCH, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_PKG_VERSION_MISMATCH, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_DUPLICATE_OBJECT_ID, OperationReturnValues_t}
   *
   * @copydetails doc_note_object_is_copied
   *
   * @see createUncertParameter()
   * @see getUncertParameter(const std::string& sid)
   * @see getUncertParameter(unsigned int n)
   * @see getNumUncertParameters()
   * @see removeUncertParameter(const std::string& sid)
   * @see removeUncertParameter(unsigned int n)
   */
  int addUncertParameter(const UncertParameter* up);


  int addUncertSpan(const UncertSpan* us);
  /**
   * Get the number of UncertParameter objects in this Uncertainty.
   *
   * @return the number of UncertParameter objects in this Uncertainty.
   *
   * @see addUncertParameter(const UncertParameter* object)
   * @see createUncertParameter()
   * @see getUncertParameter(const std::string& sid)
   * @see getUncertParameter(unsigned int n)
   * @see removeUncertParameter(const std::string& sid)
   * @see removeUncertParameter(unsigned int n)
   */
  unsigned int getNumUncertParameters() const;


  UncertParameter* createUncertParameter();
    

  UncertSpan* createUncertSpan();
  /**
   * Removes the nth UncertParameter from this Uncertainty and returns a
   * pointer to it.
   *
   * @param n an unsigned int representing the index of the UncertParameter to
   * remove.
   *
   * @return a pointer to the nth UncertParameter in this Uncertainty.
   *
   * @copydetails doc_warning_returns_owned_pointer
   *
   * @see addUncertParameter(const UncertParameter* object)
   * @see createUncertParameter()
   * @see getUncertParameter(const std::string& sid)
   * @see getUncertParameter(unsigned int n)
   * @see getNumUncertParameters()
   * @see removeUncertParameter(const std::string& sid)
   */
  UncertParameter* removeUncertParameter(unsigned int n);


  /**
   * Returns the XML element name of this Uncertainty object.
   *
   * For Uncertainty, the XML element name is always @c "uncertainty".
   *
   * @return the name of this element, i.e. @c "uncertainty".
   */
  virtual const std::string& getElementName() const;


  /**
   * Returns the libSBML type code for this Uncertainty object.
   *
   * @copydetails doc_what_are_typecodes
   *
   * @return the SBML type code for this object:
   * @sbmlconstant{SBML_DISTRIB_UNCERTAINTY, SBMLDistribTypeCode_t}.
   *
   * @copydetails doc_warning_typecodes_not_unique
   *
   * @see getElementName()
   * @see getPackageName()
   */
  virtual int getTypeCode() const;


  /**
   * Predicate returning @c true if all the required attributes for this
   * Uncertainty object have been set.
   *
   * @return @c true to indicate that all the required attributes of this
   * Uncertainty have been set, otherwise @c false is returned.
   */
  virtual bool hasRequiredAttributes() const;


  /**
   * Predicate returning @c true if all the required elements for this
   * Uncertainty object have been set.
   *
   * @return @c true to indicate that all the required elements of this
   * Uncertainty have been set, otherwise @c false is returned.
   *
   *
   * @note The required elements for the Uncertainty object are:
   */
  virtual bool hasRequiredElements() const;



  /** @cond doxygenLibsbmlInternal */

  /**
   * Write any contained elements
   */
  virtual void writeElements(XMLOutputStream& stream) const;

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Accepts the given SBMLVisitor
   */
  virtual bool accept(SBMLVisitor& v) const;

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Sets the parent SBMLDocument
   */
  virtual void setSBMLDocument(SBMLDocument* d);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Connects to child elements
   */
  virtual void connectToChild();

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Enables/disables the given package with this element
   */
  virtual void enablePackageInternal(const std::string& pkgURI,
                                     const std::string& pkgPrefix,
                                     bool flag);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Updates the namespaces when setLevelVersion is used
   */
  virtual void updateSBMLNamespace(const std::string& package,
                                   unsigned int level,
                                   unsigned int version);

  /** @endcond */




  #ifndef SWIG



  /** @cond doxygenLibsbmlInternal */

  /**
   * Gets the value of the "attributeName" attribute of this Uncertainty.
   *
   * @param attributeName, the name of the attribute to retrieve.
   *
   * @param value, the address of the value to record.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  virtual int getAttribute(const std::string& attributeName, bool& value)
    const;

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Gets the value of the "attributeName" attribute of this Uncertainty.
   *
   * @param attributeName, the name of the attribute to retrieve.
   *
   * @param value, the address of the value to record.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  virtual int getAttribute(const std::string& attributeName, int& value) const;

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Gets the value of the "attributeName" attribute of this Uncertainty.
   *
   * @param attributeName, the name of the attribute to retrieve.
   *
   * @param value, the address of the value to record.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  virtual int getAttribute(const std::string& attributeName,
                           double& value) const;

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Gets the value of the "attributeName" attribute of this Uncertainty.
   *
   * @param attributeName, the name of the attribute to retrieve.
   *
   * @param value, the address of the value to record.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  virtual int getAttribute(const std::string& attributeName,
                           unsigned int& value) const;

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Gets the value of the "attributeName" attribute of this Uncertainty.
   *
   * @param attributeName, the name of the attribute to retrieve.
   *
   * @param value, the address of the value to record.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  virtual int getAttribute(const std::string& attributeName,
                           std::string& value) const;

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Predicate returning @c true if this Uncertainty's attribute
   * "attributeName" is set.
   *
   * @param attributeName, the name of the attribute to query.
   *
   * @return @c true if this Uncertainty's attribute "attributeName" has been
   * set, otherwise @c false is returned.
   */
  virtual bool isSetAttribute(const std::string& attributeName) const;

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Sets the value of the "attributeName" attribute of this Uncertainty.
   *
   * @param attributeName, the name of the attribute to set.
   *
   * @param value, the value of the attribute to set.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  virtual int setAttribute(const std::string& attributeName, bool value);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Sets the value of the "attributeName" attribute of this Uncertainty.
   *
   * @param attributeName, the name of the attribute to set.
   *
   * @param value, the value of the attribute to set.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  virtual int setAttribute(const std::string& attributeName, int value);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Sets the value of the "attributeName" attribute of this Uncertainty.
   *
   * @param attributeName, the name of the attribute to set.
   *
   * @param value, the value of the attribute to set.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  virtual int setAttribute(const std::string& attributeName, double value);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Sets the value of the "attributeName" attribute of this Uncertainty.
   *
   * @param attributeName, the name of the attribute to set.
   *
   * @param value, the value of the attribute to set.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  virtual int setAttribute(const std::string& attributeName,
                           unsigned int value);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Sets the value of the "attributeName" attribute of this Uncertainty.
   *
   * @param attributeName, the name of the attribute to set.
   *
   * @param value, the value of the attribute to set.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  virtual int setAttribute(const std::string& attributeName,
                           const std::string& value);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Unsets the value of the "attributeName" attribute of this Uncertainty.
   *
   * @param attributeName, the name of the attribute to query.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  virtual int unsetAttribute(const std::string& attributeName);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Creates and returns an new "elementName" object in this Uncertainty.
   *
   * @param elementName, the name of the element to create.
   *
   * @return pointer to the element created.
   */
  virtual SBase* createChildObject(const std::string& elementName);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Adds a new "elementName" object to this Uncertainty.
   *
   * @param elementName, the name of the element to create.
   *
   * @param element, pointer to the element to be added.
   *
   * @copydetails doc_returns_success_code
   * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
   * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
   */
  virtual int addChildObject(const std::string& elementName,
                             const SBase* element);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Removes and returns the new "elementName" object with the given id in this
   * Uncertainty.
   *
   * @param elementName, the name of the element to remove.
   *
   * @param id, the id of the element to remove.
   *
   * @return pointer to the element removed.
   */
  virtual SBase* removeChildObject(const std::string& elementName,
                                   const std::string& id);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Returns the number of "elementName" in this Uncertainty.
   *
   * @param elementName, the name of the element to get number of.
   *
   * @return unsigned int number of elements.
   */
  virtual unsigned int getNumObjects(const std::string& elementName);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Returns the nth object of "objectName" in this Uncertainty.
   *
   * @param elementName, the name of the element to get number of.
   *
   * @param index, unsigned int the index of the object to retrieve.
   *
   * @return pointer to the object.
   */
  virtual SBase* getObject(const std::string& elementName, unsigned int index);

  /** @endcond */




  #endif /* !SWIG */


  /**
   * Returns the first child element that has the given @p id in the model-wide
   * SId namespace, or @c NULL if no such object is found.
   *
   * @param id a string representing the id attribute of the object to
   * retrieve.
   *
   * @return a pointer to the SBase element with the given @p id. If no such
   * object is found, this method returns @c NULL.
   */
  virtual SBase* getElementBySId(const std::string& id);


  /**
   * Returns the first child element that has the given @p metaid, or @c NULL
   * if no such object is found.
   *
   * @param metaid a string representing the metaid attribute of the object to
   * retrieve.
   *
   * @return a pointer to the SBase element with the given @p metaid. If no
   * such object is found this method returns @c NULL.
   */
  virtual SBase* getElementByMetaId(const std::string& metaid);


  /**
   * Returns a List of all child SBase objects, including those nested to an
   * arbitrary depth.
   *
   * @param filter an ElementFilter that may impose restrictions on the objects
   * to be retrieved.
   *
   * @return a List pointer of pointers to all SBase child objects with any
   * restriction imposed.
   */
  virtual List* getAllElements(ElementFilter * filter = NULL);


protected:


  /** @cond doxygenLibsbmlInternal */

  /**
   * Creates a new object from the next XMLToken on the XMLInputStream
   */
  virtual SBase* createObject(XMLInputStream& stream);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Adds the expected attributes for this element
   */
  virtual void addExpectedAttributes(ExpectedAttributes& attributes);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Reads the expected attributes into the member data variables
   */
  virtual void readAttributes(const XMLAttributes& attributes,
                              const ExpectedAttributes& expectedAttributes);

  /** @endcond */



  /** @cond doxygenLibsbmlInternal */

  /**
   * Writes the attributes to the stream
   */
  virtual void writeAttributes(XMLOutputStream& stream) const;

  /** @endcond */


};



LIBSBML_CPP_NAMESPACE_END




#endif /* __cplusplus */




#ifndef SWIG




LIBSBML_CPP_NAMESPACE_BEGIN




BEGIN_C_DECLS


/**
 * Creates a new Uncertainty_t using the given SBML Level, Version and
 * &ldquo;distrib&rdquo; package version.
 *
 * @param level an unsigned int, the SBML Level to assign to this
 * Uncertainty_t.
 *
 * @param version an unsigned int, the SBML Version to assign to this
 * Uncertainty_t.
 *
 * @param pkgVersion an unsigned int, the SBML Distrib Version to assign to
 * this Uncertainty_t.
 *
 * @copydetails doc_note_setting_lv_pkg
 *
 * @copydetails doc_returned_owned_pointer
 *
 * @memberof Uncertainty_t
 */
LIBSBML_EXTERN
Uncertainty_t *
Uncertainty_create(unsigned int level,
                   unsigned int version,
                   unsigned int pkgVersion);


/**
 * Creates and returns a deep copy of this Uncertainty_t object.
 *
 * @param u the Uncertainty_t structure.
 *
 * @return a (deep) copy of this Uncertainty_t object.
 *
 * @copydetails doc_returned_owned_pointer
 *
 * @memberof Uncertainty_t
 */
LIBSBML_EXTERN
Uncertainty_t*
Uncertainty_clone(const Uncertainty_t* u);


/**
 * Frees this Uncertainty_t object.
 *
 * @param u the Uncertainty_t structure.
 *
 * @memberof Uncertainty_t
 */
LIBSBML_EXTERN
void
Uncertainty_free(Uncertainty_t* u);


/**
 * Returns a ListOf_t * containing UncertParameter_t objects from this
 * Uncertainty_t.
 *
 * @param u the Uncertainty_t structure whose ListOfUncertParameters is sought.
 *
 * @return the ListOfUncertParameters from this Uncertainty_t as a ListOf_t *.
 *
 * @copydetails doc_returned_unowned_pointer
 *
 * @see Uncertainty_addUncertParameter()
 * @see Uncertainty_createUncertParameter()
 * @see Uncertainty_getUncertParameterById()
 * @see Uncertainty_getUncertParameter()
 * @see Uncertainty_getNumUncertParameters()
 * @see Uncertainty_removeUncertParameterById()
 * @see Uncertainty_removeUncertParameter()
 *
 * @memberof Uncertainty_t
 */
LIBSBML_EXTERN
ListOf_t*
Uncertainty_getListOfUncertParameters(Uncertainty_t* u);


/**
 * Get an UncertParameter_t from the Uncertainty_t.
 *
 * @param u the Uncertainty_t structure to search.
 *
 * @param n an unsigned int representing the index of the UncertParameter_t to
 * retrieve.
 *
 * @return the nth UncertParameter_t in the ListOfUncertParameters within this
 * Uncertainty or @c NULL if no such object exists.
 *
 * @copydetails doc_returned_unowned_pointer
 *
 * @memberof Uncertainty_t
 */
LIBSBML_EXTERN
UncertParameter_t*
Uncertainty_getUncertParameter(Uncertainty_t* u, unsigned int n);


/**
 * Get an UncertParameter_t from the Uncertainty_t based on the element to
 * which it refers.
 *
 * @param u the Uncertainty_t structure to search.
 *
 * @param sid a string representing the "var" attribute of the
 * UncertParameter_t object to retrieve.
 *
 * @return the first UncertParameter_t in this Uncertainty_t based on the given
 * var attribute or NULL if no such UncertParameter_t exists.
 *
 * @copydetails doc_returned_unowned_pointer
 *
 * @memberof Uncertainty_t
 */
LIBSBML_EXTERN
UncertParameter_t*
Uncertainty_getUncertParameterByVar(Uncertainty_t* u, const char *sid);


/**
 * Adds a copy of the given UncertParameter_t to this Uncertainty_t.
 *
 * @param u the Uncertainty_t structure to which the UncertParameter_t should
 * be added.
 *
 * @param up the UncertParameter_t object to add.
 *
 * @copydetails doc_returns_success_code
 * @li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_OPERATION_FAILED, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_INVALID_OBJECT, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_LEVEL_MISMATCH, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_VERSION_MISMATCH, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_PKG_VERSION_MISMATCH, OperationReturnValues_t}
 * @li @sbmlconstant{LIBSBML_DUPLICATE_OBJECT_ID, OperationReturnValues_t}
 *
 * @memberof Uncertainty_t
 */
LIBSBML_EXTERN
int
Uncertainty_addUncertParameter(Uncertainty_t* u, const UncertParameter_t* up);


/**
 * Get the number of UncertParameter_t objects in this Uncertainty_t.
 *
 * @param u the Uncertainty_t structure to query.
 *
 * @return the number of UncertParameter_t objects in this Uncertainty_t.
 *
 * @memberof Uncertainty_t
 */
LIBSBML_EXTERN
unsigned int
Uncertainty_getNumUncertParameters(Uncertainty_t* u);


/**
 * Removes the nth UncertParameter_t from this Uncertainty_t and returns a
 * pointer to it.
 *
 * @param u the Uncertainty_t structure to search.
 *
 * @param n an unsigned int representing the index of the UncertParameter_t to
 * remove.
 *
 * @return a pointer to the nth UncertParameter_t in this Uncertainty_t.
 *
 * @copydetails doc_warning_returns_owned_pointer
 *
 * @memberof Uncertainty_t
 */
LIBSBML_EXTERN
UncertParameter_t*
Uncertainty_removeUncertParameter(Uncertainty_t* u, unsigned int n);


/**
 * Predicate returning @c 1 (true) if all the required attributes for this
 * Uncertainty_t object have been set.
 *
 * @param u the Uncertainty_t structure.
 *
 * @return @c 1 (true) to indicate that all the required attributes of this
 * Uncertainty_t have been set, otherwise @c 0 (false) is returned.
 *
 * @memberof Uncertainty_t
 */
LIBSBML_EXTERN
int
Uncertainty_hasRequiredAttributes(const Uncertainty_t * u);


/**
 * Predicate returning @c 1 (true) if all the required elements for this
 * Uncertainty_t object have been set.
 *
 * @param u the Uncertainty_t structure.
 *
 * @return @c 1 (true) to indicate that all the required elements of this
 * Uncertainty_t have been set, otherwise @c 0 (false) is returned.
 *
 *
 * @note The required elements for the Uncertainty_t object are:
 *
 * @memberof Uncertainty_t
 */
LIBSBML_EXTERN
int
Uncertainty_hasRequiredElements(const Uncertainty_t * u);




END_C_DECLS




LIBSBML_CPP_NAMESPACE_END




#endif /* !SWIG */




#endif /* !Uncertainty_H__ */


