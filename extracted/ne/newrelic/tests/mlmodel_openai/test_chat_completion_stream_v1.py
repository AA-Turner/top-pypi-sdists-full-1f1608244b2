# Copyright 2010 New Relic, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import openai
import pytest
from conftest import get_openai_version
from testing_support.fixtures import override_llm_token_callback_settings, reset_core_stats_engine, validate_attributes
from testing_support.ml_testing_utils import (
    add_token_count_to_events,
    disabled_ai_monitoring_record_content_settings,
    disabled_ai_monitoring_settings,
    disabled_ai_monitoring_streaming_settings,
    events_sans_content,
    events_sans_llm_metadata,
    events_with_context_attrs,
    llm_token_count_callback,
    set_trace_info,
)
from testing_support.validators.validate_custom_event import validate_custom_event_count
from testing_support.validators.validate_custom_events import validate_custom_events
from testing_support.validators.validate_transaction_metrics import validate_transaction_metrics

from newrelic.api.background_task import background_task
from newrelic.api.llm_custom_attributes import WithLlmCustomAttributes
from newrelic.api.transaction import add_custom_attribute

# TODO: Once instrumentation support is added for `.with_streaming_response.`
# the validator checks can be uncommented/active.

OPENAI_VERSION = get_openai_version()
SKIP_IF_NO_OPENAI_WITH_STREAMING_RESPONSE = pytest.mark.skipif(
    OPENAI_VERSION < (1, 8), reason="OpenAI does not support .with_streaming_response. until v1.8"
)


_test_openai_chat_completion_messages = (
    {"role": "system", "content": "You are a scientist."},
    {"role": "user", "content": "What is 212 degrees Fahrenheit converted to Celsius?"},
)

chat_completion_recorded_events = [
    (
        {"type": "LlmChatCompletionSummary"},
        {
            "id": None,  # UUID that varies with each run
            "llm.conversation_id": "my-awesome-id",
            "llm.foo": "bar",
            "span_id": None,
            "trace_id": "trace-id",
            "request_id": "f8d0f53b6881c5c0a3698e55f8f410ac",
            "duration": None,  # Response time varies each test run
            "request.model": "gpt-3.5-turbo",
            "response.model": "gpt-3.5-turbo-0613",
            "response.organization": "new-relic-nkmd8b",
            # Usage tokens aren't available when streaming.
            "request.temperature": 0.7,
            "request.max_tokens": 100,
            "response.choices.finish_reason": "stop",
            "response.headers.llmVersion": "2020-10-01",
            "response.headers.ratelimitLimitRequests": 200,
            "response.headers.ratelimitLimitTokens": 40000,
            "response.headers.ratelimitResetTokens": "180ms",
            "response.headers.ratelimitResetRequests": "11m32.334s",
            "response.headers.ratelimitRemainingTokens": 39880,
            "response.headers.ratelimitRemainingRequests": 198,
            "vendor": "openai",
            "ingest_source": "Python",
            "response.number_of_messages": 3,
        },
    ),
    (
        {"type": "LlmChatCompletionMessage"},
        {
            "id": "chatcmpl-8TJ9dS50zgQM7XicE8PLnCyEihRug-0",
            "llm.conversation_id": "my-awesome-id",
            "llm.foo": "bar",
            "request_id": "f8d0f53b6881c5c0a3698e55f8f410ac",
            "span_id": None,
            "trace_id": "trace-id",
            "content": "You are a scientist.",
            "role": "system",
            "completion_id": None,
            "sequence": 0,
            "response.model": "gpt-3.5-turbo-0613",
            "vendor": "openai",
            "ingest_source": "Python",
        },
    ),
    (
        {"type": "LlmChatCompletionMessage"},
        {
            "id": "chatcmpl-8TJ9dS50zgQM7XicE8PLnCyEihRug-1",
            "llm.conversation_id": "my-awesome-id",
            "llm.foo": "bar",
            "request_id": "f8d0f53b6881c5c0a3698e55f8f410ac",
            "span_id": None,
            "trace_id": "trace-id",
            "content": "What is 212 degrees Fahrenheit converted to Celsius?",
            "role": "user",
            "completion_id": None,
            "sequence": 1,
            "response.model": "gpt-3.5-turbo-0613",
            "vendor": "openai",
            "ingest_source": "Python",
        },
    ),
    (
        {"type": "LlmChatCompletionMessage"},
        {
            "id": "chatcmpl-8TJ9dS50zgQM7XicE8PLnCyEihRug-2",
            "llm.conversation_id": "my-awesome-id",
            "llm.foo": "bar",
            "request_id": "f8d0f53b6881c5c0a3698e55f8f410ac",
            "span_id": None,
            "trace_id": "trace-id",
            "content": "212 degrees Fahrenheit is equal to 100 degrees Celsius.",
            "role": "assistant",
            "completion_id": None,
            "sequence": 2,
            "response.model": "gpt-3.5-turbo-0613",
            "vendor": "openai",
            "is_response": True,
            "ingest_source": "Python",
        },
    ),
]


@reset_core_stats_engine()
@validate_custom_events(events_with_context_attrs(chat_completion_recorded_events))
# One summary event, one system message, one user message, and one response message from the assistant
# @validate_custom_event_count(count=4)
@validate_transaction_metrics(
    name="test_chat_completion_stream_v1:test_openai_chat_completion_sync_with_llm_metadata",
    custom_metrics=[(f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1)],
    background_task=True,
)
@validate_attributes("agent", ["llm"])
@background_task()
def test_openai_chat_completion_sync_with_llm_metadata(set_trace_info, sync_openai_client):
    set_trace_info()
    add_custom_attribute("llm.conversation_id", "my-awesome-id")
    add_custom_attribute("llm.foo", "bar")
    add_custom_attribute("non_llm_attr", "python-agent")

    with WithLlmCustomAttributes({"context": "attr"}):
        generator = sync_openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=_test_openai_chat_completion_messages,
            temperature=0.7,
            max_tokens=100,
            stream=True,
        )

        for resp in generator:
            assert resp


@SKIP_IF_NO_OPENAI_WITH_STREAMING_RESPONSE
@reset_core_stats_engine()
@pytest.mark.parametrize("stream_set, stream_val", [(False, None), (True, True), (True, False)])
@validate_transaction_metrics(
    name="test_chat_completion_stream_v1:test_openai_chat_completion_sync_with_llm_metadata_with_streaming_response_lines",
    # custom_metrics=[
    #     (f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1),
    # ],
    background_task=True,
)
# @validate_attributes("agent", ["llm"])
@background_task()
def test_openai_chat_completion_sync_with_llm_metadata_with_streaming_response_lines(
    set_trace_info, sync_openai_client, stream_set, stream_val
):
    set_trace_info()
    add_custom_attribute("llm.conversation_id", "my-awesome-id")
    add_custom_attribute("llm.foo", "bar")
    add_custom_attribute("non_llm_attr", "python-agent")

    create_dict = {
        "model": "gpt-3.5-turbo",
        "messages": _test_openai_chat_completion_messages,
        "temperature": 0.7,
        "max_tokens": 100,
    }
    if stream_set:
        create_dict["stream"] = stream_val

    with sync_openai_client.chat.completions.with_streaming_response.create(**create_dict) as generator:
        for _ in generator.iter_lines():
            pass


@SKIP_IF_NO_OPENAI_WITH_STREAMING_RESPONSE
@reset_core_stats_engine()
@pytest.mark.parametrize("stream_set, stream_val", [(False, None), (True, True), (True, False)])
@validate_transaction_metrics(
    name="test_chat_completion_stream_v1:test_openai_chat_completion_sync_with_llm_metadata_with_streaming_response_bytes",
    # custom_metrics=[
    #     (f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1),
    # ],
    background_task=True,
)
# @validate_attributes("agent", ["llm"])
@background_task()
def test_openai_chat_completion_sync_with_llm_metadata_with_streaming_response_bytes(
    set_trace_info, sync_openai_client, stream_set, stream_val
):
    set_trace_info()
    add_custom_attribute("llm.conversation_id", "my-awesome-id")
    add_custom_attribute("llm.foo", "bar")
    add_custom_attribute("non_llm_attr", "python-agent")

    create_dict = {
        "model": "gpt-3.5-turbo",
        "messages": _test_openai_chat_completion_messages,
        "temperature": 0.7,
        "max_tokens": 100,
    }
    if stream_set:
        create_dict["stream"] = stream_val

    with sync_openai_client.chat.completions.with_streaming_response.create(**create_dict) as generator:
        for _ in generator.iter_bytes():
            pass


@SKIP_IF_NO_OPENAI_WITH_STREAMING_RESPONSE
@reset_core_stats_engine()
@pytest.mark.parametrize("stream_set, stream_val", [(False, None), (True, True), (True, False)])
@validate_transaction_metrics(
    name="test_chat_completion_stream_v1:test_openai_chat_completion_sync_with_llm_metadata_with_streaming_response_text",
    # custom_metrics=[
    #     (f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1),
    # ],
    background_task=True,
)
# @validate_attributes("agent", ["llm"])
@background_task()
def test_openai_chat_completion_sync_with_llm_metadata_with_streaming_response_text(
    set_trace_info, sync_openai_client, stream_set, stream_val
):
    set_trace_info()
    add_custom_attribute("llm.conversation_id", "my-awesome-id")
    add_custom_attribute("llm.foo", "bar")
    add_custom_attribute("non_llm_attr", "python-agent")

    create_dict = {
        "model": "gpt-3.5-turbo",
        "messages": _test_openai_chat_completion_messages,
        "temperature": 0.7,
        "max_tokens": 100,
    }
    if stream_set:
        create_dict["stream"] = stream_val

    with sync_openai_client.chat.completions.with_streaming_response.create(**create_dict) as generator:
        for _ in generator.iter_text():
            pass


@reset_core_stats_engine()
@disabled_ai_monitoring_record_content_settings
@validate_custom_events(events_sans_content(chat_completion_recorded_events))
# One summary event, one system message, one user message, and one response message from the assistant
# @validate_custom_event_count(count=4)
@validate_transaction_metrics(
    name="test_chat_completion_stream_v1:test_openai_chat_completion_sync_no_content",
    custom_metrics=[(f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1)],
    background_task=True,
)
@validate_attributes("agent", ["llm"])
@background_task()
def test_openai_chat_completion_sync_no_content(set_trace_info, sync_openai_client):
    set_trace_info()
    add_custom_attribute("llm.conversation_id", "my-awesome-id")
    add_custom_attribute("llm.foo", "bar")

    generator = sync_openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=_test_openai_chat_completion_messages,
        temperature=0.7,
        max_tokens=100,
        stream=True,
    )

    for resp in generator:
        assert resp


@reset_core_stats_engine()
@override_llm_token_callback_settings(llm_token_count_callback)
@validate_custom_events(add_token_count_to_events(chat_completion_recorded_events))
# One summary event, one system message, one user message, and one response message from the assistant
@validate_custom_event_count(count=4)
@validate_transaction_metrics(
    name="test_chat_completion_stream_v1:test_openai_chat_completion_sync_in_txn_with_llm_metadata_with_token_count",
    custom_metrics=[(f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1)],
    background_task=True,
)
@validate_attributes("agent", ["llm"])
@background_task()
def test_openai_chat_completion_sync_in_txn_with_llm_metadata_with_token_count(set_trace_info, sync_openai_client):
    set_trace_info()
    add_custom_attribute("llm.conversation_id", "my-awesome-id")
    add_custom_attribute("llm.foo", "bar")

    generator = sync_openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=_test_openai_chat_completion_messages,
        temperature=0.7,
        max_tokens=100,
        stream=True,
    )
    for resp in generator:
        assert resp


@reset_core_stats_engine()
@validate_custom_events(events_sans_llm_metadata(chat_completion_recorded_events))
# One summary event, one system message, one user message, and one response message from the assistant
@validate_custom_event_count(count=4)
@validate_transaction_metrics(
    "test_chat_completion_stream_v1:test_openai_chat_completion_sync_no_llm_metadata",
    scoped_metrics=[("Llm/completion/OpenAI/create", 1)],
    rollup_metrics=[("Llm/completion/OpenAI/create", 1)],
    background_task=True,
)
@background_task()
def test_openai_chat_completion_sync_no_llm_metadata(set_trace_info, sync_openai_client):
    set_trace_info()

    generator = sync_openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=_test_openai_chat_completion_messages,
        temperature=0.7,
        max_tokens=100,
        stream=True,
    )

    for resp in generator:
        assert resp


@disabled_ai_monitoring_streaming_settings
@reset_core_stats_engine()
@validate_custom_event_count(count=0)
@validate_transaction_metrics(
    "test_chat_completion_stream_v1:test_openai_chat_completion_sync_ai_monitoring_streaming_disabled",
    custom_metrics=[(f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1)],
    scoped_metrics=[("Llm/completion/OpenAI/create", 1)],
    rollup_metrics=[("Llm/completion/OpenAI/create", 1)],
    background_task=True,
)
@background_task()
def test_openai_chat_completion_sync_ai_monitoring_streaming_disabled(sync_openai_client):
    generator = sync_openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=_test_openai_chat_completion_messages,
        temperature=0.7,
        max_tokens=100,
        stream=True,
    )

    for resp in generator:
        assert resp


@reset_core_stats_engine()
@validate_custom_event_count(count=0)
def test_openai_chat_completion_sync_outside_txn(sync_openai_client):
    generator = sync_openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=_test_openai_chat_completion_messages,
        temperature=0.7,
        max_tokens=100,
        stream=True,
    )

    for resp in generator:
        assert resp


@disabled_ai_monitoring_settings
@reset_core_stats_engine()
@validate_custom_event_count(count=0)
@background_task()
def test_openai_chat_completion_sync_ai_monitoring_disabled(sync_openai_client):
    generator = sync_openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=_test_openai_chat_completion_messages,
        temperature=0.7,
        max_tokens=100,
        stream=True,
    )

    for resp in generator:
        assert resp


@reset_core_stats_engine()
@validate_custom_events(events_sans_llm_metadata(chat_completion_recorded_events))
@validate_custom_event_count(count=4)
@validate_transaction_metrics(
    "test_chat_completion_stream_v1:test_openai_chat_completion_async_no_llm_metadata",
    scoped_metrics=[("Llm/completion/OpenAI/create", 1)],
    rollup_metrics=[("Llm/completion/OpenAI/create", 1)],
    background_task=True,
)
@background_task()
def test_openai_chat_completion_async_no_llm_metadata(loop, set_trace_info, async_openai_client):
    set_trace_info()

    async def consumer():
        generator = await async_openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=_test_openai_chat_completion_messages,
            temperature=0.7,
            max_tokens=100,
            stream=True,
        )
        async for resp in generator:
            assert resp

    loop.run_until_complete(consumer())


@reset_core_stats_engine()
@validate_custom_events(events_with_context_attrs(chat_completion_recorded_events))
@validate_custom_event_count(count=4)
@validate_transaction_metrics(
    "test_chat_completion_stream_v1:test_openai_chat_completion_async_with_llm_metadata",
    scoped_metrics=[("Llm/completion/OpenAI/create", 1)],
    rollup_metrics=[("Llm/completion/OpenAI/create", 1)],
    custom_metrics=[(f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1)],
    background_task=True,
)
@validate_attributes("agent", ["llm"])
@background_task()
def test_openai_chat_completion_async_with_llm_metadata(loop, set_trace_info, async_openai_client):
    set_trace_info()
    add_custom_attribute("llm.conversation_id", "my-awesome-id")
    add_custom_attribute("llm.foo", "bar")
    add_custom_attribute("non_llm_attr", "python-agent")

    async def consumer():
        generator = await async_openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=_test_openai_chat_completion_messages,
            temperature=0.7,
            max_tokens=100,
            stream=True,
        )
        async for resp in generator:
            assert resp

    with WithLlmCustomAttributes({"context": "attr"}):
        loop.run_until_complete(consumer())


@SKIP_IF_NO_OPENAI_WITH_STREAMING_RESPONSE
@reset_core_stats_engine()
@pytest.mark.parametrize("stream_set, stream_val", [(False, None), (True, True), (True, False)])
# @validate_custom_events(chat_completion_recorded_events)
# @validate_custom_event_count(count=4)
@validate_transaction_metrics(
    "test_chat_completion_stream_v1:test_openai_chat_completion_async_with_llm_metadata_with_streaming_response_lines",
    # scoped_metrics=[("Llm/completion/OpenAI/create", 1)],
    # rollup_metrics=[("Llm/completion/OpenAI/create", 1)],
    # custom_metrics=[
    #     (f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1),
    # ],
    background_task=True,
)
# @validate_attributes("agent", ["llm"])
@background_task()
def test_openai_chat_completion_async_with_llm_metadata_with_streaming_response_lines(
    loop, set_trace_info, async_openai_client, stream_set, stream_val
):
    set_trace_info()
    add_custom_attribute("llm.conversation_id", "my-awesome-id")
    add_custom_attribute("llm.foo", "bar")
    add_custom_attribute("non_llm_attr", "python-agent")
    create_dict = {
        "model": "gpt-3.5-turbo",
        "messages": _test_openai_chat_completion_messages,
        "temperature": 0.7,
        "max_tokens": 100,
    }
    if stream_set:
        create_dict["stream"] = stream_val

    async def consumer():
        async with async_openai_client.chat.completions.with_streaming_response.create(**create_dict) as generator:
            async for _ in generator.iter_lines():
                pass

    loop.run_until_complete(consumer())


@SKIP_IF_NO_OPENAI_WITH_STREAMING_RESPONSE
@reset_core_stats_engine()
@pytest.mark.parametrize("stream_set, stream_val", [(False, None), (True, True), (True, False)])
# @validate_custom_events(chat_completion_recorded_events)
# @validate_custom_event_count(count=4)
@validate_transaction_metrics(
    "test_chat_completion_stream_v1:test_openai_chat_completion_async_with_llm_metadata_with_streaming_response_bytes",
    # scoped_metrics=[("Llm/completion/OpenAI/create", 1)],
    # rollup_metrics=[("Llm/completion/OpenAI/create", 1)],
    # custom_metrics=[
    #     (f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1),
    # ],
    background_task=True,
)
# @validate_attributes("agent", ["llm"])
@background_task()
def test_openai_chat_completion_async_with_llm_metadata_with_streaming_response_bytes(
    loop, set_trace_info, async_openai_client, stream_set, stream_val
):
    set_trace_info()
    add_custom_attribute("llm.conversation_id", "my-awesome-id")
    add_custom_attribute("llm.foo", "bar")
    add_custom_attribute("non_llm_attr", "python-agent")
    create_dict = {
        "model": "gpt-3.5-turbo",
        "messages": _test_openai_chat_completion_messages,
        "temperature": 0.7,
        "max_tokens": 100,
    }
    if stream_set:
        create_dict["stream"] = stream_val

    async def consumer():
        async with async_openai_client.chat.completions.with_streaming_response.create(**create_dict) as generator:
            async for _ in generator.iter_bytes():
                pass

    loop.run_until_complete(consumer())


@SKIP_IF_NO_OPENAI_WITH_STREAMING_RESPONSE
@reset_core_stats_engine()
@pytest.mark.parametrize("stream_set, stream_val", [(False, None), (True, True), (True, False)])
# @validate_custom_events(chat_completion_recorded_events)
# @validate_custom_event_count(count=4)
@validate_transaction_metrics(
    "test_chat_completion_stream_v1:test_openai_chat_completion_async_with_llm_metadata_with_streaming_response_text",
    # scoped_metrics=[("Llm/completion/OpenAI/create", 1)],
    # rollup_metrics=[("Llm/completion/OpenAI/create", 1)],
    # custom_metrics=[
    #     (f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1),
    # ],
    background_task=True,
)
# @validate_attributes("agent", ["llm"])
@background_task()
def test_openai_chat_completion_async_with_llm_metadata_with_streaming_response_text(
    loop, set_trace_info, async_openai_client, stream_set, stream_val
):
    set_trace_info()
    add_custom_attribute("llm.conversation_id", "my-awesome-id")
    add_custom_attribute("llm.foo", "bar")
    add_custom_attribute("non_llm_attr", "python-agent")
    create_dict = {
        "model": "gpt-3.5-turbo",
        "messages": _test_openai_chat_completion_messages,
        "temperature": 0.7,
        "max_tokens": 100,
    }
    if stream_set:
        create_dict["stream"] = stream_val

    async def consumer():
        async with async_openai_client.chat.completions.with_streaming_response.create(**create_dict) as generator:
            async for _ in generator.iter_text():
                pass

    loop.run_until_complete(consumer())


@reset_core_stats_engine()
@disabled_ai_monitoring_record_content_settings
@validate_custom_events(events_sans_content(chat_completion_recorded_events))
@validate_custom_event_count(count=4)
@validate_transaction_metrics(
    "test_chat_completion_stream_v1:test_openai_chat_completion_async_no_content",
    scoped_metrics=[("Llm/completion/OpenAI/create", 1)],
    rollup_metrics=[("Llm/completion/OpenAI/create", 1)],
    custom_metrics=[(f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1)],
    background_task=True,
)
@validate_attributes("agent", ["llm"])
@background_task()
def test_openai_chat_completion_async_no_content(loop, set_trace_info, async_openai_client):
    set_trace_info()
    add_custom_attribute("llm.conversation_id", "my-awesome-id")
    add_custom_attribute("llm.foo", "bar")

    async def consumer():
        generator = await async_openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=_test_openai_chat_completion_messages,
            temperature=0.7,
            max_tokens=100,
            stream=True,
        )
        async for resp in generator:
            assert resp

    loop.run_until_complete(consumer())


@reset_core_stats_engine()
@override_llm_token_callback_settings(llm_token_count_callback)
@validate_custom_events(add_token_count_to_events(chat_completion_recorded_events))
# One summary event, one system message, one user message, and one response message from the assistant
# @validate_custom_event_count(count=4)
@validate_transaction_metrics(
    name="test_chat_completion_stream_v1:test_openai_chat_completion_async_with_token_count",
    custom_metrics=[(f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1)],
    background_task=True,
)
@validate_attributes("agent", ["llm"])
@background_task()
def test_openai_chat_completion_async_with_token_count(set_trace_info, loop, async_openai_client):
    set_trace_info()
    add_custom_attribute("llm.conversation_id", "my-awesome-id")
    add_custom_attribute("llm.foo", "bar")

    async def consumer():
        generator = await async_openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=_test_openai_chat_completion_messages,
            temperature=0.7,
            max_tokens=100,
            stream=True,
        )
        async for resp in generator:
            assert resp

    loop.run_until_complete(consumer())


@disabled_ai_monitoring_streaming_settings
@reset_core_stats_engine()
@validate_custom_event_count(count=0)
@validate_transaction_metrics(
    "test_chat_completion_stream_v1:test_openai_chat_completion_async_ai_monitoring_streaming_disabled",
    custom_metrics=[(f"Supportability/Python/ML/OpenAI/{openai.__version__}", 1)],
    scoped_metrics=[("Llm/completion/OpenAI/create", 1)],
    rollup_metrics=[("Llm/completion/OpenAI/create", 1)],
    background_task=True,
)
@background_task()
def test_openai_chat_completion_async_ai_monitoring_streaming_disabled(loop, async_openai_client):
    async def consumer():
        generator = await async_openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=_test_openai_chat_completion_messages,
            temperature=0.7,
            max_tokens=100,
            stream=True,
        )
        async for resp in generator:
            assert resp

    loop.run_until_complete(consumer())


@reset_core_stats_engine()
@validate_custom_event_count(count=0)
def test_openai_chat_completion_async_outside_transaction(loop, async_openai_client):
    async def consumer():
        generator = await async_openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=_test_openai_chat_completion_messages,
            temperature=0.7,
            max_tokens=100,
            stream=True,
        )
        async for resp in generator:
            assert resp

    loop.run_until_complete(consumer())


@disabled_ai_monitoring_settings
@reset_core_stats_engine()
@validate_custom_event_count(count=0)
@background_task()
def test_openai_chat_completion_async_disabled_ai_monitoring_settings(loop, async_openai_client):
    async def consumer():
        generator = await async_openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=_test_openai_chat_completion_messages,
            temperature=0.7,
            max_tokens=100,
            stream=True,
        )
        async for resp in generator:
            assert resp

    loop.run_until_complete(consumer())
