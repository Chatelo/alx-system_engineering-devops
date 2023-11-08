#!/usr/bin/env python3

from datadog_api_client import Configuration, ThreadedApiClient
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

configuration = Configuration()

# configuration.api_key["apiKeyAuth"] = "<API KEY>"
configuration.api_key["apiKeyAuth"] = "0b80690c-c14e-46e0-a625-a8a7987dcda8"

# configuration.api_key["appKeyAuth"] = "<APPLICATION KEY>"
configuration.api_key["appKeyAuth"] = (
    "96d15e62-a9c5-4c4a-9784-334b2d77d525"
)

with ThreadedApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    result = api_instance.list_dashboards()
    dashboards = result.get()
    print(dashboards)
