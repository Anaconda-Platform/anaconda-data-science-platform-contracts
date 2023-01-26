""" AE Project Record Definition """

import datetime
from typing import Union

from ...type.record_project_create_status import AERecordProjectCreateStatusType
from ...type.record_project_editor import AERecordProjectEditorType
from ...type.record_project_resource_profile import AERecordProjectResourceProfileType
from .abstract import AbstractAERecord


class AERecordProject(AbstractAERecord):
    """AE Project Record DTO"""

    updated: datetime.datetime
    repo_url: str
    url: str
    repository: str
    id: str
    editor: Union[AERecordProjectEditorType, str]
    resource_profile: Union[AERecordProjectResourceProfileType, str]
    owner: str
    git_repos: dict  # TODO: Further details are needed in order to fully define this DTO
    project_create_status: Union[AERecordProjectCreateStatusType, str]
    created: datetime.datetime
    repo_owned: bool
    name: str
    git_server: str
