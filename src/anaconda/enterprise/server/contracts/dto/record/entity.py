""" Anaconda Enterprise Entity Record Definition """

from typing import Optional

from ..base_model import BaseModel


class AEEntityRecord(BaseModel):
    """
    Anaconda Enterprise Entity Record Definition

    Attributes
    ----------
    id: str
        The user or group Id
    first_name: Optional[str]
        Entity First Name
    email: Optional[str]
        Entity Email
    last_name: Optional[str]
        Entity Last Name
    """

    id: str
    first_name: Optional[str]
    email: Optional[str]
    last_name: Optional[str]
