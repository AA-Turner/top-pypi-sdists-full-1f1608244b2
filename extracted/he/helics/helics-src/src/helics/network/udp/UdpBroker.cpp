/*
Copyright (c) 2017-2025,
Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Sustainable
Energy, LLC.  See the top-level NOTICE for additional details. All rights reserved.
SPDX-License-Identifier: BSD-3-Clause
*/

#include "UdpBroker.h"

#include "../NetworkBroker_impl.hpp"
#include "UdpComms.h"

namespace helics {
template class NetworkBroker<udp::UdpComms, gmlc::networking::InterfaceTypes::UDP, 7>;
}  // namespace helics
