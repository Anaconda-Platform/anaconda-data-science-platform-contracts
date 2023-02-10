""" Collaborator Update Response Definition """

from typing import List

from ..action_summary import AEActionSummary
from ..base_model import BaseModel
from ..record.collaborator import AECollaboratorRecord


class CollaboratorUpdateResponse(BaseModel):
    """
    Collaborator Update Response DTO

    Attributes
    ----------
    collaborators: List[AECollaboratorRecord]
        The collaborators after update
    action: AEActionSummary
        The action summary for the request
    """

    collaborators: List[AECollaboratorRecord]
    action: AEActionSummary
