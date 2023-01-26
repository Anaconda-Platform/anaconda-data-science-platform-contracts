""" Project Upload Request Definition """

from pathlib import Path

from ..base_model import BaseModel


class ProjectUploadRequest(BaseModel):
    """Project Upload Request DTO"""

    project_archive_path: Path
    name: str
