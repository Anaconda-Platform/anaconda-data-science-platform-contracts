""" Secret Names Get Response Definition """

from typing import List

from ....contracts.dto.base_model import BaseModel


class SecretNamesGetResponse(BaseModel):
    """Secret Names Get Response DTO"""

    secrets: List[str]
