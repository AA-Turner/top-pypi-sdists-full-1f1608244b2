# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dialogue_input import DialogueInput
from ..types.model_settings_response_model import ModelSettingsResponseModel
from ..types.pronunciation_dictionary_version_locator import PronunciationDictionaryVersionLocator
from .raw_client import AsyncRawTextToDialogueClient, RawTextToDialogueClient
from .types.text_to_dialogue_convert_request_output_format import TextToDialogueConvertRequestOutputFormat
from .types.text_to_dialogue_stream_request_output_format import TextToDialogueStreamRequestOutputFormat

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TextToDialogueClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTextToDialogueClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTextToDialogueClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTextToDialogueClient
        """
        return self._raw_client

    def convert(
        self,
        *,
        inputs: typing.Sequence[DialogueInput],
        output_format: typing.Optional[TextToDialogueConvertRequestOutputFormat] = None,
        model_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[ModelSettingsResponseModel] = OMIT,
        pronunciation_dictionary_locators: typing.Optional[
            typing.Sequence[PronunciationDictionaryVersionLocator]
        ] = OMIT,
        seed: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        <Warning>Eleven v3 API access is currently not publicly available, but will be soon.</Warning><br/>Converts a list of text and voice ID pairs into speech (dialogue) and returns audio.

        Parameters
        ----------
        inputs : typing.Sequence[DialogueInput]
            A list of dialogue inputs, each containing text and a voice ID which will be converted into speech.

        output_format : typing.Optional[TextToDialogueConvertRequestOutputFormat]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        settings : typing.Optional[ModelSettingsResponseModel]
            Settings controlling the dialogue generation.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The generated audio file

        Examples
        --------
        from elevenlabs import DialogueInput, ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.text_to_dialogue.convert(
            inputs=[
                DialogueInput(
                    text="Knock knock",
                    voice_id="JBFqnCBsd6RMkjVDRZzb",
                ),
                DialogueInput(
                    text="Who is there?",
                    voice_id="Aw4FAjKCGjjNkVhN1Xmq",
                ),
            ],
        )
        """
        with self._raw_client.convert(
            inputs=inputs,
            output_format=output_format,
            model_id=model_id,
            settings=settings,
            pronunciation_dictionary_locators=pronunciation_dictionary_locators,
            seed=seed,
            request_options=request_options,
        ) as r:
            yield from r.data

    def stream(
        self,
        *,
        inputs: typing.Sequence[DialogueInput],
        output_format: typing.Optional[TextToDialogueStreamRequestOutputFormat] = None,
        model_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[ModelSettingsResponseModel] = OMIT,
        pronunciation_dictionary_locators: typing.Optional[
            typing.Sequence[PronunciationDictionaryVersionLocator]
        ] = OMIT,
        seed: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        <Warning>Eleven v3 API access is currently not publicly available, but will be soon.</Warning><br/>Converts a list of text and voice ID pairs into speech (dialogue) and returns an audio stream.

        Parameters
        ----------
        inputs : typing.Sequence[DialogueInput]
            A list of dialogue inputs, each containing text and a voice ID which will be converted into speech.

        output_format : typing.Optional[TextToDialogueStreamRequestOutputFormat]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        settings : typing.Optional[ModelSettingsResponseModel]
            Settings controlling the dialogue generation.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Streaming audio data

        Examples
        --------
        from elevenlabs import DialogueInput, ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.text_to_dialogue.stream(
            inputs=[
                DialogueInput(
                    text="Knock knock",
                    voice_id="JBFqnCBsd6RMkjVDRZzb",
                ),
                DialogueInput(
                    text="Who is there?",
                    voice_id="Aw4FAjKCGjjNkVhN1Xmq",
                ),
            ],
        )
        """
        with self._raw_client.stream(
            inputs=inputs,
            output_format=output_format,
            model_id=model_id,
            settings=settings,
            pronunciation_dictionary_locators=pronunciation_dictionary_locators,
            seed=seed,
            request_options=request_options,
        ) as r:
            yield from r.data


class AsyncTextToDialogueClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTextToDialogueClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTextToDialogueClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTextToDialogueClient
        """
        return self._raw_client

    async def convert(
        self,
        *,
        inputs: typing.Sequence[DialogueInput],
        output_format: typing.Optional[TextToDialogueConvertRequestOutputFormat] = None,
        model_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[ModelSettingsResponseModel] = OMIT,
        pronunciation_dictionary_locators: typing.Optional[
            typing.Sequence[PronunciationDictionaryVersionLocator]
        ] = OMIT,
        seed: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        <Warning>Eleven v3 API access is currently not publicly available, but will be soon.</Warning><br/>Converts a list of text and voice ID pairs into speech (dialogue) and returns audio.

        Parameters
        ----------
        inputs : typing.Sequence[DialogueInput]
            A list of dialogue inputs, each containing text and a voice ID which will be converted into speech.

        output_format : typing.Optional[TextToDialogueConvertRequestOutputFormat]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        settings : typing.Optional[ModelSettingsResponseModel]
            Settings controlling the dialogue generation.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The generated audio file

        Examples
        --------
        import asyncio

        from elevenlabs import AsyncElevenLabs, DialogueInput

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.text_to_dialogue.convert(
                inputs=[
                    DialogueInput(
                        text="Knock knock",
                        voice_id="JBFqnCBsd6RMkjVDRZzb",
                    ),
                    DialogueInput(
                        text="Who is there?",
                        voice_id="Aw4FAjKCGjjNkVhN1Xmq",
                    ),
                ],
            )


        asyncio.run(main())
        """
        async with self._raw_client.convert(
            inputs=inputs,
            output_format=output_format,
            model_id=model_id,
            settings=settings,
            pronunciation_dictionary_locators=pronunciation_dictionary_locators,
            seed=seed,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def stream(
        self,
        *,
        inputs: typing.Sequence[DialogueInput],
        output_format: typing.Optional[TextToDialogueStreamRequestOutputFormat] = None,
        model_id: typing.Optional[str] = OMIT,
        settings: typing.Optional[ModelSettingsResponseModel] = OMIT,
        pronunciation_dictionary_locators: typing.Optional[
            typing.Sequence[PronunciationDictionaryVersionLocator]
        ] = OMIT,
        seed: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        <Warning>Eleven v3 API access is currently not publicly available, but will be soon.</Warning><br/>Converts a list of text and voice ID pairs into speech (dialogue) and returns an audio stream.

        Parameters
        ----------
        inputs : typing.Sequence[DialogueInput]
            A list of dialogue inputs, each containing text and a voice ID which will be converted into speech.

        output_format : typing.Optional[TextToDialogueStreamRequestOutputFormat]
            Output format of the generated audio. Formatted as codec_sample_rate_bitrate. So an mp3 with 22.05kHz sample rate at 32kbs is represented as mp3_22050_32. MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM with 44.1kHz sample rate requires you to be subscribed to Pro tier or above. Note that the μ-law format (sometimes written mu-law, often approximated as u-law) is commonly used for Twilio audio inputs.

        model_id : typing.Optional[str]
            Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for text to speech, you can check this using the can_do_text_to_speech property.

        settings : typing.Optional[ModelSettingsResponseModel]
            Settings controlling the dialogue generation.

        pronunciation_dictionary_locators : typing.Optional[typing.Sequence[PronunciationDictionaryVersionLocator]]
            A list of pronunciation dictionary locators (id, version_id) to be applied to the text. They will be applied in order. You may have up to 3 locators per request

        seed : typing.Optional[int]
            If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result. Determinism is not guaranteed. Must be integer between 0 and 4294967295.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Streaming audio data

        Examples
        --------
        import asyncio

        from elevenlabs import AsyncElevenLabs, DialogueInput

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.text_to_dialogue.stream(
                inputs=[
                    DialogueInput(
                        text="Knock knock",
                        voice_id="JBFqnCBsd6RMkjVDRZzb",
                    ),
                    DialogueInput(
                        text="Who is there?",
                        voice_id="Aw4FAjKCGjjNkVhN1Xmq",
                    ),
                ],
            )


        asyncio.run(main())
        """
        async with self._raw_client.stream(
            inputs=inputs,
            output_format=output_format,
            model_id=model_id,
            settings=settings,
            pronunciation_dictionary_locators=pronunciation_dictionary_locators,
            seed=seed,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk
