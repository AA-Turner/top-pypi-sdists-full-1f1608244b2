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
import json
import time
from datetime import datetime, timezone
from browserstack_sdk.sdk_cli.bstack11111ll1l1_opy_ import (
    bstack1llllll111l_opy_,
    bstack1llllll1l1l_opy_,
    bstack11111l1l1l_opy_,
    bstack1lllllll1ll_opy_,
    bstack1lllllll111_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lll1l1l111_opy_ import bstack1lll11l1l11_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1ll1ll1lll1_opy_, bstack1lll11lllll_opy_, bstack1llll1lll11_opy_
from browserstack_sdk.sdk_cli.bstack1ll111l11l1_opy_ import bstack1ll111ll1l1_opy_
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1l1llll1111_opy_
from browserstack_sdk import sdk_pb2 as structs
from bstack_utils.measure import measure
from bstack_utils.constants import *
from typing import Tuple, List, Any
class bstack1ll1lll1lll_opy_(bstack1ll111ll1l1_opy_):
    bstack1l1l11ll1ll_opy_ = bstack1l1lll1_opy_ (u"ࠨࡴࡦࡵࡷࡣࡩࡸࡩࡷࡧࡵࡷࠧጸ")
    bstack1l1llll1l11_opy_ = bstack1l1lll1_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࠨጹ")
    bstack1l1l1l1l1ll_opy_ = bstack1l1lll1_opy_ (u"ࠣࡰࡲࡲࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥጺ")
    bstack1l1l1l1111l_opy_ = bstack1l1lll1_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠤጻ")
    bstack1l1l1l11lll_opy_ = bstack1l1lll1_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡶࡸࡦࡴࡣࡦࡡࡵࡩ࡫ࡹࠢጼ")
    bstack1l1ll1lll1l_opy_ = bstack1l1lll1_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡦࡶࡪࡧࡴࡦࡦࠥጽ")
    bstack1l1l11llll1_opy_ = bstack1l1lll1_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡲࡦࡳࡥࠣጾ")
    bstack1l1l1l11l1l_opy_ = bstack1l1lll1_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡸࡺࡡࡵࡷࡶࠦጿ")
    def __init__(self):
        super().__init__(bstack1ll111l11ll_opy_=self.bstack1l1l11ll1ll_opy_, frameworks=[bstack1lll11l1l11_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1ll1l1lll1l_opy_((bstack1ll1ll1lll1_opy_.BEFORE_EACH, bstack1lll11lllll_opy_.POST), self.bstack1l11lllll1l_opy_)
        TestFramework.bstack1ll1l1lll1l_opy_((bstack1ll1ll1lll1_opy_.TEST, bstack1lll11lllll_opy_.PRE), self.bstack1ll1l11111l_opy_)
        TestFramework.bstack1ll1l1lll1l_opy_((bstack1ll1ll1lll1_opy_.TEST, bstack1lll11lllll_opy_.POST), self.bstack1ll11l1ll1l_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11lllll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1lll11_opy_,
        bstack1llllll1l11_opy_: Tuple[bstack1ll1ll1lll1_opy_, bstack1lll11lllll_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1lll11l11_opy_ = self.bstack1l11lllll11_opy_(instance.context)
        if not bstack1l1lll11l11_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡴࡧࡷࡣࡦࡩࡴࡪࡸࡨࡣࡩࡸࡩࡷࡧࡵࡷ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥፀ") + str(bstack1llllll1l11_opy_) + bstack1l1lll1_opy_ (u"ࠣࠤፁ"))
        f.bstack1111111lll_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1llll1l11_opy_, bstack1l1lll11l11_opy_)
        bstack1l11llll111_opy_ = self.bstack1l11lllll11_opy_(instance.context, bstack1l11lll11l1_opy_=False)
        f.bstack1111111lll_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1l1l1l1ll_opy_, bstack1l11llll111_opy_)
    def bstack1ll1l11111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1lll11_opy_,
        bstack1llllll1l11_opy_: Tuple[bstack1ll1ll1lll1_opy_, bstack1lll11lllll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11lllll1l_opy_(f, instance, bstack1llllll1l11_opy_, *args, **kwargs)
        if not f.bstack1llllllll11_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1l11llll1_opy_, False):
            self.__1l11lll1l11_opy_(f,instance,bstack1llllll1l11_opy_)
    def bstack1ll11l1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1lll11_opy_,
        bstack1llllll1l11_opy_: Tuple[bstack1ll1ll1lll1_opy_, bstack1lll11lllll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11lllll1l_opy_(f, instance, bstack1llllll1l11_opy_, *args, **kwargs)
        if not f.bstack1llllllll11_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1l11llll1_opy_, False):
            self.__1l11lll1l11_opy_(f, instance, bstack1llllll1l11_opy_)
        if not f.bstack1llllllll11_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1l1l11l1l_opy_, False):
            self.__1l11llll11l_opy_(f, instance, bstack1llllll1l11_opy_)
    def bstack1l11lll1l1l_opy_(
        self,
        f: bstack1lll11l1l11_opy_,
        driver: object,
        exec: Tuple[bstack1lllllll1ll_opy_, str],
        bstack1llllll1l11_opy_: Tuple[bstack1llllll111l_opy_, bstack1llllll1l1l_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if not f.bstack1ll111l1l1l_opy_(instance):
            return
        if f.bstack1llllllll11_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1l1l11l1l_opy_, False):
            return
        driver.execute_script(
            bstack1l1lll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠢፂ").format(
                json.dumps(
                    {
                        bstack1l1lll1_opy_ (u"ࠥࡥࡨࡺࡩࡰࡰࠥፃ"): bstack1l1lll1_opy_ (u"ࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠢፄ"),
                        bstack1l1lll1_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣፅ"): {bstack1l1lll1_opy_ (u"ࠨࡳࡵࡣࡷࡹࡸࠨፆ"): result},
                    }
                )
            )
        )
        f.bstack1111111lll_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1l1l11l1l_opy_, True)
    def bstack1l11lllll11_opy_(self, context: bstack1lllllll111_opy_, bstack1l11lll11l1_opy_= True):
        if bstack1l11lll11l1_opy_:
            bstack1l1lll11l11_opy_ = self.bstack1ll111lll11_opy_(context, reverse=True)
        else:
            bstack1l1lll11l11_opy_ = self.bstack1ll111ll111_opy_(context, reverse=True)
        return [f for f in bstack1l1lll11l11_opy_ if f[1].state != bstack1llllll111l_opy_.QUIT]
    @measure(event_name=EVENTS.bstack1ll11111_opy_, stage=STAGE.bstack1lllll111l_opy_)
    def __1l11llll11l_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1lll11_opy_,
        bstack1llllll1l11_opy_: Tuple[bstack1ll1ll1lll1_opy_, bstack1lll11lllll_opy_],
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l1lll1_opy_ (u"ࠢࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠧፇ")).get(bstack1l1lll1_opy_ (u"ࠣࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧፈ")):
            bstack1l1lll11l11_opy_ = f.bstack1llllllll11_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1llll1l11_opy_, [])
            if not bstack1l1lll11l11_opy_:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡶࡩࡹࡥࡡࡤࡶ࡬ࡺࡪࡥࡤࡳ࡫ࡹࡩࡷࡹ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧፉ") + str(bstack1llllll1l11_opy_) + bstack1l1lll1_opy_ (u"ࠥࠦፊ"))
                return
            driver = bstack1l1lll11l11_opy_[0][0]()
            status = f.bstack1llllllll11_opy_(instance, TestFramework.bstack1l1l1l1l11l_opy_, None)
            if not status:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡸ࡫ࡴࡠࡣࡦࡸ࡮ࡼࡥࡠࡦࡵ࡭ࡻ࡫ࡲࡴ࠼ࠣࡲࡴࠦࡳࡵࡣࡷࡹࡸࠦࡦࡰࡴࠣࡸࡪࡹࡴ࠭ࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨፋ") + str(bstack1llllll1l11_opy_) + bstack1l1lll1_opy_ (u"ࠧࠨፌ"))
                return
            bstack1l1l11ll1l1_opy_ = {bstack1l1lll1_opy_ (u"ࠨࡳࡵࡣࡷࡹࡸࠨፍ"): status.lower()}
            bstack1l1l1l11l11_opy_ = f.bstack1llllllll11_opy_(instance, TestFramework.bstack1l1l1l1l111_opy_, None)
            if status.lower() == bstack1l1lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧፎ") and bstack1l1l1l11l11_opy_ is not None:
                bstack1l1l11ll1l1_opy_[bstack1l1lll1_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨፏ")] = bstack1l1l1l11l11_opy_[0][bstack1l1lll1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬፐ")][0] if isinstance(bstack1l1l1l11l11_opy_, list) else str(bstack1l1l1l11l11_opy_)
            driver.execute_script(
                bstack1l1lll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠣፑ").format(
                    json.dumps(
                        {
                            bstack1l1lll1_opy_ (u"ࠦࡦࡩࡴࡪࡱࡱࠦፒ"): bstack1l1lll1_opy_ (u"ࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠣፓ"),
                            bstack1l1lll1_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤፔ"): bstack1l1l11ll1l1_opy_,
                        }
                    )
                )
            )
            f.bstack1111111lll_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1l1l11l1l_opy_, True)
    @measure(event_name=EVENTS.bstack1l11lllll1_opy_, stage=STAGE.bstack1lllll111l_opy_)
    def __1l11lll1l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1lll11_opy_,
        bstack1llllll1l11_opy_: Tuple[bstack1ll1ll1lll1_opy_, bstack1lll11lllll_opy_]
    ):
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1l1lll1_opy_ (u"ࠢࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠧፕ")).get(bstack1l1lll1_opy_ (u"ࠣࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥፖ")):
            test_name = f.bstack1llllllll11_opy_(instance, TestFramework.bstack1l11lll1ll1_opy_, None)
            if not test_name:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡲࡦࡳࡥࠣፗ"))
                return
            bstack1l1lll11l11_opy_ = f.bstack1llllllll11_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1llll1l11_opy_, [])
            if not bstack1l1lll11l11_opy_:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡷࡪࡺ࡟ࡢࡥࡷ࡭ࡻ࡫࡟ࡥࡴ࡬ࡺࡪࡸࡳ࠻ࠢࡱࡳࠥࡹࡴࡢࡶࡸࡷࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠬࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࠧፘ") + str(bstack1llllll1l11_opy_) + bstack1l1lll1_opy_ (u"ࠦࠧፙ"))
                return
            for bstack1l1ll11l1ll_opy_, bstack1l11lll111l_opy_ in bstack1l1lll11l11_opy_:
                if not bstack1lll11l1l11_opy_.bstack1ll111l1l1l_opy_(bstack1l11lll111l_opy_):
                    continue
                driver = bstack1l1ll11l1ll_opy_()
                if not driver:
                    continue
                driver.execute_script(
                    bstack1l1lll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠥፚ").format(
                        json.dumps(
                            {
                                bstack1l1lll1_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨ፛"): bstack1l1lll1_opy_ (u"ࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ፜"),
                                bstack1l1lll1_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ፝"): {bstack1l1lll1_opy_ (u"ࠤࡱࡥࡲ࡫ࠢ፞"): test_name},
                            }
                        )
                    )
                )
            f.bstack1111111lll_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1l11llll1_opy_, True)
    def bstack1l1lll111l1_opy_(
        self,
        instance: bstack1llll1lll11_opy_,
        f: TestFramework,
        bstack1llllll1l11_opy_: Tuple[bstack1ll1ll1lll1_opy_, bstack1lll11lllll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11lllll1l_opy_(f, instance, bstack1llllll1l11_opy_, *args, **kwargs)
        bstack1l1lll11l11_opy_ = [d for d, _ in f.bstack1llllllll11_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1llll1l11_opy_, [])]
        if not bstack1l1lll11l11_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡳࡳࡥࡡࡧࡶࡨࡶࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠢࡷࡳࠥࡲࡩ࡯࡭ࠥ፟"))
            return
        if not bstack1l1llll1111_opy_():
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤ፠"))
            return
        for bstack1l11lll1lll_opy_ in bstack1l1lll11l11_opy_:
            driver = bstack1l11lll1lll_opy_()
            if not driver:
                continue
            timestamp = int(time.time() * 1000)
            data = bstack1l1lll1_opy_ (u"ࠧࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࡘࡿ࡮ࡤ࠼ࠥ፡") + str(timestamp)
            driver.execute_script(
                bstack1l1lll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠦ።").format(
                    json.dumps(
                        {
                            bstack1l1lll1_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢ፣"): bstack1l1lll1_opy_ (u"ࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ፤"),
                            bstack1l1lll1_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧ፥"): {
                                bstack1l1lll1_opy_ (u"ࠥࡸࡾࡶࡥࠣ፦"): bstack1l1lll1_opy_ (u"ࠦࡆࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠣ፧"),
                                bstack1l1lll1_opy_ (u"ࠧࡪࡡࡵࡣࠥ፨"): data,
                                bstack1l1lll1_opy_ (u"ࠨ࡬ࡦࡸࡨࡰࠧ፩"): bstack1l1lll1_opy_ (u"ࠢࡥࡧࡥࡹ࡬ࠨ፪")
                            }
                        }
                    )
                )
            )
    def bstack1ll1111ll1l_opy_(
        self,
        instance: bstack1llll1lll11_opy_,
        f: TestFramework,
        bstack1llllll1l11_opy_: Tuple[bstack1ll1ll1lll1_opy_, bstack1lll11lllll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11lllll1l_opy_(f, instance, bstack1llllll1l11_opy_, *args, **kwargs)
        keys = [
            bstack1ll1lll1lll_opy_.bstack1l1llll1l11_opy_,
            bstack1ll1lll1lll_opy_.bstack1l1l1l1l1ll_opy_,
        ]
        bstack1l1lll11l11_opy_ = []
        for key in keys:
            bstack1l1lll11l11_opy_.extend(f.bstack1llllllll11_opy_(instance, key, []))
        if not bstack1l1lll11l11_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡸࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡥࡳࡿࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡴࠢࡷࡳࠥࡲࡩ࡯࡭ࠥ፫"))
            return
        if f.bstack1llllllll11_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1ll1lll1l_opy_, False):
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡇࡇ࡚ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡥࡵࡩࡦࡺࡥࡥࠤ፬"))
            return
        self.bstack1ll1l1111ll_opy_()
        bstack11lll1ll1_opy_ = datetime.now()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll1l1lllll_opy_)
        req.test_framework_name = TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll11llllll_opy_)
        req.test_framework_version = TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1l1ll1ll1l1_opy_)
        req.test_framework_state = bstack1llllll1l11_opy_[0].name
        req.test_hook_state = bstack1llllll1l11_opy_[1].name
        req.test_uuid = TestFramework.bstack1llllllll11_opy_(instance, TestFramework.bstack1ll1l11l11l_opy_)
        for bstack1l1ll11l1ll_opy_, driver in bstack1l1lll11l11_opy_:
            try:
                webdriver = bstack1l1ll11l1ll_opy_()
                if webdriver is None:
                    self.logger.debug(bstack1l1lll1_opy_ (u"࡛ࠥࡪࡨࡄࡳ࡫ࡹࡩࡷࠦࡩ࡯ࡵࡷࡥࡳࡩࡥࠡ࡫ࡶࠤࡓࡵ࡮ࡦࠢࠫࡶࡪ࡬ࡥࡳࡧࡱࡧࡪࠦࡥࡹࡲ࡬ࡶࡪࡪࠩࠣ፭"))
                    continue
                session = req.automation_sessions.add()
                session.provider = (
                    bstack1l1lll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠥ፮")
                    if bstack1lll11l1l11_opy_.bstack1llllllll11_opy_(driver, bstack1lll11l1l11_opy_.bstack1l11llll1ll_opy_, False)
                    else bstack1l1lll1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࡥࡧࡳ࡫ࡧࠦ፯")
                )
                session.ref = driver.ref()
                session.hub_url = bstack1lll11l1l11_opy_.bstack1llllllll11_opy_(driver, bstack1lll11l1l11_opy_.bstack1l1l1lll111_opy_, bstack1l1lll1_opy_ (u"ࠨࠢ፰"))
                session.framework_name = driver.framework_name
                session.framework_version = driver.framework_version
                session.framework_session_id = bstack1lll11l1l11_opy_.bstack1llllllll11_opy_(driver, bstack1lll11l1l11_opy_.bstack1l1l1lll1ll_opy_, bstack1l1lll1_opy_ (u"ࠢࠣ፱"))
                caps = None
                if hasattr(webdriver, bstack1l1lll1_opy_ (u"ࠣࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢ፲")):
                    try:
                        caps = webdriver.capabilities
                        self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡖࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࡧࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠣࡨ࡮ࡸࡥࡤࡶ࡯ࡽࠥ࡬ࡲࡰ࡯ࠣࡨࡷ࡯ࡶࡦࡴ࠱ࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤ፳"))
                    except Exception as e:
                        self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡶࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠢࡩࡶࡴࡳࠠࡥࡴ࡬ࡺࡪࡸ࠮ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࡀࠠࠣ፴") + str(e) + bstack1l1lll1_opy_ (u"ࠦࠧ፵"))
                try:
                    bstack1l11lll11ll_opy_ = json.dumps(caps).encode(bstack1l1lll1_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦ፶")) if caps else bstack1l11llll1l1_opy_ (u"ࠨࡻࡾࠤ፷")
                    req.capabilities = bstack1l11lll11ll_opy_
                except Exception as e:
                    self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡨࡧࡷࡣࡨࡨࡴࡠࡧࡹࡩࡳࡺ࠺ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫࡮ࡥࠢࡶࡩࡷ࡯ࡡ࡭࡫ࡽࡩࠥࡩࡡࡱࡵࠣࡪࡴࡸࠠࡳࡧࡴࡹࡪࡹࡴ࠻ࠢࠥ፸") + str(e) + bstack1l1lll1_opy_ (u"ࠣࠤ፹"))
            except Exception as e:
                self.logger.error(bstack1l1lll1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡪࡲࡪࡸࡨࡶࠥ࡯ࡴࡦ࡯࠽ࠤࠧ፺") + str(str(e)) + bstack1l1lll1_opy_ (u"ࠥࠦ፻"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1ll1l111l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1lll11_opy_,
        bstack1llllll1l11_opy_: Tuple[bstack1ll1ll1lll1_opy_, bstack1lll11lllll_opy_],
        *args,
        **kwargs
    ):
        bstack1l1lll11l11_opy_ = f.bstack1llllllll11_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1llll1l11_opy_, [])
        if not bstack1l1llll1111_opy_() and len(bstack1l1lll11l11_opy_) == 0:
            bstack1l1lll11l11_opy_ = f.bstack1llllllll11_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1l1l1l1ll_opy_, [])
        if not bstack1l1lll11l11_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡧࡶ࡮ࡼࡥࡳࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢ፼") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠧࠨ፽"))
            return {}
        if len(bstack1l1lll11l11_opy_) > 1:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡽ࡯ࡩࡳ࠮ࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤ፾") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠢࠣ፿"))
            return {}
        bstack1l1ll11l1ll_opy_, bstack1l1ll11l111_opy_ = bstack1l1lll11l11_opy_[0]
        driver = bstack1l1ll11l1ll_opy_()
        if not driver:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡤࡳ࡫ࡹࡩࡷࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᎀ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠤࠥᎁ"))
            return {}
        capabilities = f.bstack1llllllll11_opy_(bstack1l1ll11l111_opy_, bstack1lll11l1l11_opy_.bstack1l1l1ll1111_opy_)
        if not capabilities:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠠࡧࡱࡸࡲࡩࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᎂ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠦࠧᎃ"))
            return {}
        return capabilities.get(bstack1l1lll1_opy_ (u"ࠧࡧ࡬ࡸࡣࡼࡷࡒࡧࡴࡤࡪࠥᎄ"), {})
    def bstack1ll11l1ll11_opy_(
        self,
        f: TestFramework,
        instance: bstack1llll1lll11_opy_,
        bstack1llllll1l11_opy_: Tuple[bstack1ll1ll1lll1_opy_, bstack1lll11lllll_opy_],
        *args,
        **kwargs
    ):
        bstack1l1lll11l11_opy_ = f.bstack1llllllll11_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1llll1l11_opy_, [])
        if not bstack1l1llll1111_opy_() and len(bstack1l1lll11l11_opy_) == 0:
            bstack1l1lll11l11_opy_ = f.bstack1llllllll11_opy_(instance, bstack1ll1lll1lll_opy_.bstack1l1l1l1l1ll_opy_, [])
        if not bstack1l1lll11l11_opy_:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᎅ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠢࠣᎆ"))
            return
        if len(bstack1l1lll11l11_opy_) > 1:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡿࡱ࡫࡮ࠩࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶ࠭ࢂࠦࡤࡳ࡫ࡹࡩࡷࡹࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᎇ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠤࠥᎈ"))
        bstack1l1ll11l1ll_opy_, bstack1l1ll11l111_opy_ = bstack1l1lll11l11_opy_[0]
        driver = bstack1l1ll11l1ll_opy_()
        if not driver:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᎉ") + str(kwargs) + bstack1l1lll1_opy_ (u"ࠦࠧᎊ"))
            return
        return driver