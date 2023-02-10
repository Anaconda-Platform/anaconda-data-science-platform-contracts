""" Collaborator Update Request """

from enum import Enum


class CollaborationPermissionType(str, Enum):
    """
    Collaboration Permissions Type
    Permissions are either read-only, or read-write.
    """

    READ_ONLY = "r"
    READ_WRITE = "rw"
