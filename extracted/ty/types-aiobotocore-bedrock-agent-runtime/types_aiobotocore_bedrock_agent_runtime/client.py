"""
Type annotations for bedrock-agent-runtime service Client.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_bedrock_agent_runtime.client import AgentsforBedrockRuntimeClient

    session = get_session()
    async with session.create_client("bedrock-agent-runtime") as client:
        client: AgentsforBedrockRuntimeClient
    ```
"""

from __future__ import annotations

import sys
from types import TracebackType
from typing import Any, overload

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetAgentMemoryPaginator,
    ListInvocationsPaginator,
    ListInvocationStepsPaginator,
    ListSessionsPaginator,
    RerankPaginator,
    RetrievePaginator,
)
from .type_defs import (
    CreateInvocationRequestTypeDef,
    CreateInvocationResponseTypeDef,
    CreateSessionRequestTypeDef,
    CreateSessionResponseTypeDef,
    DeleteAgentMemoryRequestTypeDef,
    DeleteSessionRequestTypeDef,
    EndSessionRequestTypeDef,
    EndSessionResponseTypeDef,
    GenerateQueryRequestTypeDef,
    GenerateQueryResponseTypeDef,
    GetAgentMemoryRequestTypeDef,
    GetAgentMemoryResponseTypeDef,
    GetInvocationStepRequestTypeDef,
    GetInvocationStepResponseTypeDef,
    GetSessionRequestTypeDef,
    GetSessionResponseTypeDef,
    InvokeAgentRequestTypeDef,
    InvokeAgentResponseTypeDef,
    InvokeFlowRequestTypeDef,
    InvokeFlowResponseTypeDef,
    InvokeInlineAgentRequestTypeDef,
    InvokeInlineAgentResponseTypeDef,
    ListInvocationsRequestTypeDef,
    ListInvocationsResponseTypeDef,
    ListInvocationStepsRequestTypeDef,
    ListInvocationStepsResponseTypeDef,
    ListSessionsRequestTypeDef,
    ListSessionsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    OptimizePromptRequestTypeDef,
    OptimizePromptResponseTypeDef,
    PutInvocationStepRequestTypeDef,
    PutInvocationStepResponseTypeDef,
    RerankRequestTypeDef,
    RerankResponseTypeDef,
    RetrieveAndGenerateRequestTypeDef,
    RetrieveAndGenerateResponseTypeDef,
    RetrieveAndGenerateStreamRequestTypeDef,
    RetrieveAndGenerateStreamResponseTypeDef,
    RetrieveRequestTypeDef,
    RetrieveResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateSessionRequestTypeDef,
    UpdateSessionResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Self, Unpack
else:
    from typing_extensions import Literal, Self, Unpack


__all__ = ("AgentsforBedrockRuntimeClient",)


class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    BadGatewayException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DependencyFailedException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ModelNotReadyException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class AgentsforBedrockRuntimeClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AgentsforBedrockRuntimeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/can_paginate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#can_paginate)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/generate_presigned_url.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#generate_presigned_url)
        """

    async def create_invocation(
        self, **kwargs: Unpack[CreateInvocationRequestTypeDef]
    ) -> CreateInvocationResponseTypeDef:
        """
        Creates a new invocation within a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/create_invocation.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#create_invocation)
        """

    async def create_session(
        self, **kwargs: Unpack[CreateSessionRequestTypeDef]
    ) -> CreateSessionResponseTypeDef:
        """
        Creates a session to temporarily store conversations for generative AI (GenAI)
        applications built with open-source frameworks such as LangGraph and
        LlamaIndex.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/create_session.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#create_session)
        """

    async def delete_agent_memory(
        self, **kwargs: Unpack[DeleteAgentMemoryRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes memory from the specified memory identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/delete_agent_memory.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#delete_agent_memory)
        """

    async def delete_session(self, **kwargs: Unpack[DeleteSessionRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a session that you ended.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/delete_session.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#delete_session)
        """

    async def end_session(
        self, **kwargs: Unpack[EndSessionRequestTypeDef]
    ) -> EndSessionResponseTypeDef:
        """
        Ends the session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/end_session.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#end_session)
        """

    async def generate_query(
        self, **kwargs: Unpack[GenerateQueryRequestTypeDef]
    ) -> GenerateQueryResponseTypeDef:
        """
        Generates an SQL query from a natural language query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/generate_query.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#generate_query)
        """

    async def get_agent_memory(
        self, **kwargs: Unpack[GetAgentMemoryRequestTypeDef]
    ) -> GetAgentMemoryResponseTypeDef:
        """
        Gets the sessions stored in the memory of the agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/get_agent_memory.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#get_agent_memory)
        """

    async def get_invocation_step(
        self, **kwargs: Unpack[GetInvocationStepRequestTypeDef]
    ) -> GetInvocationStepResponseTypeDef:
        """
        Retrieves the details of a specific invocation step within an invocation in a
        session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/get_invocation_step.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#get_invocation_step)
        """

    async def get_session(
        self, **kwargs: Unpack[GetSessionRequestTypeDef]
    ) -> GetSessionResponseTypeDef:
        """
        Retrieves details about a specific session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/get_session.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#get_session)
        """

    async def invoke_agent(
        self, **kwargs: Unpack[InvokeAgentRequestTypeDef]
    ) -> InvokeAgentResponseTypeDef:
        """
        Sends a prompt for the agent to process and respond to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/invoke_agent.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#invoke_agent)
        """

    async def invoke_flow(
        self, **kwargs: Unpack[InvokeFlowRequestTypeDef]
    ) -> InvokeFlowResponseTypeDef:
        """
        Invokes an alias of a flow to run the inputs that you specify and return the
        output of each node as a stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/invoke_flow.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#invoke_flow)
        """

    async def invoke_inline_agent(
        self, **kwargs: Unpack[InvokeInlineAgentRequestTypeDef]
    ) -> InvokeInlineAgentResponseTypeDef:
        """
        Invokes an inline Amazon Bedrock agent using the configurations you provide
        with the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/invoke_inline_agent.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#invoke_inline_agent)
        """

    async def list_invocation_steps(
        self, **kwargs: Unpack[ListInvocationStepsRequestTypeDef]
    ) -> ListInvocationStepsResponseTypeDef:
        """
        Lists all invocation steps associated with a session and optionally, an
        invocation within the session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/list_invocation_steps.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#list_invocation_steps)
        """

    async def list_invocations(
        self, **kwargs: Unpack[ListInvocationsRequestTypeDef]
    ) -> ListInvocationsResponseTypeDef:
        """
        Lists all invocations associated with a specific session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/list_invocations.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#list_invocations)
        """

    async def list_sessions(
        self, **kwargs: Unpack[ListSessionsRequestTypeDef]
    ) -> ListSessionsResponseTypeDef:
        """
        Lists all sessions in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/list_sessions.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#list_sessions)
        """

    async def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List all the tags for the resource you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/list_tags_for_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#list_tags_for_resource)
        """

    async def optimize_prompt(
        self, **kwargs: Unpack[OptimizePromptRequestTypeDef]
    ) -> OptimizePromptResponseTypeDef:
        """
        Optimizes a prompt for the task that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/optimize_prompt.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#optimize_prompt)
        """

    async def put_invocation_step(
        self, **kwargs: Unpack[PutInvocationStepRequestTypeDef]
    ) -> PutInvocationStepResponseTypeDef:
        """
        Add an invocation step to an invocation in a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/put_invocation_step.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#put_invocation_step)
        """

    async def rerank(self, **kwargs: Unpack[RerankRequestTypeDef]) -> RerankResponseTypeDef:
        """
        Reranks the relevance of sources based on queries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/rerank.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#rerank)
        """

    async def retrieve(self, **kwargs: Unpack[RetrieveRequestTypeDef]) -> RetrieveResponseTypeDef:
        """
        Queries a knowledge base and retrieves information from it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/retrieve.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#retrieve)
        """

    async def retrieve_and_generate(
        self, **kwargs: Unpack[RetrieveAndGenerateRequestTypeDef]
    ) -> RetrieveAndGenerateResponseTypeDef:
        """
        Queries a knowledge base and generates responses based on the retrieved results
        and using the specified foundation model or <a
        href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">inference
        profile</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/retrieve_and_generate.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#retrieve_and_generate)
        """

    async def retrieve_and_generate_stream(
        self, **kwargs: Unpack[RetrieveAndGenerateStreamRequestTypeDef]
    ) -> RetrieveAndGenerateStreamResponseTypeDef:
        """
        Queries a knowledge base and generates responses based on the retrieved
        results, with output in streaming format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/retrieve_and_generate_stream.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#retrieve_and_generate_stream)
        """

    async def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associate tags with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/tag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#tag_resource)
        """

    async def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Remove tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/untag_resource.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#untag_resource)
        """

    async def update_session(
        self, **kwargs: Unpack[UpdateSessionRequestTypeDef]
    ) -> UpdateSessionResponseTypeDef:
        """
        Updates the metadata or encryption settings of a session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/update_session.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#update_session)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_agent_memory"]
    ) -> GetAgentMemoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_invocation_steps"]
    ) -> ListInvocationStepsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_invocations"]
    ) -> ListInvocationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sessions"]
    ) -> ListSessionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["rerank"]
    ) -> RerankPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["retrieve"]
    ) -> RetrievePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/client/get_paginator.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/#get_paginator)
        """

    async def __aenter__(self) -> Self:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/)
        """

    async def __aexit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_bedrock_agent_runtime/client/)
        """
