import requests


class DatabricksApi(requests.Session):
    def __init__(self, domain, token):
        super().__init__()
        self.BASE_URL = f"https://{domain}/api/2.0"
        self.headers = {"Authorization": f"Bearer {token}"}

    def get(self, end_point, *args, **kwargs):
        return super().get(self.BASE_URL + end_point, *args, **kwargs)

    def post(self, end_point, *args, **kwargs):
        return super().post(self.BASE_URL + end_point, *args, **kwargs)
