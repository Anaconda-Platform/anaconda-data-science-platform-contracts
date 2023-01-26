""" Project Command Error Definition """

from typing import Optional

from .base_model import BaseModel


class ProjectCommandError(BaseModel):
    """Project Command Error DTO"""

    id: str
    description: str
    default: Optional[bool]
