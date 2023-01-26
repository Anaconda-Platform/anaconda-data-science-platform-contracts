""" AE Response Wrapper Definition """

from typing import Generic, TypeVar

from .base_model import BaseModel

T = TypeVar("T")


class AEResponseWrapper(BaseModel, Generic[T]):
    """

    AE Response Wrapper DTO

    Some server responses are wrapped in `data`. This appears to include secrets, but not projects.
    """

    data: T
