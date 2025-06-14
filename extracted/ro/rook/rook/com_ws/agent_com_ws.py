import os
from rook.com_ws.agent_com_impel.multithread_agent_com import MultiThreadAgentCom as AgentComMT
from rook.logger import logger
from sys import platform

SINGLE_THREAD_AGENT_COM = object()
MULTI_THREAD_AGENT_COM = object()

thread_connection_type = None

if os.getenv("ROOKOUT_SINGLETHREAD_COMM", "0") == "1":
    if platform in ("linux", "linux2"):
        from rook.com_ws.agent_com_impel.singlethread_agent_com import SingleThreadAgentCom as AgentComSingle

        logger.info("Using single-threaded communication")
        AgentCom = AgentComSingle

        thread_connection_type = SINGLE_THREAD_AGENT_COM
    else:
        logger.info('Not using single-threaded communication because os is not Linux, using multi-threaded communication')
        AgentCom = AgentComMT

        thread_connection_type = MULTI_THREAD_AGENT_COM
else:
    logger.debug("Using multi-threaded communication")
    AgentCom = AgentComMT

    thread_connection_type = MULTI_THREAD_AGENT_COM
