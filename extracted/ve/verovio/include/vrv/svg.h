/////////////////////////////////////////////////////////////////////////////
// Name:        svg.h
// Author:      Laurent Pugin
// Created:     2017
// Copyright (c) Authors and others. All rights reserved.
/////////////////////////////////////////////////////////////////////////////

#ifndef __VRV_SVG_H__
#define __VRV_SVG_H__

#include "atts_shared.h"
#include "object.h"

namespace vrv {

//----------------------------------------------------------------------------
// Svg
//----------------------------------------------------------------------------

class Svg : public Object {
public:
    /**
     * @name Constructors, destructors, reset and class name methods
     * Reset method reset all attribute classes
     */
    ///@{
    Svg();
    virtual ~Svg();
    void Reset() override;
    std::string GetClassName() const override { return "svg"; }
    ///@}

    /**
     * @name Setter and getter for the svg figure (stored as pugi::xml_node)
     */
    ///@{
    void Set(pugi::xml_node svg);
    pugi::xml_node Get() { return m_svg.first_child(); }
    ///@}

    /**
     * @name Get the width and height of the svg (as given in the svg root)
     */
    ///@{
    int GetWidth() const;
    int GetHeight() const;
    ///@}

    /**
     * Interface for class functor visitation
     */
    ///@{
    FunctorCode Accept(Functor &functor) override;
    FunctorCode Accept(ConstFunctor &functor) const override;
    FunctorCode AcceptEnd(Functor &functor) override;
    FunctorCode AcceptEnd(ConstFunctor &functor) const override;
    ///@}

private:
    //
public:
    //
private:
    /**
     * The svg stored as pugi::xml_document
     */
    pugi::xml_document m_svg;
};

} // namespace vrv

#endif
