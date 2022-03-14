from pathlib import Path

import yaml

ROOT_DIR = Path(__file__).parent.parent
CONFIG_DIR = ROOT_DIR / "configs"
CONFIG_FILES = [x.name for x in CONFIG_DIR.glob('*.yml')]
NAME_TO_CONFIG_FILE = {x[:-4]: (CONFIG_DIR / x).__str__() for x in CONFIG_FILES}


def get_config(container_type):
    """get config from yaml file
    :param container_type: the container type to read config
    :type container_type: str
    :returns: config
    :rtype: dict
    """
    file_name = NAME_TO_CONFIG_FILE.get(container_type)
    with open(file_name) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    return config
