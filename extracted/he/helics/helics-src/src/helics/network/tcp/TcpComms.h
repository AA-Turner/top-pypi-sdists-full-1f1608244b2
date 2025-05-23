/*
Copyright (c) 2017-2025,
Battelle Memorial Institute; Lawrence Livermore National Security, LLC; Alliance for Sustainable
Energy, LLC.  See the top-level NOTICE for additional details. All rights reserved.
SPDX-License-Identifier: BSD-3-Clause
*/
#pragma once

#include "../NetworkCommsInterface.hpp"
#include "gmlc/containers/BlockingQueue.hpp"

#include <atomic>
#include <memory>
#include <set>
#include <string>

namespace gmlc::networking {
class AsioContextManager;
class TcpConnection;
}  // namespace gmlc::networking

namespace helics::tcp {

/** implementation for the communication interface that uses TCP messages to communicate*/
class TcpComms final: public NetworkCommsInterface {
  public:
    /** default constructor*/
    TcpComms() noexcept;
    /** destructor*/
    ~TcpComms();
    /** load network information into the comms object*/
    virtual void loadNetworkInfo(const NetworkBrokerData& netInfo) override;

    virtual void setFlag(std::string_view flag, bool val) override;

  private:
    bool reuse_address{false};
    std::string encryption_config;
    virtual int getDefaultBrokerPort() const override;
    virtual void queue_rx_function() override;  //!< the functional loop for the receive queue
    virtual void queue_tx_function() override;  //!< the loop for transmitting data

    virtual void closeReceiver() override;  //!< function to instruct the receiver loop to close

    /** make the initial connection to a broker and get setup information*/
    bool establishBrokerConnection(
        std::shared_ptr<gmlc::networking::AsioContextManager>& ioctx,
        std::shared_ptr<gmlc::networking::TcpConnection>& brokerConnection);
    /** process an incoming message
return code for required action 0=NONE, -1 TERMINATE*/
    int processIncomingMessage(ActionMessage&& cmd);
    // promise and future for communicating port number from tx_thread to rx_thread
    gmlc::containers::BlockingQueue<ActionMessage> rxMessageQueue;

    void txReceive(const char* data, size_t bytes_received, const std::string& errorMessage);

    /** callback function for receiving data asynchronously from the socket
@param connection pointer to the connection
@param data the pointer to the data
@param bytes_received the length of the received data
@return a the number of bytes used by the function
*/
    size_t dataReceive(gmlc::networking::TcpConnection* connection,
                       const char* data,
                       size_t bytes_received);

    //  bool errorHandle()
};

}  // namespace helics::tcp
