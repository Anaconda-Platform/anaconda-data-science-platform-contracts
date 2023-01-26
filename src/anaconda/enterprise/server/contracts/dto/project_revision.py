""" Project Revision Definition """

import datetime
from typing import List, Union

from .base_model import BaseModel
from .project_command import ProjectCommand
from .project_command_error import ProjectCommandError


class ProjectRevision(BaseModel):
    """Project Revision DTO"""

    id: str
    name: str
    url: str
    owner: str
    created: datetime.datetime
    updated: datetime.datetime
    commands: List[Union[ProjectCommand, ProjectCommandError]]
