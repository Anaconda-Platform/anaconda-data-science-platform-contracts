""" Project Create Request Definition """

from typing import Optional

from ..base_model import BaseModel


class ProjectCreateRequest(BaseModel):
    """
    Project Create Request DTO

    Attributes
    ----------
    name: Optional[str] = None
        The name of the project to create.
    source: str
        The source to use when creating the project.
    make_unique: bool = True
        This flag controls the addition of a nonce to the end of name.
    """

    name: Optional[str] = None
    source: str
    make_unique: bool = True
