# -*- coding: utf-8 -*-
import os
import glob
import json

_config = {}

def _dict_merge(dest, origin):
    if origin is None:
        return

    for origin_key, origin_value in origin.items():
        dest_value = dest.get(origin_key)

        if (not isinstance(origin_value, dict)) or (not isinstance(dest_value, dict)):
            dest[origin_key] = origin_value

        else:   # They are both dictionaries.
            _dict_merge(dest_value, origin_value)


def load_from_dict(new__config):
    _dict_merge(_config, new__config)

def load_from_directory(_config_base_dir):
    new__config = {}
    for filename in glob.iglob(os.path.join(_config_base_dir, '*.json')):
        key = os.path.splitext(os.path.split(filename)[1])[0]

        with open(filename) as f:
            new__config[key] = json.load(f)

    _dict_merge(_config, new__config)

def load_from_env_directory(env_var):
    load_from_directory(os.environ.get(env_var))

def get_config():
    return _config