""" Projects Get Response Definition """

from typing import List

from ..base_model import BaseModel
from ..record.project import AEProjectRecord


class ProjectsGetResponse(BaseModel):
    """Projects Get Response DTO"""

    records: List[AEProjectRecord]
