""" Collaborator Update Request """

from ..record.entity import AEEntityRecord
from ...type.collaboration_permission_type import CollaborationPermissionType
from ...type.collaborator_type import CollaboratorType
from ...type.record_type import RecordType


class Collaborator(AEEntityRecord):
    """
    Collaborator Update Request DTO

    Attributes
    ----------
    _record_type: RecordType.COLLABORATOR = RecordType.COLLABORATOR
        The explicitly record type definition for a collaborator.
    type: CollaboratorType
        The type of collaborator
    permission: CollaborationPermissionType
        The assignable permissions
    """

    _record_type: RecordType.COLLABORATOR = RecordType.COLLABORATOR
    type: CollaboratorType
    permission: CollaborationPermissionType
