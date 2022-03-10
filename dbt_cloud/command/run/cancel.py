import requests
from enum import IntEnum
from dbt_cloud.command.command import DbtCloudCommand
from dbt_cloud.field import RUN_ID_FIELD


class DbtCloudRunStatus(IntEnum):
    QUEUED = 1
    STARTING = 2
    RUNNING = 3
    SUCCESS = 10
    ERROR = 20
    CANCELLED = 30


class DbtCloudRunCancelCommand(DbtCloudCommand):
    """Cancels a running dbt Cloud job."""

    run_id: int = RUN_ID_FIELD

    @property
    def api_url(self) -> str:
        return f"{super().api_url}/runs/{self.run_id}/cancel/"

    def execute(self) -> requests.Response:
        response = requests.post(url=self.api_url, headers=self.request_headers)
        return response
