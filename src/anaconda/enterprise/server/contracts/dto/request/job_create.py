""" Job Create Request Definition """
from .project_options import ProjectOptions


class JobCreateRequest(ProjectOptions):
    """
    Job Create Request DTO

    Attributes
    ----------
    schedule: str
        Cron like schedule, example: # '*/10 * * * *'
    autorun: bool
    """

    schedule: str
    autorun: bool
