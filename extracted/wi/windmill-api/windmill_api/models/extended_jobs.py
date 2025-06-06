from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extended_jobs_jobs_item_type_0 import ExtendedJobsJobsItemType0
    from ..models.extended_jobs_jobs_item_type_1 import ExtendedJobsJobsItemType1
    from ..models.extended_jobs_obscured_jobs_item import ExtendedJobsObscuredJobsItem


T = TypeVar("T", bound="ExtendedJobs")


@_attrs_define
class ExtendedJobs:
    """
    Attributes:
        jobs (List[Union['ExtendedJobsJobsItemType0', 'ExtendedJobsJobsItemType1']]):
        obscured_jobs (List['ExtendedJobsObscuredJobsItem']):
        omitted_obscured_jobs (Union[Unset, bool]): Obscured jobs omitted for security because of too specific filtering
    """

    jobs: List[Union["ExtendedJobsJobsItemType0", "ExtendedJobsJobsItemType1"]]
    obscured_jobs: List["ExtendedJobsObscuredJobsItem"]
    omitted_obscured_jobs: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.extended_jobs_jobs_item_type_0 import ExtendedJobsJobsItemType0

        jobs = []
        for jobs_item_data in self.jobs:
            jobs_item: Dict[str, Any]

            if isinstance(jobs_item_data, ExtendedJobsJobsItemType0):
                jobs_item = jobs_item_data.to_dict()

            else:
                jobs_item = jobs_item_data.to_dict()

            jobs.append(jobs_item)

        obscured_jobs = []
        for obscured_jobs_item_data in self.obscured_jobs:
            obscured_jobs_item = obscured_jobs_item_data.to_dict()

            obscured_jobs.append(obscured_jobs_item)

        omitted_obscured_jobs = self.omitted_obscured_jobs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jobs": jobs,
                "obscured_jobs": obscured_jobs,
            }
        )
        if omitted_obscured_jobs is not UNSET:
            field_dict["omitted_obscured_jobs"] = omitted_obscured_jobs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.extended_jobs_jobs_item_type_0 import ExtendedJobsJobsItemType0
        from ..models.extended_jobs_jobs_item_type_1 import ExtendedJobsJobsItemType1
        from ..models.extended_jobs_obscured_jobs_item import ExtendedJobsObscuredJobsItem

        d = src_dict.copy()
        jobs = []
        _jobs = d.pop("jobs")
        for jobs_item_data in _jobs:

            def _parse_jobs_item(data: object) -> Union["ExtendedJobsJobsItemType0", "ExtendedJobsJobsItemType1"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    jobs_item_type_0 = ExtendedJobsJobsItemType0.from_dict(data)

                    return jobs_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                jobs_item_type_1 = ExtendedJobsJobsItemType1.from_dict(data)

                return jobs_item_type_1

            jobs_item = _parse_jobs_item(jobs_item_data)

            jobs.append(jobs_item)

        obscured_jobs = []
        _obscured_jobs = d.pop("obscured_jobs")
        for obscured_jobs_item_data in _obscured_jobs:
            obscured_jobs_item = ExtendedJobsObscuredJobsItem.from_dict(obscured_jobs_item_data)

            obscured_jobs.append(obscured_jobs_item)

        omitted_obscured_jobs = d.pop("omitted_obscured_jobs", UNSET)

        extended_jobs = cls(
            jobs=jobs,
            obscured_jobs=obscured_jobs,
            omitted_obscured_jobs=omitted_obscured_jobs,
        )

        extended_jobs.additional_properties = d
        return extended_jobs

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
