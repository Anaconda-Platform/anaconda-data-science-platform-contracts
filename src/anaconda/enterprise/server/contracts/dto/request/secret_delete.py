""" Secret Delete Request Definition """

from ..base_model import BaseModel


class SecretDeleteRequest(BaseModel):
    """Secret Delete Request DTO"""

    key: str
