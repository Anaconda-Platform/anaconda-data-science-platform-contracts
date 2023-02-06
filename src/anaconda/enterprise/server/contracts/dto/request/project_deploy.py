""" Project Deployment Request Definition """

from typing import Optional

from .project_options import ProjectOptions


class ProjectDeployRequest(ProjectOptions):
    """Project Deployment Request DTO"""

    public: bool
    static_endpoint: Optional[str] = None  # If defined is used as the static endpoint for serving.
