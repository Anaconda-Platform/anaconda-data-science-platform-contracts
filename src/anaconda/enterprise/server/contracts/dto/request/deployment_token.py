""" Deployment Token Request Definition """

from ..base_model import BaseModel


class DeploymentTokenRequest(BaseModel):
    """
    Deployment Token Request DTO

    Attributes
    ----------
    id: str
        The Project Deployment Id.
    """

    id: str
