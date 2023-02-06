""" Project Options Definition """

from typing import Dict, Union

from ...type.project_deploy_target import ProjectDeployTargetType
from ...type.record_project_resource_profile import AERecordProjectResourceProfileType
from ..base_model import BaseModel


class ProjectOptions(BaseModel):
    """
    Project Options DTO
    This defines the project specific options for a request.
    """

    source: str  # revision_source_url
    revision: str  # revision_name
    resource_profile: Union[AERecordProjectResourceProfileType, str]
    command: str
    target: Union[ProjectDeployTargetType, str]  # TODO: the full enumeration is not known.
    variables: Dict[str, str]
