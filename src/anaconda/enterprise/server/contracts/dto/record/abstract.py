""" Abstract AE Record Definition """

from ..base_model import BaseModel


class AbstractAERecord(BaseModel):
    """Abstract AE Record DTO"""

    _record_type: str  # TODO: Is this an enumeration?
