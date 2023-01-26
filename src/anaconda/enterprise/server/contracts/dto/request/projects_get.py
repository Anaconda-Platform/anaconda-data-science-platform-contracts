""" Projects Get Request Definition """

from typing import Optional

from ..base_model import BaseModel


class ProjectsGetRequest(BaseModel):
    """Projects Get Request DTO"""

    filter: Optional[str] = None
    collaborators: bool = False
