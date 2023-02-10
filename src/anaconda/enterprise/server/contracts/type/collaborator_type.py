""" Collaborator Type Definition """

from enum import Enum


class CollaboratorType(str, Enum):
    """
    Collaborator Type
    Collaborators can be a user or group within AE.
    """

    GROUP = "group"
    USER = "user"
