# Copyright (c) pallets/itsdangerous
# Copyright (C) 2024 Graz University of Technology.
# copy pasted over to invenio-base because of removable from itsdangerous with version 2.1.0
# https://raw.githubusercontent.com/pallets/itsdangerous/refs/tags/2.0.1/tests/test_itsdangerous/test_serializer.py

# Original license
# Copyright 2011 Pallets

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:

# 1.  Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.

# 2.  Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.

# 3.  Neither the name of the copyright holder nor the names of its
#     contributors may be used to endorse or promote products derived from
#     this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


import hashlib
import pickle
from functools import partial
from io import BytesIO, StringIO
from typing import IO, Any, Union, cast, overload

import pytest
from itsdangerous.exc import BadPayload, BadSignature
from itsdangerous.serializer import Serializer
from itsdangerous.signer import Signer, _lazy_sha1


@overload
def coerce_str(ref: str, s: str) -> str: ...


@overload
def coerce_str(ref: bytes, s: str) -> bytes: ...


def coerce_str(ref: Union[str, bytes], s: str) -> Union[str, bytes]:
    if isinstance(ref, bytes):
        return s.encode("utf8")

    return s


class TestSerializer:
    @pytest.fixture(params=(Serializer, partial(Serializer, serializer=pickle)))
    def serializer_factory(self, request):
        return partial(request.param, secret_key="secret_key")

    @pytest.fixture()
    def serializer(self, serializer_factory):
        return serializer_factory()

    @pytest.fixture()
    def value(self):
        return {"id": 42}

    @pytest.mark.parametrize(
        "value", (None, True, "str", "text", [1, 2, 3], {"id": 42})
    )
    def test_serializer(self, serializer: Serializer, value: Any):
        assert serializer.loads(serializer.dumps(value)) == value

    @pytest.mark.parametrize(
        "transform",
        (
            lambda s: s.upper(),
            lambda s: s + coerce_str(s, "a"),
            lambda s: coerce_str(s, "a") + s[1:],
            lambda s: s.replace(coerce_str(s, "."), coerce_str(s, "")),
        ),
    )
    def test_changed_value(self, serializer: Serializer, value: Any, transform):
        signed = serializer.dumps(value)
        assert serializer.loads(signed) == value
        changed = transform(signed)

        with pytest.raises(BadSignature):
            serializer.loads(changed)

    def test_bad_signature_exception(self, serializer: Serializer, value: Any):
        bad_signed = serializer.dumps(value)[:-1]

        with pytest.raises(BadSignature) as exc_info:
            serializer.loads(bad_signed)

        payload = cast(bytes, exc_info.value.payload)
        assert serializer.load_payload(payload) == value

    def test_bad_payload_exception(self, serializer: Serializer, value: Any):
        original = serializer.dumps(value)
        payload = original.rsplit(coerce_str(original, "."), 1)[0]  # type: ignore
        bad = serializer.make_signer().sign(payload[:-1])

        with pytest.raises(BadPayload) as exc_info:
            serializer.loads(bad)

        assert exc_info.value.original_error is not None

    def test_loads_unsafe(self, serializer: Serializer, value: Any):
        signed = serializer.dumps(value)
        assert serializer.loads_unsafe(signed) == (True, value)

        bad_signed = signed[:-1]
        assert serializer.loads_unsafe(bad_signed) == (False, value)

        payload = signed.rsplit(coerce_str(signed, "."), 1)[0]  # type: ignore
        bad_payload = serializer.make_signer().sign(payload[:-1])[:-1]
        assert serializer.loads_unsafe(bad_payload) == (False, None)

        class BadUnsign(serializer.signer):  # type: ignore
            def unsign(self, signed_value, *args, **kwargs):
                try:
                    return super().unsign(signed_value, *args, **kwargs)
                except BadSignature as e:
                    e.payload = None
                    raise

        serializer.signer = BadUnsign
        assert serializer.loads_unsafe(bad_signed) == (False, None)

    def test_file(self, serializer: Serializer, value: Any):
        f = cast(
            IO, BytesIO() if isinstance(serializer.dumps(value), bytes) else StringIO()
        )
        serializer.dump(value, f)
        f.seek(0)
        assert serializer.load(f) == value
        f.seek(0)
        assert serializer.load_unsafe(f) == (True, value)

    def test_alt_salt(self, serializer: Serializer, value: Any):
        signed = serializer.dumps(value, salt="other")

        with pytest.raises(BadSignature):
            serializer.loads(signed)

        assert serializer.loads(signed, salt="other") == value

    def test_signer_cls(self, serializer_factory, serializer: Serializer, value: Any):
        class Other(serializer.signer):  # type: ignore
            default_key_derivation = "hmac"

        other = serializer_factory(signer=Other)
        assert other.loads(other.dumps(value)) == value
        assert other.dumps(value) != serializer.dumps(value)

    def test_signer_kwargs(
        self, serializer_factory, serializer: Serializer, value: Any
    ):
        other = serializer_factory(signer_kwargs={"key_derivation": "hmac"})
        assert other.loads(other.dumps(value)) == value
        assert other.dumps("value") != serializer.dumps("value")

    def test_serializer_kwargs(self, serializer_factory):
        serializer = serializer_factory(serializer_kwargs={"skipkeys": True})

        try:
            serializer.serializer.dumps(None, skipkeys=True)
        except TypeError:
            return

        assert serializer.loads(serializer.dumps({(): 1})) == {}

    def test_fallback_signers(self, serializer_factory, value: Any):
        serializer = serializer_factory(signer_kwargs={"digest_method": hashlib.sha256})
        signed = serializer.dumps(value)

        fallback_serializer = serializer_factory(
            signer_kwargs={"digest_method": hashlib.sha1},
            fallback_signers=[{"digest_method": hashlib.sha256}],
        )

        assert fallback_serializer.loads(signed) == value

    def test_iter_unsigners(self, serializer: Serializer, serializer_factory):
        class Signer256(serializer.signer):  # type: ignore
            default_digest_method = hashlib.sha256

        serializer = serializer_factory(
            secret_key="secret_key",
            fallback_signers=[
                {"digest_method": hashlib.sha256},
                (Signer, {"digest_method": hashlib.sha256}),
                Signer256,
            ],
        )

        unsigners = serializer.iter_unsigners()
        assert next(unsigners).digest_method == _lazy_sha1

        for signer in unsigners:
            assert signer.digest_method == hashlib.sha256


def test_digests():
    factory = partial(Serializer, secret_key="dev key", salt="dev salt")
    default_value = factory(signer_kwargs={}).dumps([42])
    sha1_value = factory(signer_kwargs={"digest_method": hashlib.sha1}).dumps([42])
    sha512_value = factory(signer_kwargs={"digest_method": hashlib.sha512}).dumps([42])
    assert default_value == sha1_value
    assert sha1_value == "[42].-9cNi0CxsSB3hZPNCe9a2eEs1ZM"
    assert sha512_value == (
        "[42].MKCz_0nXQqv7wKpfHZcRtJRmpT2T5uvs9YQsJEhJimqxc"
        "9bCLxG31QzS5uC8OVBI1i6jyOLAFNoKaF5ckO9L5Q"
    )
