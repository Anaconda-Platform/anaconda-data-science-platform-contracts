""" Project Upload Response Definition """

import datetime

from ..action_summary import AEActionSummary
from ..base_model import BaseModel


class ProjectUploadResponse(BaseModel):
    """Project Upload Response DTO"""

    updated: datetime.datetime
    id: str
    owner: str
    name: str
    action: AEActionSummary
