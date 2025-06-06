# TODO: REMOVE IN 8.0
import json
import logging
from collections import OrderedDict
from datetime import datetime
from os import path
from typing import Any, Union

from pydantic import Field
from pydantic.dataclasses import dataclass

from ipfabric.tools.shared import raise_for_status

logger = logging.getLogger("ipfabric")


@dataclass
class RestoreIntents:
    ipf: Any = Field(exclude=True)

    def __post_init__(self):
        logger.warning(
            "This is a deprecated class. Use the `IPFClient().settings.appliance_configuration` utility instead."
        )

    def restore_from_file(self, intents_file: str, groups_file: str, dashboard_file: str):
        if not all(path.exists(f) for f in [intents_file, groups_file, dashboard_file]):
            logger.critical("File(s) do not exist.")
            exit()
        with open(intents_file, "r") as file:
            intents = json.load(file)
        with open(groups_file, "r") as file:
            groups = json.load(file)
        with open(dashboard_file, "r") as file:
            dashboard = json.load(file)
        self._restore(intents, groups, dashboard)

    def restore_from_dictionary(self, intents: list, groups: list, dashboard: Union[dict, OrderedDict]):
        if not all(isinstance(f, list) for f in [intents, groups]) and not isinstance(dashboard, (dict, OrderedDict)):
            logger.critical("Intents and Groups must be Lists and Dashboard a Dictionary or OrderedDict.")
            exit()
        self._restore(intents, groups, dashboard)

    @staticmethod
    def _save_to_file(intents, groups, dashboard):
        tstamp = datetime.now().strftime("%Y%m%d-%H%M%S")

        def save(name, data):
            filename = name + "_" + tstamp + ".json"
            logger.info(f"Saving {name} to {filename}.")
            with open(filename, "w") as file:
                json.dump(data, file)
            logger.info(f"Saved {name} to {filename}.")

        save("intents", intents)
        save("groups", groups)
        save("dashboard", dashboard)

    def _restore(self, intents, groups, dashboard):
        i = input("\nDO YOU ACCEPT OVERRIDING ALL INTENTS, INTENT GROUPS, DASHBOARD SETTINGS? (y/n): ").strip().lower()
        if i and "y" not in i[0]:
            logger.warning("Exiting Script before making changes.")
            exit()

        old_intents = self.ipf.get("reports").json()
        old_intent_groups = self.ipf.get("reports/groups").json()
        old_dashboard = json.loads(self.ipf.get("settings/dashboard").text, object_pairs_hook=OrderedDict)
        self._save_to_file(old_intents, old_intent_groups, old_dashboard)

        logger.info("Deleting All Intents.")
        for i in old_intents:
            raise_for_status(self.ipf.delete(f"reports/{i['id']}"))
        logger.info("Deleted All Intents.")

        logger.info("Deleting All Intent Groups.")
        for g in old_intent_groups:
            raise_for_status(self.ipf.delete(f"reports/groups/{g['id']}"))
        logger.info("Deleted All Intent Groups.")

        intent_mapping = {i["id"]: None for i in intents}
        logger.info("Creating Intent Verification Rules.")
        for i in intents:
            i["groups"] = []
            i.pop("custom", None)
            src_id = i.pop("id", None)
            res = raise_for_status(self.ipf.post("reports", json=i))
            intent_mapping[src_id] = res.json()["id"]
        logger.info("Created Intent Verification Rules.")

        group_mapping = {g["id"]: None for g in groups}
        logger.info("Creating Intent Groups.")
        for g in groups:
            for c in g["children"]:
                c["id"] = intent_mapping[c["id"]]
            src_id = g.pop("id", None)
            g.pop("custom", None)
            res = raise_for_status(self.ipf.post("reports/groups", json=g))
            group_mapping[src_id] = res.json()["id"]
        logger.info("Created Intent Groups.")

        raw_dashboard = json.dumps(dashboard)
        logger.info("Creating Dashboard.")
        for src_group, dst_group in group_mapping.items():
            raw_dashboard = raw_dashboard.replace(src_group, dst_group)

        raise_for_status(self.ipf.put("settings/dashboard", json=json.loads(raw_dashboard)))
        logger.info("Created Dashboard.")
        return True
