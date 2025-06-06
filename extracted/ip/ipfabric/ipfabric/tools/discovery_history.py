import logging
from typing import Any, Union

from pydantic import Field, BaseModel

from ipfabric.tools.shared import convert_timestamp, date_parser, raise_for_status

logger = logging.getLogger("ipfabric")

COLUMNS = ["id", "sn", "hostname", "loginIp", "loginType", "ts", "username", "usernameNotes"]


class DiscoveryHistory(BaseModel):
    ipf: Any = Field(exclude=True)

    def get_all_history(
        self, columns: list = None, sort: dict = None, filters: dict = None, ts_format: str = "utc"
    ) -> list:
        """returns information about the discovery process

        Args:

        columns: columns for discovery-history table
        sort: Default timestamp descending
        filters: filter for discovery-history table
        ts_format: Valid formats ['utc', 'datetime', 'int']; datetime will return python datetime object

        Returns:
            list[Dict]
        """
        columns = columns or COLUMNS
        if ts_format not in ["utc", "datetime", "int"] and "ts" in columns:
            raise SyntaxError(f"{ts_format} is not a valid format; please use one of ['utc', 'datetime', 'int'].")
        sort = sort or {"order": "desc", "column": "ts"}
        history = self.ipf.fetch_all(
            "tables/inventory/discovery-history", columns=columns, filters=filters, sort=sort, snapshot=False
        )
        if ts_format == "datetime" and "ts" in columns:
            [h.update({"ts": convert_timestamp(h["ts"])}) for h in history]
        elif ts_format == "utc" and "ts" in columns:
            [h.update({"ts": convert_timestamp(h["ts"], ts_format="ziso")}) for h in history]
        return history

    def get_snapshot_history(
        self, snapshot_id: str = None, columns: list = None, sort: dict = None, ts_format: str = "utc"
    ) -> tuple:
        """returns information about a specific snapshot

        Args:
            snapshot_id: Specific ID or defaults to class initialized ID
            columns: Default All
            sort: Default timestamp descending
            ts_format: Valid formats ['utc', 'datetime', 'int']; datetime will return python datetime object

        Returns:
            First list has history of devices in the snapshot, second list has device that
            did not have history usually because it is an AP or API connection
        """
        snapshot = self.ipf.snapshots[snapshot_id or self.ipf.snapshot_id]
        hist = {
            h["sn"]: h
            for h in self.get_history_date(
                daterange=int(snapshot.start.timestamp()), columns=columns, sort=sort, ts_format=ts_format
            )
        }
        history, no_history = list(), list()
        for device in self.ipf.inventory.devices.all(columns=["sn", "hostname", "loginIp", "loginType"]):
            if device["sn"] in hist:
                history.append(hist[device["sn"]])
            else:
                no_history.append(device)
        return history, no_history

    def get_history_date(
        self, daterange: Union[tuple, str, int], columns: list = None, sort: dict = None, ts_format: str = "utc"
    ) -> list:
        """get a full history of a snapshot

        Args:
            daterange: Date can be string or int in seconds "11/22/ 1:30" or 1637629200
                        This will filter from that date to now
                        Or can be a tuple of a date range to filter history in that range.
            columns: Default All
            sort: Default timestamp descending
            ts_format: Valid formats ['utc', 'datetime', 'int']; datetime will return python datetime object

        Returns: First list has history of devices in the snapshot, second list has device that
                did not have history usually because it is an AP or API connection
        """
        if isinstance(daterange, tuple):
            filters = {
                "and": [
                    {"ts": ["gte", int(date_parser(daterange[0]).timestamp() * 1000)]},
                    {"ts": ["lte", int(date_parser(daterange[1]).timestamp() * 1000)]},
                ]
            }

        else:
            filters = {"ts": ["gte", int(date_parser(daterange).timestamp() * 1000)]}
        return self.get_all_history(columns=columns, sort=sort, filters=filters, ts_format=ts_format)

    def delete_history(self, history_id: Union[list[str], str]):
        if isinstance(history_id, str):
            history_id = [history_id]

        raise_for_status(self.ipf.request("DELETE", "discovery/history", json=history_id))
        logger.debug("Deleted the following discovery history IDs:")
        logger.debug(f"{history_id}")
        return True

    def delete_history_prior_to_ts(self, timestamp: Union[int, str]) -> list:
        """removes history from IPF based on the date passed to timestamp

        Args:
            timestamp: Can be string or int in seconds "11/22/ 1:30" or 1637629200
        Returns:
            List of history
        """
        filters = {"ts": ["lte", int(date_parser(timestamp).timestamp() * 1000)]}
        history = self.get_all_history(filters=filters)
        if not history:
            logger.debug(f"Did not locate any history prior to {date_parser(timestamp).isoformat()}")
            return history
        history_ids = [h["id"] for h in history]
        self.delete_history(history_ids)
        logger.debug("Deleted the following discovery history entries:")
        [logger.debug(f"{h}") for h in history]
        return history
