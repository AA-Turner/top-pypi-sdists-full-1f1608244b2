# coding: utf-8

"""
    Wandelbots NOVA API

    Interact with robots in an easy and intuitive way. 

    The version of the OpenAPI document: 1.0.0 beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class VirtualControllerTypes(str, Enum):
    """
    VirtualControllerTypes
    """

    """
    allowed enum values
    """
    ABB_MINUS_IRB1010_037_15 = 'abb-irb1010_037_15'
    ABB_MINUS_IRB1100_0475_4 = 'abb-irb1100_0475_4'
    ABB_MINUS_IRB1100_058_4 = 'abb-irb1100_058_4'
    ABB_MINUS_IRB1200_7 = 'abb-irb1200_7'
    ABB_MINUS_IRB1300_09_11 = 'abb-irb1300_09_11'
    ABB_MINUS_IRB1300_115_10 = 'abb-irb1300_115_10'
    ABB_MINUS_IRB1300_14_12 = 'abb-irb1300_14_12'
    ABB_MINUS_IRB1300_14_7 = 'abb-irb1300_14_7'
    ABB_MINUS_IRB1600_12_10 = 'abb-irb1600_12_10'
    ABB_MINUS_IRB1600_12_6 = 'abb-irb1600_12_6'
    ABB_MINUS_IRB1600_145_10 = 'abb-irb1600_145_10'
    ABB_MINUS_IRB1600_145_6 = 'abb-irb1600_145_6'
    ABB_MINUS_IRB2600_ID_185_15 = 'abb-irb2600ID_185_15'
    ABB_MINUS_IRB2600_ID_200_8 = 'abb-irb2600ID_200_8'
    ABB_MINUS_IRB2600_165_12 = 'abb-irb2600_165_12'
    ABB_MINUS_IRB2600_165_20 = 'abb-irb2600_165_20'
    ABB_MINUS_IRB2600_185_12 = 'abb-irb2600_185_12'
    ABB_MINUS_IRB4600_205_45 = 'abb-irb4600_205_45'
    ABB_MINUS_IRB4600_205_60 = 'abb-irb4600_205_60'
    ABB_MINUS_IRB4600_250_20 = 'abb-irb4600_250_20'
    ABB_MINUS_IRB4600_255_40 = 'abb-irb4600_255_40'
    FANUC_MINUS_ARC_MATE_100I_D = 'fanuc-arc_mate_100iD'
    FANUC_MINUS_ARC_MATE_100I_D16_S = 'fanuc-arc_mate_100iD16S'
    FANUC_MINUS_ARC_MATE_120I_D = 'fanuc-arc_mate_120iD'
    FANUC_MINUS_ARC_MATE_120I_D12_L = 'fanuc-arc_mate_120iD12L'
    FANUC_MINUS_ARC_MATE_120I_D35 = 'fanuc-arc_mate_120iD35'
    FANUC_MINUS_CR35IB = 'fanuc-cr35ib'
    FANUC_MINUS_CR7IA = 'fanuc-cr7ia'
    FANUC_MINUS_CR7IAL = 'fanuc-cr7ial'
    FANUC_MINUS_CRX10IA = 'fanuc-crx10ia'
    FANUC_MINUS_CRX10IAL = 'fanuc-crx10ial'
    FANUC_MINUS_CRX20IAL = 'fanuc-crx20ial'
    FANUC_MINUS_CRX25IA = 'fanuc-crx25ia'
    FANUC_MINUS_CRX30IA = 'fanuc-crx30ia'
    FANUC_MINUS_LR_MATE_200I_D = 'fanuc-lr_mate_200iD'
    FANUC_MINUS_LR_MATE_200I_D4_S = 'fanuc-lr_mate_200iD4S'
    FANUC_MINUS_LR_MATE_200I_D7_L = 'fanuc-lr_mate_200iD7L'
    FANUC_MINUS_M10I_D12 = 'fanuc-m10iD12'
    FANUC_MINUS_M10I_D16_S = 'fanuc-m10iD16S'
    FANUC_MINUS_M20I_D25 = 'fanuc-m20iD25'
    FANUC_MINUS_M20I_D35 = 'fanuc-m20iD35'
    FANUC_MINUS_M900I_B280_L = 'fanuc-m900iB280L'
    FANUC_MINUS_M900I_B360_E = 'fanuc-m900iB360E'
    FANUC_MINUS_R2000IC125L = 'fanuc-r2000ic125l'
    FANUC_MINUS_R2000IC210F = 'fanuc-r2000ic210f'
    KUKA_MINUS_KR10_R1100 = 'kuka-kr10_r1100'
    KUKA_MINUS_KR10_R1100_2 = 'kuka-kr10_r1100_2'
    KUKA_MINUS_KR10_R900 = 'kuka-kr10_r900'
    KUKA_MINUS_KR10_R900_2 = 'kuka-kr10_r900_2'
    KUKA_MINUS_KR120_R2700_2 = 'kuka-kr120_r2700_2'
    KUKA_MINUS_KR12_R1810_2 = 'kuka-kr12_r1810_2'
    KUKA_MINUS_KR150_R2 = 'kuka-kr150_r2'
    KUKA_MINUS_KR16_R1610_2 = 'kuka-kr16_r1610_2'
    KUKA_MINUS_KR16_R2010_2 = 'kuka-kr16_r2010_2'
    KUKA_MINUS_KR20_R1810 = 'kuka-kr20_r1810'
    KUKA_MINUS_KR20_R1810_2 = 'kuka-kr20_r1810_2'
    KUKA_MINUS_KR210_R2700_2 = 'kuka-kr210_r2700_2'
    KUKA_MINUS_KR210_R3100_2 = 'kuka-kr210_r3100_2'
    KUKA_MINUS_KR210_R3300_2 = 'kuka-kr210_r3300_2'
    KUKA_MINUS_KR240_R2700 = 'kuka-kr240_r2700'
    KUKA_MINUS_KR250_R2700_2 = 'kuka-kr250_r2700_2'
    KUKA_MINUS_KR30_R2100 = 'kuka-kr30_r2100'
    KUKA_MINUS_KR30_R3 = 'kuka-kr30_r3'
    KUKA_MINUS_KR360_L240_3 = 'kuka-kr360_l240_3'
    KUKA_MINUS_KR3_R540 = 'kuka-kr3_r540'
    KUKA_MINUS_KR4_R600 = 'kuka-kr4_r600'
    KUKA_MINUS_KR500_L340_3 = 'kuka-kr500_l340_3'
    KUKA_MINUS_KR50_R2500 = 'kuka-kr50_r2500'
    KUKA_MINUS_KR6_R1820 = 'kuka-kr6_r1820'
    KUKA_MINUS_KR6_R700_2 = 'kuka-kr6_r700_2'
    KUKA_MINUS_KR6_R700_SIXX = 'kuka-kr6_r700_sixx'
    KUKA_MINUS_KR6_R900 = 'kuka-kr6_r900'
    KUKA_MINUS_KR6_R900_2 = 'kuka-kr6_r900_2'
    KUKA_MINUS_LBR_IISY_11_R1300 = 'kuka-lbr_iisy_11_r1300'
    UNIVERSALROBOTS_MINUS_UR10CB = 'universalrobots-ur10cb'
    UNIVERSALROBOTS_MINUS_UR10E = 'universalrobots-ur10e'
    UNIVERSALROBOTS_MINUS_UR16E = 'universalrobots-ur16e'
    UNIVERSALROBOTS_MINUS_UR20E = 'universalrobots-ur20e'
    UNIVERSALROBOTS_MINUS_UR3E = 'universalrobots-ur3e'
    UNIVERSALROBOTS_MINUS_UR5CB = 'universalrobots-ur5cb'
    UNIVERSALROBOTS_MINUS_UR5E = 'universalrobots-ur5e'
    YASKAWA_MINUS_AR1440 = 'yaskawa-ar1440'
    YASKAWA_MINUS_AR1730 = 'yaskawa-ar1730'
    YASKAWA_MINUS_AR2010 = 'yaskawa-ar2010'
    YASKAWA_MINUS_AR3120 = 'yaskawa-ar3120'
    YASKAWA_MINUS_AR700 = 'yaskawa-ar700'
    YASKAWA_MINUS_AR900 = 'yaskawa-ar900'
    YASKAWA_MINUS_GP110 = 'yaskawa-gp110'
    YASKAWA_MINUS_GP12 = 'yaskawa-gp12'
    YASKAWA_MINUS_GP180 = 'yaskawa-gp180'
    YASKAWA_MINUS_GP180_MINUS_120 = 'yaskawa-gp180-120'
    YASKAWA_MINUS_GP20HL = 'yaskawa-gp20hl'
    YASKAWA_MINUS_GP215 = 'yaskawa-gp215'
    YASKAWA_MINUS_GP225 = 'yaskawa-gp225'
    YASKAWA_MINUS_GP25 = 'yaskawa-gp25'
    YASKAWA_MINUS_GP250 = 'yaskawa-gp250'
    YASKAWA_MINUS_GP25_12 = 'yaskawa-gp25_12'
    YASKAWA_MINUS_GP280 = 'yaskawa-gp280'
    YASKAWA_MINUS_GP35_L = 'yaskawa-gp35L'
    YASKAWA_MINUS_GP400 = 'yaskawa-gp400'
    YASKAWA_MINUS_GP50 = 'yaskawa-gp50'
    YASKAWA_MINUS_GP600 = 'yaskawa-gp600'
    YASKAWA_MINUS_GP7 = 'yaskawa-gp7'
    YASKAWA_MINUS_GP8 = 'yaskawa-gp8'
    YASKAWA_MINUS_GP88 = 'yaskawa-gp88'
    YASKAWA_MINUS_HC10DTP = 'yaskawa-hc10dtp'
    YASKAWA_MINUS_HC20DTP = 'yaskawa-hc20dtp'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualControllerTypes from a JSON string"""
        return cls(json.loads(json_str))


