# coding: UTF-8
import sys
bstack11lllll_opy_ = sys.version_info [0] == 2
bstack1l1l1_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1l1l11_opy_):
    global bstack11lll_opy_
    bstack11llll_opy_ = ord (bstack1l1l11_opy_ [-1])
    bstack111ll1l_opy_ = bstack1l1l11_opy_ [:-1]
    bstack1l1l_opy_ = bstack11llll_opy_ % len (bstack111ll1l_opy_)
    bstack1ll11l1_opy_ = bstack111ll1l_opy_ [:bstack1l1l_opy_] + bstack111ll1l_opy_ [bstack1l1l_opy_:]
    if bstack11lllll_opy_:
        bstack11lll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1_opy_ - (bstack1lll_opy_ + bstack11llll_opy_) % bstack1ll1l1_opy_) for bstack1lll_opy_, char in enumerate (bstack1ll11l1_opy_)])
    else:
        bstack11lll11_opy_ = str () .join ([chr (ord (char) - bstack1l1l1_opy_ - (bstack1lll_opy_ + bstack11llll_opy_) % bstack1ll1l1_opy_) for bstack1lll_opy_, char in enumerate (bstack1ll11l1_opy_)])
    return eval (bstack11lll11_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1111l11111_opy_ import bstack11111lll11_opy_
class bstack1lll1llll1l_opy_(abc.ABC):
    bin_session_id: str
    bstack1111l11111_opy_: bstack11111lll11_opy_
    def __init__(self):
        self.bstack1llll11l1l1_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1111l11111_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll1l1lll1_opy_(self):
        return (self.bstack1llll11l1l1_opy_ != None and self.bin_session_id != None and self.bstack1111l11111_opy_ != None)
    def configure(self, bstack1llll11l1l1_opy_, config, bin_session_id: str, bstack1111l11111_opy_: bstack11111lll11_opy_):
        self.bstack1llll11l1l1_opy_ = bstack1llll11l1l1_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1111l11111_opy_ = bstack1111l11111_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡩࡩࠦ࡭ࡰࡦࡸࡰࡪࠦࡻࡴࡧ࡯ࡪ࠳ࡥ࡟ࡤ࡮ࡤࡷࡸࡥ࡟࠯ࡡࡢࡲࡦࡳࡥࡠࡡࢀ࠾ࠥࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࡃࠢᇉ") + str(self.bin_session_id) + bstack1l1lll1_opy_ (u"ࠦࠧᇊ"))
    def bstack1ll1l1111ll_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1l1lll1_opy_ (u"ࠧࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠦࡣࡢࡰࡱࡳࡹࠦࡢࡦࠢࡑࡳࡳ࡫ࠢᇋ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False