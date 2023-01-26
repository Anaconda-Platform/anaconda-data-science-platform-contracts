""" Action Summary Definition """


import datetime
from typing import Union

from ..type.action_summary import AEActionSummaryType
from ..type.action_summary_status import AEActionSummaryStatusType
from .base_model import BaseModel


class AEActionSummary(BaseModel):
    """Action Summary DTO"""

    message: str
    updated: datetime.datetime
    id: str
    owner: str
    status: Union[AEActionSummaryStatusType, str]  # TODO: the enumeration needs further definition.
    created: datetime.datetime
    type: Union[AEActionSummaryType, str]  # TODO: the enumeration needs further definition.
    done: bool
    error: bool
