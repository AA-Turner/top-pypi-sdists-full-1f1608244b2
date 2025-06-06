/*
Copyright (c) 2017-2025,
Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Sustainable
Energy, LLC.  See the top-level NOTICE for additional details. All rights reserved.
SPDX-License-Identifier: BSD-3-Clause
*/
#pragma once

#include "../common/GuardedTypes.hpp"
#include "../core/Core.hpp"
#include "../core/FederateIdExtra.hpp"
#include "Endpoints.hpp"
#include "data_view.hpp"
#include "gmlc/containers/DualStringMappedVector.hpp"
#include "gmlc/containers/SimpleQueue.hpp"

#include <cstdint>
#include <deque>
#include <functional>
#include <map>
#include <memory>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
namespace helics {
class Core;
class MessageFederate;
/** class handling the implementation details of a value Federate
@details the functions will parallel those in message Federate and contain the actual implementation
details
*/
class MessageFederateManager {
  public:
    /** construct from a pointer to a core and a specified federate id
     */
    MessageFederateManager(Core* coreOb,
                           MessageFederate* mFed,
                           LocalFederateId id,
                           bool singleThreaded);
    ~MessageFederateManager();
    /** register an endpoint
    @param name the name of the endpoint
    @param type the defined type of the interface for endpoint checking if requested
    */
    Endpoint& registerEndpoint(std::string_view name, std::string_view type);

    /** register a targeted endpoint
@param name the name of the endpoint
@param type the defined type of the interface for endpoint checking if requested
*/
    Endpoint& registerTargetedEndpoint(std::string_view name, std::string_view type);

    /** register a data sink
    @param name the name of the data sink
    */
    Endpoint& registerDataSink(std::string_view name);

    /** check if the federate has any outstanding messages*/
    bool hasMessage() const;
    /* check if a given endpoint has any unread messages*/
    static bool hasMessage(const Endpoint& ept);

    /**
     * Returns the number of pending receives for the specified destination endpoint.
     */
    static uint64_t pendingMessageCount(const Endpoint& ept);
    /**
     * Returns the number of pending receives for the specified destination endpoint.
     */
    uint64_t pendingMessageCount() const;
    /** receive a packet from a particular endpoint
    @param ept the identifier for the endpoint
    @return a message object*/
    static std::unique_ptr<Message> getMessage(const Endpoint& ept);
    /* receive a communication message for any endpoint in the federate*/
    std::unique_ptr<Message> getMessage();

    /** update the time from oldTime to newTime
    @param newTime the newTime of the federate
    @param oldTime the oldTime of the federate
    */
    void updateTime(Time newTime, Time oldTime);
    /** transition from Startup To the Initialize State*/
    void startupToInitializeStateTransition();
    /** transition from initialize to execution State*/
    void initializeToExecuteStateTransition(iteration_time result);
    /** generate results for a local query */
    std::string localQuery(std::string_view queryStr) const;

    /** get an endpoint object from its name
    @param name the endpoint
    @return ivalid_publication_id if name is not recognized otherwise returns the publication_id*/
    Endpoint& getEndpoint(std::string_view name);
    const Endpoint& getEndpoint(std::string_view name) const;

    Endpoint& getEndpoint(int index);
    const Endpoint& getEndpoint(int index) const;

    /** get a data sink from its name
    @param name the data sink
    @return an invalid endpoint if name is not recognized otherwise returns the requested endpoint
    object*/
    Endpoint& getDataSink(std::string_view name);
    const Endpoint& getDataSink(std::string_view name) const;

    /** register a callback function to call when any endpoint receives a message
    @details there can only be one generic callback
    @param callback the function to call
    */
    void setEndpointNotificationCallback(const std::function<void(Endpoint&, Time)>& callback);
    /** register a callback function to call when the specified endpoint receives a message
    @param ept  the endpoint id to register the callback for
    @param callback the function to call
    */
    static void
        setEndpointNotificationCallback(const Endpoint& ept,
                                        const std::function<void(Endpoint&, Time)>& callback);

    /**disconnect from the coreObject*/
    void disconnect();
    /**get the number of registered endpoints*/
    int getEndpointCount() const;

  private:
    class EndpointData {
      public:
        gmlc::containers::SimpleQueue<std::unique_ptr<Message>> messages;
        std::function<void(Endpoint&, Time)> callback;
    };
    /// storage for the local endpoint information
    shared_guarded_opt<gmlc::containers::DualStringMappedVector<Endpoint, InterfaceHandle>>
        mLocalEndpoints;
    atomic_guarded<std::function<void(Endpoint&, Time)>> allCallback;
    Time CurrentTime = Time::minVal();  //!< the current simulation time
    Core* coreObject;  //!< the pointer to the actual core
    MessageFederate* mFed;  //!< pointer back to the message Federate
    const LocalFederateId fedID;  //!< storage for the federate ID
    /// the storage for the message queues and other unique Endpoint information
    shared_guarded_opt<std::deque<EndpointData>> eptData;
    /// maintaining a list of the ordered messages
    guarded_opt<std::vector<unsigned int>> messageOrder;

  private:
    void removeOrderedMessage(unsigned int index);
};
}  // namespace helics
