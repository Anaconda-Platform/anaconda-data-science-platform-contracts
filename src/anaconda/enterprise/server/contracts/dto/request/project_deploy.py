""" Project Deployment Request Definition """

from typing import Optional, Union, Dict

from ...type.project_deploy_target import ProjectDeployTargetType
from ..base_model import BaseModel


class ProjectDeployRequest(BaseModel):
    """Project Deployment Request DTO"""

    name: str  # deployment name
    source: str  # revision_source_url
    revision: str  # revision_name
    resource_profile: str
    command: str
    public: bool
    target: Union[ProjectDeployTargetType, str]  # TODO: the full enumeration is not known.
    static_endpoint: Optional[str] = None  # If defined is used as the static endpoint for serving.
    variables: Dict[str, str]
