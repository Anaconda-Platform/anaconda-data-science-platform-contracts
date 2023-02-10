""" Action Summary Status Type Definition """

from enum import Enum


class AEActionSummaryStatusType(str, Enum):
    """
    Action Summary Status Type Enumeration

    TODO: Determine if this is complete.
    """

    INITIAL = "initial"
    CREATED = "created"
    DONE = "done"
