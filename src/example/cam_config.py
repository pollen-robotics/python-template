import json
from importlib.resources import files
from typing import Any, List


class CamConfig:
    def __init__(
        self,
        cam_config_json: str,
    ) -> None:
        self.cam_config_json = cam_config_json

        config = json.load(open(self.cam_config_json, "rb"))
        self.socket_to_name = config["socket_to_name"]
        self.inverted = config["inverted"]
        self.fisheye = config["fisheye"]
        self.mono = config["mono"]

    def to_string(self) -> str:
        ret_string = "Camera Config: \n"
        ret_string += "Inverted: {}\n".format(self.inverted)
        ret_string += "Fisheye: {}\n".format(self.fisheye)
        ret_string += "Mono: {}\n".format(self.mono)

        return ret_string


def get_config_files_names() -> List[str]:
    path = files("config_files")
    return [file.stem for file in path.glob("**/*.json")]  # type: ignore[attr-defined]


def get_config_file_path(name: str) -> Any:
    path = files("config_files")
    for file in path.glob("**/*"):  # type: ignore[attr-defined]
        if file.stem == name:
            return file.resolve()
    return None
