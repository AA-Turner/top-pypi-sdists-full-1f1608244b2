"""
Manage Cloudwatch alarms

.. versionadded:: 2014.7.0

Create and destroy cloudwatch alarms. Be aware that this interacts with
Amazon's services, and so may incur charges.

This module uses boto, which can be installed via package, or pip.

This module accepts explicit credentials but can also utilize
IAM roles assigned to the instance through Instance Profiles. Dynamic
credentials are then automatically obtained from AWS API and no further
configuration is necessary. More Information available at:

http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html

If IAM roles are not used you need to specify them either in a pillar or
in the minion's config file::

    cloudwatch.keyid: GKTADJGHEIQSXMKKRBJ08H
    cloudwatch.key: askdjghsdfjkghWupUjasdflkdfklgjsdfjajkghs

It's also possible to specify key, keyid and region via a profile, either
as a passed in dict, or as a string to pull from pillars or minion config:

.. code-block:: yaml

    myprofile:
      keyid: GKTADJGHEIQSXMKKRBJ08H
      key: askdjghsdfjkghWupUjasdflkdfklgjsdfjajkghs
      region: us-east-1

.. code-block:: yaml

    my test alarm:
      boto_cloudwatch_alarm.present:
        - name: my test alarm
        - attributes:
            metric: ApproximateNumberOfMessagesVisible
            namespace: AWS/SQS
            statistic: Average
            comparison: ">="
            threshold: 20000.0
            period: 60
            evaluation_periods: 1
            description: test alarm via salt
            dimensions:
              QueueName:
                - the-sqs-queue-name
            alarm_actions:
              - arn:aws:sns:us-east-1:1111111:myalerting-action
"""

import salt.utils.data


def __virtual__():
    """
    Only load if boto is available.
    """
    if "boto_cloudwatch.get_alarm" in __salt__:
        return "boto_cloudwatch_alarm"
    return (False, "boto_cloudwatch module could not be loaded")


def present(name, attributes, region=None, key=None, keyid=None, profile=None):
    """
    Ensure the cloudwatch alarm exists.

    name
        Name of the alarm

    attributes
        A dict of key/value cloudwatch alarm attributes.

    region
        Region to connect to.

    key
        Secret key to be used.

    keyid
        Access key to be used.

    profile
        A dict with region, key and keyid, or a pillar key (string)
        that contains a dict with region, key and keyid.
    """
    ret = {"name": name, "result": True, "comment": "", "changes": {}}
    alarm_details = __salt__["boto_cloudwatch.get_alarm"](
        name, region, key, keyid, profile
    )

    # Convert to arn's
    for k in ["alarm_actions", "insufficient_data_actions", "ok_actions"]:
        if k in attributes:
            attributes[k] = __salt__["boto_cloudwatch.convert_to_arn"](
                attributes[k], region, key, keyid, profile
            )

    # Diff the alarm_details with the passed-in attributes, allowing for the
    # AWS type transformations
    difference = []
    if alarm_details:
        for k, v in attributes.items():
            if k not in alarm_details:
                difference.append(f"{k}={v} (new)")
                continue
            v = salt.utils.data.decode(v)
            v2 = salt.utils.data.decode(alarm_details[k])
            if v == v2:
                continue
            if isinstance(v, str) and v == v2:
                continue
            if isinstance(v, float) and v == float(v2):
                continue
            if isinstance(v, int) and v == int(v2):
                continue
            if isinstance(v, list) and sorted(v) == sorted(v2):
                continue
            difference.append(f"{k}='{v}' was: '{v2}'")
    else:
        difference.append("new alarm")
    create_or_update_alarm_args = {
        "name": name,
        "region": region,
        "key": key,
        "keyid": keyid,
        "profile": profile,
    }
    create_or_update_alarm_args.update(attributes)
    if alarm_details:  # alarm is present.  update, or do nothing
        # check to see if attributes matches is_present. If so, do nothing.
        if len(difference) == 0:
            ret["comment"] = f"alarm {name} present and matching"
            return ret
        if __opts__["test"]:
            msg = f"alarm {name} is to be created/updated."
            ret["comment"] = msg
            ret["result"] = None
            return ret
        result = __salt__["boto_cloudwatch.create_or_update_alarm"](
            **create_or_update_alarm_args
        )
        if result:
            ret["changes"]["diff"] = difference
        else:
            ret["result"] = False
            ret["comment"] = f"Failed to create {name} alarm"
    else:  # alarm is absent. create it.
        if __opts__["test"]:
            msg = f"alarm {name} is to be created/updated."
            ret["comment"] = msg
            ret["result"] = None
            return ret
        result = __salt__["boto_cloudwatch.create_or_update_alarm"](
            **create_or_update_alarm_args
        )
        if result:
            ret["changes"]["new"] = attributes
        else:
            ret["result"] = False
            ret["comment"] = f"Failed to create {name} alarm"
    return ret


def absent(name, region=None, key=None, keyid=None, profile=None):
    """
    Ensure the named cloudwatch alarm is deleted.

    name
        Name of the alarm.

    region
        Region to connect to.

    key
        Secret key to be used.

    keyid
        Access key to be used.

    profile
        A dict with region, key and keyid, or a pillar key (string)
        that contains a dict with region, key and keyid.
    """
    ret = {"name": name, "result": True, "comment": "", "changes": {}}

    is_present = __salt__["boto_cloudwatch.get_alarm"](
        name, region, key, keyid, profile
    )

    if is_present:
        if __opts__["test"]:
            ret["comment"] = f"alarm {name} is set to be removed."
            ret["result"] = None
            return ret
        deleted = __salt__["boto_cloudwatch.delete_alarm"](
            name, region, key, keyid, profile
        )
        if deleted:
            ret["changes"]["old"] = name
            ret["changes"]["new"] = None
        else:
            ret["result"] = False
            ret["comment"] = f"Failed to delete {name} alarm."
    else:
        ret["comment"] = f"{name} does not exist in {region}."

    return ret
