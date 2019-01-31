import yaml


def get_dict_from_yaml(yaml_filepath):
    with open(yaml_filepath, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as e:
            print(e)