import base64
import glob
import json
import os

from tools.datapricks_api import DatabricksApi


def get_wheel():
    return glob.glob("dist/*.whl")[0]


def main():
    DOMAIN = os.getenv("DATABRICKS_DOMAIN")
    TOKEN = os.getenv("DATABRICKS_API_TOKEN")
    CLUSTER_ID = os.getenv("DATABRICKS_CLUSTER_ID")

    api = DatabricksApi(DOMAIN, TOKEN)
    wheel_path = get_wheel()
    dbfs_path = f"/dblib/{os.path.basename(wheel_path)}"

    # Upload the wheel to Databricks.
    with open(wheel_path, "rb") as f:
        data = {
            "path": dbfs_path,
            "overwrite": "true",  # `True` does not work.
            "contents": base64.b64encode(f.read()),
        }
        resp = api.post("/dbfs/put", data=data, files={"contents": f})
        print(resp.text)

    # Install the wheel to a cluster.
    data = {
        "cluster_id": CLUSTER_ID,
        "libraries": [{"whl": f"dbfs:{dbfs_path}"}],
    }

    resp = api.post("/libraries/install", data=json.dumps(data))
    print(resp.text)


if __name__ == "__main__":
    main()
