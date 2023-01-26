""" Secret Put Request Definition """

from ..base_model import BaseModel


class SecretPutRequest(BaseModel):
    """Secret Put Request DTO"""

    key: str
    value: str
