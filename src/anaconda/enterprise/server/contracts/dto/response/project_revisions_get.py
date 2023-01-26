""" Project Revisions Get Response Definition """

from typing import List

from ..base_model import BaseModel
from ..project_revision import ProjectRevision


class ProjectRevisionsGetResponse(BaseModel):
    """Project Revisions Get Response DTO"""

    revisions: List[ProjectRevision]
