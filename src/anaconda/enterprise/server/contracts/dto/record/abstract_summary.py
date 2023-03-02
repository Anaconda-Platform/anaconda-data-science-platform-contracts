""" Abstract AE Record Summary Definition """

from typing import Dict, Optional

from ..action_summary import AEActionSummary
from .abstract import AbstractAERecord


class AbstractAERecordSummary(AbstractAERecord):
    """
    Abstract AE Record Summary DTO
    Extends the Abstract Record.  This summary is further subclassed.
    """

    source: str
    project_name: str
    goal_state: Optional[str]
    action: AEActionSummary
    revision: str
    variables: Dict[str, str]
    project_url: str
    command: str

    state: str  # TODO: Is this an enumeration?
    status_text: str
    project_owner: str
