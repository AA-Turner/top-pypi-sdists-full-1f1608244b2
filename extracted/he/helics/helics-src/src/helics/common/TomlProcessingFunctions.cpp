/*
Copyright (c) 2017-2025,
Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Sustainable
Energy, LLC.  See the top-level NOTICE for additional details. All rights reserved.
SPDX-License-Identifier: BSD-3-Clause
*/

#include "TomlProcessingFunctions.hpp"

#include "../core/helicsTime.hpp"
#include "../utilities/timeStringOps.hpp"

#include <fstream>
#include <string>

namespace helics::fileops {

bool hasTomlExtension(std::string_view tomlString)
{
    auto ext = tomlString.substr(tomlString.length() - 4);
    return ((ext == "toml") || (ext == "TOML") || (ext == ".ini") || (ext == ".INI"));
}

bool looksLikeConfigToml(std::string_view tomlString)
{
    if (tomlString.empty()) {
        return false;
    }
    if (tomlString.find("[[") != std::string_view::npos) {
        return true;
    }

    return (tomlString.find_first_of('=') != std::string_view::npos);
}

toml::value loadToml(const std::string& tomlString)
{
    if (tomlString.size() > 128) {
        try {
            return loadTomlStr(tomlString);
        }
        catch (const std::invalid_argument&) {
            ;  // just pass through this was an assumption
        }
    }
    std::ifstream file(tomlString, std::ios_base::binary);

    try {
        if (file.is_open()) {
            return toml::parse(file);
        }
        return loadTomlStr(tomlString);
    }
    catch (const toml::exception& se) {
        throw(std::invalid_argument(se.what()));
    }
}

toml::value loadTomlStr(const std::string& tomlString)
{
    try {
        std::istringstream tstring(tomlString);
        toml::value doc = toml::parse(tstring);
        return doc;
    }
    catch (const toml::exception& se) {
        throw(std::invalid_argument(se.what()));
    }
}
// NOLINTNEXTLINE
static const std::string emptyString;

/** read a time from a JSON value element*/
helics::Time loadTomlTime(const toml::value& timeElement, time_units defaultUnits)
{
    if (timeElement.is_table()) {
        const auto& unit = toml::find_or<std::string>(timeElement, "unit", emptyString);
        if (!unit.empty()) {
            defaultUnits = gmlc::utilities::timeUnitsFromString(unit);
        }
        const auto& units = toml::find_or<std::string>(timeElement, "units", emptyString);
        if (!units.empty()) {
            defaultUnits = gmlc::utilities::timeUnitsFromString(units);
        }
        const toml::value emptyVal;
        auto val = toml::find_or(timeElement, "value", emptyVal);
        if (!val.is_empty()) {
            if (val.is_integer()) {
                return {val.as_integer(), defaultUnits};
            }
            if (val.is_floating()) {
                return {val.as_floating() * toSecondMultiplier(defaultUnits)};
            }
            return gmlc::utilities::loadTimeFromString<helics::Time>(tomlAsString(val) + " " +
                                                                     units);
        }
    } else if (timeElement.is_integer()) {
        return {timeElement.as_integer(), defaultUnits};
    } else if (timeElement.is_floating()) {
        return {timeElement.as_floating() * toSecondMultiplier(defaultUnits)};
    } else if (timeElement.is_local_time()) {
        return {toml::get<std::chrono::nanoseconds>(timeElement)};
    } else {
        return gmlc::utilities::loadTimeFromString<helics::Time>(tomlAsString(timeElement));
    }
    return helics::Time::minVal();
}

std::string getName(const toml::value& element)
{
    std::string retval = toml::find_or(element, "key", emptyString);
    if (retval.empty()) {
        retval = toml::find_or(element, "name", emptyString);
    }
    return retval;
}

std::string tomlAsString(const toml::value& element)
{
    switch (element.type()) {
        case toml::value_t::string:
            return element.as_string(std::nothrow_t());  // NOLINT
        case toml::value_t::floating:
            return std::to_string(element.as_floating(std::nothrow_t()));
        case toml::value_t::integer:
            return std::to_string(element.as_integer(std::nothrow_t()));
        default: {
            std::ostringstream str;
            str << element;
            return str.str();
        }
    }
}
}  // namespace helics::fileops
