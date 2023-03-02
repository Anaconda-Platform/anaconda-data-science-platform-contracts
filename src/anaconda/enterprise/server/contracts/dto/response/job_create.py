""" Job Create Response Definition """
from typing import Optional

from ..record.abstract_summary import AbstractAERecordSummary


class JobCreateResponse(AbstractAERecordSummary):
    """Job Create Response DTO"""

    schedule: Optional[str]
