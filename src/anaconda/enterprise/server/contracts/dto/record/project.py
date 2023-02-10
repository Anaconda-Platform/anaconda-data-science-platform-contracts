""" AE Project Record Definition """

from typing import Union

from ...type.record_project_create_status import AERecordProjectCreateStatusType
from ...type.record_project_editor import AERecordProjectEditorType
from .abstract import AbstractAERecord


class AERecordProject(AbstractAERecord):
    """AE Project Record DTO"""

    _record_type: str  # TODO: Move to enumeration: RecordType

    project_create_status: Union[AERecordProjectCreateStatusType, str]
    editor: Union[AERecordProjectEditorType, str]
    repository: str
    repo_url: str
    repo_owned: bool
    git_server: str
