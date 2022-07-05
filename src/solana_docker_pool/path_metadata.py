import json
import os 
from pkg_resources._vendor.jaraco.text import indent

CONFIG_PATH = "/config.json"


class PathMetadata():
    
    def __init__(self, path="./cetd",
                 describtion='A path metadata',
                 network='main',
                 name='main'):
        self.path = path
        self.is_initialized = False
        self.network = network
        self.name = name
        self.description = describtion
        self.load()
    
    def load(self):
        path = self.path + CONFIG_PATH
        if not os.path.isfile(path):
            self.is_initialized = False
            return
        with open(path, 'r') as file:
            map = json.load(file)
            for key in map:
                self.set(key, map.get(key))
    
    def save(self):
        path = self.path + CONFIG_PATH
        with open(path, 'w') as file:
            json.dump(self.__dict__, file, indent=4)
    
    def __setattr__(self, key, value):
        self.__dict__[key] = value
        return value
    
    def set(self, key, value):
        return self.__setattr__(key, value)
    
    def __getattr__(self, key):
        return self.get(key)
    
    def get(self, key, default=None):
        if key in self.__dict__:
            return self.__dict__[key]
        return default
    
    def __str__(self):
        return json.dumps(self.__dict__, indent=4)


def create_path_metadata(path):
    """ Creates new metadata object
    
    Path object point to a path with metadata.
    This function create a new path metadata and return it as result.
    """
    # create folder if not exist
    if not os.path.isdir(path):
        os.mkdir(path)
    
    path_metadata = PathMetadata(
        path=path
    )
    return path_metadata

