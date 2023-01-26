""" Project Command Definition """

from typing import Optional

from .base_model import BaseModel


class ProjectCommand(BaseModel):
    """Project Command DTO"""

    id: str
    description: str
    env_spec: str
    supports_http_options: bool
    unix: str
    default: Optional[bool]
