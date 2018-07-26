import yaml

CONFIG_FILE_PATH = "pompem_configs.yaml"
stream = open(CONFIG_FILE_PATH, "r")
configs = yaml.load(stream)
