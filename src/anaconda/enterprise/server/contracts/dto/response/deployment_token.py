""" Deployment Token Response Definition """

from ..base_model import BaseModel


class DeploymentTokenResponse(BaseModel):
    """Deployment Token Response DTO"""

    token: str
