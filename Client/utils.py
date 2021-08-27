import os


def get_environment_value(key, default_value=None):
    """
    Get a variable from environment.
    :param key: The name of the variable
    :param default_value: Default value if env variable not found
    :return: value of the variable
    """
    return os.environ.get(key, default_value)


def get_model_version():
    model_host = get_environment_value('HOSTNAME')
    return model_host.split('-')[1]
