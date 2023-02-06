""" Job Create Response Definition """

from ..record.abstract_summary import AbstractAERecordSummary


class JobCreateResponse(AbstractAERecordSummary):
    """Job Create Response DTO"""

    schedule: str
