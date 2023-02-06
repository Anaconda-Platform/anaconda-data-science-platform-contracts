""" Project Revision Definition """

import datetime
from typing import List, Union

from .project_command import ProjectCommand
from .project_command_error import ProjectCommandError
from .record.abstract_base import AbstractAEBase


class ProjectRevision(AbstractAEBase):
    """Project Revision DTO"""

    url: str
    created: datetime.datetime
    commands: List[Union[ProjectCommand, ProjectCommandError]]
