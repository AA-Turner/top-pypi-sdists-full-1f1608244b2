"""
Type annotations for sqs service ServiceResource.

[Documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from aiobotocore.session import get_session

    from types_aiobotocore_sqs.service_resource import SQSServiceResource
    import types_aiobotocore_sqs.service_resource as sqs_resources

    session = get_session()
    async with session.resource("sqs") as resource:
        resource: SQSServiceResource

        my_message: sqs_resources.Message = resource.Message(...)
        my_queue: sqs_resources.Queue = resource.Queue(...)
```
"""

from __future__ import annotations

import sys
from typing import NoReturn

from aioboto3.resources.base import AIOBoto3ServiceResource
from aioboto3.resources.collection import AIOResourceCollection

from .client import SQSClient
from .literals import MessageSystemAttributeNameType, QueueAttributeNameType
from .type_defs import (
    AddPermissionRequestQueueAddPermissionTypeDef,
    ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef,
    ChangeMessageVisibilityBatchResultTypeDef,
    ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef,
    CreateQueueRequestServiceResourceCreateQueueTypeDef,
    DeleteMessageBatchRequestQueueDeleteMessagesTypeDef,
    DeleteMessageBatchResultTypeDef,
    GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef,
    MessageAttributeValueOutputTypeDef,
    ReceiveMessageRequestQueueReceiveMessagesTypeDef,
    RemovePermissionRequestQueueRemovePermissionTypeDef,
    SendMessageBatchRequestQueueSendMessagesTypeDef,
    SendMessageBatchResultTypeDef,
    SendMessageRequestQueueSendMessageTypeDef,
    SendMessageResultTypeDef,
    SetQueueAttributesRequestQueueSetAttributesTypeDef,
)

try:
    from boto3.resources.base import ResourceMeta
except ImportError:
    from builtins import object as ResourceMeta  # type: ignore[assignment]
if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import AsyncIterator, Awaitable, Sequence
else:
    from typing import AsyncIterator, Awaitable, Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack


__all__ = (
    "Message",
    "Queue",
    "QueueDeadLetterSourceQueuesCollection",
    "SQSServiceResource",
    "ServiceResourceQueuesCollection",
)


class ServiceResourceQueuesCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/queues.html#SQS.ServiceResource.queues)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#serviceresourcequeuescollection)
    """

    def all(self) -> ServiceResourceQueuesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/queues.html#SQS.ServiceResource.all)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#serviceresourcequeuescollection)
        """

    def filter(  # type: ignore[override]
        self, *, QueueNamePrefix: str = ..., NextToken: str = ..., MaxResults: int = ...
    ) -> ServiceResourceQueuesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/queues.html#filter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#serviceresourcequeuescollection)
        """

    def limit(self, count: int) -> ServiceResourceQueuesCollection:
        """
        Return at most this many Queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/queues.html#limit)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#serviceresourcequeuescollection)
        """

    def page_size(self, count: int) -> ServiceResourceQueuesCollection:
        """
        Fetch at most this many Queues per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/queues.html#page_size)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#serviceresourcequeuescollection)
        """

    def pages(  # type: ignore[override]
        self,
    ) -> AsyncIterator[List[Queue]]:
        """
        A generator which yields pages of Queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/queues.html#pages)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#serviceresourcequeuescollection)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/queues.html#__iter__)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#serviceresourcequeuescollection)
        """

    def __aiter__(self) -> AsyncIterator[Queue]:
        """
        A generator which yields Queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/queues.html#__iter__)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#serviceresourcequeuescollection)
        """


class QueueDeadLetterSourceQueuesCollection(AIOResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/dead_letter_source_queues.html#SQS.Queue.dead_letter_source_queues)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuedead_letter_source_queues)
    """

    def all(self) -> QueueDeadLetterSourceQueuesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/dead_letter_source_queues.html#SQS.Queue.all)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuedead_letter_source_queues)
        """

    def filter(  # type: ignore[override]
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> QueueDeadLetterSourceQueuesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/dead_letter_source_queues.html#filter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuedead_letter_source_queues)
        """

    def limit(self, count: int) -> QueueDeadLetterSourceQueuesCollection:
        """
        Return at most this many Queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/dead_letter_source_queues.html#limit)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuedead_letter_source_queues)
        """

    def page_size(self, count: int) -> QueueDeadLetterSourceQueuesCollection:
        """
        Fetch at most this many Queues per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/dead_letter_source_queues.html#page_size)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuedead_letter_source_queues)
        """

    def pages(  # type: ignore[override]
        self,
    ) -> AsyncIterator[List[Queue]]:
        """
        A generator which yields pages of Queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/dead_letter_source_queues.html#pages)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuedead_letter_source_queues)
        """

    def __iter__(self) -> NoReturn:
        """
        A generator which yields Queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/dead_letter_source_queues.html#__iter__)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuedead_letter_source_queues)
        """

    def __aiter__(self) -> AsyncIterator[Queue]:
        """
        A generator which yields Queues.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/dead_letter_source_queues.html#__iter__)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuedead_letter_source_queues)
        """


class Message(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/message/index.html#SQS.Message)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#message)
    """

    queue_url: str
    receipt_handle: str
    message_id: Awaitable[str]
    md5_of_body: Awaitable[str]
    body: Awaitable[str]
    attributes: Awaitable[Dict[MessageSystemAttributeNameType, str]]
    md5_of_message_attributes: Awaitable[str]
    message_attributes: Awaitable[Dict[str, MessageAttributeValueOutputTypeDef]]
    meta: SQSResourceMeta  # type: ignore[override]

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/message/get_available_subresources.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#messageget_available_subresources-method)
        """

    async def change_visibility(
        self, **kwargs: Unpack[ChangeMessageVisibilityRequestMessageChangeVisibilityTypeDef]
    ) -> None:
        """
        Changes the visibility timeout of a specified message in a queue to a new value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/message/change_visibility.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#messagechange_visibility-method)
        """

    async def delete(self) -> None:
        """
        Deletes the specified message from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/message/delete.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#messagedelete-method)
        """

    async def Queue(self) -> _Queue:
        """
        Creates a Queue resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/message/Queue.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#messagequeue-method)
        """


_Message = Message


class Queue(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/index.html#SQS.Queue)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queue)
    """

    url: str
    dead_letter_source_queues: QueueDeadLetterSourceQueuesCollection
    attributes: Awaitable[Dict[QueueAttributeNameType, str]]
    meta: SQSResourceMeta  # type: ignore[override]

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/get_available_subresources.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queueget_available_subresources-method)
        """

    async def add_permission(
        self, **kwargs: Unpack[AddPermissionRequestQueueAddPermissionTypeDef]
    ) -> None:
        """
        Adds a permission to a queue for a specific <a
        href="https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#P">principal</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/add_permission.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queueadd_permission-method)
        """

    async def change_message_visibility_batch(
        self,
        **kwargs: Unpack[
            ChangeMessageVisibilityBatchRequestQueueChangeMessageVisibilityBatchTypeDef
        ],
    ) -> ChangeMessageVisibilityBatchResultTypeDef:
        """
        Changes the visibility timeout of multiple messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/change_message_visibility_batch.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuechange_message_visibility_batch-method)
        """

    async def delete(self) -> None:
        """
        Deletes the queue specified by the <code>QueueUrl</code>, regardless of the
        queue's contents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/delete.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuedelete-method)
        """

    async def delete_messages(
        self, **kwargs: Unpack[DeleteMessageBatchRequestQueueDeleteMessagesTypeDef]
    ) -> DeleteMessageBatchResultTypeDef:
        """
        Deletes up to ten messages from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/delete_messages.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuedelete_messages-method)
        """

    async def purge(self) -> None:
        """
        Deletes available messages in a queue (including in-flight messages) specified
        by the <code>QueueURL</code> parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/purge.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuepurge-method)
        """

    async def receive_messages(
        self, **kwargs: Unpack[ReceiveMessageRequestQueueReceiveMessagesTypeDef]
    ) -> List[_Message]:
        """
        Retrieves one or more messages (up to 10), from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/receive_messages.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuereceive_messages-method)
        """

    async def remove_permission(
        self, **kwargs: Unpack[RemovePermissionRequestQueueRemovePermissionTypeDef]
    ) -> None:
        """
        Revokes any permissions in the queue policy that matches the specified
        <code>Label</code> parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/remove_permission.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queueremove_permission-method)
        """

    async def send_message(
        self, **kwargs: Unpack[SendMessageRequestQueueSendMessageTypeDef]
    ) -> SendMessageResultTypeDef:
        """
        Delivers a message to the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/send_message.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuesend_message-method)
        """

    async def send_messages(
        self, **kwargs: Unpack[SendMessageBatchRequestQueueSendMessagesTypeDef]
    ) -> SendMessageBatchResultTypeDef:
        """
        You can use <code>SendMessageBatch</code> to send up to 10 messages to the
        specified queue by assigning either identical or different values to each
        message (or by not assigning values at all).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/send_messages.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuesend_messages-method)
        """

    async def set_attributes(
        self, **kwargs: Unpack[SetQueueAttributesRequestQueueSetAttributesTypeDef]
    ) -> None:
        """
        Sets the value of one or more queue attributes, like a policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/set_attributes.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queueset_attributes-method)
        """

    async def Message(self, receipt_handle: str) -> _Message:
        """
        Creates a Message resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/Message.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuemessage-method)
        """

    async def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/load.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queueload-method)
        """

    async def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/queue/reload.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#queuereload-method)
        """


_Queue = Queue


class SQSResourceMeta(ResourceMeta):
    client: SQSClient  # type: ignore[override]


class SQSServiceResource(AIOBoto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/index.html)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/)
    """

    meta: SQSResourceMeta  # type: ignore[override]
    queues: ServiceResourceQueuesCollection

    async def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/get_available_subresources.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#sqsserviceresourceget_available_subresources-method)
        """

    async def create_queue(
        self, **kwargs: Unpack[CreateQueueRequestServiceResourceCreateQueueTypeDef]
    ) -> _Queue:
        """
        Creates a new standard or FIFO queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/create_queue.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#sqsserviceresourcecreate_queue-method)
        """

    async def get_queue_by_name(
        self, **kwargs: Unpack[GetQueueUrlRequestServiceResourceGetQueueByNameTypeDef]
    ) -> _Queue:
        """
        The <code>GetQueueUrl</code> API returns the URL of an existing Amazon SQS
        queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/get_queue_by_name.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#sqsserviceresourceget_queue_by_name-method)
        """

    async def Message(self, queue_url: str, receipt_handle: str) -> _Message:
        """
        Creates a Message resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/Message.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#sqsserviceresourcemessage-method)
        """

    async def Queue(self, url: str) -> _Queue:
        """
        Creates a Queue resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/service-resource/Queue.html)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_sqs/service_resource/#sqsserviceresourcequeue-method)
        """
