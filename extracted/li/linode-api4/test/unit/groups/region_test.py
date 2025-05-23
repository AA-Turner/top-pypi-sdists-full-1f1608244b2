import json
from test.unit.base import ClientBaseCase

from linode_api4.objects.region import RegionAvailabilityEntry


class RegionTest(ClientBaseCase):
    """
    Tests methods of the Region class
    """

    def test_list_availability(self):
        """
        Tests that region availability can be listed and filtered on.
        """

        with self.mock_get("/regions/availability") as m:
            avail_entries = self.client.regions.availability(
                RegionAvailabilityEntry.filters.region == "us-east",
                RegionAvailabilityEntry.filters.plan == "premium4096.7",
            )

            assert len(avail_entries) > 0

            for entry in avail_entries:
                assert entry.region is not None
                assert len(entry.region) > 0

                assert entry.plan is not None
                assert len(entry.plan) > 0

                assert entry.available is not None

            # Ensure all three pages are read
            assert m.call_count == 3
            assert m.mock.call_args_list[0].args[0] == "//regions/availability"

            assert (
                m.mock.call_args_list[1].args[0]
                == "//regions/availability?page=2&page_size=100"
            )
            assert (
                m.mock.call_args_list[2].args[0]
                == "//regions/availability?page=3&page_size=100"
            )

            # Ensure the filter headers are correct
            for k, call in m.mock.call_args_list:
                assert json.loads(call.get("headers").get("X-Filter")) == {
                    "+and": [{"region": "us-east"}, {"plan": "premium4096.7"}]
                }
