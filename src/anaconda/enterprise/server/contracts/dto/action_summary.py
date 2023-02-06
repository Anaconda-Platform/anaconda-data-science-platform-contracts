""" Action Summary Definition """


import datetime
from typing import Union

from ..type.action_summary import AEActionSummaryType
from ..type.action_summary_status import AEActionSummaryStatusType
from .base_model import BaseModel


class AEActionSummary(BaseModel):
    """Action Summary DTO"""

    id: str
    owner: str
    created: datetime.datetime
    updated: datetime.datetime

    status: Union[AEActionSummaryStatusType, str]  # TODO: the enumeration needs further definition.
    type: Union[AEActionSummaryType, str]  # TODO: the enumeration needs further definition.
    message: str

    done: bool
    error: bool
