from unittest import TestCase

from fastecdsa.curve import brainpoolP256r1, brainpoolP384r1, brainpoolP512r1


class TestBrainpoolECDH(TestCase):
    def test_256bit(self):
        # https://tools.ietf.org/html/rfc7027#appendix-A.1
        dA = 0x81DB1EE100150FF2EA338D708271BE38300CB54241D79950F77B063039804F1D
        qA = dA * brainpoolP256r1.G

        self.assertEqual(
            qA.x, 0x44106E913F92BC02A1705D9953A8414DB95E1AAA49E81D9E85F929A8E3100BE5
        )
        self.assertEqual(
            qA.y, 0x8AB4846F11CACCB73CE49CBDD120F5A900A69FD32C272223F789EF10EB089BDC
        )

        dB = 0x55E40BC41E37E3E2AD25C3C6654511FFA8474A91A0032087593852D3E7D76BD3
        qB = dB * brainpoolP256r1.G

        self.assertEqual(
            qB.x, 0x8D2D688C6CF93E1160AD04CC4429117DC2C41825E1E9FCA0ADDD34E6F1B39F7B
        )
        self.assertEqual(
            qB.y, 0x990C57520812BE512641E47034832106BC7D3E8DD0E4C7F1136D7006547CEC6A
        )

        self.assertEqual((dA * qB).x, (dB * qA).x)
        self.assertEqual((dA * qB).y, (dB * qA).y)

        Z = dA * qB
        self.assertEqual(
            Z.x, 0x89AFC39D41D3B327814B80940B042590F96556EC91E6AE7939BCE31F3A18BF2B
        )
        self.assertEqual(
            Z.y, 0x49C27868F4ECA2179BFD7D59B1E3BF34C1DBDE61AE12931648F43E59632504DE
        )

    def test_384bit(self):
        # https://tools.ietf.org/html/rfc7027#appendix-A.2
        dA = int(
            "1E20F5E048A5886F1F157C74E91BDE2B98C8B52D58E5003D57053FC4B0BD6"
            "5D6F15EB5D1EE1610DF870795143627D042",
            16,
        )
        qA = dA * brainpoolP384r1.G

        self.assertEqual(
            qA.x,
            int(
                "68B665DD91C195800650CDD363C625F4E742E8134667B767B1B47679358"
                "8F885AB698C852D4A6E77A252D6380FCAF068",
                16,
            ),
        )
        self.assertEqual(
            qA.y,
            int(
                "55BC91A39C9EC01DEE36017B7D673A931236D2F1F5C83942D049E3FA206"
                "07493E0D038FF2FD30C2AB67D15C85F7FAA59",
                16,
            ),
        )

        dB = int(
            "032640BC6003C59260F7250C3DB58CE647F98E1260ACCE4ACDA3DD869F74E"
            "01F8BA5E0324309DB6A9831497ABAC96670",
            16,
        )
        qB = dB * brainpoolP384r1.G

        self.assertEqual(
            qB.x,
            int(
                "4D44326F269A597A5B58BBA565DA5556ED7FD9A8A9EB76C25F46DB69D19"
                "DC8CE6AD18E404B15738B2086DF37E71D1EB4",
                16,
            ),
        )
        self.assertEqual(
            qB.y,
            int(
                "62D692136DE56CBE93BF5FA3188EF58BC8A3A0EC6C1E151A21038A42E91"
                "85329B5B275903D192F8D4E1F32FE9CC78C48",
                16,
            ),
        )

        self.assertEqual((dA * qB).x, (dB * qA).x)
        self.assertEqual((dA * qB).y, (dB * qA).y)

        Z = dA * qB
        self.assertEqual(
            Z.x,
            int(
                "0BD9D3A7EA0B3D519D09D8E48D0785FB744A6B355E6304BC51C229FBBCE2"
                "39BBADF6403715C35D4FB2A5444F575D4F42",
                16,
            ),
        )
        self.assertEqual(
            Z.y,
            int(
                "0DF213417EBE4D8E40A5F76F66C56470C489A3478D146DECF6DF0D94BAE9"
                "E598157290F8756066975F1DB34B2324B7BD",
                16,
            ),
        )

    def test_512bit(self):
        # https://tools.ietf.org/html/rfc7027#appendix-A.2
        dA = int(
            "16302FF0DBBB5A8D733DAB7141C1B45ACBC8715939677F6A56850A38BD87B"
            "D59B09E80279609FF333EB9D4C061231FB26F92EEB04982A5F1D1764CAD57665422",
            16,
        )
        qA = dA * brainpoolP512r1.G

        self.assertEqual(
            qA.x,
            int(
                "0A420517E406AAC0ACDCE90FCD71487718D3B953EFD7FBEC5F7F27E28C6"
                "149999397E91E029E06457DB2D3E640668B392C2A7E737A7F0BF04436D11640FD09FD",
                16,
            ),
        )
        self.assertEqual(
            qA.y,
            int(
                "72E6882E8DB28AAD36237CD25D580DB23783961C8DC52DFA2EC138AD472"
                "A0FCEF3887CF62B623B2A87DE5C588301EA3E5FC269B373B60724F5E82A6AD147FDE7",
                16,
            ),
        )

        dB = int(
            "230E18E1BCC88A362FA54E4EA3902009292F7F8033624FD471B5D8ACE49D1"
            "2CFABBC19963DAB8E2F1EBA00BFFB29E4D72D13F2224562F405CB80503666B25429",
            16,
        )
        qB = dB * brainpoolP512r1.G

        self.assertEqual(
            qB.x,
            int(
                "9D45F66DE5D67E2E6DB6E93A59CE0BB48106097FF78A081DE781CDB31FC"
                "E8CCBAAEA8DD4320C4119F1E9CD437A2EAB3731FA9668AB268D871DEDA55A5473199F",
                16,
            ),
        )
        self.assertEqual(
            qB.y,
            int(
                "2FDC313095BCDD5FB3A91636F07A959C8E86B5636A1E930E8396049CB48"
                "1961D365CC11453A06C719835475B12CB52FC3C383BCE35E27EF194512B71876285FA",
                16,
            ),
        )

        self.assertEqual((dA * qB).x, (dB * qA).x)
        self.assertEqual((dA * qB).y, (dB * qA).y)

        Z = dA * qB
        self.assertEqual(
            Z.x,
            int(
                "A7927098655F1F9976FA50A9D566865DC530331846381C87256BAF322624"
                "4B76D36403C024D7BBF0AA0803EAFF405D3D24F11A9B5C0BEF679FE1454B21C4CD1F",
                16,
            ),
        )
        self.assertEqual(
            Z.y,
            int(
                "7DB71C3DEF63212841C463E881BDCF055523BD368240E6C3143BD8DEF8B3"
                "B3223B95E0F53082FF5E412F4222537A43DF1C6D25729DDB51620A832BE6A26680A2",
                16,
            ),
        )
