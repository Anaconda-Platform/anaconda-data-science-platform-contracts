""" Abstract AE Base Definition """

import datetime

from ..base_model import BaseModel


class AbstractAEBase(BaseModel):
    """Abstract AE Base DTO"""

    updated: datetime.datetime
    id: str
    owner: str
    name: str
