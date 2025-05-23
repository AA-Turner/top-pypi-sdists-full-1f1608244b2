# Copyright (c) 2011 X.commerce, a business unit of eBay Inc.
# Copyright 2010 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# Copyright 2011 Piston Cloud Computing, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
This module provides models for BCC-SDK.
"""


class Billing(object):
    """
	This class define billing.
	param: paymentTiming: 
		The pay time of the payment,
		see more detail in https://bce.baidu.com/doc/BCC/API.html#Billing
	param: reservationLength: 
		The duration to buy in specified time unit,
		available values are [1,2,3,4,5,6,7,8,9,12,24,36] now.
	param: reservationTimeUnit: 
		The time unit to specify the duration ,only "Month" can be used now.
	"""

    def __init__(self, paymentTiming=None, reservationLength=1, reservationTimeUnit='Month'):
        if paymentTiming:
            self.paymentTiming = paymentTiming
        self.reservation = {
            'reservationLength': reservationLength,
            'reservationTimeUnit': reservationTimeUnit
        }


class EphemeralDisk(object):
    """
    This class define detail of creating ephemeral volume.
    param: sizeInGB:
        The size of volume in GB.
	param: storageType:
		The storage type of volume,
		see more detail in https://bce.baidu.com/doc/BCC/API.html#StorageType
    """

    def __init__(self, sizeInGB, storageType='sata'):
        self.sizeInGB = sizeInGB
        self.storageType = storageType


class CreateCdsModel(object):
    """
	This class define detail of creating volume.
	param: cdsSizeInGB: 
		The size of volume in GB.
	param: storageType: 
		The storage type of volume, 
		see more detail in https://bce.baidu.com/doc/BCC/API.html#StorageType
	param: snapshotId: 
		The id of snapshot.
	param: encryptKey
	"""

    def __init__(self, cdsSizeInGB=None, storageType='hp1', snapshotId=None, encryptKey=None):
        self.cdsSizeInGB = cdsSizeInGB
        self.storageType = storageType
        self.snapshotId = snapshotId
        self.encryptKey = encryptKey


class SecurityGroupRuleModel(object):
    """
	This class define the rule of the securitygroup.
	param: remark: 
		The remark for the rule.
	param: direction: 
		The parameter to define the rule direction,available value are "ingress/egress".
	param: ethertype: 
		The ethernet protocol.
	param: portRange: 
		The port range to specify the port which the rule will work on.
		Available range is rang [0, 65535], the fault value is "" for all port.
	param: protocol: 
		The parameter specify which protocol will the rule work on, the fault value is "" for all protocol.
		Available protocol are tcp, udp and icmp.
	param: sourceGroupId: 
		The id of source securitygroup.
		Only works for direction = "ingress".
	param: sourceIp: 
		The source ip range with CIDR formats. The default value 0.0.0.0/0 (allow all ip address),
		other supported formats such as {ip_addr}/12 or {ip_addr}. Only supports IPV4.
		Only works for  direction = "ingress".
	param: destGroupId: 
		The id of destination securitygroup.
		Only works for  direction = "egress".
	param: destIp: 
		The destination ip range with CIDR formats. The default value 0.0.0.0/0 (allow all ip address),
		other supported formats such as {ip_addr}/12 or {ip_addr}. Only supports IPV4.
		Only works for  direction = "egress".
	param: securityGroupId: 
		The id of the securitygroup for the rule.
	"""

    def __init__(self, remark=None, direction=None, ethertype=None, portRange=None,
                 protocol=None, sourceGroupId=None, sourceIp=None, destGroupId=None, destIp=None,
                 securityGroupId=None):
        self.remark = remark
        self.direction = direction
        self.ethertype = ethertype
        self.portRange = portRange
        self.protocol = protocol
        self.sourceGroupId = sourceGroupId
        self.sourceIp = sourceIp
        self.destGroupId = destGroupId
        self.destIp = destIp
        self.securityGroupId = securityGroupId


class TagModel(object):
    """
    TAGModel
    """

    def __init__(self, tagKey=None, tagValue=None):
        self.tagKey = tagKey
        self.tagValue = tagValue


class PayTimingChangeReqModel(object):
    """
    This class define detail of change pay timing.
    """

    def __init__(self, instanceId, relationCds=False, cdsList=None, duration=None, autoPay=True,
                 autoRenew=None, autoRenewPeriod=None):
        self.instanceId = instanceId
        self.relationCds = relationCds
        self.cdsList = cdsList
        self.duration = duration
        self.autoPay = autoPay
        self.autoRenew = autoRenew
        self.autoRenewPeriod = autoRenewPeriod


class DestRegionInfoModel(object):
    """
    This class define for snapshot remote copy.
    """

    def __init__(self, destRegion, name):
        self.destRegion = destRegion
        self.name = name


class AutoSnapshotPolicyModel(object):
    """
        This class define auto snapshot policy.
    """

    def __init__(self, name, timePoints, repeatWeekdays, retentionDays=None):
        self.name = name
        self.timePoints = timePoints
        self.repeatWeekdays = repeatWeekdays
        self.retentionDays = retentionDays


class ModifyReservedInstanceModel(object):
    """
    ModifyReservedInstanceModel
    """

    def __init__(self, reservedInstanceId=None, zoneName=None, reservedInstanceName=None, ehcClusterId=None):
        self.reservedInstanceId = reservedInstanceId
        self.zoneName = zoneName
        self.reservedInstanceName = reservedInstanceName
        self.ehcClusterId = ehcClusterId


class CdsCustomPeriod(object):
    """
    This class define custom period.
    """

    def __init__(self, period=None, volume_id=None):
        self.period = period
        self.volumeId = volume_id


class FileSystemModel(object):
    """
        This class define file system.
    """

    def __init__(self, fsId=None, mountAds=None, path=None, protocol=None):
        self.fsId = fsId
        self.mountAds = mountAds
        self.path = path
        self.protocol = protocol
