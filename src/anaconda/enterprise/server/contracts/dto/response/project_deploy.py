""" Project Deploy Response Definition """

from ..record.abstract_summary import AbstractAERecordSummary


class ProjectDeployResponse(AbstractAERecordSummary):
    """Project Deploy Response DTO"""

    public: bool
    replicas: int
