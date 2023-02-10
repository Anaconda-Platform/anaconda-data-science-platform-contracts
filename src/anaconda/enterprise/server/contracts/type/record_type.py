""" Record Type Definition"""

from enum import Enum


class RecordType(str, Enum):
    """
    Record Type Enumeration
    TODO: There are other types, these should be added when possible.
    """

    COLLABORATOR = "collaborator"
