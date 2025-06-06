from __future__ import annotations
from typing import Dict, Optional, Tuple


class Curve:
    r"""Representation of an elliptic curve.

    Defines a group with the arithmetic operations of point addition and scalar multiplication.
    Currently only curves defined via the equation :math:`y^2 \equiv x^3 + ax + b \pmod{p}` are
    supported.

    Attributes:
        |  name (str): The name of the curve
        |  p (int): The value of :math:`p` in the curve equation.
        |  a (int): The value of :math:`a` in the curve equation.
        |  b (int): The value of :math:`b` in the curve equation.
        |  q (int): The order of the base point of the curve.
        |  oid (bytes): The object identifier of the curve.
    """

    _oid_lookup: Dict[
        bytes, Curve
    ] = {}  # a lookup table for getting curve instances by their object identifier

    def __init__(
        self,
        name: str,
        p: int,
        a: int,
        b: int,
        q: int,
        gx: int,
        gy: int,
        oid: Optional[bytes] = None,
    ) -> None:
        r"""Initialize the parameters of an elliptic curve.

        WARNING: Do not generate your own parameters unless you know what you are doing or you could
        generate a curve severely less secure than you think. Even then, consider using a
        standardized curve for the sake of interoperability.

        Currently only curves defined via the equation :math:`y^2 \equiv x^3 + ax + b \pmod{p}` are
        supported.

        Args:
            |  name (string): The name of the curve
            |  p (int): The value of :math:`p` in the curve equation.
            |  a (int): The value of :math:`a` in the curve equation.
            |  b (int): The value of :math:`b` in the curve equation.
            |  q (int): The order of the base point of the curve.
            |  gx (int): The x coordinate of the base point of the curve.
            |  gy (int): The y coordinate of the base point of the curve.
            |  oid (bytes): The object identifier of the curve.
        """
        self.name = name
        self.p = p
        self.a = a
        self.b = b
        self.q = q
        self.gx = gx
        self.gy = gy
        self.oid = oid

        if oid is not None:
            self._oid_lookup[oid] = self

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def get_curve_by_oid(cls, oid: bytes) -> Optional[Curve]:
        r"""Get a curve via its object identifier.

        Args:
            oid (bytes): The object identifier for the curve.

        Returns:
            Curve | None: The curve corresponding to the object identifier. If the identifier does
            not correspond to a supported curve :code:`None` is returned.

        """
        return cls._oid_lookup.get(oid, None)

    def is_point_on_curve(self, point: Tuple[int, int]) -> bool:
        r"""Check if a point lies on this curve.

        The check is done by evaluating the curve equation :math:`y^2 \equiv x^3 + ax + b \pmod{p}`
        at the given point :math:`(x,y)` with this curve's domain parameters :math:`(a, b, p)`. If
        the congruence holds, then the point lies on this curve.

        Args:
            point (int, int): A tuple representing the point :math:`P` as an :math:`(x, y)` coordinate
            pair.

        Returns:
            bool: :code:`True` if the point lies on this curve, otherwise :code:`False`.
        """
        (
            x,
            y,
        ) = point
        left = y * y
        right = (x * x * x) + (self.a * x) + self.b
        return (left - right) % self.p == 0

    def evaluate(self, x: int) -> int:
        r"""Evaluate the elliptic curve polynomial at 'x'

        Args:
            x (int): The position to evaluate the polynomial at

        Returns:
            int: the value of :math:`(x^3 + ax + b) \bmod{p}`
        """
        return (x**3 + self.a * x + self.b) % self.p

    @property
    def G(self):  # type: ignore
        """The base point of the curve.

        For the purposes of ECDSA this point is multiplied by a private key to obtain the
        corresponding public key. Make a property to avoid cyclic dependency of Point on Curve
        (a point lies on a curve) and Curve on Point (curves have a base point).
        """
        from .point import Point

        return Point(self.gx, self.gy, self)


# see https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-186-draft.pdf
# Setion 4.2.1 "Weierstrass Curves" for params
P192 = Curve(
    "P192",
    6277101735386680763835789423207666416083908700390324961279,
    -3,
    2455155546008943817740293915197451784769108058161191238065,
    6277101735386680763835789423176059013767194773182842284081,
    602046282375688656758213480587526111916698976636884684818,
    174050332293622031404857552280219410364023488927386650641,
    b"\x2a\x86\x48\xce\x3d\x03\x01\x01",
)
P224 = Curve(
    "P224",
    26959946667150639794667015087019630673557916260026308143510066298881,
    -3,
    18958286285566608000408668544493926415504680968679321075787234672564,
    26959946667150639794667015087019625940457807714424391721682722368061,
    19277929113566293071110308034699488026831934219452440156649784352033,
    19926808758034470970197974370888749184205991990603949537637343198772,
    b"\x2b\x81\x04\x00\x21",
)
P256 = Curve(
    "P256",
    115792089210356248762697446949407573530086143415290314195533631308867097853951,
    -3,
    41058363725152142129326129780047268409114441015993725554835256314039467401291,
    115792089210356248762697446949407573529996955224135760342422259061068512044369,
    48439561293906451759052585252797914202762949526041747995844080717082404635286,
    36134250956749795798585127919587881956611106672985015071877198253568414405109,
    b"\x2a\x86\x48\xce\x3d\x03\x01\x07",
)
P384 = Curve(
    "P384",
    int(
        "39402006196394479212279040100143613805079739270465446667948293404245721771496870329047266"
        "088258938001861606973112319"
    ),
    -3,
    int(
        "27580193559959705877849011840389048093056905856361568521428707301988689241309860865136260"
        "764883745107765439761230575"
    ),
    int(
        "39402006196394479212279040100143613805079739270465446667946905279627659399113263569398956"
        "308152294913554433653942643"
    ),
    int(
        "26247035095799689268623156744566981891852923491109213387815615900925518854738050089022388"
        "053975719786650872476732087"
    ),
    int(
        "83257109614890299855467512895201081792878530488613155947092059024805031998844192244386437"
        "60392947333078086511627871"
    ),
    b"\x2b\x81\x04\x00\x22",
)
P521 = Curve(
    "P521",
    int(
        "68647976601306097149819007990813932172694353001433054093944634591855431833976560521225596"
        "40661454554977296311391480858037121987999716643812574028291115057151"
    ),
    -3,
    int(
        "10938490380737342745111123907668055699362075989516837489945863944959531161507350160137087"
        "37573759623248592132296706313309438452531591012912142327488478985984"
    ),
    int(
        "68647976601306097149819007990813932172694353001433054093944634591855431833976553942450577"
        "46333217197532963996371363321113864768612440380340372808892707005449"
    ),
    int(
        "26617408020502170632287687167233609607298591687569731477066713684188029449964278084915450"
        "80627771902352094241225065558662157113545570916814161637315895999846"
    ),
    int(
        "37571800257700204635455072244911836035944551347697624866945677796155444774405563166912344"
        "05012945539562144444537289428522585666729196580810124344277578376784"
    ),
    b"\x2b\x81\x04\x00\x23",
)
W25519 = Curve(
    "W25519",
    0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFED,
    0x2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA984914A144,
    0x7B425ED097B425ED097B425ED097B425ED097B425ED097B4260B5E9C7710C864,
    0x1000000000000000000000000000000014DEF9DEA2F79CD65812631A5CF5D3ED,
    0x2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD245A,
    0x5F51E65E475F794B1FE122D388B72EB36DC2B28192839E4DD6163A5D81312C14,
)
W448 = Curve(
    "W448",
    int(
        "72683872429560689054932380788800453435364136068731806028149019918061232816673077268639638"
        "3698676545930088884461843637361053498018365439"
    ),
    int(
        "48455914953040459369954920525866968956909424045821204018766013278707488544448718179093092"
        "2465784363953392589641229091574035657199637535"
    ),
    int(
        "26919952751689144094419400292148316087171902247678446677092229599281938080249287877273940"
        "1369880202196329216467349495319191685664513904"
    ),
    int(
        "18170968107390172263733095197200113358841034017182951507037254979514600396153958571619575"
        "5291692375963310293709091662304773755859649779"
    ),
    int(
        "48455914953040459369954920525866968956909424045821204018766013278707488544448718179093092"
        "2465784363953392589641229091574035665345629073"
    ),
    int(
        "35529392678556817526412750206378333480897639938771427183188089843516908878696741000293267"
        "3765864550910142774147268105838985595290606362"
    ),
)

# see http://www.secg.org/sec2-v2.pdf for params
secp192k1 = Curve(
    "secp192k1",
    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFEE37,
    0x0,
    0x3,
    0xFFFFFFFFFFFFFFFFFFFFFFFE26F2FC170F69466A74DEFD8D,
    0xDB4FF10EC057E9AE26B07D0280B7F4341DA5D1B1EAE06C7D,
    0x9B2F2F6D9C5628A7844163D015BE86344082AA88D95E2F9D,
    b"\x2b\x81\x04\x00\x1f",
)

secp224k1 = Curve(
    "secp224k1",
    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFE56D,
    0x0,
    0x5,
    0x10000000000000000000000000001DCE8D2EC6184CAF0A971769FB1F7,
    0xA1455B334DF099DF30FC28A169A467E9E47075A90F7E650EB6B7A45C,
    0x7E089FED7FBA344282CAFBD6F7E319F7C0B0BD59E2CA4BDB556D61A5,
    b"\x2b\x81\x04\x00\x20",
)

secp256k1 = Curve(
    "secp256k1",
    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F,
    0x0,
    0x7,
    0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141,
    0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
    0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
    b"\x2b\x81\x04\x00\x0a",
)

# see https://tools.ietf.org/html/rfc5639#section-3.1 for params
brainpoolP160r1 = Curve(
    "brainpoolP160r1",
    0xE95E4A5F737059DC60DFC7AD95B3D8139515620F,
    0x340E7BE2A280EB74E2BE61BADA745D97E8F7C300,
    0x1E589A8595423412134FAA2DBDEC95C8D8675E58,
    0xE95E4A5F737059DC60DF5991D45029409E60FC09,
    0xBED5AF16EA3F6A4F62938C4631EB5AF7BDBCDBC3,
    0x1667CB477A1A8EC338F94741669C976316DA6321,
    b"\x2b\x24\x03\x03\x02\x08\x01\x01\x01",
)

brainpoolP192r1 = Curve(
    "brainpoolP192r1",
    0xC302F41D932A36CDA7A3463093D18DB78FCE476DE1A86297,
    0x6A91174076B1E0E19C39C031FE8685C1CAE040E5C69A28EF,
    0x469A28EF7C28CCA3DC721D044F4496BCCA7EF4146FBF25C9,
    0xC302F41D932A36CDA7A3462F9E9E916B5BE8F1029AC4ACC1,
    0xC0A0647EAAB6A48753B033C56CB0F0900A2F5C4853375FD6,
    0x14B690866ABD5BB88B5F4828C1490002E6773FA2FA299B8F,
    b"\x2b\x24\x03\x03\x02\x08\x01\x01\x03",
)

brainpoolP224r1 = Curve(
    "brainpoolP224r1",
    0xD7C134AA264366862A18302575D1D787B09F075797DA89F57EC8C0FF,
    0x68A5E62CA9CE6C1C299803A6C1530B514E182AD8B0042A59CAD29F43,
    0x2580F63CCFE44138870713B1A92369E33E2135D266DBB372386C400B,
    0xD7C134AA264366862A18302575D0FB98D116BC4B6DDEBCA3A5A7939F,
    0x0D9029AD2C7E5CF4340823B2A87DC68C9E4CE3174C1E6EFDEE12C07D,
    0x58AA56F772C0726F24C6B89E4ECDAC24354B9E99CAA3F6D3761402CD,
    b"\x2b\x24\x03\x03\x02\x08\x01\x01\x05",
)

brainpoolP256r1 = Curve(
    "brainpoolP256r1",
    0xA9FB57DBA1EEA9BC3E660A909D838D726E3BF623D52620282013481D1F6E5377,
    0x7D5A0975FC2C3057EEF67530417AFFE7FB8055C126DC5C6CE94A4B44F330B5D9,
    0x26DC5C6CE94A4B44F330B5D9BBD77CBF958416295CF7E1CE6BCCDC18FF8C07B6,
    0xA9FB57DBA1EEA9BC3E660A909D838D718C397AA3B561A6F7901E0E82974856A7,
    0x8BD2AEB9CB7E57CB2C4B482FFC81B7AFB9DE27E1E3BD23C23A4453BD9ACE3262,
    0x547EF835C3DAC4FD97F8461A14611DC9C27745132DED8E545C1D54C72F046997,
    b"\x2b\x24\x03\x03\x02\x08\x01\x01\x07",
)

brainpoolP320r1 = Curve(
    "brainpoolP320r1",
    0xD35E472036BC4FB7E13C785ED201E065F98FCFA6F6F40DEF4F92B9EC7893EC28FCD412B1F1B32E27,
    0x3EE30B568FBAB0F883CCEBD46D3F3BB8A2A73513F5EB79DA66190EB085FFA9F492F375A97D860EB4,
    0x520883949DFDBC42D3AD198640688A6FE13F41349554B49ACC31DCCD884539816F5EB4AC8FB1F1A6,
    0xD35E472036BC4FB7E13C785ED201E065F98FCFA5B68F12A32D482EC7EE8658E98691555B44C59311,
    0x43BD7E9AFB53D8B85289BCC48EE5BFE6F20137D10A087EB6E7871E2A10A599C710AF8D0D39E20611,
    0x14FDD05545EC1CC8AB4093247F77275E0743FFED117182EAA9C77877AAAC6AC7D35245D1692E8EE1,
    b"\x2b\x24\x03\x03\x02\x08\x01\x01\x09",
)

brainpoolP384r1 = Curve(
    "brainpoolP384r1",
    int(
        "8CB91E82A3386D280F5D6F7E50E641DF152F7109ED5456B412B1DA197FB71123ACD3A729901D1A718747001331"
        "07EC53",
        16,
    ),
    int(
        "7BC382C63D8C150C3C72080ACE05AFA0C2BEA28E4FB22787139165EFBA91F90F8AA5814A503AD4EB04A8C7DD22"
        "CE2826",
        16,
    ),
    int(
        "04A8C7DD22CE28268B39B55416F0447C2FB77DE107DCD2A62E880EA53EEB62D57CB4390295DBC9943AB78696FA"
        "504C11",
        16,
    ),
    int(
        "8CB91E82A3386D280F5D6F7E50E641DF152F7109ED5456B31F166E6CAC0425A7CF3AB6AF6B7FC3103B883202E9"
        "046565",
        16,
    ),
    int(
        "1D1C64F068CF45FFA2A63A81B7C13F6B8847A3E77EF14FE3DB7FCAFE0CBD10E8E826E03436D646AAEF87B2E247"
        "D4AF1E",
        16,
    ),
    int(
        "8ABE1D7520F9C2A45CB1EB8E95CFD55262B70B29FEEC5864E19C054FF99129280E464621779181114282034126"
        "3C5315",
        16,
    ),
    b"\x2b\x24\x03\x03\x02\x08\x01\x01\x0b",
)

brainpoolP512r1 = Curve(
    "brainpoolP512r1",
    int(
        "AADD9DB8DBE9C48B3FD4E6AE33C9FC07CB308DB3B3C9D20ED6639CCA703308717D4D9B009BC66842AECDA12AE6"
        "A380E62881FF2F2D82C68528AA6056583A48F3",
        16,
    ),
    int(
        "7830A3318B603B89E2327145AC234CC594CBDD8D3DF91610A83441CAEA9863BC2DED5D5AA8253AA10A2EF1C98B"
        "9AC8B57F1117A72BF2C7B9E7C1AC4D77FC94CA",
        16,
    ),
    int(
        "3DF91610A83441CAEA9863BC2DED5D5AA8253AA10A2EF1C98B9AC8B57F1117A72BF2C7B9E7C1AC4D77FC94CADC"
        "083E67984050B75EBAE5DD2809BD638016F723",
        16,
    ),
    int(
        "AADD9DB8DBE9C48B3FD4E6AE33C9FC07CB308DB3B3C9D20ED6639CCA70330870553E5C414CA92619418661197F"
        "AC10471DB1D381085DDADDB58796829CA90069",
        16,
    ),
    int(
        "81AEE4BDD82ED9645A21322E9C4C6A9385ED9F70B5D916C1B43B62EEF4D0098EFF3B1F78E2D0D48D50D1687B93"
        "B97D5F7C6D5047406A5E688B352209BCB9F822",
        16,
    ),
    int(
        "7DDE385D566332ECC0EABFA9CF7822FDF209F70024A57B1AA000C55B881F8111B2DCDE494A5F485E5BCA4BD88A"
        "2763AED1CA2B2FA8F0540678CD1E0F3AD80892",
        16,
    ),
    b"\x2b\x24\x03\x03\x02\x08\x01\x01\x0d",
)
