""" Action Summary Type Definition """

from enum import Enum


class AEActionSummaryType(str, Enum):
    """
    Action Summary Type Enumeration

    TODO: Determine if this is complete.
    """

    CREATE_ACTION = "create_action"
    DEPLOY_ACTION = "deploy_action"
