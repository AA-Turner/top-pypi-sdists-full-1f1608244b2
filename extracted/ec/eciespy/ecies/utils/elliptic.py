from coincurve import PrivateKey, PublicKey
from coincurve.utils import get_valid_secret
from typing_extensions import deprecated

from ..consts import ETH_PUBLIC_KEY_LENGTH
from .hash import derive_key
from .hex import decode_hex


@deprecated("Use `ecies.keys.PrivateKey` instead")
def generate_key() -> PrivateKey:
    """
    Generate a random coincurve.PrivateKey`

    Returns
    -------
    coincurve.PrivateKey
        A secp256k1 key
    """
    return PrivateKey(get_valid_secret())


@deprecated("Use `ecies.keys.PublicKey.from_hex` instead")
def hex2pk(pk_hex: str) -> PublicKey:
    """
    Convert public key hex to `coincurve.PublicKey`
    The hex should be 65 bytes (uncompressed) or 33 bytes (compressed), but ethereum public key has 64 bytes.
    `0x04` will be appended if it's an ethereum public key.

    Parameters
    ----------
    pk_hex: str
        Public key hex string

    Returns
    -------
    coincurve.PublicKey
        A secp256k1 public key

    """
    return PublicKey(convert_eth_public_key(decode_hex(pk_hex)))


@deprecated("Use `ecies.keys.PrivateKey.from_hex` instead")
def hex2sk(sk_hex: str) -> PrivateKey:
    """
    Convert ethereum hex to `coincurve.PrivateKey`

    Parameters
    ----------
    sk_hex: str
        Private key hex string

    Returns
    -------
    coincurve.PrivateKey
        A secp256k1 private key

    """
    return PrivateKey(decode_hex(sk_hex))


# private below
@deprecated("Use `ecies.keys.PrivateKey.encapsulate` instead")
def encapsulate(
    private_key: PrivateKey, peer_public_key: PublicKey, is_compressed: bool = False
) -> bytes:
    shared_point = peer_public_key.multiply(private_key.secret)
    master = private_key.public_key.format(is_compressed) + shared_point.format(
        is_compressed
    )
    return derive_key(master)


@deprecated("Use `ecies.keys.PrivateKey.decapsulate` instead")
def decapsulate(
    public_key: PublicKey, peer_private_key: PrivateKey, is_compressed: bool = False
) -> bytes:
    shared_point = public_key.multiply(peer_private_key.secret)
    master = public_key.format(is_compressed) + shared_point.format(is_compressed)
    return derive_key(master)


def convert_eth_public_key(data: bytes):
    if len(data) == ETH_PUBLIC_KEY_LENGTH:
        data = b"\x04" + data
    return data
