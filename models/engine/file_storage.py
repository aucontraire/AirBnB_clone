#!/usr/bin/python3
"""FileStorage module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """class FileStorage"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """"""
        return self.__objects

    def new(self, obj):
        """"""
        if obj:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        json_str = json.dumps(obj_dict)
        #print('json_str:', json_str) #delete
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        """"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for key, obj_dict in json_dict.items():
                    self.new(BaseModel(**obj_dict))
        except FileNotFoundError:
            pass
