import os

import requests


class DatabricksApi(requests.Session):
    def __init__(self):
        super().__init__()
        DATABRICKS_DOMAIN = os.getenv("DATABRICKS_DOMAIN")
        DATABRICKS_API_TOKEN = os.getenv("DATABRICKS_API_TOKEN")
        self.headers = {"Authorization": f"Bearer {DATABRICKS_API_TOKEN}"}
        self.BASE_URL = f"https://{DATABRICKS_DOMAIN}/api/2.0"

    def get(self, end_point, *args, **kwargs):
        super().get(self.BASE_URL + end_point, *args, **kwargs)

     def post(self, end_point, *args, **kwargs):
        super().post(self.BASE_URL + end_point, *args, **kwargs)
