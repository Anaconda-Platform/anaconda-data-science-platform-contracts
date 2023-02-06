""" Abstract AE Record Definition """

import datetime
from typing import Union

from ...type.record_project_resource_profile import AERecordProjectResourceProfileType
from .abstract_base import AbstractAEBase


class AbstractAERecord(AbstractAEBase):
    """Abstract AE Record DTO"""

    url: str
    resource_profile: Union[AERecordProjectResourceProfileType, str]
    created: datetime.datetime
    git_repos: dict  # TODO: Further details are needed in order to fully define this DTO
