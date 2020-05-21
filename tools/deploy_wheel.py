import glob
import os

from tools.datapricks_api import DatabricksApi


def get_wheel():
    return glob.glob("dist/*.whl")[0]


def main():
    api = DatabricksApi()
    wheel_path = get_wheel()
    dbfs_path = f"/dblib/{os.path.basename(wheel_path)}"

    with open(wheel_path, "rb") as f:
        data = {
            "path": dbfs_path,
            "overwrite": True,
            "contents": f,
        }
        api.post("/dbfs/put", data=data)


if __name__ == "__main__":
    main()
