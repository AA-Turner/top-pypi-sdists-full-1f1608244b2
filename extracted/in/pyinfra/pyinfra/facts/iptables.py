from __future__ import annotations

from typing_extensions import override

from pyinfra.api import FactBase

# Mapping for iptables code arguments to variable names
IPTABLES_ARGS = {
    "-A": "chain",
    "-j": "jump",
    # Boolean matches
    "-p": "protocol",
    "-s": "source",
    "-d": "destination",
    "-i": "in_interface",
    "-o": "out_interface",
    # Logging
    "--log-prefix": "log_prefix",
    # NAT exit rules
    "--to-destination": "to_destination",
    "--to-source": "to_source",
    "--to-ports": "to_ports",
}


def parse_iptables_rule(line):
    """
    Parse one iptables rule. Returns a dict where each iptables code argument
    is mapped to a name using IPTABLES_ARGS.
    """

    bits = line.split()

    definition: dict = {}

    key = None
    args: list[str] = []
    not_arg = False

    def add_args() -> None:
        arg_string = " ".join(args)

        if key and key in IPTABLES_ARGS:
            definition_key = "not_{0}".format(IPTABLES_ARGS[key]) if not_arg else IPTABLES_ARGS[key]
            definition[definition_key] = arg_string
        else:
            definition.setdefault("extras", []).extend((key, arg_string))

    for bit in bits:
        if bit == "!":
            if key:
                add_args()
                args = []
                key = None

            not_arg = True

        elif bit.startswith("-"):
            if key:
                add_args()
                args = []
                not_arg = False

            key = bit

        else:
            args.append(bit)

    if key:
        add_args()

    if "extras" in definition:
        definition["extras"] = set(definition["extras"])

    return definition


class IptablesRules(FactBase):
    """
    Returns a list of iptables rules for a specific table:

    .. code:: python

        [
            {
                "chain": "PREROUTING",
                "jump": "DNAT",
            },
        ]
    """

    default = list

    @override
    def command(self, table="filter"):
        return "iptables-save -t {0}".format(table)

    @override
    def process(self, output):
        rules = []

        for line in output:
            if line.startswith("-"):
                rules.append(parse_iptables_rule(line))

        return rules


class Ip6tablesRules(IptablesRules):
    """
    Returns a list of ip6tables rules for a specific table:

    .. code:: python

        [
            {
                "chain": "PREROUTING",
                "jump": "DNAT",
            },
        ]
    """

    @override
    def command(self, table="filter"):
        return "ip6tables-save -t {0}".format(table)


class IptablesChains(FactBase):
    """
    Returns a dict of iptables chains & policies:

    .. code:: python

        {
            "NAME": "POLICY",
        }
    """

    default = dict

    @override
    def command(self, table="filter"):
        return "iptables-save -t {0}".format(table)

    @override
    def process(self, output):
        chains = {}

        for line in output:
            if line.startswith(":"):
                line = line[1:]

                name, policy, _ = line.split()
                chains[name] = policy

        return chains


class Ip6tablesChains(IptablesChains):
    """
    Returns a dict of ip6tables chains & policies:

    .. code:: python

        {
            "NAME": "POLICY",
        }
    """

    @override
    def command(self, table="filter"):
        return "ip6tables-save -t {0}".format(table)
