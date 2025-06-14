from __future__ import absolute_import, division, print_function

import pytest

import telnyx

CALL_CONTROL_ID = "AgDIxmoRX6QMuaIj_uXRXnPAXP0QlNfXczRrZvZakpWxBlpw48KyZQ=="


def create_dial():
    return telnyx.Call.create(
        connection_id="1111111111222222223", to="+12223334444", from_="+12223330000"
    )


class TestCall(object):
    def test_is_creatable(self, request_mock):
        resource = create_dial()
        request_mock.assert_requested("post", "/v2/calls")
        assert isinstance(resource, telnyx.Call)

    def test_can_call_reject(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.reject(cause="USER_BUSY")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/reject" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_reject(self, request_mock):
        resource = create_dial()
        resource.create_reject(CALL_CONTROL_ID, cause="USER_BUSY")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/reject" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_answer(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.answer()
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/answer" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_answer(self, request_mock):
        resource = create_dial()
        resource.create_answer(CALL_CONTROL_ID)
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/answer" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_hangup(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.hangup()
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/hangup" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_hangup(self, request_mock):
        resource = create_dial()
        resource.create_hangup(CALL_CONTROL_ID)
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/hangup" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_bridge(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.bridge(call_control_id=CALL_CONTROL_ID)
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/bridge" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_bridge(self, request_mock):
        resource = create_dial()
        resource.create_bridge(CALL_CONTROL_ID, call_control_id=CALL_CONTROL_ID)
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/bridge" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_fork_start(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.fork_start()
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/fork_start" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_fork_start(self, request_mock):
        resource = create_dial()
        resource.create_fork_start(CALL_CONTROL_ID)
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/fork_start" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_fork_stop(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.fork_stop()
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/fork_stop" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_fork_stop(self, request_mock):
        resource = create_dial()
        resource.create_fork_stop(CALL_CONTROL_ID)
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/fork_stop" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_gather_using_audio(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.gather_using_audio(audio_url="http://telnyx-audio.url")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/gather_using_audio" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_gather_using_audio(self, request_mock):
        resource = create_dial()
        resource.create_gather_using_audio(
            CALL_CONTROL_ID, audio_url="http://telnyx-audio.url"
        )
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/gather_using_audio" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_gather_using_speak(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.gather_using_speak(
            language="en-US", voice="female", payload="Hello from the other side"
        )
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/gather_using_speak" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_gather_using_speak(self, request_mock):
        resource = create_dial()
        resource.create_gather_using_speak(
            CALL_CONTROL_ID,
            language="en-US",
            voice="female",
            payload="Hello from the other side",
        )
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/gather_using_speak" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_gather_stop(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.gather_stop()
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/gather_stop" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_gather_stop(self, request_mock):
        resource = create_dial()
        resource.create_gather_stop(CALL_CONTROL_ID)
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/gather_stop" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_playback_start(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.playback_start(audio_url="http://telnyx-audio.url")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/playback_start" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_playback_start(self, request_mock):
        resource = create_dial()
        resource.create_playback_start(
            CALL_CONTROL_ID, audio_url="http://telnyx-audio.url"
        )
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/playback_start" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_playback_stop(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.playback_stop()
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/playback_stop" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_playback_stop(self, request_mock):
        resource = create_dial()
        resource.create_playback_stop(CALL_CONTROL_ID)
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/playback_stop" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_record_pause(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.record_pause()
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/record_pause" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_record_pause(self, request_mock):
        resource = create_dial()
        resource.create_record_pause(CALL_CONTROL_ID)
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/record_pause" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_record_resume(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.record_resume()
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/record_resume" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_record_resume(self, request_mock):
        resource = create_dial()
        resource.create_record_resume(CALL_CONTROL_ID)
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/record_resume" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_record_start(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.record_start(channels="single", format="mp3")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/record_start" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_record_start(self, request_mock):
        resource = create_dial()
        resource.create_record_start(CALL_CONTROL_ID, channels="single", format="mp3")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/record_start" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_record_stop(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.record_stop()
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/record_stop" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_record_stop(self, request_mock):
        resource = create_dial()
        resource.create_record_stop(CALL_CONTROL_ID)
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/record_stop" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_refer(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.refer(sip_address="sip:username@sip.non-telnyx-address.com")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/refer" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_refer(self, request_mock):
        resource = create_dial()
        resource.create_refer(
            CALL_CONTROL_ID, sip_address="sip:username@sip.non-telnyx-address.com"
        )
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/refer" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_send_dtmf(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.send_dtmf(digits="1www2WABCDw9")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/send_dtmf" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_send_dtmf(self, request_mock):
        resource = create_dial()
        resource.create_send_dtmf(CALL_CONTROL_ID, digits="1www2WABCDw9")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/send_dtmf" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_speak(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.speak(
            language="en-US", voice="female", payload="Hello from the other side"
        )
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/speak" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_speak(self, request_mock):
        resource = create_dial()
        resource.create_speak(
            CALL_CONTROL_ID,
            language="en-US",
            voice="female",
            payload="Hello from the other side",
        )
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/speak" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_can_call_transcription_start(self, request_mock):
        resource = telnyx.Call()
        resource.call_control_id = CALL_CONTROL_ID
        resource.transcription_start(language="en")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/transcription_start" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    @pytest.mark.skip(reason="Prism mock 500 invalid response")
    def test_can_call_calls_transcription_start(self, request_mock):
        resource = telnyx.Call.create_transcription_start(
            CALL_CONTROL_ID, language="en"
        )
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/transcription_start" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.telnyx_object.TelnyxObject)

    def test_can_call_transcription_stop(self, request_mock):
        resource = telnyx.Call()
        resource.call_control_id = CALL_CONTROL_ID
        resource.transcription_stop()
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/transcription_stop" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_transcription_stop(self, request_mock):
        resource = telnyx.Call.create_transcription_stop(CALL_CONTROL_ID)
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/transcription_stop" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.telnyx_object.TelnyxObject)

    def test_can_call_transfer(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.transfer(to="+11111222222")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/transfer" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_transfer(self, request_mock):
        resource = create_dial()
        resource.create_transfer(CALL_CONTROL_ID, to="+11111222222")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/transfer" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_enqueue(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.enqueue("a_queue")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/enqueue" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_enqueue(self, request_mock):
        resource = create_dial()
        resource.create_enqueue(CALL_CONTROL_ID, queue_name="a_queue")
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/enqueue" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_leave_queue(self, request_mock):
        resource = create_dial()
        resource.call_control_id = CALL_CONTROL_ID
        resource.leave_queue()
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/leave_queue" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)

    def test_can_call_calls_leave_queue(self, request_mock):
        resource = create_dial()
        resource.create_leave_queue(CALL_CONTROL_ID)
        request_mock.assert_requested(
            "post", "/v2/calls/%s/actions/leave_queue" % CALL_CONTROL_ID
        )
        assert isinstance(resource, telnyx.Call)
