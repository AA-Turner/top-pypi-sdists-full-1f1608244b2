# -*- coding: utf-8 -*-
"""
Call class - along with its list class
"""

from plivo.base import (ListResponseObject, PlivoResource,
                        PlivoResourceInterface)
from plivo.utils import to_param_dict
from plivo.utils.validators import *


class Call(PlivoResource):
    _name = 'Call'
    _identifier_string = 'call_uuid'

    def update(self,
               legs=None,
               aleg_url=None,
               aleg_method=None,
               bleg_url=None,
               bleg_method=None):
        return self.client.calls.update(self.id,
                                        **to_param_dict(self.update, locals()))

    def get(self):
        return self.client.calls.get(self.id)

    def record(self,
               time_limit=None,
               file_format=None,
               transcription_type=None,
               transcription_url=None,
               transcription_method=None,
               callback_url=None,
               callback_method=None,
               record_channel_type=None):
        return self.client.calls.record(self.id,
                                        **to_param_dict(self.record, locals()))

    def start_recording(self,
                        time_limit=None,
                        file_format=None,
                        transcription_type=None,
                        transcription_url=None,
                        transcription_method=None,
                        callback_url=None,
                        callback_method=None):
        return self.client.calls.start_recording(self.id,
                                                 **to_param_dict(
                                                     self.start_recording,
                                                     locals()))

    def stop_recording(self):
        return self.client.calls.stop_recording(self.id)

    def play(self, urls, length=None, legs=None, loop=None, mix=None):
        return self.client.calls.play(self.id,
                                      **to_param_dict(self.start_playing,
                                                      locals()))

    def start_playing(self, urls, length=None, legs=None, loop=None, mix=None):
        return self.client.calls.play(self.id,
                                      **to_param_dict(self.start_playing,
                                                      locals()))

    def stop_playing(self):
        return self.client.calls.stop_playing(self.id)

    def speak(self,
              call_uuid,
              text,
              voice=None,
              language=None,
              legs=None,
              loop=None,
              mix=None,
              type=None, is_voice_request=True):
        return self.client.calls.speak(self.id,
                                       **to_param_dict(self.start_playing,
                                                       locals()))

    def start_speaking(self,
                       text,
                       voice=None,
                       language=None,
                       legs=None,
                       loop=None,
                       mix=None,
                       type=None):
        return self.client.calls.start_speaking(self.id,
                                                **to_param_dict(
                                                    self.start_playing,
                                                    locals()))

    def stop_speaking(self):
        return self.client.calls.stop_speaking(self.id)

    def send_digits(self, digits, leg):
        return self.client.calls.send_digits(self.id,
                                             **to_param_dict(
                                                 self.start_playing, locals()))

    def delete(self):
        return self.client.calls.delete(self.id)

    def hangup(self):
        return self.client.calls.delete(self.id)

    def start_stream(self,
                     service_url,
                     bidirectional=None,
                     audio_track=None,
                     stream_timeout=None,
                     status_callback_url=None,
                     status_callback_method=None,
                     content_type=None,
                     extra_headers=None):
        return self.client.calls.start_stream(self.id,
                                              **to_param_dict(
                                                  self.start_stream(),
                                                  locals()))

    def delete_specific_stream(self,
                               stream_id):
        return self.client.calls.delete_specific_stream(self.id,
                                                        **to_param_dict(
                                                            self.delete_specific_stream(),
                                                            locals()))

    def delete_all_streams(self):
        return self.client.calls.delete_all_streams(self.id,
                                                    **to_param_dict(
                                                        self.delete_all_streams(),
                                                        locals()))

    def get_details_of_specific_stream(self,
                                       stream_id):
        return self.client.calls.get_details_of_specific_stream(self.id,
                                                                **to_param_dict(
                                                                    self.get_details_of_specific_stream(),
                                                                    locals()))

    def get_all_streams(self):
        return self.client.calls.get_all_streams(self.id,
                                                 **to_param_dict(
                                                     self.get_details_of_specific_stream(),
                                                     locals()))


class Calls(PlivoResourceInterface):
    _resource_type = Call

    @validate_args(
        from_=[is_phonenumber()],
        to_=[is_iterable(of_type(six.text_type), sep='<')],
        answer_url=[is_url()],
        answer_method=[optional(of_type(six.text_type))],
        hangup_url=[optional(is_url())],
        hangup_method=[optional(of_type(six.text_type))],
        fallback_url=[optional(is_url())],
        fallback_method=[optional(of_type(six.text_type))],
        ring_url=[optional(is_url())],
        ring_method=[optional(of_type(six.text_type))],
        machine_detection_url=[optional(is_url())],
        machine_detection_method=[optional(of_type(six.text_type))],
        caller_name=[optional(of_type(six.text_type))],
        error_if_parent_not_found=[optional(of_type_exact(bool))],
        parent_call_uuid=[optional(of_type(six.text_type))],
        ring_timeout=[
            optional(of_type(*six.integer_types)),
            check(
                lambda ring_timeout: 0 <= ring_timeout,
                message='0 <= ring_timeout')
        ],
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def create(self,
               from_,
               to_,
               answer_url,
               answer_method='POST',
               ring_url=None,
               ring_method='POST',
               hangup_url=None,
               hangup_method='POST',
               fallback_url=None,
               fallback_method='POST',
               caller_name=None,
               send_digits=None,
               send_on_preanswer=None,
               time_limit=None,
               hangup_on_ring=None,
               machine_detection=None,
               machine_detection_time=5000,
               machine_detection_url=None,
               machine_detection_method='POST',
               sip_headers=None,
               ring_timeout=120,
               parent_call_uuid=None,
               error_if_parent_not_found=False,
               callback_url=None,
               callback_method=None):
        if from_ in to_.split('<'):
            raise ValidationError('src and destination cannot overlap')
        return self.client.request('POST', ('Call',), to_param_dict(self.create, locals()), is_voice_request=True)

    @validate_args(
        subaccount=[optional(is_subaccount())],
        call_direction=[
            optional(of_type(six.text_type), is_in(('inbound', 'outbound')))
        ],
        from_number=[optional(is_phonenumber())],
        to_number=[optional(is_iterable(of_type(six.text_type), sep='<'))],
        limit=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda limit: 0 < limit <= 20, '0 < limit <= 20')))
        ],
        offset=[
            optional(
                all_of(
                    of_type(*six.integer_types),
                    check(lambda offset: 0 <= offset, '0 <= offset')))
        ],
        parent_call_uuid=[
            optional(of_type(six.text_type))
        ],
        hangup_cause_code=[
            optional(
                all_of(
                    of_type(*six.integer_types)))
        ],
        hangup_source=[
            optional(of_type(six.text_type))
        ],
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def list(self,
             subaccount=None,
             call_direction=None,
             call_direction__lt=None,
             call_direction__lte=None,
             call_direction__gt=None,
             call_direction__gte=None,
             end_time__lt=None,
             end_time__lte=None,
             end_time__gt=None,
             end_time__gte=None,
             end_time=None,
             from_number=None,
             to_number=None,
             bill_duration=None,
             limit=20,
             offset=0,
             status=None,
             parent_call_uuid=None,
             hangup_cause_code=None,
             hangup_source=None,
             callback_url=None,
             callback_method=None
             ):
        # Adding if else block because if we are fetching response without callback_url then response will be of type
        # ListResponseObject, if passing callback_url then will be of type
        # {'api_id': '94722e88-ae7c-11ec-b52e-0242ac11000a', 'message': 'async api spawned'}
        if callback_url:
            return self.client.request(
                'GET',
                ('Call',),
                to_param_dict(self.list, locals()),
                is_voice_request=True
            )
        else:
            return self.client.request(
                'GET',
                ('Call',),
                to_param_dict(self.list, locals()),
                response_type=ListResponseObject,
                is_voice_request=True
            )

    @validate_args(
        call_uuid=[of_type(six.text_type)],
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def get(self,
            call_uuid,
            callback_url=None,
            callback_method=None):
        return self.client.request('GET', ('Call', call_uuid), to_param_dict(self.get, locals()), is_voice_request=True)

    @validate_args(
        call_uuid=[of_type(six.text_type)],
        legs=[of_type(six.text_type),
              is_in(('aleg', 'bleg', 'both'))],
        aleg_url=[optional(is_url())],
        aleg_method=[optional(of_type(six.text_type))],
        bleg_method=[optional(of_type(six.text_type))],
        bleg_url=[optional(is_url())],
    )
    def update(self,
               call_uuid,
               legs=None,
               aleg_url=None,
               aleg_method=None,
               bleg_url=None,
               bleg_method=None,
               callback_url=None,
               callback_method=None):
        return self.client.request('POST', ('Call', call_uuid),
                                   to_param_dict(self.update, locals()), is_voice_request=True)

    @validate_args(
        call_uuid=[of_type(six.text_type)],
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def transfer(self,
                 call_uuid,
                 legs=None,
                 aleg_url=None,
                 aleg_method=None,
                 bleg_url=None,
                 bleg_method=None,
                 callback_url=None,
                 callback_method=None):
        return self.update(
            call_uuid,
            legs=legs,
            aleg_method=aleg_method,
            aleg_url=aleg_url,
            bleg_url=bleg_url,
            bleg_method=bleg_method,
            callback_url=callback_url,
            callback_method=callback_method)

    @validate_args(call_uuid=[of_type(six.text_type)])
    def record(self,
               call_uuid,
               time_limit=None,
               file_format=None,
               transcription_type=None,
               transcription_url=None,
               transcription_method=None,
               callback_url=None,
               callback_method=None,
               record_channel_type=None):
        return self.start_recording(**to_param_dict(self.start_recording,
                                                    locals()))

    @validate_args(call_uuid=[of_type(six.text_type)])
    def start_recording(self,
                        call_uuid,
                        time_limit=None,
                        file_format=None,
                        transcription_type=None,
                        transcription_url=None,
                        transcription_method=None,
                        callback_url=None,
                        callback_method=None,
                        record_channel_type=None):
        return self.client.request('POST', ('Call', call_uuid, 'Record'),
                                   to_param_dict(self.start_recording,
                                                 locals()), is_voice_request=True)

    def record_stop(self, call_uuid, callback_url=None, callback_method=None):
        return self.client.calls.stop_recording(call_uuid, callback_url, callback_method)

    @validate_args(call_uuid=[of_type(six.text_type)],
                   callback_url=[optional(is_url())],
                   callback_method=[optional(of_type(six.text_type))]
                   )
    def stop_recording(self, call_uuid, callback_url, callback_method):
        return self.client.request('DELETE', ('Call', call_uuid, 'Record'),
                                   to_param_dict(self.stop_recording, locals()), is_voice_request=True)

    @validate_args(call_uuid=[of_type(six.text_type)])
    def play(self,
             call_uuid,
             urls,
             length=None,
             legs=None,
             loop=None,
             mix=None,
             callback_url=None,
             callback_method=None):
        return self.start_playing(**to_param_dict(self.play, locals()))

    @validate_args(call_uuid=[of_type(six.text_type)])
    def start_playing(self,
                      call_uuid,
                      urls,
                      length=None,
                      legs=None,
                      loop=None,
                      mix=None,
                      callback_url=None,
                      callback_method=None):
        return self.client.request('POST', ('Call', call_uuid, 'Play'),
                                   to_param_dict(self.play, locals()), is_voice_request=True)

    def play_stop(self, call_uuid, callback_url=None, callback_method=None):
        return self.client.calls.stop_playing(call_uuid, callback_url, callback_method)

    @validate_args(call_uuid=[of_type(six.text_type)],
                   callback_url=[optional(is_url())],
                   callback_method=[optional(of_type(six.text_type))]
                   )
    def stop_playing(self, call_uuid, callback_url=None, callback_method=None):
        return self.client.request('DELETE', ('Call', call_uuid, 'Play'), to_param_dict(self.stop_playing, locals()),
                                   is_voice_request=True)

    @validate_args(call_uuid=[of_type(six.text_type)],
                   callback_url=[optional(is_url())],
                   callback_method=[optional(of_type(six.text_type))],
                   )
    def speak(self,
              call_uuid,
              text,
              voice=None,
              language=None,
              legs=None,
              loop=None,
              mix=None,
              callback_url=None,
              callback_method=None,
              type=None,
              ):
        return self.start_speaking(call_uuid, text, voice, language, legs,
                                   loop, mix, callback_url, callback_method, type)

    @validate_args(call_uuid=[of_type(six.text_type)])
    def start_speaking(self,
                       call_uuid,
                       text,
                       voice=None,
                       language=None,
                       legs=None,
                       loop=None,
                       mix=None,
                       callback_url=None,
                       callback_method=None,
                       type=None
                       ):
        return self.client.request('POST', ('Call', call_uuid, 'Speak'),
                                   to_param_dict(self.start_speaking,
                                                 locals()), is_voice_request=True)

    @validate_args(call_uuid=[of_type(six.text_type)])
    def stop_speaking(self, call_uuid, callback_url=None, callback_method=None):
        return self.client.request('DELETE', ('Call', call_uuid, 'Speak'), to_param_dict(self.stop_speaking, locals()),
                                   is_voice_request=True)

    @validate_args(
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))]
    )
    def speak_stop(self, call_uuid, callback_url=None, callback_method=None):
        return self.client.calls.stop_speaking(call_uuid, callback_url, callback_method)

    @validate_args(call_uuid=[of_type(six.text_type)],
                   callback_url=[optional(is_url())],
                   callback_method=[optional(of_type(six.text_type))],
                   )
    def send_digits(self, call_uuid, digits, leg=None, callback_url=None, callback_method=None):
        return self.client.request('POST', ('Call', call_uuid, 'DTMF'),
                                   to_param_dict(self.send_digits, locals()), is_voice_request=True)

    @validate_args(
        call_uuid=[of_type(six.text_type)],
        callback_url=[optional(is_url())],
        callback_method=[optional(of_type(six.text_type))],
    )
    def delete(self,
               call_uuid,
               callback_url=None,
               callback_method=None):
        return self.client.request('DELETE', ('Call', call_uuid), to_param_dict(self.delete, locals()),
                                   is_voice_request=True)

    @validate_args(call_uuid=[of_type(six.text_type)])
    def hangup(self, call_uuid):
        return self.client.calls.delete(call_uuid)

    def cancel(self, request_uuid):
        return self.client.request('DELETE', ('Request', request_uuid), is_voice_request=True)

    def live_call_list_ids(self, limit=None, offset=None):
        return self.client.live_calls.list_ids(limit, offset)

    def live_call_get(self, _id):
        return self.client.live_calls.get(_id)

    def queued_call_list_ids(self, limit=None, offset=None):
        return self.client.queued_calls.list_ids(limit, offset)

    def queued_call_get(self, _id):
        return self.client.queued_calls.get(_id)

    @validate_args(
        call_uuid=[of_type(six.text_type)],
        service_url=[of_type(six.text_type)]
    )
    def start_stream(self,
                     call_uuid,
                     service_url,
                     bidirectional=None,
                     audio_track=None,
                     stream_timeout=None,
                     status_callback_url=None,
                     status_callback_method=None,
                     content_type=None,
                     extra_headers=None,
                     cx_bot=None):
        return self.client.request('POST', ('Call', call_uuid, 'Stream'),
                                   to_param_dict(self.start_stream,
                                                 locals()), is_voice_request=True)

    @validate_args(
        call_uuid=[of_type(six.text_type)],
        stream_id=[of_type(six.text_type)]
    )
    def delete_specific_stream(self,
                               call_uuid,
                               stream_id):
        return self.client.request('DELETE', ('Call', call_uuid, 'Stream', stream_id),
                                   to_param_dict(self.delete_specific_stream,
                                                 locals()), is_voice_request=True)

    @validate_args(
        call_uuid=[of_type(six.text_type)]
    )
    def delete_all_streams(self,
                           call_uuid):
        return self.client.request('DELETE', ('Call', call_uuid, 'Stream'),
                                   to_param_dict(self.delete_all_streams,
                                                 locals()), is_voice_request=True)

    @validate_args(
        call_uuid=[of_type(six.text_type)],
        stream_id=[of_type(six.text_type)]
    )
    def get_details_of_specific_stream(self,
                                       call_uuid,
                                       stream_id):
        return self.client.request('GET', ('Call', call_uuid, 'Stream', stream_id), is_voice_request=True)

    @validate_args(
        call_uuid=[of_type(six.text_type)]
    )
    def get_all_streams(self,
                        call_uuid):
        return self.client.request('GET', ('Call', call_uuid, 'Stream'), is_voice_request=True)

