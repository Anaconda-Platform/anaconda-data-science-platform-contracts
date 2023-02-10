""" Collaborator Record Definition """

from ...type.collaboration_permission_type import CollaborationPermissionType
from ...type.collaborator_type import CollaboratorType
from ...type.record_type import RecordType
from ..record.entity import AEEntityRecord


class AECollaboratorRecord(AEEntityRecord):
    """
    Collaborator Record DTO

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
