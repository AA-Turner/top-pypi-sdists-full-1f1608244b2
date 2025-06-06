# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.


import re
from binascii import unhexlify
from typing import Optional, List

from amazon_transcribe import AWSCRTEventLoop
from amazon_transcribe.auth import AwsCrtCredentialResolver, CredentialResolver
from amazon_transcribe.endpoints import (
    BaseEndpointResolver,
    _TranscribeRegionEndpointResolver,
)
from amazon_transcribe.eventstream import EventStreamMessageSerializer
from amazon_transcribe.eventstream import EventSigner
from amazon_transcribe.httpsession import AwsCrtHttpSessionManager
from amazon_transcribe.model import (
    AudioStream,
    StartStreamTranscriptionRequest,
    StartStreamTranscriptionEventStream,
)
from amazon_transcribe.serialize import (
    AudioEventSerializer,
    TranscribeStreamingSerializer,
)
from amazon_transcribe.deserialize import TranscribeStreamingResponseParser
from amazon_transcribe.signer import SigV4RequestSigner


class TranscribeStreamingClient:
    """High level client for orchestrating setup and transmission of audio
    streams to Amazon TranscribeStreaming service.

    :param region: An AWS region to use for Amazon Transcribe (e.g. us-east-2)
    :param endpoint_resolver: Optional resolver for client endpoints.
    :param credential_resolver: Optional credential resolver for client.
    """

    def __init__(
        self,
        *,
        region: str,
        endpoint_resolver: Optional[BaseEndpointResolver] = None,
        credential_resolver: Optional[CredentialResolver] = None,
    ):
        if endpoint_resolver is None:
            endpoint_resolver = _TranscribeRegionEndpointResolver()
        self._endpoint_resolver = endpoint_resolver
        self.service_name = "transcribe"
        self.region = region
        self._event_signer = EventSigner(self.service_name, self.region)
        self._eventloop = AWSCRTEventLoop().bootstrap
        if credential_resolver is None:
            credential_resolver = AwsCrtCredentialResolver(self._eventloop)
        self._credential_resolver = credential_resolver
        self._response_parser = TranscribeStreamingResponseParser()
        self._serializer = TranscribeStreamingSerializer()
        self._session_manager = AwsCrtHttpSessionManager(self._eventloop)

    async def start_stream_transcription(
        self,
        *,
        language_code: str,
        media_sample_rate_hz: int,
        media_encoding: str,
        vocabulary_name: Optional[str] = None,
        vocabulary_names: Optional[List[str]] = None,
        session_id: Optional[str] = None,
        vocab_filter_method: Optional[str] = None,
        vocab_filter_name: Optional[str] = None,
        vocab_filter_names: Optional[List[str]] = None,
        show_speaker_label: Optional[bool] = None,
        enable_channel_identification: Optional[bool] = None,
        number_of_channels: Optional[int] = None,
        enable_partial_results_stabilization: Optional[bool] = None,
        partial_results_stability: Optional[str] = None,
        language_model_name: Optional[str] = None,
        identify_language: Optional[bool] = None,
        preferred_language: Optional[str] = None,
        identify_multiple_languages: Optional[bool] = None,
        language_options: Optional[List[str]] = None,
        pii_entity_types=None,
        content_redaction_type=None,
        content_identification_type=None,
    ) -> StartStreamTranscriptionEventStream:
        """Coordinate transcription settings and start stream.

        Pay careful attention to language_code and media_sample_rate_hz configurations.
        Incorrect setups may lead to streams hanging indefinitely.
        More info on constraints can be found here:
        https://docs.aws.amazon.com/transcribe/latest/dg/streaming.html

        The service processes audio chunks for this operation in realtime, if
        the audio chunks provided are not coming from a realtime source (e.g. a
        pre-recorded file) the audio chunks should be rate limited to match the
        appropriate realtime bitrate for the stream. Failure to send the audio
        chunks in realtime can lead to signing issues for audio streams longer
        than 5 minutes.

        :param language_code:
            Indicates the source language used in the input audio stream. Set to
            None if identify_languages or identify_multiple_languages is set to True
        :param media_sample_rate_hz:
            The sample rate, in Hertz, of the input audio. We suggest that you
            use 8000 Hz for low quality audio and 16000 Hz for high quality audio.
        :param media_encoding:
            The encoding used for the input audio.
        :param vocabulary_name:
            The name of the vocabulary to use when processing the transcription job.
        :param vocabulary_names:
            When using language identification, the name of the vocabulary to
            use for each language option.
        :param session_id:
            A identifier for the transcription session. Use this parameter when you
            want to retry a session. If you don't provide a session ID,
            Amazon Transcribe will generate one for you and return it in the response.
        :param vocab_filter_method:
            The manner in which you use your vocabulary filter to filter words in
            your transcript. See Transcribe Streaming API docs for more info.
        :param vocab_filter_name:
            The name of the vocabulary filter you've created that is unique to
            your AWS account. Provide the name in this field to successfully
            use it in a stream. Use only when identify_languages and
            identify_multiple_languages are set to None
        :param vocab_filter_names:
            The name of the vocabulary filters to use for each language option. To be
            used in conjunction with identify_languages and identify_multiple_languages
        :param show_speaker_label:
            When true, enables speaker identification in your real-time stream.
        :param enable_channel_identification:
            When true, instructs Amazon Transcribe to process each audio channel
            separately and then merge the transcription output of each channel
            into a single transcription. Amazon Transcribe also produces a
            transcription of each item. An item includes the start time, end time,
            and any alternative transcriptions. You can't set both ShowSpeakerLabel
            and EnableChannelIdentification in the same request. If you set both,
            your request returns a BadRequestException.
        :param number_of_channels:
            The number of channels that are in your audio stream.
        :param enable_partial_results_stabilization:
            When true, instructs Amazon Transcribe to present transcription results
            that have the partial results stabilized. Normally, any word or phrase
            from one partial result can change in a subsequent partial result. With
            partial results stabilization enabled, only the last few words of one
            partial result can change in another partial result.
        :param partial_results_stability
            You can use this field to set the stability level of the transcription
            results. A higher stability level means that the transcription results
            are less likely to change. Higher stability levels can come with lower
            overall transcription accuracy. Defaults to "high" if not set explicitly.
        :param language_model_name:
            The name of the language model you want to use.
        :param identify_language:
            if True, the language of the stream will be automatically detected. Set
            language_code to None and provide at least two language_options when
            identify_language is True.
        :param preferred_language:
            Adding a preferred language can speed up the language identification
            process, which is helpful for short audio clips.
        :param identify_multiple_languages:
            If true, all languages spoken in the stream are identified. A multilingual
            transcripts is created your transcript using each identified language.
            You must also provide at least two language_options and set
            language_code to None
        :param language_options:
            A list of possible language to use when identify_language or
            identify_multiple_languages is set to True. Note that not all languages
             supported by Transcribe are supported for multiple language identification
        :param pii_entity_types: what entity types to identify or redact when using either
        content_redaction_type or content_identification_type. This includes names, bank
        account details, etc. See https://docs.aws.amazon.com/transcribe/latest/dg/pii-redaction-stream.html
        for a full list. When this is not explicitly set, the default is "ALL"
        :param content_redaction_type: What kinds of content to redact. Currently, the
            only supported value is "PII". When set, personally identifiable information
            in the transcript will be redacted and replaced by "[PII]". This cannot be
            set together with content_identification_type
        :param content_identification_type: What kinds of content to identify. Currently, the
            only supported value is "PII". When set, personally identifiable information
            in the transcript will be detected and an additional "entities" field will be
            returned in the transcript object. This cannot be set together with
            content_redaction_type
        """
        transcribe_streaming_request = StartStreamTranscriptionRequest(
            language_code,
            media_sample_rate_hz,
            media_encoding,
            vocabulary_name,
            vocabulary_names,
            session_id,
            vocab_filter_method,
            vocab_filter_name,
            vocab_filter_names,
            show_speaker_label,
            enable_channel_identification,
            number_of_channels,
            enable_partial_results_stabilization,
            partial_results_stability,
            language_model_name,
            identify_language,
            preferred_language,
            identify_multiple_languages,
            language_options,
            pii_entity_types,
            content_redaction_type,
            content_identification_type,
        )
        endpoint = await self._endpoint_resolver.resolve(self.region)

        request = self._serializer.serialize_start_stream_transcription_request(
            endpoint=endpoint,
            request_shape=transcribe_streaming_request,
        ).prepare()

        creds = await self._credential_resolver.get_credentials()
        signer = SigV4RequestSigner("transcribe", self.region)
        signed_request = signer.sign(request, creds)

        response = await self._session_manager.make_request(
            signed_request.uri,
            method=signed_request.method,
            headers=signed_request.headers.as_list(),
            body=signed_request.body,
        )
        resolved_response = await response.resolve_response()

        status_code = resolved_response.status_code
        if status_code >= 400:
            # We need to close before we can consume the body or this will hang
            signed_request.body.close()
            body_bytes = await response.consume_body()
            raise self._response_parser.parse_exception(resolved_response, body_bytes)
        elif status_code != 200:
            raise RuntimeError("Unexpected status code encountered: %s" % status_code)

        parsed_response = (
            self._response_parser.parse_start_stream_transcription_response(
                resolved_response,
                response,
            )
        )

        # The audio stream is returned as output because it requires
        # the signature from the initial HTTP request to be useable
        audio_stream = self._create_audio_stream(signed_request)
        return StartStreamTranscriptionEventStream(audio_stream, parsed_response)

    def _create_audio_stream(self, signed_request):
        initial_signature = self._extract_signature(signed_request)
        return AudioStream(
            input_stream=signed_request.body,
            event_serializer=AudioEventSerializer(),
            eventstream_serializer=EventStreamMessageSerializer(),
            event_signer=self._event_signer,
            initial_signature=initial_signature,
            credential_resolver=self._credential_resolver,
        )

    def _extract_signature(self, signed_request):
        auth = signed_request.headers.get("Authorization", "")
        auth = re.split("Signature=", auth)[-1]
        return unhexlify(auth)
