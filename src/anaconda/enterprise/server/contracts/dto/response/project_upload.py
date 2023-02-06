""" Project Upload Response Definition """

from ..action_summary import AEActionSummary
from ..record.abstract_base import AbstractAEBase


class ProjectUploadResponse(AbstractAEBase):
    """Project Upload Response DTO"""

    action: AEActionSummary
