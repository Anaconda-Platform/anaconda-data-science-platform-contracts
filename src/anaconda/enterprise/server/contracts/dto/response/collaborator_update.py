""" Collaborator Update Response Definition """

from typing import List

from ..base_model import BaseModel
from ..record.collaborator import Collaborator
from ..action_summary import AEActionSummary


class CollaboratorUpdateResponse(BaseModel):
    """
    Collaborator Update Response DTO

    Attributes
    ----------
    collaborators: List[Collaborator]
        The collaborators after update
    action: AEActionSummary
        The action summary for the request
    """

    collaborators: List[Collaborator]
    action: AEActionSummary
